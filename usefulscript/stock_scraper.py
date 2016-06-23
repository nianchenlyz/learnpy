import urllib
import urllib2
import time
from bs4 import BeautifulSoup


def get_stock_tickers():
    req = urllib2.Request(
        'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            tickers.append(str(col[0].string.strip()))
    tickers.sort()
    return tickers


def get_stock_prices(ticker_list,iii):
    for ticker in ticker_list:
        iii=iii+1
        time.sleep(2)
        htmlfile = urllib2.urlopen(
            "http://finance.yahoo.com/q?s={0}".format(ticker)
        )
        htmltext = htmlfile.read()
        soup = BeautifulSoup(htmltext, 'html.parser')
        htmlSelector = 'yfs_l84_{0}'.format(ticker.lower())
        for price in soup.find_all(id=htmlSelector):
            print('{0} is {1}'.format(ticker, price.text))
    print iii


def main():
    iii=0
    all_tickers = get_stock_tickers()
    get_stock_prices(all_tickers,iii)


if __name__ == '__main__':
    main()
