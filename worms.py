coins = [25, 10, 5, 1]  # sorted largest first
amount = 41
count = 0

for coin in coins:
    count += amount // coin   # how many of this coin fit?
    amount %= coin            # what's left?
    print(coin, count, amount)

# 25 → take 1,  remaining 16
# 10 → take 1,  remaining 6
# 5  → take 1,  remaining 1
# 1  → take 1,  remaining 0
# total coins = 4