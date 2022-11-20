stock = {
    'city': 'Москва',
    'temperature': 20 
}
print(stock['city'])
stock['temperature'] = stock['temperature'] - 5
print(stock)
print(stock.get('country', 'Россия'))
stock['date'] = '27.05.2019'
print(len(stock))