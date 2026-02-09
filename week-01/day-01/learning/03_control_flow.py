# --- if / elif / else ---
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")        # this prints
elif score >= 70:
    print("C")
else:
    print("F")

# Only ONE branch executes — first match wins, rest skipped

# Multiple conditions
age = 22
has_license = True

if age >= 16 and has_license:
    print("Can drive")
elif age >= 16 and not has_license:
    print("Get a license first")
else:
    print("Too young")


# --- Ternary Operator ---
# result = value_if_true if condition else value_if_false
x = 15
label = "even" if x % 2 == 0 else "odd"
print(label)    # odd

# You'll use this constantly in LeetCode for one-liners
bigger = a if a > b else b     # max of two values
sign = "positive" if x > 0 else "negative" if x < 0 else "zero"


# --- match / case (Python 3.10+) ---
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command")    # _ is the default/wildcard

# Honestly you won't use match/case much in DSA. if/elif is king.


# --- Nested Conditionals ---
num = -5

if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")     # prints
else:
    print("Zero")

# Better way — flatten it:
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Keep nesting shallow. Deep nesting = hard to read = bugs.


# --- Common DSA patterns with control flow ---

# Guard clause: return early instead of nesting
def find_value(lst, target):
    if not lst:              # empty list check
        return -1
    if len(lst) == 1:        # single element
        return 0 if lst[0] == target else -1
    # main logic here...
    return -1

# Boundary checking (you'll write this in EVERY grid/matrix problem)
rows, cols = 5, 5
r, c = 2, 3
if 0 <= r < rows and 0 <= c < cols:
    print("Valid position")