address=input("Enter the path: ")
lst=address.split('/')
print("Directory: ","/".join(lst[:-1]))
print("Filename: ",lst[-1])
ext=lst[-1].split(".")
print("File extension: ",ext[-1])
