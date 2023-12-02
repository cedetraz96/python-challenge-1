from Account import Account

def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, interest_rate)
    
    monthly_interest_rate = cd_account.balance * cd_account.interest_rate / 12
    total_interest = monthly_interest_rate * months
    updated_cd_balance = cd_account.balance + total_interest 
  
    cd_account.set_balance(updated_cd_balance)
   
    cd_account.set_balance(updated_cd_balance + total_interest)
     
    return updated_cd_balance, total_interest
