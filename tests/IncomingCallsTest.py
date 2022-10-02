import unittest
from src.incoming_calls import IncomingCalls
from src.client_record import ClientRecord
from datetime import datetime

class MyTestCase(unittest.TestCase):
    def test_something(self):

        dt1 = datetime.strptime("01/01/2022", '%d/%m/%Y')
        dt2 = datetime.strptime("05/01/2022", '%d/%m/%Y')
        dt3 = datetime.strptime("10/01/2022", '%d/%m/%Y')
        dt4 = datetime.strptime("15/01/2022", '%d/%m/%Y')

        incoming_calls = IncomingCalls(dt1, 10)
        incoming_calls.add_call(dt2, 20)
        incoming_calls.add_call(dt3, 30)
        incoming_calls.add_call(dt4, 40)

        ## We have four calls
        ## First date is 01/01/2022
        ## Average is 10 + 20 + 30 + 40 / 4 -> 25

        incoming_calls.add_last_name("Einstein")
        incoming_calls.add_first_name("Albert")
        incoming_calls.add_first_name("Jacques")
        incoming_calls.add_last_name("Chirac")

        client_record = incoming_calls.get_client_data()

        self.assertEqual(client_record.get_avg_call_duration() == 25.0, True)  # add assertion here
        self.assertEqual(client_record.get_first_call() == dt1, True)  # add assertion here

        ##TODO it would have been better to make a set of tuple (first_name, last_name) to avoid having a discrepency between
        ## one first_name which does not match another last_name
        self.assertEqual(client_record.get_first_name() == "Jacques", True)
        self.assertEqual(client_record.get_last_name() == "Einstein", True)

if __name__ == '__main__':
    unittest.main()
