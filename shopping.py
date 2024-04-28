budget = int(input())
price = input()
left_budget = budget
while price != "End":
    price =int(price)
    if left_budget < price:
        print("You went in overdraft!")
        break
    else:
        left_budget -= price
        price = input()
else:
    print("You bought everything needed.")

