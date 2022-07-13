import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "LJ1S61U2S1BQE3FN"
}
parameters_news = {
    "apikey": "386780eff8264a80851624485cbdc647",
    "q": "tesla"
}

account_sid = "ACb2b6cc6288147430b835198ca7500126"
auth_token = 'b77a51468978c2f61d64c6afa1e63163'
client = Client(account_sid, auth_token)

response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
news_data = response_news.json()

response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stock)
stock_data = response_stock.json()

current_Date = datetime.datetime.today() - datetime.timedelta(days=3)
previous_Date = datetime.datetime.today() - datetime.timedelta(days=4)

try:
    close_price_today = float(stock_data["Time Series (Daily)"][f"{current_Date.date()}"]["4. close"])
    close_price_yesterday = float(stock_data["Time Series (Daily)"][f"{previous_Date.date()}"]["4. close"])
    PERC_change = (float(abs((close_price_yesterday - close_price_today) / close_price_today) * 100))

    if int(PERC_change) >= 5:
        if close_price_yesterday > close_price_today:
            PERC_change = (
                '{0:.2g}'.format(float(((close_price_yesterday - close_price_today) / close_price_today) * 100)))
            for n in range(len(news_data["articles"])):
                message = client.messages \
                    .create(
                    body=f"TSLA: 🔻{PERC_change}% Headline:{news_data['articles'][n]['title']} (TSLA)?. Brief: {news_data['articles'][n]['description']}",
                    from_='+15185030691',
                    to='+919501545441'
                )
                print(message.status)

        else:
            PERC_change = (
                '{0:.2g}'.format(float(((close_price_today - close_price_yesterday) / close_price_today) * 100)))
            for n in range(len(news_data["articles"])):
                message = client.messages \
                    .create(
                    body=f"TSLA: 🔺{PERC_change}% Headline:{news_data['articles'][n]['title']} (TSLA)?. Brief: {news_data['articles'][n]['description']}",
                    from_='+15185030691',
                    to='+919501545441'
                )
                print(message.status)
    else:
        message = client.messages \
            .create(
            body=f"No major change on {current_Date}",
            from_='+15185030691',
            to='+919501545441'
        )
        print(message.status)

except KeyError:
    print("Market is close (holiday) you should also close this program")
