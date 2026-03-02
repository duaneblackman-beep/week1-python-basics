#!/usr/bin/env python
# coding: utf-8

# # Day 5 — Lists and Dictionaries
# **Topics:** lists, indexing, slicing, list methods, dicts, dict methods, nested dicts, list of dicts
# 
# Run each cell with **Shift + Enter**. Read the output. Then do the exercises at the bottom.

# ---
# ## Section 1 — Lists
# A list is an **ordered collection** of items. Items can be any type. Lists use square brackets `[]`.

# In[1]:


open_tickets = ["T001", "T002", "T003", "T004", "T005"]
print(open_tickets)
print(type(open_tickets))


# ---
# ## Section 2 — Indexing and Slicing
# - **Indexing** — access one item by position (starts at 0)
# - **Slicing** — access a range with `[start:end]` (end is not included)
# - Negative index `-1` means the last item

# In[2]:


open_tickets = ["T001", "T002", "T003", "T004", "T005"]

print(open_tickets[0])    # first item
print(open_tickets[-1])   # last item
print(open_tickets[1:3])  # index 1 and 2 (T002, T003)
print(open_tickets[:3])   # first 3
print(open_tickets[2:])   # from index 2 to end


# ---
# ## Section 3 — List Methods
# Methods are built-in functions that belong to a list object. Called with `list.method()`.

# In[3]:


servers = ["web-01", "web-02", "db-01"]

servers.append("db-02")        # add to end
print("After append:", servers)

servers.insert(1, "web-03")    # insert at index 1
print("After insert:", servers)

servers.remove("web-02")       # remove by value
print("After remove:", servers)

popped = servers.pop()         # remove and return last item
print(f"Popped: {popped}")
print("After pop:", servers)

print(f"Count: {len(servers)}")
print(f"'web-01' in list: {'web-01' in servers}")


# ---
# ## Section 4 — Dictionaries
# A dict stores **key-value pairs** — like a lookup table. Keys must be unique. Uses curly braces `{}`.

# In[4]:


ticket = {
    "id": "T042",
    "title": "VPN not connecting",
    "priority": "high",
    "assignee": "Duane",
    "resolved": False
}

print(ticket["title"])                          # access by key
print(ticket.get("priority"))                   # safer — returns None if missing
print(ticket.get("category", "Uncategorized"))  # default if key missing

ticket["resolved"] = True       # update a value
ticket["category"] = "Network"  # add a new key
print(ticket)


# ---
# ## Section 5 — Dict Methods
# `.keys()`, `.values()`, `.items()` — the three most important dict methods.

# In[5]:


ticket = {
    "id": "T042",
    "title": "VPN not connecting",
    "priority": "high",
    "assignee": "Duane",
    "category": "Network"
}

print(ticket.keys())    # all keys
print(ticket.values())  # all values
print(ticket.items())   # key-value pairs as tuples

# Loop over items — the most common pattern
print("\nTicket details:")
for key, value in ticket.items():
    print(f"  {key}: {value}")

# Check if a key exists
if "assignee" in ticket:
    print(f"\nAssigned to: {ticket['assignee']}")

# Remove a key
ticket.pop("id")
print("\nAfter pop:", ticket)


# ---
# ## Section 6 — Nested Dictionaries
# A dict can contain another dict as a value. Common pattern for structured records (think: database rows).

# In[6]:


servers = {
    "web-01": {"ip": "10.0.0.1", "status": "healthy", "cpu": 42},
    "web-02": {"ip": "10.0.0.2", "status": "down",    "cpu": 0},
    "db-01":  {"ip": "10.0.0.3", "status": "healthy", "cpu": 78},
}

# Access nested value — outer key first, then inner key
print(servers["web-01"]["status"])
print(servers["db-01"]["cpu"])

# Loop over all servers
print("\nServer Status Report:")
for name, info in servers.items():
    print(f"  {name} ({info['ip']}) — {info['status']} | CPU: {info['cpu']}%")


# ---
# ## Section 7 — List of Dictionaries
# The most common real-world pattern. Think: rows in a spreadsheet, results from a database, API responses.
# 
# This is **exactly** how your ticket triage data from Project 2 works.

# In[7]:


tickets = [
    {"id": "T001", "priority": "high",   "status": "open"},
    {"id": "T002", "priority": "low",    "status": "closed"},
    {"id": "T003", "priority": "medium", "status": "open"},
    {"id": "T004", "priority": "high",   "status": "open"},
    {"id": "T005", "priority": "low",    "status": "closed"},
]

print("Open tickets:")
for ticket in tickets:
    if ticket["status"] == "open":
        print(f"  {ticket['id']} — {ticket['priority']} priority")


# ---
# ## Exercise 1 — List operations
# Create a list called `team` with 5 IT staff names.
# - Print the first name, last name, and the middle 3 as a slice
# - Add a new member with `append()`, remove one with `remove()`
# - Print the final list and total count

# In[18]:


# List creation here
team = ["Duane", "Steve", "Tim", "Andy", "Jim"]
print (team[0])
print (team[-1])
print (team[1:4])
team.append("Peter")
team.remove("Tim")
print(team)
print(f"Total team members: {len(team)}")



# ## Exercise 2 — Laptop asset dictionary
# Create a dictionary called `asset` representing a laptop with these fields:
# `hostname`, `user`, `os`, `ram_gb`, `encrypted` (True/False)
# - Print each field using a loop over `.items()`
# - Update `ram_gb` to 32
# - Add a new field `ticket_count` set to 0
# - Print the updated dict

# In[29]:


# Asset
asset = {
    "hostname": "laptop-01",
    "user": "john.doe",
    "os": "Windows 11",
    "ram_gb": 16,
    "encrypted": True
}
for field in asset:
    print(field)

asset["ram_gb"] = 32
for key in asset.values():
    print(key)

asset["ticke_count"] = 0
print(asset)




# ## Exercise 3 — summarize_tickets()
# Using the tickets list from Section 7, write a function `summarize_tickets(tickets)` that:
# - Counts total tickets
# - Counts open tickets
# - Counts high priority tickets
# - Prints a summary report
# 
# Call it with the tickets list.

# In[45]:


tickets = [
    {"id": "T001", "priority": "high",   "status": "open"},
    {"id": "T002", "priority": "low",    "status": "closed"},
    {"id": "T003", "priority": "medium", "status": "open"},
    {"id": "T004", "priority": "high",   "status": "open"},
    {"id": "T005", "priority": "low",    "status": "closed"},
]

#Ticket count
print("\nTicket count:")
for ticket in tickets:
    ticket_count = len(tickets)
print(f"There are",ticket_count, "tickets")

#Open Tickets
print("\nOpen Tickets:")
open_ticket = 0
for ticket in tickets:
    if ticket["status"] == "open":
        open_ticket = open_ticket + 1
print(f"There are curretly", open_ticket, "open tickets")

#High Priotity Tickets
print("\nHigh priority tickets:")
hp_ticket = 0
for ticket in tickets:
    if ticket["priority"] == "high":
        hp_ticket = hp_ticket + 1
print(f"There are curretly", hp_ticket, "high prioriy tickets")

#Summary Report
print("\nSummary Report")
# Table header
print(f"{'ID':<5} {'Priority':<15} {'Status':<10}")
print("-" * 30)

# Table rows
for ticket in tickets:
    print(f"{ticket['id']:<5} {ticket['priority']:<15} {ticket['status']:<10}")








# ---
# ## Drill — filter_tickets()
# Write a function `filter_tickets(tickets, status)` that:
# - Takes the tickets list and a status string (`"open"` or `"closed"`)
# - Returns a **new list** containing only tickets matching that status
# 
# Test it with both `"open"` and `"closed"` and print the results.

# In[65]:


tickets = [
    {"id": "T001", "priority": "high",   "status": "open"},
    {"id": "T002", "priority": "low",    "status": "closed"},
    {"id": "T003", "priority": "medium", "status": "open"},
    {"id": "T004", "priority": "high",   "status": "open"},
    {"id": "T005", "priority": "low",    "status": "closed"},
]

# YOUR CODE HERE

def filter_tickets(tickets, status):
    filtered = []
    for ticket in tickets:
        if ticket["status"] == status:
            filtered.append(ticket)
    print(filtered)

filter_tickets(tickets,"closed")



# ---
# ## Build — IT Asset Tracker
# Build a small asset tracking system using a **dict of dicts**.
# 
# Each asset is stored by hostname as the key. Example structure:
# ```python
# assets = {
#     "LAPTOP-001": {"user": "jsmith", "os": "Windows 11", "ram_gb": 16, "encrypted": True},
#     ...
# }
# ```
# 
# Write these 4 functions:
# 1. `add_asset(assets, hostname, user, os, ram_gb, encrypted)` — adds a new record
# 2. `update_asset(assets, hostname, field, value)` — updates one field on an existing asset
# 3. `report(assets)` — prints a formatted table of all assets
# 4. `find_unencrypted(assets)` — returns a list of hostnames where `encrypted=False`
# 
# Then run a demo: add 3 assets, update one, print the report, print unencrypted machines.

# In[86]:


# Start with an empty asset store
assets = {}

# YOUR CODE HERE

def add_assets(assets,hostname,users,os,ram_gb,encrypted):#You are adding a dictionary, format accordingly
    assets[hostname] = {
        "users": users,
        "os" : os,
        "ram_gb": ram_gb,
        "encrypted": encrypted
    }        
def update_assets(assets,hostname,field,value):
    assets[hostname][field] = value


def report_assets(assets):
    print(f"{'Hostname':<15} {'User':<10} {'OS':<15} {'RAM (GB)':<10} {'Encrypted':<10}")
    print("-" * 60)
    for hostname, info in assets.items():
        print(f"{hostname:<15} {info['users']:<10} {info['os']:<15} {info['ram_gb']:<10} {str(info['encrypted']):<10}")

def find_unencrypted(assets, field, value):
    for hostname, info in assets.items():
        if info[field] == value:
            print(f"{hostname}: {info}")  

add_assets(assets, "LAPTOP-01", "jsmith", "Windows 11", 16, True)
add_assets(assets, "LAPTOP-02", "jmo", "Windows 10", 32, False)
add_assets(assets, "LAPTOP-03", "dblackman", "Linux", 16, True)
update_assets(assets, "LAPTOP-03","users", "dblack01")
add_assets(assets, "LAPTOP-04", "jmost", "Windows 12", 32, False)
report_assets(assets)
find_unencrypted(assets, "encrypted", False)




# In[ ]:




