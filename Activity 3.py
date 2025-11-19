number_of_users=int(input("Enter the number: "))
What_amount=int(input("Enter the number to compare with: "))

if number_of_users>What_amount:
    print("The number is greater than", What_amount)
elif number_of_users<What_amount:
    print("The number is less than", What_amount)
else:
    print("The number is equal to", What_amount)