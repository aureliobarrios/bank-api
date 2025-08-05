from bank import Bank
from user import BankUser
bank_one = Bank("INSERT BANK NAME HERE")
#should be an error, we dont want to be able to access the bank data
#bank_one.__bank_data

user_one = BankUser("USERNAME", "PASSWORD", bank_one)

#should be an error, we dont want to be able to access users password
#user_one.__password

#output should be zero
user_one.check_balance()

user_one.deposit(150)

user_one.withdraw(50)

#output should be 100
user_one.check_balance()

#should not work since balance is only 50
user_one.withdraw(2000)