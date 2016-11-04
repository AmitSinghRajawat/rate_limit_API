from functools import wraps
from flask import request, abort, make_response
from config import config
import time
import json


def check_rate_limit(api_arg):
    '''
    This is a decorator defintion.
    Usage: This is called just before calling any API (```getCityHotels``` in this case), to check the Rate limit of
    the API before calling
    :param api_arg: is the ```api_key``` parameter string in the request body to check if request contains api_key
    :return: this decorator returns the get_hotels function as argument.
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = json.loads(request.data)
            if api_arg not in json_object:                                                                                              # if api_key is not present in request body
                abort(make_response("API key not found", 400))
            if config.API_KEYS.has_key(func.__name__):                                                                                  # if API supports Rate limiting functionality
                api_key_value = json_object[api_arg]
                if config.API_KEYS[func.__name__].has_key(api_key_value):                                                               # checks if API key value is correct
                    if config.KEY_RATE_LIMIT.has_key(api_key_value):                                                                    # checks if threshold time is set for this API
                        if time.time() > config.KEY_RATE_LIMIT[
                            api_key_value]:                                                                                             # if current time has passed the API limit time
                            config.KEY_RATE_LIMIT[api_key_value] = int(time.time()) + (config.API_KEYS[func.__name__][
                                                                                           api_key_value] or config.GLOBAL_RATE_LIMIT)  # setting API limit time to config value
                            if api_key_value in config.ALREADY_SUSPENDED:
                                '''
                                Ideally we have to set cron job to reset the ALREADY_SUSPENDED API key,
                                in this case if ALREADY_SUSPENDED and limit time has passed then remove the API key
                                from the ALREADY_SUSPENDED list
                                '''
                                config.ALREADY_SUSPENDED.remove(api_key_value)
                        else:
                            if api_key_value not in config.ALREADY_SUSPENDED:                                                           # if not already suspended but exceeded the rate limit, suspending for next 5 minutes
                                config.KEY_RATE_LIMIT[api_key_value] = int(time.time()) + config.SUSPENSION_TIME_LIMIT
                                config.ALREADY_SUSPENDED.append(api_key_value)
                                abort(make_response("Limit Exceeded, Suspending for {} minute(s)".format(config.SUSPENSION_TIME_LIMIT/60), 400))
                            else:
                                abort(make_response("Already suspended for 5 minutes", 400))
                    else:
                        config.KEY_RATE_LIMIT[api_key_value] = int(time.time()) + (
                            config.API_KEYS[func.__name__][api_key_value] or config.GLOBAL_RATE_LIMIT)
                else:
                    abort(make_response("Invalid API key", 400))
            else:
                abort(make_response("Invalid request", 400))
            return func(*args, **kwargs)

        return wrapper

    return decorator
