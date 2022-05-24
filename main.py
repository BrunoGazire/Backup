import pandas as pd
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores2 = scores.split(" ")
accum = 0
print(scores2)
for score in scores2:
    score = int(score)
    if score >= 90:
        accum += 1
print(accum)


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org1 = org.split()
acro = ""
for char in org1:
    if len(char) > 3:
        char = char.upper()
        acro += char[0]
        stopwords.append(char[1:])
print(acro)

p_phrase = "was it a car or a cat I saw"
r_phrase = ""
for char in p_phrase:
    r_phrase = char + r_phrase
print(r_phrase)












