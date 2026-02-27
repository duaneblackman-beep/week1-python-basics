# Day 2 — Conditionals
# Topics: if, elif, else, comparison operators, logical operators, nested conditionals

# ─────────────────────────────────────────
# SECTION 1: Basic if/elif/else
# ─────────────────────────────────────────

# A ticket priority router — given a priority level, print the response SLA
priority = "high"

if priority == "critical":
    print("SLA: 15 minutes — page on-call immediately")
elif priority == "high":
    print("SLA: 1 hour — assign to senior engineer")
elif priority == "medium":
    print("SLA: 4 hours — assign to next available engineer")
else:
    print("SLA: 24 hours — add to backlog")


# ─────────────────────────────────────────
# SECTION 2: Comparison operators
# ─────────────────────────────────────────
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

cpu_usage = 87

if cpu_usage >= 90:
    print("ALERT: CPU critical")
elif cpu_usage >= 75:
    print("WARNING: CPU elevated")
else:
    print("OK: CPU normal")


# ─────────────────────────────────────────
# SECTION 3: Logical operators (and, or, not)
# ─────────────────────────────────────────

# and — both conditions must be True
# or  — at least one condition must be True
# not — flips True to False, False to True

is_authenticated = True
is_admin = False

if is_authenticated and is_admin:
    print("Access granted: admin portal")
elif is_authenticated and not is_admin:
    print("Access granted: standard portal")
else:
    print("Access denied: please log in")


# ─────────────────────────────────────────
# SECTION 4: Chained comparisons
# ─────────────────────────────────────────

# Python lets you chain comparisons — unique to Python
disk_usage = 68

if 0 <= disk_usage < 70:
    print("Disk: healthy")
elif 70 <= disk_usage < 90:
    print("Disk: monitor closely")
else:
    print("Disk: critical — escalate now")


# ─────────────────────────────────────────
# SECTION 5: Nested conditionals
# ─────────────────────────────────────────

# A nested conditional is an if statement inside another if statement
# Use sparingly — too many levels gets hard to read

user_role = "engineer"
ticket_region = "US"

if user_role == "engineer":
    if ticket_region == "US":
        print("Assigned to: US engineering queue")
    else:
        print("Assigned to: international engineering queue")
elif user_role == "manager":
    print("Assigned to: management review queue")
else:
    print("Assigned to: general queue")

# ─────────────────────────────────────────
# EXERCISES — try these yourself
# ─────────────────────────────────────────

# EXERCISE 1:
# Write an if/elif/else block that takes a variable called `ping_ms`
# and prints:
#   "Excellent" if under 20ms
#   "Good" if 20–50ms
#   "Acceptable" if 51–100ms
#   "Poor" if over 100ms

ping_ms = 45

if ping_ms < 20:
    print("Excellent")
elif 20 <= ping_ms <= 50:
    print("Good")
elif 51 <= ping_ms <= 100:
    print("Acceptable")
else:
    print("Poor")




# EXERCISE 2:
# Write a condition that checks two variables:
#   `vpn_connected` (True/False)
#   `office_network` (True/False)
# Print "Remote access OK" only if vpn is connected AND not on office network
# Print "On-site access OK" only if on office network
# Print "No access" otherwise

vpn_connected = True
office_network = False
# YOUR CODE HERE
if vpn_connected and not office_network:
    print("Remote access OK")
elif office_network:
    print("On-site access OK")
else:    print("No access") 

# EXERCISE 3:
# Take the grade calculator from day 1 and rewrite calculate_grade()
# using a single chained comparison per condition instead of just >=
# Example: 80 <= percentage < 90 instead of percentage >= 80

# YOUR CODE HERE
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

percentage = float(input("Enter your percentage grade: "))
print(f"Your letter grade is: {calculate_grade(percentage)}")