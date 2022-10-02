import datetime
from src.client_record import ClientRecord


class IncomingCalls:

    def __init__(self, date: datetime, duration_in_sec: int):
        self.__first_incoming_call: datetime = date
        self.__call_durations: list[int] = [duration_in_sec]
        self.__first_name = set()
        self.__last_name = set()

    def add_call(self, date: datetime, duration_in_sec):
        if self.__first_incoming_call > date:
            self.__first_incoming_call = date
        self.__call_durations.append(duration_in_sec)

    def __get_first_call_date(self):
        return self.__first_incoming_call

    def __get_average_call_duration(self):
        return sum(self.__call_durations) / len(self.__call_durations)

    def add_first_name(self, first_name):
        self.__first_name.add(first_name)

    def add_last_name(self, last_name):
        self.__last_name.add(last_name)

    def get_client_data(self):
        ## We may have some cases with multiple names for one phone number
        ## in a second step we can think of an algorithm to reconciliate all the names attached to a number
        ## Here we just take the first name and last_name
        if len(self.__first_name) > 0 and len(self.__last_name) > 0:
            return ClientRecord(sorted(self.__first_name).pop(), sorted(self.__last_name).pop(),
                                self.__get_average_call_duration(),
                                self.__get_first_call_date())
        else:
            return None
