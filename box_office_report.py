name=input("Name of Movie: ")
num1=int(input("How many adult tickets were sold? "))
num2=int(input("How many child tickets were sold? "))
num1=num1*10
num2=num2*6
numG=num1+num2 
numN=numG*.2
amount=numG-numN
print()
print("Movie Name: ",name)
print("Adult Tickets Sold: ",num1)
print("Child Tickets Sold: ",num2)
print("Gross Box Office Profit: $",numG)
print("Net Box Office Profit: $",numN)
print("Amount Paid to Distributor: $",amount)
