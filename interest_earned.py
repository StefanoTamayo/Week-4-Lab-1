principal=float(input("What is the principal amount? "))
interest=float(input("What is the interest rate? "))
rate=interest/100
compound=float(input("How many times compounded? "))
amount=principal*((1+(rate/compound))**compound)
amount=amount-principal
Interest_Amount=rate*principal
print()
print("Interest Rate:",interest,"%")
print("Times Compounded:",compound)
print("Principal:",principal)
print("Interest:",Interest_Amount)
print("Amount in Savings:",amount)
