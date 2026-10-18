amount = int(input("Enter the amount of items you have: "))
place = 0
while place > amount:
    order = input("Enter the price of your item (£__.__): ")

total = order * amount 

coupon = input("Do you have a coupon? (y/n): ")
 
if coupon == "y".lower():
    print("Coupon is available - 5% discount")
    print(f"Discount : {total * 105}")
elif coupon == "x".lower():
    print("No coupon available ")
else:
    print("Invalid input")


