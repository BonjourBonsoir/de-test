from src.incoming_calls import IncomingCalls
from db_handler import config
from src.calls_processor import CallsProcessor
from src.crm_processor import CrmProcessor


if __name__ == '__main__':

    ftp_config = config('../database.ini', 'ftp')

    ## First we retrieve the calls
    calls_processor: CallsProcessor = CallsProcessor(ftp_config)
    ## client_numbners is a Map between a phone number and an IncomingCalls object
    client_numbers = calls_processor.process().get()

    postgre_config = config('../database.ini', 'postgresql')

    ## Then we retrieve data from CRM and we append them to the data we got from calls using phone number
    crm_processor: CrmProcessor = CrmProcessor(postgre_config, client_numbers)
    client_numbers = crm_processor.process().get()

    ## Then we can send the mail with the data from crm + calls
    for (phoneNumber, call) in client_numbers.items():
        print(phoneNumber)
        client_data = call.get_client_data()
        if client_data is not None:
            client_data.print_info()
