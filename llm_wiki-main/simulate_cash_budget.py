def simulate_cash_budget():
    # 1. SETUP: Input Data (Forecasts)
    months = ["January", "February", "March", "April"]
    sales_forecast = [100000, 120000, 80000, 150000]
    
    # Assumptions
    initial_cash = 15000
    min_cash_balance = 10000
    collection_rate_current = 0.20  
    collection_rate_next = 0.80     
    purchases_rate = 0.50           
    fixed_expenses = 30000          
    interest_rate = 0.01            
    
    cash_balance = initial_cash
    borrowing = 0
    
    receivable_from_prev = 60000 
    
    header = f"{'Month':<10} | {'Receipts':<10} | {'Disburs.':<10} | {'Net CF':<10} | {'Debt':<10} | {'Final Cash':<10}"
    print("\n" + "="*75)
    print("                 MONTHLY CASH BUDGET SIMULATION ")
    print("="*75)
    print(header)
    print("-" * 75)

    for i, month in enumerate(months):
        current_sales = sales_forecast[i]
        cash_from_current = current_sales * collection_rate_current
        cash_from_prev = receivable_from_prev
        total_receipts = cash_from_current + cash_from_prev
        
        receivable_from_prev = current_sales * collection_rate_next
        
        next_sales = sales_forecast[i+1] if i+1 < len(months) else sales_forecast[i]
        purchases = next_sales * purchases_rate
        total_disbursements = purchases + fixed_expenses
        
        net_cf = total_receipts - total_disbursements
        interest_payment = borrowing * interest_rate
        prelim_balance = cash_balance + net_cf - interest_payment
        
        financing_needed = 0
        repayment = 0
        
        if prelim_balance < min_cash_balance:
            financing_needed = min_cash_balance - prelim_balance
            borrowing += financing_needed
            cash_balance = min_cash_balance
        else:
            surplus = prelim_balance - min_cash_balance
            if borrowing > 0:
                repayment = min(surplus, borrowing)
                borrowing -= repayment
                cash_balance = prelim_balance - repayment
            else:
                cash_balance = prelim_balance

        print(f"{month:<10} | {total_receipts:10.0f} | {total_disbursements:10.0f} | {net_cf:10.0f} | {borrowing:10.0f} | {cash_balance:10.0f}")

    print("="*75)
    print(f"\nAudit Note: Minimum Cash Balance requirement of €{min_cash_balance} was maintained.")

if __name__ == "__main__":
    simulate_cash_budget()

if __name__ == "__main__":
    simulate_cash_budget()
