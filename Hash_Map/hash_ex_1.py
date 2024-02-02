#(1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#  (a) What was the average temperature in first week of Jan
#  (b) What was the maximum temperature in first 10 days of Jan
#  Figure out data structure that is best for this problem

temperatures = []
with open("nyc_weather.csv", "r") as f:
    for line in f:
        token = line.split(',')
        try:
            temperature = int(token[1])
            temperatures.append(temperature)
        except:
            print('Invalid temperature. Ignore this value!')

print(f'The average temperature in first week of Jan is {sum(temperatures[0:7])/7}.')
print(f'The maximum temperature in first 10 days of Jan was {max(temperatures[0:10])}.')
