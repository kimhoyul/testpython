from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.coindesk.com/'
r = session.get(url)
r.html.render()

articles = r.html.find('.article-cardstyles__AcTitle-q1x8lc-1.bzAuaw')
for article in articles:
    title = article.find('a', first=True).text
    print(title)