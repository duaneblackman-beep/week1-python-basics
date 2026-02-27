# Day 3 — Loops
# Topics: for loops, while loops, range(), break, continue, looping over lists and dicts

# ─────────────────────────────────────────
# SECTION 1: for loop
# ─────────────────────────────────────────
# A for loop runs a block of code once for each item in a sequence

servers = ["web-01", "web-02", "db-01", "db-02"]

for server in servers:
    print(f"Pinging {server}....")


# ─────────────────────────────────────────
# SECTION 2: range()
# ─────────────────────────────────────────
# range() generates a sequence of numbers
# range(5)      → 0, 1, 2, 3, 4
# range(1, 6)   → 1, 2, 3, 4, 5
# range(0, 10, 2) → 0, 2, 4, 6, 8  (step of 2)

print("\nRetry attempts:")
for attempt in range(1, 4):
    print(f"  Attempt {attempt} of 3...")
print("Connection attempts completed.")


# ─────────────────────────────────────────
# SECTION 3: while loop
# ─────────────────────────────────────────
# A while loop keeps running as long as a condition is True
# Use when you don't know in advance how many iterations you need

connection_attempts = 0
max_attempts = 3
connected = False

while not connected and connection_attempts < max_attempts:
    connection_attempts += 1
    print(f"Connecting... attempt {connection_attempts}")
    if connection_attempts == 2:  # simulate success on attempt 2
        connected = True

if connected:
    print("Connection established.")
else:
    print("Failed to connect after 3 attempts.")


# ─────────────────────────────────────────
# SECTION 4: break and continue
# ─────────────────────────────────────────
# break  — exit the loop immediately
# continue — skip the rest of this iteration, go to next one

tickets = ["T001", "T002", "ESCALATE", "T003", "T004"]

print("\nProcessing tickets:")
for ticket in tickets:
    if ticket == "ESCALATE":
        print("  Escalation ticket found — stopping queue")
        break
    print(f"  Processing {ticket}")

print("\nSkipping closed tickets:")
statuses = ["open", "closed", "open", "closed", "open"]
for i, status in enumerate(statuses):
    if status == "closed":
        continue
    print(f"  Ticket {i + 1} is open — processing")


# ─────────────────────────────────────────
# SECTION 5: looping over a dictionary
# ─────────────────────────────────────────
# .items() gives you both the key and value on each iteration

server_status = {
    "web-01": "healthy",
    "web-02": "down",
    "db-01": "healthy",
    "db-02": "degraded"
}

print("\nServer health report:")
for server, status in server_status.items():
    if status != "healthy":
        print(f"  ALERT: {server} is {status}")
    else:
        print(f"  OK: {server}")


# ─────────────────────────────────────────
# SECTION 6: nested loops
# ─────────────────────────────────────────
# A loop inside a loop — the inner loop runs completely for each outer iteration
# Use carefully — can get slow with large data

datacenters = ["NYC", "LON"]
racks = ["rack-A", "rack-B"]

print("\nDatacenter inventory:")
for dc in datacenters:
    for rack in racks:
        print(f"  {dc} / {rack}")


# ─────────────────────────────────────────
# EXERCISES — try these yourself
# ─────────────────────────────────────────

# EXERCISE 1:
# Loop over this list of CPU readings and print "ALERT" for any reading over 85
# otherwise print "OK"
cpu_readings = [42, 78, 91, 55, 88, 63, 95]
# YOUR CODE HERE

print("\nCpu readings:")
cpu_readings = [42, 78, 91, 55, 88, 63, 95]

for cpu in cpu_readings:
    if cpu > 85:
        print("Alert")
    else:
        print("ok")
print("Finished processing CPU readings.")


# EXERCISE 2:
# Use a while loop that asks the user to enter a password
# Keep asking until they enter "admin123"
# Print "Access granted" when correct, "Wrong password, try again" each failed attempt
# YOUR CODE HERE

password = ""
while password != "admin123":
    password = input("Enter password: ")
    if password != "admin123":
        print("Wrong password, try again")
print("Access granted")


# EXERCISE 3:
# Loop over the server_status dict from Section 5
# Count how many servers are "healthy" and print the total at the end
# Example output: "3 of 4 servers healthy"
# YOUR CODE HERE
server_status = {
    "web-01": "healthy",
    "web-02": "down",
    "db-01": "healthy",
    "db-02": "degraded"
}
healthy = 0
total = len(server_status)
print("\nServer health report:")

for server, status in server_status.items():
    if status == "healthy":
        healthy = healthy + 1
        
print(healthy,"of", total,"servers are healthy")