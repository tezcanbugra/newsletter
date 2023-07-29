from helper import crawler
from helper import parser
from helper import db 
from helper import helper
from datetime import date
import time 
import logging



def main():
    
    #set up basic logging. 

    logging.basicConfig(
        level=logging.INFO,
        filename=f'./logs/{date.today()}.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    tic = time.perf_counter()


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

    db.ping_db() #ping db to see if its accessible. 

    for ticker in tickers:
        helper.helper(ticker,receiverlist)

    toc = time.perf_counter()

    logging.info(f"A cycle is completed in {toc - tic} seconds...")


if __name__ == '__main__':
    main()
