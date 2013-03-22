import urllib2
from BeautifulSoup import *
from urlparse import urljoin
import sqlite3 as sqlite

ignorewords = set(['the','of','to','and','a','in','is','are'])

class Crawler:
  def __init__(self, dbname):
    self.conn = sqlite.connect(dbname)

  def __del__(self):
    self.conn.close()

  def dbcommit(self):
    self.conn.commit()

  def get_entry_id(self,table,field,value,createnew = True):
    return None

  # Index an indivual page
  def add_to_index(self, url , soup):
    print 'Indexing %s' % url


  def get_text_only(self, soup):
    return None

  def separate_words(self, text):
    return None

  def is_indexed(self, url):
    return False

  def add_link_ref(self, urlFrom, urlTo, linkText):
    pass

  def crawl(self, pages, depth = 3):
    for i in range(depth):
      newpages=set()
      for page in pages:
        try:
          c = urllib2.urlopen(page)
        except:
          print "could not open %s" % page
          continue
        soup = BeautifulSoup(c.read())
        self.add_to_index(page,soup)

        links=soup('a')
        for link in links:
          if 'href' in dict(link.attrs):
            url = urljoin(page,link['href'])
            if url.find("'") != -1:
              continue
            url = url.split('#')[0]
            if url[0:4]=='http' and not self.is_indexed(url):
              newpages.add(url)
            linkText = self.get_text_only(link)
            self.add_link_ref(page,url,linkText)

        self.dbcommit()

      pages = newpages



  def create_index_tables(self):
    pass
