from datetime import datetime
import sys

# Function to check eligibility (importable)
def check_eligibility(age, weight, last_donation):
    days_since = (datetime.now() - datetime.strptime(last_donation, "%Y-%m-%d")).days

    if age < 18:
        return "Not Eligible - Age must be at least 18"
    elif weight < 50:
        return "Not Eligible - Weight must be at least 50 kg"
    elif days_since < 90:
        return "Not Eligible - Last donation must be at least 90 days ago"
    else:
        return "Eligible"

# Default values (if no arguments provided)
DEFAULT_AGE = 20
DEFAULT_WEIGHT = 55
DEFAULT_LAST_DONATION = "2024-01-01"

# CLI / Jenkins execution
if __name__ == "__main__":
    # Command-line arguments
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

    # Convert to correct types
    age = int(age)
    weight = float(weight)

    # Check eligibility
    status = check_eligibility(age, weight, last_donation)

    # Output
    print("Age:", age)
    print("Weight:", weight, "kg")
    print("Last Donation Date:", last_donation)
    days_since = (datetime.now() - datetime.strptime(last_donation, "%Y-%m-%d")).days
    print("Days Since Last Donation:", days_since)
    print("Donation Status:", status)
