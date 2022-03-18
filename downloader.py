from requests_html import HTMLSession
from datetime import datetime
import arrow

session = HTMLSession()

class Downloader:
  url_gainers = ['https://finance.yahoo.com/gainers?guce_referrer=aHR0cHM6Ly93d3cuYmluZy5jb20v&guce_referrer_sig=AQAAALuTr6U_0eqQoqMX-yqKzvLVw254_f_JoZNCCKevIznYXD10ftNrOZf6pw0i5XtGOfBkgd6PfhnpJEGCLpoBIuqlq4tDnICtVx5ZFAK7-S-yJ4DPS7ErbzzE94nx4r7vEamHpCnxUX0ucUUISEquxP5de3h11KMSwndmo2Y6vSQV&offset=0&count=250',
          'https://finance.yahoo.com/gainers?guce_referrer=aHR0cHM6Ly93d3cuYmluZy5jb20v&guce_referrer_sig=AQAAALuTr6U_0eqQoqMX-yqKzvLVw254_f_JoZNCCKevIznYXD10ftNrOZf6pw0i5XtGOfBkgd6PfhnpJEGCLpoBIuqlq4tDnICtVx5ZFAK7-S-yJ4DPS7ErbzzE94nx4r7vEamHpCnxUX0ucUUISEquxP5de3h11KMSwndmo2Y6vSQV&offset=250&count=250']
  url_losers = 'https://finance.yahoo.com/losers?offset=0&count=200'
  date_time =  datetime.now()
  gainers = []
  losers = []

  def __init__(self):
    self.losers.extend(self.parse_data(self.url_losers))
    for url in self.url_gainers:
      self.gainers.extend(self.parse_data(url))
  
  def get_page(self,url):
    r = session.get(url)
    self.date_time = arrow.utcnow().timestamp()
    return r 

  def parse_data(self,url):
    self.data = []
    r = self.get_page(url)
    table_rows = r.html.find('tbody')[0].find('tr')
    for row in table_rows:
      for ind, td in enumerate(row.find('td')):
        if ind == 0:
          symbol = td.text#.strip()
        if ind == 1:
          company = td.text#.strip()
        if ind == 4:
          pct_change = td.text#.strip()
      self.data.append({'symbol':symbol, 'company':company, 'pct_change':pct_change})
    return self.data
  
