# Import datetime for time parsing
from datetime import datetime

# Import time-related functions
from modules.date_and_time import get_date_time

def greet():
    """
    Generates an appropriate greeting based on the current time of day.
    
    Returns:
        str: Greeting message (Good Morning/Good Afternoon/Good Evening)
    """
    # Get current time and extract the hour
    current_time, _, _ = get_date_time()
    hour = datetime.strptime(current_time, "%I:%M %p").hour

    if hour >= 5 and hour < 12:
        greeting = "Good Morning"
    elif  hour >= 12 and hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return greeting

if __name__ == "__main__":
    greeting = greet()
    print(f"{greeting}")