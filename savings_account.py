from Account import Account

def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)
    
    monthly_interest_rate = savings_account.balance * savings_account.interest_rate / 12
    total_interest = monthly_interest_rate * months
    updated_savings_balance = savings_account.balance + total_interest 
  
    savings_account.set_balance(updated_savings_balance)
   
    savings_account.set_balance(updated_savings_balance + total_interest)
     
    return updated_savings_balance, total_interest
