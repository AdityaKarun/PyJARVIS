# Import datetime for time and date operations
from datetime import datetime

def get_date_time():
    """
    Gets the current time, date, and day of the week.
    
    Returns:
        tuple: (current_time, date, day)
            - current_time (str): Current time in 12-hour format with AM/PM
            - date (str): Current date in Month Day, Year format
            - day (str): Current day of the week
    """
    # Get current time in 12-hour format (e.g., "10:30 PM")
    current_time = datetime.now().strftime("%I:%M %p")
    # Get current date in full format (e.g., "November 6, 2025")
    date = datetime.now().strftime("%B %d, %Y")
    # Get current day of the week (e.g., "Thursday")
    day = datetime.now().strftime("%A")

    return current_time, date, day

if __name__ == "__main__":
    current_time, date, day = get_date_time()
    print(f"Current Time: {current_time}")
    print(f"Date: {date}")
    print(f"Day: {day}")