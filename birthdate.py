
print("Hello,Dear!")

# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's birth date in dd.mm.yy format
birth_input = input("Enter your birth date (dd.mm.yy): ")

# Split the input and extract the year
day, month, year = birth_input.split('.')

# Convert year to 4-digit format
year = int(year)
if year < 100:
    if year <= 25:
        year += 2000
    else:
        year += 1900

# Calculate age
from datetime import datetime
current_year = datetime.now().year
age = current_year - year

# Show a personalized message
print(f"\nDear {name}, you are {age} years old now. Best wishes for you! 🎉")
