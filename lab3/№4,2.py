arr = []

print("Введите 10 целых чисел:")
for i in range(10):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

# Считаем сумму элементов больше 5
sum_greater_than_5 = 0
for x in arr:
    if x > 5:
        sum_greater_than_5 += x

# Более короткий вариант через генератор списка: sum(x for x in arr if x > 5)

print(f"\nМассив: {arr}")
print(f"Сумма чисел, которые больше 5: {sum_greater_than_5}")