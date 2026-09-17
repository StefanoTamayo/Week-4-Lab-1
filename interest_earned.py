#Stefano Tamayo
#CMP-131-80230
#Week 4
#Lab 2
#Box Office Report
#9/16/26

principal=float(input("What is the principal amount? "))
interest=float(input("What is the interest rate? "))
rate=interest/100
compound=float(input("How many times compounded? "))
amount=principal*((1+(rate/compound))**compound)
Interest_Amount=amount-principal
savings=Interest_Amount+principal
print()
print("Interest Rate:",interest,"%")
print("Times Compounded:",compound)
print(f"Principal: ${principal:,.2f}")
print(f"Interest: ${Interest_Amount:,.2f}")
print(f"Amount in Savings: ${savings:,.2f}")
