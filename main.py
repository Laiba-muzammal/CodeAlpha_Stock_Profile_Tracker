import yfinance as fyp # type: ignore

stock_portfolio={}

def add_stock_value(symbol,amount):
    stock_portfolio[symbol]=stock_portfolio.get(symbol,0)+amount
    print(f"Your amount : {amount} is successfully added")

def del_stock_value(symbol):      
    if symbol in stock_portfolio:
        del stock_portfolio[symbol]
        print(f"Your symbol : {symbol} is successfully deleted")
    else :
        print("Oops! symbol not found")
    

def view_stock_profile():
    for symbol,amount in stock_portfolio.items(): 
        track=fyp.Ticker(symbol)
        value=track.history(period='1d')['Close'].iloc[-1]
        print(f"\n{symbol}: You have a share of {amount} i.e., {value:.2f} USD")

while (True):
    print("\n*************MENU***********\n1.Add stock\n2.Delete stock\n3.Display stock\n4.Exit")
    option=int(input("Enter your option: "))      

    if(option==1):
        print("\n*****Adding stock******")
        amount=float(input("Enter amount you want to add: "))
        symbol=input("Enter the symbol of respective stock: ")
        add_stock_value(symbol,amount)
        
    elif(option==2):
        print("\n*****Deleting stock******")
        symbol=input("Enter the symbol of respective stock: ")
        del_stock_value(symbol)

    elif(option==3):
        view_stock_profile()

    elif(option==4):
        print("\nSee you soon!")
        exit()

    else :
        print("Invalid Option!")
                    
