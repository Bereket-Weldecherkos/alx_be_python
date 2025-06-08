from datetime import timedelta
from datetime import datetime
def display_current_datetime ():
    return datetime.now()

current_date = display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {current_date}")

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

days = int(input("Enter the number of days to add to the current date: "))
print(f"Future Date: {calculate_future_date(days)}")