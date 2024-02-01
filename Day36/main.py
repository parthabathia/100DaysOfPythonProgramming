import requests
from twilio.rest import Client

TWI_ACCOUNT_SID = "your_account_sid"
TWI_AUTH_TOKEN = "your_auth_token"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VAN_API_KEY = "your_api_key"
NEW_API_KEY = "your_api_key"


def check_stock():
    stock_api_endpoint = "https://www.alphavantage.co/query"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VAN_API_KEY
    }
    response = requests.get(url=stock_api_endpoint, params=stock_parameters)
    stock_data = response.json()['Time Series (Daily)']
    historic_data = list(stock_data.items())[:2]
    yesterday_close = float(historic_data[0][1]['4. close'])
    day_before_yesterday_close = float(historic_data[1][1]['4. close'])
    print(yesterday_close, day_before_yesterday_close)
    difference = yesterday_close - day_before_yesterday_close
    up_down = None
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"
    diff_percentage = round((difference / yesterday_close) * 100)
    if abs(diff_percentage) > 1:
        news = get_news()
        send_message(news, up_down,diff_percentage)


# STEP 2: Use https://newsapi.org
def get_news():
    news_api_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": "tesla",
        "searchIn": ("title", "content"),
        "language": "en",
        "apikey": "5a45cbf64098418b8c9d922c8ac086b2"
    }
    response = requests.get(url=news_api_endpoint, params=news_parameters)
    news_data = response.json()['articles'][:3]
    return news_data


def send_message(news_data, up_down, diff_percentage):
    formatted_articles = [f"{STOCK}: {up_down}{diff_percentage}%\nHeadline: {data['title']}.\nBrief: {data['description']}" for data in news_data]
    print(formatted_articles)
    client = Client(TWI_ACCOUNT_SID, TWI_AUTH_TOKEN)
    for data in formatted_articles:
        message = client.messages \
            .create(
            body=data,
            from_='temp_number',
            to='your_number'
        )
        print(message.status)


check_stock()
