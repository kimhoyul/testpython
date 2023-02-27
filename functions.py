import json


def scrap_theblock(soup):
    container = soup.find('div', {'class': 'cardContainer'})
    href = "https://www.theblock.co/latest" + container.find('a')['href']
    title = soup.find('span', {'ga-event-action': 'Click'}).text
    pubdate = container.find('div', {'class': 'pubDate'}).text.replace('\n', '').strip()
    data = {
        "href": href,
        "title": title,
        "pubdate": pubdate
    }
    return [data]


def scrap_coindesk(soup):
    html_str = str(soup)
    start_point = '\"sections\\\":\\\"\\\",\\\"size\\\":6}\":'
    start = html_str.find(start_point) + len(start_point)
    end = html_str.find(',\"subheadlines\":', start)
    result = html_str[start:end] + "}]}"
    json_obj = json.loads(result)
    data = {
        "href": "https://www.coindesk.com/" + json_obj['data'][0]['url'],
        "title":  json_obj['data'][0]['title'],
        "pubdate": json_obj['data'][0]['date'],
    }
    return [data]


