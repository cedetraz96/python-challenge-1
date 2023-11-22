# Import the create_cd_account and create_savings_account functions

from Account import Account
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function

def main():

# This function prompts the user to enter the savings and cd account balance, interest rate,
# and the length of months to determine the interest gained.
# It displays the interest earned on the savings and CD accounts and updates the balances.
  
# Prompt the user to set the savings balance, interest rate, and months for the savings account.
  
    savings_balance = float(input("Enter the account balance: "))
    savings_interest = float(input("Enter the account interest: "))
    savings_maturity = int(input("Enter the account maturity in months: "))
        
# Call the create_savings_account function and pass the variables from the user.

updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

def create_savings_account(balance, interest_rate, months): 
    monthly_interest_rate = savings_balance * interest_rate / 12
    total_interest = monthly_interest_rate * savings_maturity
    updated_savings_balance = savings_balance + total_interest 
    return updated_savings_balance, total_interest

# Print out the interest earned and updated savings account balance with interest earned for the given months.
   
    print(f"The account balance after {savings_maturity} months is {updated_balance: .2f}.")

# Prompt the user to set the CD balance, interest rate, and months for the CD account.
   
    cd_balance = float(input("Enter the CD balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_maturity = int(input("Enter the CD maturity in months: "))

# Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

def create_cd_account(balance, interest_rate, months):
    monthly_interest_rate = cd_balance * interest_rate / 12
    total_interest = monthly_interest_rate * cd_maturity
    updated_cd_balance = cd_balance + total_interest
    return updated_cd_balance, total_interest

# Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The account balance after {maturity} months is {updated_balance; .2f}.")

if __name__ == "__main__":

# Call the main function.

    main()
