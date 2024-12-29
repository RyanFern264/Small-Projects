import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
alpha_adv_api_key = ""
news_api_key = ""


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')

alpha_adv_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_adv_api_key
}

news_params = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "searchIn": "title"
}

#TODO: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


alpha_adv = requests.get(url="https://www.alphavantage.co/query", params=alpha_adv_params)
alpha_adv.raise_for_status()
alpha_adv_data = alpha_adv.json()

day_before_yesterday = str(datetime.date.today() - datetime.timedelta(2)) #  at the time of writing this the api hadn't gotten yesterday's data so, yeah
day_before_day_before_yesterday = str(datetime.date.today() - datetime.timedelta(3)) #  lol

open_price_one = float(alpha_adv_data["Time Series (Daily)"][day_before_yesterday]["1. open"]) #  open price
open_price_two = float(alpha_adv_data["Time Series (Daily)"][day_before_day_before_yesterday]["1. open"])

percent_of_change = get_change(open_price_one, open_price_two)

#TODO: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percent_of_change > 3: #  made this 3 instead of 5 for testing purposes
    stock_news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    stock_news.raise_for_status()
    stock_news_data = stock_news.json()
    #printing the first three articles, API returns them in order of popularity by default

    for i in range(0, 3):
        article_title = stock_news_data["articles"][i]["title"]
        article_description = stock_news_data["articles"][i]["description"]
        print(f"TSLA mover: {percent_of_change}\nHeadline:{article_title}\nBrief:{article_description}")

#TODO: Send a seperate message with the percentage change and each article's title and description to your phone number.
#nah, not gaining anything from doing that. The above API calling practice is good, don't need to do SMS/emailing again.


