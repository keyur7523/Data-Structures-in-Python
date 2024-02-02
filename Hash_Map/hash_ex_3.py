# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

word = {}

with open("poem.txt", "r") as f:
    for line in f:
        #print(line)
        line = line.replace('\n', ' ')
        k = line.split(' ')
        for i in k:
            if i in word.keys():
                word[i] += 1
            else:
                word[i] = 1

print(word)
