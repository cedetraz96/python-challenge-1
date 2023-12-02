from savings_account import create_savings_account
from cd_account import create_cd_account
from cd_account import create_cd_account

def main():
    
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the account interest rate: "))
    savings_maturity = int(input("Enter the account maturity in months: "))     
    updated_savings_balance = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"The account balance after {savings_maturity} months is ${updated_savings_balance:.2f}.")

    savings_balance = float(input("Enter the savings balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_maturity = int(input("Enter the CD maturity in months: "))
    updated_cd_balance, interest_rate = create_cd_account(savings_balance, cd_interest, cd_maturity)
    print(f"The account balance after {cd_maturity} months is ${updated_cd_balance:.2f}.")

if __name__ == "__main__":
    main()


