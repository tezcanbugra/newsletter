# newsletter

Newsletter is an automated tool that consumes AlphaVantage's NEWS_SENTIMENT API and sends a mail notification to the receivers with the news and the sentiment score for the news. 

It has MongoDB integration and all crawled news are stored in MongoDB for further processing/preventing repetitive emails. 

All actions - email triggers - and errors are logged under /logs/ folder. 

## Limitations

AlphaVantage API ratelimits are applied. (Free version - 5 API requests per minute and 100 requests per day. ) 

## Requirements
- Python 3
- AlphaVantage API key
- Gmail account
- MongoDB 

## How to use? 

1 - Clone the repo 

```
git clone https://github.com/tezcanbugra/newsletter.git
```

2 - Install requirements 
```
pip3 install -r requirements.txt
```

3 - create .env file. You can modify the .env.EXAMPLE file. 

```
DEBUG=true
DATABASE_URI =                                       // Example: "mongodb+srv://{username}:{password}@{mongodbURL}/?retryWrites=true&w=majority"
ALPHAVANTAGE_API_KEY =                              //AlphaVantage API key
EMAIL_PASS =                                        //Sender email account passwd
SENDER_EMAIL =                                      //sender email address 

```

4 - configure receiver email addresses and interested tickers on main.py

```

    tickers=[
        "AAPL",
        "MSFT",
        "NVDA",
        "META",
        "TSLA",
    ]

    receiverlist = [
        "{sampleemail1}",
        "{sampleemail2}"
    ]
```

5 - Run main.py

```
python3 main.py
```

Example Email: 

<img width="915" alt="image" src="https://github.com/tezcanbugra/newsletter/assets/32716552/b5f944fc-79b7-450d-a81e-7ee540c137a4">


