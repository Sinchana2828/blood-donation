from blood import check_eligibility
from datetime import datetime, timedelta

def test_eligible():
    # Age >=18, Weight >=50, Last donation > 90 days ago
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    expected_output = "Eligible"
    assert check_eligibility(25, 60, last_donation) == expected_output

def test_age_warning():
    # Age less than 18
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    expected_output = "Not Eligible - Age must be at least 18"
    assert check_eligibility(16, 60, last_donation) == expected_output

def test_weight_warning():
    # Weight less than 50
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    expected_output = "Not Eligible - Weight must be at least 50 kg"
    assert check_eligibility(25, 45, last_donation) == expected_output

def test_recent_donation_warning():
    # Last donation less than 90 days ago
    last_donation = (datetime.now() - timedelta(days=50)).strftime("%Y-%m-%d")
    expected_output = "Not Eligible - Last donation must be at least 90 days ago"
    assert check_eligibility(25, 60, last_donation) == expected_output
