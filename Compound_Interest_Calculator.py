account = 100
interest_rate = 0.004
years = 3

print(f"Initial amount: {amount}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"years{counter}: {account}")
    counter += 1
