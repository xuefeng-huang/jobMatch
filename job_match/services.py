from models import Writer
from newspaper import Article # extract the main content
import rake # extract keywords
import os
from django_contect_matching.settings import BASE_DIR

def get_writer_score(writer):
    industry_list = writer.industry.split(',')
    if any(item.strip() in ['Lifestyle & Travel'] for item in industry_list):
        total_links = 0
        relavent_links = 0
        publications = writer.publication_set.all()
        
        if publications:
            for item in publications:
                article_text = get_text(item.link)
                article_keywords = get_keywords(article_text) # list of tuples ('key words', score)
                for keywords in article_keywords:
                    print keywords[0]
                    items = keywords[0].split() # get the keywords part and split into a list
                    if any(item.lower() in ['travel', 'singapore', 'tourism', 'sightseeing'] for item in items):
                        relavent_links += 1
                        break
                total_links += 1
                
            return float(relavent_links) / total_links * min(relavent_links, 100)
        else:
            return 0
    else:
        return 0

def get_text(link):
    article = Article(link)
    article.download()
    article.parse()
    return article.text
    
def get_keywords(text):
    rake_obj = rake.Rake(os.path.join(BASE_DIR, 'job_match', 'stop_words.txt'), 3, # at least xxx char in each keyword
                                                                                5, # at most xxx words in the phrase
                                                                                2) # at least appear xxx times
    return rake_obj.run(text)[0:3] # return first 3 keywords list