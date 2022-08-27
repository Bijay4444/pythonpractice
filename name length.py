name = input("Enter your name: ")

if len(name) < 3 :
    print("name must be at least three characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
print("thank you")