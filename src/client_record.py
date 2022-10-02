import datetime


class ClientRecord:

    def __init__(self, first_name: str, last_name: str, avg_call_duration: float, first_call: datetime):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__avg_call_duration = avg_call_duration
        self.__first_call = first_call

    def print_info(self):
        print(self.__first_name, self.__last_name, self.__avg_call_duration, self.__first_call)

    def get_first_call(self):
        return self.__first_call

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_avg_call_duration(self):
        return self.__avg_call_duration