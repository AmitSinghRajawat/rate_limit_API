import csv

class CSVReader(object):
    '''
    This is the data store for this application.
    Parsing the file and storing the data for the current running instance of the server
    '''
    def __init__(self):
        self.hotel_data_dict = {}
        self.csv_reader()

    def csv_reader(self):
        with open('hoteldb.csv', 'rU') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|', dialect=csv.excel_tab)
            for row in csvreader:
                if csvreader.line_num == 1:
                    self.headers = row
                    try:
                        hotel_id_idx = self.headers.index('CITY')
                    except ValueError:
                        hotel_id_idx = 0
                else:
                    hotel_data = row
                    if self.hotel_data_dict.has_key(row[hotel_id_idx]):
                        self.hotel_data_dict[row[hotel_id_idx]].append(hotel_data)
                    else:
                        self.hotel_data_dict[row[hotel_id_idx]] = [hotel_data]
