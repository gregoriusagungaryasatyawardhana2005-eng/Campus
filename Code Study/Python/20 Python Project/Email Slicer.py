#Email Slicer Program

email = input("Enter your Email: ")
index = email.index("@")

username = email[:index]
domain = email[index+1:]

print(f"Your username is {username} and your domain is {domain}")
