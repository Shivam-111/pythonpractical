prices = tuple(map(int, input("Enter item prices separated by space: ").split()))

print(len(prices))
print(min(prices))
print(max(prices))
print(tuple(sorted(prices)))
print(prices.count(max(prices)))