"""
# create a bank account
# deposit money
# withdraw money
# details
# update details
# delete account

# We will create a JSON file to store the data of the user

"""

import json
import random
import string
from pathlib import Path

class Bank:

    database = 'data.json' # creating a json file to store the data of the user
    data = [] # creating a list to store the data of the user as dummy data so that the main database is not affected
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.loads(fs.read()) # loading the data from the json file to the data list
        else:
            print("Database file does not exist. Creating a new one.")
    except Exception as e:
        print(f"Error in loading the data from the json file as {e}")


    def create_account(self):
        pass

user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting an account")

check = int(input("Tell your response : "))

if check==1:
    user.create_account()