import yfinance as fyp # type: ignore

stock_portfolio = {}

def add_stock_value(symbol, amount):
    stock_portfolio[symbol] = stock_portfolio.get(symbol, 0) + amount
    print(f"Your amount: {amount} is successfully added.")

def del_stock_value(symbol):
    if symbol in stock_portfolio:
        del stock_portfolio[symbol]
        print(f"Your symbol: {symbol} is successfully deleted.")
    else:
        print("Oops! symbol not found.")

def view_stock_profile():
    if not stock_portfolio:
        print("Your stock portfolio is empty.")
        return

    for symbol, amount in stock_portfolio.items():
        try:
            track = fyp.Ticker(symbol)
            value = track.history(period='1d')['Close'].iloc[-1]
            print(f"\n{symbol}: You have a share of {amount} i.e., {value:.2f} USD")
        except:
            print(f"Error fetching price for {symbol}. Check symbol validity.")
