from src.incoming_calls import IncomingCalls
import psycopg2


class CrmProcessor:

    def __init__(self, config, client_numbers):
        self.__config = config
        self.__client_numbers: dict[str, IncomingCalls] = client_numbers

    def process(self):

        conn = psycopg2.connect(database=self.__config['database'],
                                host=self.__config['host'],
                                user=self.__config['user'],
                                password=self.__config['password'],
                                port=self.__config['port'])

        cursor = conn.cursor()

        cursor.execute('SELECT "FirstName", "LastName", "PhoneNumber", MAX("CreationDate") AS "MostRecentCreationDate" '
                       'FROM clients_crm '
                       'WHERE "PhoneNumber" IS NOT NULL '
                       'GROUP BY "FirstName", "LastName", "PhoneNumber" ')

        for row in cursor.fetchall():
            first_name = row[0]
            last_name = row[1]
            phone_number = row[2][1:]
            if phone_number in self.__client_numbers:
                self.__client_numbers[phone_number].add_first_name(first_name)
                self.__client_numbers[phone_number].add_last_name(last_name)

        return self

    def get(self):
        return self.__client_numbers
