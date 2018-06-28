import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, name = None, date = None):
        if date and name:
            self.year = date.split(".")[2]
            self.may = date.split(".")[1]
            self.day = date.split(".")[0]
            self.main_url = 'https://lenta.ru'
            if (name[-2:] == 'ая' or name[-2:] == 'яя' or name[-2:] == 'ий' or name[-2:] == 'ой' \
                    or name[-2:] == 'ый' or name[-2:] == 'ая') and len(name) > 4:
                self.name = name[:-2]
            elif name[-1:] == 'а' or name[-1:] == 'ь' or name[-1:] == 'й' and len(name) > 4:
                self.name = name[:-1]
            else:
                self.name = name
            self.thems = ('news', 'articles')
            self.links = []
            self.pages_name = {}
            for self.them in self.thems:
                self.url = "%s/%s/%s/%s/%s/" % (self.main_url, self.them, self.year, self.may, self.day)
                self.getPage()
                self.getLink()
            self.nameFind()

    def getPage(self):
        r = requests.get(self.url)
        self.page =  r.text

    def getLink(self):
        soup = BeautifulSoup(self.page, 'lxml')
        link_block = soup.find_all('div', class_='row')
        for blocks in link_block:
            if blocks.find_all('div', class_='titles'):
                for block in blocks.find_all('div', class_='titles'):
                    self.links.append("%s%s" % (self.main_url,block.find('a').get('href')))

    def nameFind(self):
        for url in self.links:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'lxml')
            link_block = soup.find_all('div', class_='b-topic__content')
            page_count = str(link_block).count(self.name)
            if page_count > 0:
                self.pages_name[url] = page_count
        

if __name__ == '__main__':
    name ="Путина"
    date_news = "26.06.2018"
    crawler = Crawler(name, date_news)
    print(crawler.pages_name)



































































































































