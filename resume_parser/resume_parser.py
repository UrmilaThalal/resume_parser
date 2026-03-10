# Resume Parser Program

# Ask user details
name = input("Enter your name: ")
bio = input("Enter your bio: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")
headline = input("Enter your headline: ")
photo_url = input("Enter your photo image URL: ")
resume_url = input("Enter your resume URL: ")

# Print Resume
print("\n----- RESUME -----\n")

print("Name:", name)
print("Headline:", headline)
print("Bio:", bio)

print("\nContact Information")
print("Email:", email)
print("Phone:", phone)
print("Address:", address)

print("\nLinks")
print("Photo URL:", photo_url)
print("Resume URL:", resume_url)

print("\n------------------")