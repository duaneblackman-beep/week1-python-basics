# Day 5 — Lists and Dictionaries
# Topics: creating lists, list methods, indexing, slicing,
#         creating dicts, dict methods, nested dicts, combining with loops and functions

# ─────────────────────────────────────────
# SECTION 1: Lists
# ─────────────────────────────────────────
# A list is an ordered collection of items
# Items can be any type — strings, numbers, even other lists
# Lists use square brackets []

open_tickets = ["T001", "T002", "T003", "T004", "T005"]
print(open_tickets)


# ─────────────────────────────────────────
# SECTION 2: Indexing and slicing
# ─────────────────────────────────────────
# Indexing — access one item by position (starts at 0)
# Slicing  — access a range of items [start:end] (end is not included)

print(open_tickets[0])      # first item  → "T001"
print(open_tickets[-1])     # last item   → "T005"
print(open_tickets[1:3])    # index 1 and 2 → ["T002", "T003"]
print(open_tickets[:3])     # first 3 items → ["T001", "T002", "T003"]
print(open_tickets[2:])     # from index 2 to end → ["T003", "T004", "T005"]


# ─────────────────────────────────────────
# SECTION 3: List methods
# ─────────────────────────────────────────
# Methods are built-in functions that belong to a list object

servers = ["web-01", "web-02", "db-01"]

servers.append("db-02")         # add to end
print(servers)

servers.insert(1, "web-03")     # insert at index 1
print(servers)

servers.remove("web-02")        # remove by value
print(servers)

popped = servers.pop()          # remove and return last item
print(f"Removed: {popped}")
print(servers)

print(f"Total servers: {len(servers)}")     # count items
print(f"web-01 in list: {'web-01' in servers}")  # check membership


# ─────────────────────────────────────────
# SECTION 4: Dictionaries
# ─────────────────────────────────────────
# A dict stores key-value pairs — like a lookup table
# Keys must be unique, values can be anything
# Dicts use curly braces {}

ticket = {
    "id": "T042",
    "title": "VPN not connecting",
    "priority": "high",
    "assignee": "Duane",
    "resolved": False
}

print(ticket["title"])          # access by key
print(ticket.get("priority"))   # safer access — returns None if key missing
print(ticket.get("category", "Uncategorized"))  # default if key missing

ticket["resolved"] = True       # update a value
ticket["category"] = "Network"  # add a new key
print(ticket)


# ─────────────────────────────────────────
# SECTION 5: Dict methods
# ─────────────────────────────────────────

print(ticket.keys())            # all keys
print(ticket.values())          # all values
print(ticket.items())           # all key-value pairs as tuples

# Check if a key exists
if "assignee" in ticket:
    print(f"Assigned to: {ticket['assignee']}")

# Remove a key
ticket.pop("resolved")
print(ticket)


# ─────────────────────────────────────────
# SECTION 6: Nested dictionaries
# ─────────────────────────────────────────
# A dict can contain another dict as a value
# Common pattern for representing structured records

servers = {
    "web-01": {"ip": "10.0.0.1", "status": "healthy", "cpu": 42},
    "web-02": {"ip": "10.0.0.2", "status": "down",    "cpu": 0},
    "db-01":  {"ip": "10.0.0.3", "status": "healthy", "cpu": 78},
}

print(servers["web-01"]["status"])      # access nested value
print(servers["db-01"]["cpu"])

# Loop over nested dict
print("\nServer status report:")
for name, info in servers.items():
    print(f"  {name} ({info['ip']}) — {info['status']} | CPU: {info['cpu']}%")


# ─────────────────────────────────────────
# SECTION 7: List of dictionaries
# ─────────────────────────────────────────
# The most common real-world pattern — a list of records
# Think: rows in a spreadsheet, results from a database query

tickets = [
    {"id": "T001", "priority": "high",   "status": "open"},
    {"id": "T002", "priority": "low",    "status": "closed"},
    {"id": "T003", "priority": "medium", "status": "open"},
    {"id": "T004", "priority": "high",   "status": "open"},
]

print("\nOpen tickets:")
for ticket in tickets:
    if ticket["status"] == "open":
        print(f"  {ticket['id']} — {ticket['priority']} priority")


# ─────────────────────────────────────────
# EXERCISES — try these yourself
# ─────────────────────────────────────────

# EXERCISE 1:
# Create a list called `team` with 5 IT staff names
# Print the first name, last name, and the middle 3 as a slice
# Add a new member with append(), remove one with remove()
# Print the final list and total count
# YOUR CODE HERE


# EXERCISE 2:
# Create a dictionary called `asset` that represents a laptop with these fields:
#   hostname, user, os, ram_gb, encrypted (True/False)
# Print each field using a loop over .items()
# Update the ram_gb to 32, add a new field `ticket_count` set to 0
# YOUR CODE HERE


# EXERCISE 3:
# Using the tickets list from Section 7:
# Write a function called `summarize_tickets(tickets)` that:
#   - counts total tickets
#   - counts open tickets
#   - counts high priority tickets
#   - prints a summary report
# Call it with the tickets list
# YOUR CODE HERE
