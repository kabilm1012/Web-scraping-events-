from webscrape import scrape, extract
from textdata import read, store
from send_email import send_email

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


if __name__ == "__main__":
    scraped = scrape(URL, HEADERS)
    extracted = extract(scraped)
    print(extracted)
    data = read("data.txt")
    if extracted != "No upcoming tours":
        if extracted not in data:
            store("data.txt", extracted)
            send_email(extracted)