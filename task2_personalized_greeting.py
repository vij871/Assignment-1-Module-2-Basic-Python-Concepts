first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

if first_name and last_name:
    full_name = first_name + " " + last_name
    print(f"\nHello, {full_name}! Welcome!")
else:
    print("Both first name and last name are required.")
