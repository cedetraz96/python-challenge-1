from Account import Account
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():

    savings_balance = float(input("Enter the account balance: "))
    savings_interest = float(input("Enter the account interest: "))
    savings_maturity = int(input("Enter the account maturity in months: "))
        
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

def create_savings_account(balance, interest_rate, months): 
    monthly_interest_rate = savings_balance * interest_rate / 12
    total_interest = monthly_interest_rate * savings_maturity
    updated_savings_balance = savings_balance + total_interest 
    return updated_savings_balance, total_interest

     print(f"The account balance after {savings_maturity} months is {updated_balance: .2f}.")
 
    cd_balance = float(input("Enter the CD balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_maturity = int(input("Enter the CD maturity in months: "))

    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

def create_cd_account(balance, interest_rate, months):
    monthly_interest_rate = cd_balance * interest_rate / 12
    total_interest = monthly_interest_rate * cd_maturity
    updated_cd_balance = cd_balance + total_interest
    return updated_cd_balance, total_interest

    print(f"The account balance after {maturity} months is {updated_balance; .2f}.")

if __name__ == "__main__":

    main()
