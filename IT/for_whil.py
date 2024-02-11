numbers = [11, 2, 10, 3, 1, 2, 4, 11]

max1 = float("-inf")
max2 = float("-inf")


i = 0
while i < len(numbers):
    if numbers[i] > max1:
        max2 = max1
        max1 = numbers[i]
    elif numbers[i] > max2 and numbers[i] != max1:
        max2 = numbers[i]
    i += 1


print(f"max1 {max1}")
print(f"max2 {max2}")

print("=======================")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ==========================================================

uczen = {
    "imie": "Adrian",
    "nazwisko": "Poniatowski",
    "wiek": 26,
    "matematyka": [1, 1, 2, 3, 4, 5],
    "angielski": [2, 3, 4, 5, 6, 1],
    "polski": [5, 3, 2, 10],
}


# ---------------------------------------------------------
def inf(dc):
    for k, v in dc.items():
        print(f"{k}:  {v}")


inf(uczen)
