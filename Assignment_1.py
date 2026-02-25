numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
print("Yes" if 5 in numbers else "No")

modified = numbers[1:-1]
print(tuple(sorted(modified)))