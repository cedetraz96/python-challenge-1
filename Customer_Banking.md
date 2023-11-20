from savings_account import savings_account
from cd_account import cd_account

def create_savings_account(balance, interest_rate, maturity):
    
    interest_earned = balance * interest_rate * maturity / 12
    updated_balance = balance + interest_earned
    return updated_balance, interest_earned

def user_input():
   
    balance = float(input(Enter the account balance: ))
    interest_rate = float(input(Enter the account interest rate: ))
    maturity = float(input(Enter the account maturity in months: ))
    updated_balance, _ = create_savings_account(balance, interest_rate, maturity)
    
    print(fThe account balance after {maturity} months is {updated_balance}.)
    return maturity

def calculate_updated_balance(balance, interest_rate, maturity):
  
    interest_earned = balance * interest_rate * maturity / 12
    updated_balance = balance + interest_earned
    return updated_balance, interest_earned

def print_results(updated_balance, maturity):
    print(fThe account balance after {maturity} months is {updated_balance}.)

def format_currency(value):
    return f

if __name__ == __main__:
    
    savings_balance, savings_interest, savings_maturity = user_input()
    updated_savings_balance, interest_earned_savings = calculate_updated_balance(savings_balance, savings_interest, savings_maturity)
    print_results(updated_savings_balance, savings_maturity)

    cd_balance, cd_interest, cd_maturity = user_input()
    updated_cd_balance, interest_earned_cd = calculate_updated_balance(cd_balance, cd_interest, cd_maturity)
    print_results(updated_cd_balance, cd_maturity)
