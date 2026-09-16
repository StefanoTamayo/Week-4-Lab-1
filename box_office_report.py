#Stefano Tamayo
#CMP-131-80230
#Week 4
#Lab 2
#Box Office Report
#9/16/26

name=input("Name of Movie: ")
num1=int(input("How many adult tickets were sold? "))
num2=int(input("How many child tickets were sold? "))
num11=num1*10
num22=num2*6
numG=num11+num22
numN=numG*.2
amount=numG-numN
print()
print("Movie Name: ",name)
print("Adult Tickets Sold: ",num1)
print("Child Tickets Sold: ",num2)
print(f"Gross Box Office Profit: ${numG:,.2f}")
print(f"Net Box Office Profit: ${numN:,.2f}")
print(f"Amount Paid to Distributor: ${amount:,.2f}")
