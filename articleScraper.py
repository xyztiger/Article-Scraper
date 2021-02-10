import newspaper
import pymongo
import bson
import json
import nltk


def connect_MDB():
    """
    connect to mongoDB
    """
    client = pymongo.MongoClient(
    "mongodb+srv://Dev01:M6pcc9wA01vtOj8B@cluster0-mbyvk.mongodb.net/test?retryWrites=true&w=majority")
    #print(client.mflix)
    if client is None:
        return
    try:
        db = client.FakeNewsCheckerDB
        print("Connected to FakeNewsCheckerDB successfully!")
    except:
        print("FakeNewsCheckerDB not found")

def scrape_url():
    
    collection = db.url_records
    npr_news = newspaper.build('https://www.npr.org', memoize_articles=False) # build newspaper on npr.org 
    nytimes_news = newspaper.build('http://nytimes.com', memoize_articles = False)
    newyorker_news = newspaper.build('https://www.newyorker.com/', memoize_articles = False)
    washpost_news = newspaper.build('http://washingtonpost.com', memoize_articles = False)
    wsj_news = newspaper.build('http://wsj.com', memoize_articles = False)
    cnn_news = newspaper.build('http://cnn.com', memoize_articles = False)
    theweek_news = newspaper.build('https://theweek.com/', memoize_articles = False)

    for category in npr_news.category_urls():
        category_news = newspaper.build(category, memoize_articles=False)  # rebuild the index by category
        for article in category_news.articles:
            if category == 'https://www.npr.org':  # filter out other categories

                article = newspaper.Article(article.url)   
                article.download() # downloads HTML content
                article.parse() # parse the article
                article.nlp() #  keyword extraction wrapper
                url = {                      
                "title" : "",
                "network" : "",
                "url" : "",
                "time" : "",n
                "author" : "",
                "articleBody" : "",
                "keywords" : ""
                }
                url["url"] = article.url
                url["network"] = "npr"
                url["title"] = article.title
                url["website"] = category                    
                url["time"] =  (str(article.publish_date).split(" "))[0]
                url["author"] = article.authors
                url["articleBody"] = article.text
                url["keywords"] = article.keywords
                collection.insert_one(url) # inserting matedata into FakeNewsCheckerDBNew

connect_MDB()

npr_news = newspaper.build('https://www.infowars.com', memoize_articles=False)

print(npr_news.category_urls())

for category in npr_news.category_urls():
    category_news = newspaper.build(category, memoize_articles=False)  # rebuild the index by category
    for article in category_news.articles:
        if category == 'https://www.infowars.com':  # filter out other categories
            
            article = newspaper.Article(article.url)   
            article.download() # downloads HTML content
            article.parse() # parse the article
            article.nlp() #  keyword extraction wrapper
            url = {                      
            "title" : "",
            "network" : "",
            "url" : "",
            "time" : "",
            "author" : "",
            "articleBody" : "",
            "keywords" : ""
            }
            url["url"] = article.url
            url["network"] = "infowars"
            url["title"] = article.title
            url["website"] = category                    
            url["time"] =  (str(article.publish_date).split(" "))[0]
            url["author"] = article.authors
            url["articleBody"] = article.text
            url["keywords"] = article.keywords
            
            print(url)
            
            https://www.palmerreport.com/
