import requests
from bs4 import BeautifulSoup

def stock_price(symbol: str = "AAPL") -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px) W(100%)"
    return soup.find("div", class_=class_).find("span").text


if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")