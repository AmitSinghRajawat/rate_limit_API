class Config(object):
    '''
    Config class: stores all configuration settings
    '''
    def __init__(self):
        self.CSV_DATA = None                                                                                            # Data handler for hotels data present in CSV file
        self.API_KEYS = {}
        self.API_KEYS['get_hotels'] = {}
        self.API_KEYS['get_hotels']['gethotels1234'] = 20                                                               # (in seconds)  For the API key, 1 request per 20 seconds
        self.API_KEYS['get_hotels']['gethotels7890'] = 15                                                               # (in seconds)  For the API key, 1 request per 15 seconds
        self.KEY_RATE_LIMIT = {}                                                                                        # (API key --> Time Limit) hasmap for setting the next time limit for particular API key
        self.GLOBAL_RATE_LIMIT = 10                                                                                     # 1 request per 10 seconds
        self.ALREADY_SUSPENDED = []                                                                                     # stores the API keys for which API rate limit has exceeded
        self.SUSPENSION_TIME_LIMIT = 300                                                                                # (in seconds) 5 minutes suspension for exceeding any API rate limit


config = Config()
