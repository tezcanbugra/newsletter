import time
import logging
from helper import db 
from helper import parser
from helper import crawler
from mailServer import mailserver

def helper(symbol,receiver):
    tic = time.perf_counter()


    news = crawler.get_news(symbol,50) #get last 50 news for the given symbol. 

    db.create_collection(symbol) #create the collection. 

    collect = db.db[symbol] #select the collection on DB. 

    if(news == None):
        return 0 
    
    for item in news:  
        try:
            collect.insert_one(parser.add_id(item)) #add an item to the db. item will get its unique id in the parser.add_id() function. 
            email = parser.create_mail_content(item,symbol)
            mailserver.send_email(email,receiver) #if the code is not in exception, it means the news is a new one. send email. 
        except Exception as e:
            logging.debug(e)
            logging.debug("DB is up to date for {}. Changing to the next ticker.",symbol)

            break


    toc = time.perf_counter()
    logging.info(f"Total news count for {symbol} in DB:  {collect.count_documents({})}") 
    logging.info(f"Operation completed in {toc - tic} seconds for {symbol}")