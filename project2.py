while True:
    username=input("Type a uniqe name")
    if username.isalpha():
     break
    else:
        print("Only alphabetic ")

age = int(input("Type you age"))
father = input("Type here")
print("name",{username},"age",{father})