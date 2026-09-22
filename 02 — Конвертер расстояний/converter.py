print("Конвертер единиц измерения расстояния")
print("Доступные единицы: km, m, cm, mm, mi, yd")

source = input("Исходная единица: ").lower()
target = input("Целевая единица: ").lower()
value = float(input("Введите значение: "))

if source == "km":
    meters = value * 1000
elif source == "m":
    meters = value
elif source == "cm":
    meters = value / 100
elif source == "mm":
    meters = value / 1000
elif source == "mi":
    meters = value * 1609.344
elif source == "yd":
    meters = value * 0.9144
else:
    meters = None

if meters is None:
    print("Неизвестная исходная единица")
elif target == "km":
    result = meters / 1000
    print(f"Результат: {result:.6f} km")
elif target == "m":
    result = meters
    print(f"Результат: {result:.6f} m")
elif target == "cm":
    result = meters * 100
    print(f"Результат: {result:.6f} cm")
elif target == "mm":
    result = meters * 1000
    print(f"Результат: {result:.6f} mm")
elif target == "mi":
    result = meters / 1609.344
    print(f"Результат: {result:.6f} mi")
elif target == "yd":
    result = meters / 0.9144
    print(f"Результат: {result:.6f} yd")
else:
    print("Неизвестная целевая единица")
