# Import pywhatkit for Google search functionality
import pywhatkit

def search_google(query):
    """
    Opens a web browser and performs a Google search.
    
    Args:
        query (str): The search term to look up on Google
    """
    pywhatkit.search(query)

if __name__ == "__main__":
    query = input("Search Google: ")
    print(f"Searching {query} on Google.")
    search_google(query)