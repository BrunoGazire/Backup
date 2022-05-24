sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] = word_counts[word] + 1

######################################################################################
stri = "what can I do"
char_d = {}

for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] = char_d[c] + 1

print(char_d)
print("There are ", char_d["a"])
for y in char_d:
    print("there are " + str(char_d[y]) + y + "'s")
#####################################################################################
travel = {}
travel["North America"] = 2
travel["Europe"] = 8
travel["South America"] = 3
travel["Asia"] = 4
travel["Africa"] = 1
travel["Antartica"] = 0
travel["Australia"] = 1
total = 0
for country in travel:
    total = total + travel[country]
print(total)
#######################################################################################
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later"
d = {}
for c in placement:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1
keys = list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)
print(d)
##################################################################################################################
product = "iphone and android phones"
lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] = lett_d[c] + 1
print(lett_d)
keys = list(lett_d.keys())
max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

###############################################################################################################
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for corse in Junior:
    credits = Junior[corse] + credits
print(credits)
###############################################################################################################
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] = freq[c] + 1
print(freq)
##################################################################################################################
s1 = "hello"
counts = {}
for c in s1:
    if c not in counts:
        counts[c] = 0
    counts[c] = counts[c] + 1
print(counts)
###############################################################################################################
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
list1 = str1.split()
for word in list1:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1
print(freq_words)
#############################################################################################################
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
sent_split = sent.split()
for word in sent_split:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1
print(wrd_d)
#############################################################################################################
sally = "sally sells sea shells by the sea shore"
characters = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c] + 1
best_char = 0
for key in characters[c]:
    print(key)