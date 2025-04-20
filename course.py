def openClose():
    print("___________________")

openClose
# system consists of "OS 1", "OS 2", "OS 3"
system = "OS 3"
if system == "OS 2":
    print("No update needed")
elif system == "OS 1" or system == "OS 3":
    print("Update needed")
# If the system running OS other than OS 1, OS 2 or OS 3, then nothing is printed on the console

#Conditional statement for login attempts and login attempts outside of organization hours
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in
username = "bmor"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = 0

if username in approved_list and organization_hours == True:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")

openClose()
# for loop with range
for i in range(3):
    print("Cannot connect to the destination.")

computer_assets = ["computer", "monitor", "keyboard", "mouse"]
for asset in computer_assets:
    print(asset)

string = "coursera"
for char in string:
    print(char)

openClose()
# while loop
time = 0
while time <= 4:
    print(time)
    time = time + 2

# while loop for user that reaches the maximum number of connected devices
max_devices = 5
i = 1

while i < max_devices:
    print("User can still connect to additional devices.")
    i += 1
print("User has reached the maximum number of connected devices.")

login_attempts = 0
while login_attempts < 3:
    print("Login attempts:", login_attempts)
    login_attempts += 1

openClose()
# Bool values in loop condition
count = 0
login_status = True
while login_status == 1:
    print("Try again.")
    count += 1
    if count == 3:
        login_status = 0

openClose()
# exit a 'for' or 'while' loop based on an if condition being "True"
for asset in computer_assets:
    if asset == "keyboard":
        print("Keyboard found. Exiting loop...")
        break
    print(asset)

openClose()
# continue statement
for asset in computer_assets:
    if asset == "keyboard":
        print("Keyboard found. Skipping to the next asset...")
        continue
    print(asset)

openClose()
# function for greeting employee
def greet_employee(first_name, last_name):
    print("Welcome! You're logged in", first_name, last_name + ".")
greet_employee("Kiara", "Carter")

openClose()
# Use information returned from a function
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = (failed_attempts / total_attempts) * 100
    return fail_percentage

percentage = calculate_fails(4, 2)

if percentage >= .5:
    print("Account locked.")

openClose()
# return keyword is used to return information from a function
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 3)
if remaining_attempts <= 0:
    print("Your account is locked")

openClose()
# Use the sorted function
usernames = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
sorted_usernames = sorted(usernames)
print("Sorted usernames:", sorted_usernames)
print("Original usernames:", usernames)

openClose()
# Use max() and min() functions
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

openClose()
# Calculate the average of number of failed login attempts per month for a particular user
import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
median_failed_attempts = statistics.median(monthly_failed_attempts)
print("median:", median_failed_attempts)