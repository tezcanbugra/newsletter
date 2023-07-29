import requests
import json
import os
import logging
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("API_KEY")

def get_news(symbol,limit):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&limit={limit}&apikey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx response status codes
        data = response.json()
        
        print(data)
        if data["feed"] == None:
            print("feed is empty...")
        else:
            print(f"news crawled for:  -- {symbol} -- successfully")

        # Accessing nested data
        feed = data['feed']
        #for item in feed:
            #print(item['title'])  # Output: 3 Unstoppable Growth Stocks to Buy If There's a Market Sell-Off
            #print(item['overall_sentiment_score'])
            #print(item['topics'])  # Output: [{'topic': 'Financial Markets', 'relevance_score': '0.999897'}, {'topic': 'Manufacturing', 'relevance_score': '0.5'}, {'topic': 'Earnings', 'relevance_score': '0.495866'}, {'topic': 'Technology', 'relevance_score': '0.5'}]
            # ... access other properties as needed

        return feed
    

    except requests.RequestException as e:
        logging.error(f"Error occurred during the HTTP request: {e}")
        # Handle or propagate the error as necessary

    except json.JSONDecodeError as e:
        logging.error(f"Error occurred while parsing JSON response: {e}")
        # Handle or propagate the error as necessary

    except KeyError as e:
        logging.error(f"KeyError occurred while accessing nested data: {e} ---- Probably you hit the API limit.")
        # Handle or propagate the error as necessary

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # Handle or propagate the error as necessary

 


#feed = get_news("AAPL",50)
# print(feed[0])
# print(feed[0]['title'])
# print(feed[0]['summary'])
# print(feed[0]['source'])
# print(feed[0]['summary'])
# print(feed[0]['topics'])
# print(feed[0]['overall_sentiment_score'])
# print(feed[0]['overall_sentiment_label'])
# print(feed[0]['ticker_sentiment'])
