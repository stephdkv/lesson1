def format_price(price):
    price = str(int(price))
    price = 'Цена: ' + price + ' руб.'
    return price
price = format_price(56.24)
print(price)