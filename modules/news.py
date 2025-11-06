# Import required libraries
import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_news():
    """
    Fetches top 3 headlines from BBC News using NewsAPI.
    
    Returns:
        list: List of news headlines
    """
    # Get API key from environment variables
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    new_api = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = new_api.get_top_headlines(sources="bbc-news", language="en")
    articles = top_headlines["articles"]

    headlines_list = []

    for article in articles[:3]:
        headline_title = article.get("title")
        headlines_list.append(headline_title)

    return headlines_list
    
if __name__ == "__main__":
    print("Here are the top news headlines.")
    news_report = get_news()
    print(news_report)