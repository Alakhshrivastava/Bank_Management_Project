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

    database = 'Bank_management_Project\data.json' # creating a json file to store the data of the user

    data = [] # creating a list to store the data of the user as dummy data so that the main database is not affected

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.loads(fs.read()) # loading the data from the json file to the data list
        else:
            print("Database file does not exist. Creating a new one.")
    except Exception as e:
        print(f"Error in loading the data from the json file as {e}")

    @classmethod # creating a privateclass method to update the data in the json file as we will be using this method in multiple places in the code and we don't want anyone to access this method outside the class(no need to be changed)
    def __update(cls): 
        try:
            with open(cls.database,'w') as fs: #cls will be already pointing to the class
                fs.write(json.dumps(cls.data)) # dumping the data from the data list to the json file
        except Exception as e:
            print(f"Error in updating the data in the json file as {e}")

    """
    Can also be done by using the following code to create a json file if it does not exist and then load the data from the json file to the data list

    @staticmethod # creating a static method to update the data in the json file as we will be using this method in multiple places in the code and we don't want anyone to access this method outside the class
    def update():
        try:
            with open(Bank.database,'w') as fs:
                fs.write(json.dumps(Bank.data)) # dumping the data from the data list to the json file
        except Exception as e:
            print(f"Error in updating the data in the json file as {e}")
            
    """

    def create_account(self):

        # we will ask the user to enter the details of the account and then we will store the data in the json file(The data will be stored in the form of a dictionary and will be passed to the json file as a object)
        info = {
            "name": input("Enter your name : "),
            "age": int(input("Enter your age : ")),
            "email": input("Enter your email : "),
            "pin": input("Enter your 4-digit pin : "),
            "account_number": 1234,
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Invalid age or pin. Please try again.")
        else:   
            print("Account created successfully.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number and pin for future reference.")

            Bank.data.append(info) # appending the data to the data list(dummy data) so that the main database is not affected

            Bank.__update() # calling the update method to update the data in the json file


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