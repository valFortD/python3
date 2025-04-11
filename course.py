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