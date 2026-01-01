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

    # 🚨 Jenkins-safe: REQUIRE arguments
    if len(sys.argv) != 4:
        print("ERROR: Please provide arguments -> age weight last_donation_date")
        print("Example: python blood.py 20 55 2024-01-01")
        sys.exit(1)

    age = int(sys.argv[1])
    weight = float(sys.argv[2])
    last_donation = sys.argv[3]

    status = check_eligibility(age, weight, last_donation)

    print(f"Age: {age}")
    print(f"Weight: {weight} kg")
    print(f"Last Donation Date: {last_donation}")
    print(f"Donation Status: {status}")
