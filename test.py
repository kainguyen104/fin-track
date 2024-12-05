from datetime import datetime
from core import Transaction, FinTrack

def test_new_fin_track():
    tracker = FinTrack()
    assert len(tracker.transactions) == 0, "New financial tracker should have no transactions"
    print("✓ New financial tracker test passed")

def test_add_transaction():
    tracker = FinTrack()
    tracker.add_transaction(-100, "Food", "Groceries")
    assert len(tracker.transactions) == 1, "Tracker should have one transaction"
    transaction = tracker.transactions[0]
    assert transaction.amount == -100, "Transaction should have the correct amount"
    assert transaction.category == "Food", "Transaction should have the correct category"
    print("✓ Add transaction test passed")

def test_calculate_totals():
    tracker = FinTrack()
    tracker.add_transaction(-50, "Food", "Lunch")
    tracker.add_transaction(500, "Income", "Salary")
    assert tracker.calculate_expenses() == -50, "Total expenses should be -50"
    assert tracker.calculate_income() == 500, "Total income should be 500"
    assert tracker.calculate_balance() == 450, "Balance should be 450"
    print("✓ Calculate totals test passed")

if __name__ == "__main__":
    print("Running financial tracker tests...\n")
    try:
        test_new_fin_track()
        test_add_transaction()
        test_calculate_totals()
        print("\nAll tests passed! ✨")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
