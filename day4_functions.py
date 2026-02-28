# Day 4 — Functions
# Topics: defining functions, parameters, return values, default parameters,
#         multiple return values, scope, and docstrings

# ─────────────────────────────────────────
# SECTION 1: Defining and calling a function
# ─────────────────────────────────────────
# def — keyword to define a function
# Functions let you write logic once and reuse it anywhere

def ping_server(server):
    print(f"Pinging {server}...")
    print(f"Reply from {server}: OK")

ping_server("web-01")
ping_server("db-01")


# ─────────────────────────────────────────
# SECTION 2: Parameters and return values
# ─────────────────────────────────────────
# Parameters — inputs the function expects
# return — sends a value back to the caller

def get_sla(priority):
    if priority == "critical":
        return 15
    elif priority == "high":
        return 60
    elif priority == "medium":
        return 240
    else:
        return 1440

sla = get_sla("high")
print(f"\nHigh priority SLA: {sla} minutes")


# ─────────────────────────────────────────
# SECTION 3: Multiple parameters
# ─────────────────────────────────────────

def create_ticket(title, priority, assignee):
    print(f"\nTicket created:")
    print(f"  Title:    {title}")
    print(f"  Priority: {priority}")
    print(f"  Assignee: {assignee}")
    print(f"  SLA:      {get_sla(priority)} minutes")

create_ticket("VPN not connecting", "high", "Duane")
create_ticket("Printer offline", "medium", "helpdesk")


# ─────────────────────────────────────────
# SECTION 4: Default parameters
# ─────────────────────────────────────────
# A default value is used when the caller doesn't pass that argument
# Default parameters must come AFTER non-default ones

def create_user(username, role="standard", active=True):
    print(f"\nUser created: {username} | role: {role} | active: {active}")

create_user("jsmith")                          # uses both defaults
create_user("alee", role="admin")              # overrides role only
create_user("bwilson", role="admin", active=False)  # overrides both


# ─────────────────────────────────────────
# SECTION 5: Multiple return values
# ─────────────────────────────────────────
# Python functions can return multiple values as a tuple

def check_server(server):
    # Simulating a health check
    cpu = 72
    memory = 88
    status = "degraded" if memory > 85 else "healthy"
    return status, cpu, memory

status, cpu, memory = check_server("web-01")
print(f"\nweb-01 — status: {status} | CPU: {cpu}% | Memory: {memory}%")


# ─────────────────────────────────────────
# SECTION 6: Scope
# ─────────────────────────────────────────
# Variables defined inside a function only exist inside that function
# Variables defined outside are in the "global" scope

company = "ACME Corp"  # global variable — accessible everywhere

def print_company():
    print(f"Company: {company}")  # can read global variable

def set_local():
    location = "New York"  # local variable — only exists inside this function
    print(f"Location: {location}")

print_company()
set_local()
# print(location)  # this would crash — location doesn't exist outside set_local()


# ─────────────────────────────────────────
# SECTION 7: Docstrings
# ─────────────────────────────────────────
# A docstring is a string right after the def line that documents what the function does
# Accessed via help() or by hovering in VS Code

def escalate_ticket(ticket_id, reason):
    """
    Escalates a ticket to the senior engineer queue.

    Args:
        ticket_id (str): The ticket ID to escalate (e.g. "T001")
        reason (str): Brief description of why it's being escalated

    Returns:
        str: Confirmation message
    """
    return f"Ticket {ticket_id} escalated — reason: {reason}"

result = escalate_ticket("T042", "customer threatening chargeback")
print(f"\n{result}")


# ─────────────────────────────────────────
# EXERCISES — try these yourself
# ─────────────────────────────────────────

# EXERCISE 1:
# Write a function called `categorize_ticket` that takes a `description` string
# and returns a category based on keywords:
#   "network" in description → retun "Network"
#   "password" in description → return "Access"
#   "slow" or "crash" in description → return "Performance"
#   anything else → return "General"
# Hint: use the `in` keyword to check if a word is in a string
# YOUR CODE HERE

def categorize_ticket(description):
    if "network" in description:
        return "Network"
    elif "password" in description:
        return "Access"
    elif "slow" in description or "crash" in description:
        return "Performance"
    else:
        return "General"
status = categorize_ticket("My computer is slow and keeps crashing")
print(f"\nTicket category: {status}")
    


# EXERCISE 2:
# Write a function called `server_report` that takes a list of server names
# and a default parameter `check_type` set to "ping"
# It should loop over the list and print:
#   "Running {check_type} on {server}..."
# Then return the total count of servers checked
# YOUR CODE HERE

def server_report(servers, check_type="ping"):
    count = 0
    for server in servers:
        print(f"Running {check_type} on {server}...")
        count += 1
    return count
servers = ["web-01", "web-02", "db-01"]
count = server_report(servers, "ssj-check")
print(f"\nTotal servers checked: {count}")

# EXERCISE 3:
# Rewrite the grade calculator from day 1 as two clean functions:
#   calculate_grade(percentage) — returns the letter grade
#   print_result(name, percentage) — calls calculate_grade and prints:
#     "Student: {name} | Score: {percentage}% | Grade: {letter}"
# Call print_result for at least 3 students
# YOUR CODE HERE
def calculate_grade(percentage):    
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def print_result(name, percentage):
    letter = calculate_grade(percentage)
    print(f"Student: {name} | Score: {percentage}% | Grade: {letter}")  

print_result("Duane", 92)
print_result("Alice", 85)
print_result("Bob", 73) 