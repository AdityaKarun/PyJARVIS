# Import pyjokes for programming jokes
import pyjokes

def get_joke():
    """
    Fetches a random programming joke in English.
    
    Returns:
        str: A random programming joke
    """
    joke = pyjokes.get_joke(language="en")
    
    return joke

if __name__ == "__main__":
    joke = get_joke()
    print(f"Here is the Joke: {joke}")