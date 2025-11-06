# Import requests for making HTTP requests
import requests

def get_location():
    """
    Gets the current city location based on IP address using ipinfo.io API.
    
    Returns:
        str: Name of the current city, or None if location cannot be determined
    """
    try:
        # Make HTTP request to ipinfo.io API
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        # Extract city from response
        city = data.get("city")

        return city
    
    except Exception as e:
        return None

if __name__ == "__main__":

    city = get_location()
    if city:
        print(f"You are currently in: {city}")
    else:
        print("Unable to fetch location info.")
