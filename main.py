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

    database = 'data.json'
    data = []

    with open(database) as fs:
        

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