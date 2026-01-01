from blood import check_eligibility
from datetime import datetime, timedelta

def test_eligible():
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    assert check_eligibility(25, 60, last_donation) == "Eligible"

def test_age_warning():
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    assert check_eligibility(16, 60, last_donation) == "Not Eligible - Age must be at least 18"

def test_weight_warning():
    last_donation = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
    assert check_eligibility(25, 45, last_donation) == "Not Eligible - Weight must be at least 50 kg"

def test_recent_donation_warning():
    last_donation = (datetime.now() - timedelta(days=50)).strftime("%Y-%m-%d")
    assert check_eligibility(25, 60, last_donation) == "Not Eligible - Last donation must be at least 90 days ago"
