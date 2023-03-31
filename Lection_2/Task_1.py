userList = input("Enter your list: ")
while len(userList) == 0:
    userList = input("Please enter at least 1 item: ")
if "," in userList:
    userList = userList.split(",")
elif " " in userList:
    userList = userList.split(" ")    
searchElement= input("Enter item: ")

while searchElement == "":
    searchElement = input("Enter item: ")

numberElement = 0

for i in userList:
    if searchElement == i:
        numberElement += 1

print ("In the list, the element " + str(searchElement) + " is repeated " + str(numberElement) + " times!")