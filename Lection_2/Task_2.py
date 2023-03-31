userList = input("Enter your list: ")
while len(userList) == 0:
    userList = input("Please enter at least 1 item: ")
if "," in userList:
    userList = userList.split(",")
elif " " in userList:
    userList = userList.split(" ")

unique_list = []

for i in userList:
    if i not in unique_list:
        unique_list.append(i)

print("Unique list: ", unique_list)