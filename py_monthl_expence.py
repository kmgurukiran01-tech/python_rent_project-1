#input from users
#Rent of house/flat
#food spend
#electric charge
#water bill
from http.client import parse_headers

members=int(input("Enter the number of members: "))
rent=int(input("Enter the rent: "))
Food_spend=int(input("Enter the food spend: "))
electricity=int(input("Enter the electricity_bill: "))
water_bill=int(input("Enter the water bill: "))
Total=rent+Food_spend+electricity+water_bill
perhead=Total/members
print("Total amount we have to pay: ",Total)

print("per head: ",perhead)