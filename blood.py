from datetime import datetime
import sys

def check_eligibility(age, weight, last_donation):
    last_date = datetime.strptime(last_donation, "%Y-%m-%d")
    days_since = (datetime.now() - last_date).days

    if age < 18:
        return "Not Eligible - Age must be at least 18"

    if weight < 50:
        return "Not Eligible - Weight must be at least 50 kg"

    if days_since < 90:
        return "Not Eligible - Last donation must be at least 90 days ago"

    return "Eligible"


if __name__ == "__main__":

    # Jenkins WITH parameters or command-line run
    if len(sys.argv) == 4:
        age = int(sys.argv[1])
        weight = float(sys.argv[2])
        last_donation = sys.argv[3]

    # Jenkins WITHOUT parameters / local VM run
    else:
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        last_donation = input("Enter last donation date (YYYY-MM-DD): ")

    status = check_eligibility(age, weight, last_donation)

    print(f"Age: {age}")
    print(f"Weight: {weight} kg")
    print(f"Last Donation Date: {last_donation}")
    print(f"Donation Status: {status}")