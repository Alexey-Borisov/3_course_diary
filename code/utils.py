import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.tokenize import sent_tokenize, word_tokenize


class SiteExtractor:
    
    def __init__(self):
        pass
    
    def get_page(self, page_name):
        
        r = requests.get(page_name)
        return r.text
    
    
class HTMLParser:
    
    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    def text_from_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

    def __init__(self):
        pass
    
    def parse(self, page_html):
        return self.text_from_html(page_html)
    
    
class SentenceParser:
    
    def __init__(self):
        pass
    
    def parse(self, text):
        return sent_tokenize(text)