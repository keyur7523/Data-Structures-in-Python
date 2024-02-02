#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#What was the temperature on Jan 9?
#What was the temperature on Jan 4?

temperatures = {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        token = line.split(',')
        try:
            temperatures[token[0]] = int(token[1])
        except:
            print('Invalid Temperature!')

print(f"The temperature on Jan 9 was {temperatures['Jan 9']}.")
print(f"The temperature on Jan 4 was {temperatures['Jan 4']}.")
