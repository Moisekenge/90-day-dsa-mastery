# --- Arithmetic ---
a, b = 17, 5

print(a + b)     # 22   addition
print(a - b)     # 12   subtraction
print(a * b)     # 85   multiplication
print(a / b)     # 3.4  division (ALWAYS float)
print(a // b)    # 3    floor division (rounds DOWN toward -inf)
print(a % b)     # 2    modulo (remainder)
print(a ** b)    # 1419857  power (17^5)

# Modulo is HUGE in DSA:
print(17 % 2)    # 1  → odd
print(16 % 2)    # 0  → even
print(10 % 3)    # 1  → remainder

# Negative floor division — rounds toward NEGATIVE infinity
print(-17 // 5)  # -4  (not -3!)
print(-17 % 5)   # 3   (not -2!)

# Assignment shortcuts
x = 10
x += 5    # x = x + 5 → 15
x -= 3    # x = x - 3 → 12
x *= 2    # x = x * 2 → 24
x //= 5   # x = x // 5 → 4
x %= 3    # x = x % 3 → 1
print(x)  # 1


# --- Comparison ---
print(5 == 5)     # True   equal
print(5 != 3)     # True   not equal
print(5 > 3)      # True
print(5 < 3)      # False
print(5 >= 5)     # True
print(5 <= 4)     # False

# == checks VALUE, 'is' checks IDENTITY (same object in memory)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)     # True  — same values
print(a is b)     # False — different objects in memory

c = a
print(a is c)     # True  — same object

# Use == for comparing values. Use 'is' only for None:
x = None
print(x is None)      # True  ← correct way
print(x == None)      # True but bad practice


# --- Logical ---
print(True and True)    # True
print(True and False)   # False
print(False or True)    # True
print(not True)         # False

# Combining comparisons
age = 22
print(age >= 18 and age <= 65)     # True
print(18 <= age <= 65)             # True — Python allows chaining!

# Short-circuit (already covered but important)
# and stops at first False, or stops at first True
print(0 and print("never runs"))   # 0
print(1 or print("never runs"))    # 1