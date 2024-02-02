import heapq

k = [1,2,3,4,5,-1,13,24,21,23,20]

heap = list(k)
heapq.heapify(heap)

print(heap)

print(heapq.nlargest(3, k))
print(heapq.nsmallest(3, k))

portfolio = [
    {'name':'abc', 'shares':100, 'price':91.1},
    {'name':'abm', 'shares':120, 'price':92.1},
    {'name':'ape', 'shares':30, 'price':93.2},
    {'name':'abc', 'shares':108, 'price':90.1}
]

cheap = heapq.nsmallest(2, portfolio, key=lambda s:s['shares'])
expensive = heapq.nlargest(2, portfolio, key=lambda s:s['shares'])

print(cheap)
print(expensive)