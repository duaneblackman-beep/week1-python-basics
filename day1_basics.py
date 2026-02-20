# Day 1 — Variables, Data Types, and Operators
# Run this file and then modify each section to experiment

# --- Variables and Data Types ---
name = "Duane"          # string
age = 45                # integer
salary = 95000.50       # float
is_employed = True      # boolean
Country = "USA" #string
State = "NYC"   #string
is_married = True   #boolean
hourly_rate = salary/2800


print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Country:", Country)
print("State:", State)
print("Married:", is_married)
print("Employed:", is_employed)
print("Type of name:", type(name))
print("Type of age:", type(age))


# --- String Operations ---
full_name = "Duane" + " " + "Blackman"   # concatenation
upper_name = full_name.upper()
print("\nFull name:", full_name)
print("Uppercase:", upper_name)
print("Length:", len(full_name))

# --- Math Operators ---
print("\n--- Math ---")
print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 * 7 =", 6 * 7)
print("15 / 4 =", 15 / 4)    # float division
print("15 // 4 =", 15 // 4)  # integer division
print("15 % 4 =", 15 % 4)    # remainder
print("2 ** 8 =", 2 ** 8)    # exponent
# --- User Input ---
user_name = input("What is your name? ")
print("Hello,", user_name)
print("Hello",name,"I see your age is", age , "and you live in", Country, "your hourly rate is", hourly_rate)


# Uncomment the lines below to make it interactive
# user_name = input("What is your name? ")
# print("Hello,", user_name)

# --- CHALLENGE ---
# Modify this file to:
# 1. Add your own variables (city, years_of_experience, etc.)
# 2. Print a sentence that uses at least 3 variables
# 3. Calculate: what is your hourly rate if salary / 2080?
