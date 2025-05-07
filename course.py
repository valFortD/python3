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

openClose()
# Apply upper and lower method to "Hello"
print("Hello".upper())
print("Hello".lower())

openClose()
# Extract a slice from a string
print("Hello"[1:4])

openClose()
# .index() finds the first occurrence of the input in a string and returns its location
# Use the index string method
print("HELLO".index("E"))

# Search for the character "L"
print("HELLO".index("L"))
# The answer is 2 because the first occurrence of "L" is at index 2, printing the first occurrence of "L"

openClose()
# String are immutable
# Immmutable means that once a string is created, it cannot be changed
my_string = "Hello"
# my_string[1] = "a"  # This will raise an error

openClose()
# Finding substrings with .index()
tshah_index = "tsnowflake, tshah, tcarter".index("tshah")
print(tshah_index)

openClose()
# ===== Activity work with strings =====

# Assign 'employee_id to a four digit number as an initial value 
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the `employee_id` as it currently stands

print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits

if (len(employee_id) < 5):
    employee_id = "E" + employee_id
    
# Display the `employee_id` after the update
    
print(employee_id)

"""
It's a good idea to save important data in variables when programming. This allows for quick and easy tracking and reuse of information.
Store the output of the .index() method in a variable called ind, which is short for index. This index represents the position where the domain extension ".com" starts in the url.
"""

# === Assign `url` to a specific URL ===

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 

ind = url.index(".com")

# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 

ind = url.index(".com")

# Extract the domain extension in `url` and display it

print(url[ind:ind+4])

"""
Conclusion

Strings are instrumental in storing important, security-related data, such as device IDs and URLs.
String concatenation allows you to easily combine information in a string with the information stored in another string.
String slicing is a powerful technique that enables you to extract any subsection of a string.
Python has many functions and methods that help analysts work with string values, as well as data that they want to convert to string format.
    The type() function returns the data type of its input.
    The str() function converts the input object into a string. For example, when called on an integer, str() returns that integer value converted to a string.
    The len() function returns the number of elements in an object. When called on a string, len() returns the number of characters in that string.
    The .index() method finds the first occurrence of the input in a string and returns its location. It provides the index where the substring begins.

"""

openClose()
# List methods
# Concatenate two lists
my_list = ["a", "b", "c", "d", "e"]
number_list = [1, 2, 3, 4, 5]
print(my_list + number_list)

# Use the insert method
my_list.insert(1, 7)
print(my_list)

# Use the remove method
my_list.remove("d")
print(my_list)

openClose()
ip_address = ["198.223.xx.xx", "198.101.xx.xx", "180.064.xx.xx", "192.168.xx.xx", "184.090.xx.xx"]

# Extract the first three characters from a list of IP addresses
networks = []
for address in ip_address:
    networks.append(address[0:3])
print(networks)

openClose()
#Task 4
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The user", username, "is not approved to access the system.")

# Task 5 When used on a list, the .index() method will return the position of the given value in the list.

username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# Display the value of `ind`

print(ind)

"""
Task 6

This task will allow you to build your understanding of list operations for the algorithm that you'll eventually build. It will demonstrate how you can find an index in one list and then use this index to display connected information in another list.
"""
ind = approved_users.index(username)

# Display the device ID at the index that matches the value of `ind` in `approved_devices`

print(approved_devices[ind])

"""
Task 7¶

Your next step in creating the algorithm is to determine if a username and device ID correspond.
"""
# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device
device_id = "4n482ts"

if username in approved_users and approved_devices:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

"""
Task 8

It would also be helpful for users to receive messages when their username is not approved or their device ID is incorrect.
"""
device_id = "4vn482ts"
if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# Elif statement
# Handles the case when `username` belongs to `approved_users` but element at `ind` in `approved_devices` does not match `device_id`,
# and displays two messages accordingly

elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")

"""
Task 9

In this task, you'll complete your algorithm by developing a function that uses some of the code you've written in earlier tasks. This will automate the login process.
"""
# Define a function named `login` that takes in two parameters, `username` and `device_id`

def login(username, device_id):

    # If `username` belongs to `approved_users`, 

    if username in approved_users:

        # then display "The user ______ is approved to access the system.",

        print("The user", username, "is approved to access the system.")

        # assign `ind` to the index of `username` in `approved_users`,

        ind = approved_users.index(username)

        # and execute the following conditional
        # If `device_id` matches the element at the index `ind` in `approved_devices`,

        if device_id == approved_devices[ind]:

          # then display "______ is the assigned device for ______" 

          print(device_id, "is the assigned device for", username)

        # Otherwise,

        else:

          # display "______ is not their assigned device"

          print(device_id, "is not their assigned device.")
  
    # Otherwise (part of the outer conditional and handles the case when `username` does not belong to `approved_users`),

    else:

        # Display "The user ______ is not approved to access the system."

        print("The username", username, "is not approved to access the system.")

# Call the function you just defined to experiment with different username and device_id combinations

login("bmoreno", "hl0s5o1")
login("elarson", "r2s5r9g")
login("abernard", "4n482ts")

"""
Conclusion
    Indexing a list is similar to indexing a string. Index values start at 0.
    The .append() method helps you add new elements to the end of lists.
    The .remove() method helps you remove elements from lists.
    The .index() method can be used on different types of sequences. They can be used not only with strings, but also with lists.
        With a list, the .index() method allows you to identify the position where a specified element is located in that list.
    If two lists contain information that correspond to each other in a specific order, you can use indices to pair elements from the lists together.
    Functions can be used to develop algorithms. When defining a function, you must specify the parameters it takes in and the actions it should execute.
"""

