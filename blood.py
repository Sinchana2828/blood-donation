from datetime import datetime
import sys

# Default values (if no arguments provided)
DEFAULT_AGE = 20
DEFAULT_WEIGHT = 55
DEFAULT_LAST_DONATION = "2024-01-01"

# Check for command-line arguments
if len(sys.argv) == 4:
    age = sys.argv[1]
    weight = sys.argv[2]
    last_donation = sys.argv[3]
    print("User provided input values:")
else:
    age = str(DEFAULT_AGE)
    weight = str(DEFAULT_WEIGHT)
    last_donation = DEFAULT_LAST_DONATION
    print("No input given - using default values:")

# Convert to proper types
age = int(age)
weight = float(weight)

# Calculate days since last donation
days_since = (datetime.now() - datetime.strptime(last_donation, "%Y-%m-%d")).days

# Determine eligibility
if age < 18:
    status = "Not Eligible - Age must be at least 18"
elif weight < 50:
    status = "Not Eligible - Weight must be at least 50 kg"
elif days_since < 90:
    status = "Not Eligible - Last donation must be at least 90 days ago"
else:
    status = "Eligible"

# Output
print("Age:", age)
print("Weight:", weight, "kg")
print("Last Donation Date:", last_donation)
print("Days Since Last Donation:", days_since)
print("Donation Status:", status)
