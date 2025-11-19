Actual_product_price=float(input("Please Enter the actual product price: "))
Sales_amount=float(input("Please Enter the sales amount: "))
total_profit=Sales_amount-Actual_product_price
if total_profit>0:
    print("The business made a profit of:",total_profit)
elif total_profit<0:
    print("The business got a loss of:",-total_profit)