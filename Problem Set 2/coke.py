coins = [5, 25, 10]
total = 0

while total < 50 :
    print(f"Amount Due: {50 - total}")
    coin = int(input("Insert Coin: "))
    if coin in coins:
        total += coin

print(f"Change Owed: {total - 50}")
