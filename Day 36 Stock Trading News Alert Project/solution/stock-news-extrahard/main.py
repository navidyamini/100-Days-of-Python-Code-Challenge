import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"

stock_params = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 3)
if abs(diff_percent) > 0.001:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    print(news_response)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [(f"{STOCK_NAME}: {up_down}{difference}% \nHeadline : {article['title']}. "
                           f"\nBrief: {article['description']}") for article in
                          three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
                from_=VIRTUAL_TWILIO_NUMBER,
                body=article,
                to=VERIFIED_NUMBER
            )

