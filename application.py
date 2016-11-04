from config import config


class Application(object):
    '''
    Contains all utility functions
    '''
    def __init__(self):
        pass

    def get_sorted_data(self, data, sort_type=None):
        '''
        :param data: data to be sorted
        :param sort_type: (0/1) 0 imply descending sort, 1 imply ascending sort
        :return: returns the sorted data according to sort_type
        '''
        sorted_data = data
        if sort_type == 0:
            sorted_data = sorted(data, key=lambda x: int(x[3]), reverse=True)
        elif sort_type == 1:
            sorted_data = sorted(data, key=lambda x: int(x[3]))
        return sorted_data

    def get_city_hotels(self, city_id, **kwargs):
        '''
        :param city_id: filter parameter for the data particular to that city_id if present in DB
        :param kwargs: optional if sort_type present sorts the data
        :return: return the data particular to ```city_id```
        '''
        data = None
        if city_id:
            data = config.CSV_DATA.hotel_data_dict[city_id]
            if kwargs.get('sort_type') is not None:
                sort_type = kwargs.get('sort_type')
                data = self.get_sorted_data(data, sort_type)
        return data

    def format_data(self, data, headers):
        '''
        :param data: data present in raw format
        :param headers: headers define the header name for each element in data
        :return: returns the formatted data, each element is assigned to it's header. Data in a meanigful format
        '''
        formatted_data = []

        for element in data:
            one_data = {}
            for idx in xrange(len(headers)):
                one_data[headers[idx]] = element[idx]

            formatted_data.append(one_data)
        return formatted_data
