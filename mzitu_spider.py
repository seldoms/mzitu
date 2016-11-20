from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup


spider_queue = MogoQueue('meinvxiezhenji', 'crawl_queue')
def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')
    all_a = Soup.find('div', class_='all').find_all('a')
    for a in all_a:
        title = a.get_text()
        url = a['href']
        spider_queue.push(url, title)
    """上面这个调用就是把URL写入MongoDB的队列了"""

if __name__ == "__main__":
    start('http://www.mzitu.com/all')

"""这一段儿就不解释了哦！超级简单的"""