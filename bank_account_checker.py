bank_account = 140000

if bank_account < 100000:
    difference_to_100k = 100000 - bank_account
    minimum_amount = difference_to_100k + bank_account
    print(f"Here's some money, Sport:{difference_to_100k}")
elif bank_account == 100000:
    print("You have One Hundred Thousand Dollars")
elif bank_account > 150000:
    print("You're rich! oh and you're getting taxed")
else:
    print("You're sitting pretty my friend")
