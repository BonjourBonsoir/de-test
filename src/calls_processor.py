from src.incoming_calls import IncomingCalls
from ftplib import FTP
from datetime import datetime

class CallsProcessor:

    def __init__(self, config):
        self.__config: dict[str, str] = config
        self.__calls: dict[str, IncomingCalls] = {}

    def process(self):

        ftp = FTP()
        ftp.connect(host=self.__config['host'], port=int(self.__config['port']))
        ftp.login(user=self.__config['user'], passwd=self.__config['passwd'])
        ftp.cwd('files')

        with open('raw_calls.csv', 'wb') as fp:
            ftp.retrbinary('RETR raw_calls.csv', fp.write)

        header = {}

        ##TODO that would have been better to process each call in one pass without writing them on disk
        with open("./raw_calls.csv", "r") as calls:
            for line in calls:
                if header == {}:
                    i = 0
                    for fieldName in line.strip().split(','):
                        header[fieldName] = i
                        i = i + 1
                else:
                    row = line.strip().split(',')
                    date = datetime.strptime(row[header['date']], '%d/%m/%Y')
                    duration_in_sec = int(row[header['duration_in_sec']])
                    incoming_number = row[header['incoming_number']]
                    if incoming_number != '':
                        if incoming_number in self.__calls:
                            self.__calls[incoming_number].add_call(date, duration_in_sec)
                        else:

                            self.__calls[incoming_number] = IncomingCalls(date, duration_in_sec)

        return self

    def get(self):
        return self.__calls
