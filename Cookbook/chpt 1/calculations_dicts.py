prices = {
    "TATA" : 100,
    "ADANI" : 105,
    "RELIANCE" : 128,
    "JSW" : 45,
    "RATAN" : 90
}

min_stock = min(zip(prices.values(), prices.keys()))
max_stock = max(zip(prices.values(), prices.keys()))

print(min_stock)
print(max_stock)