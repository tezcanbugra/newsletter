import json
import hashlib


def create_id(data):
    return int(hashlib.sha256(data["url"].encode('utf-8')).hexdigest(), 16) % 10**8

def add_id(data):
    data['news_id'] = create_id(data)
    return data

def create_mail_content(data,symbol):
    message = "Subject: There is a news you may want to check!!! - {4} -  \n\n  \n {0}  \n {1}  \n {2} \n {3}".format(data['title'],data['overall_sentiment_label'],data['summary'],data['url'],symbol)
    return message