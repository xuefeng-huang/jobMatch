from models import Writer
from newspaper import Article # extract the main content
import rake # extract keywords

def get_writer_score(writer):
    industry_list = writer.industry.split(',')
    if any(item in ['Lifestyle & Travel'] for item in industry_list):
        total_links = 0
        relavent_links = 0
        publications = writer.publication_set.all()
        
        if publications:
            for item in publications:
                article_text = get_text(item.link)
                article_keywords = get_keywords(article_text)
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
    rake_obj = rake.Rake('stop_words.txt', 1, 2, 2)
    return rake_obj.run(text)[0:3] # return first 3 keywords list