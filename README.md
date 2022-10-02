## DE-TEST

# Algorithm

The idea is to collect the data from different calls (ftp) and to join them with crm data (postgre) using the phone number.
To do so, IncomingCalls class has been implemented to gather for each phone number data such as : date of calls, duration, names attached to it
and it allows to compute the average call duration, retrieve the first call date. Also, because we could have several names attach to one 
phone number, a set of names has been used to gather all entries and returns only one base on a fixed rule

Then a HashMap has been implemented between a phone number and an IncomingCalls object to have a fast look up and avoid running through the list.
Therefore, the complexity of the collection is O(N+M) have N calls and M crm data.

To run the code, simple run the main.py file within src folder

# Test 
The incoming calls object has been tested within the tests directory

# Incomplete
The docker script has not been tested, and the docker container has not been generated.
The email implementation is also missing.
Tests on the collection of calls and crm data are also missing.

# Next steps
Finish all the items above
Push a cloudformation/terraform file for infrastructure
Implement a CI/CI pipeline to run the tests, build the container, deploy the container, build the AWS/GCP/other stack of the project
Build a dev/int/prd environment



