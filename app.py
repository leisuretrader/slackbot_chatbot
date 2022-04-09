from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import yfinance as yf

bot_toke = "{your_bot_token}"
app_token = "{your_app_token}"

app = App(token=bot_token)

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.info['regularMarketPrice']
    return str(price)

def get_stock_news(ticker):
    stock = yf.Ticker(ticker)
    return str(stock.news[0].get('title'))

@app.event("app_mention")
def chatbot(body, say):
#     pprint (body)
    bot_id = body.get("event", {}).get("text").split()[0]
    get_event = body.get("event", {}).get("text")
    
    message_body = get_event.replace(bot_id, "").strip().lower()
    
    ticker = message_body.split(" ")[-1] #get ticker from message_body
    if 'price' in message_body:
        say(get_stock_price(ticker))
    elif 'news' in message_body:
        say(get_stock_news(ticker))
    else:
        say("Question is not defined, please include 'price' or 'news' in your question, eg. price for msft")

if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()
    
