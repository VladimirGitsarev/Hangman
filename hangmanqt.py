import random
from random_word import RandomWords

def getWord():
    try:
        rand = RandomWords()
        word = rand.get_random_word(hasDictionaryDef="true").lower()
    except:
        words = ["summer", "autumn", "winter", "spring"]
        word = words[random.randrange(0, words.__len__())]
    return word

def play(word, let):
    counter = []
    if let in word:
        counter.clear()
        c = -1
        for i in word:
            c+=1
            if i == let:
                counter.append(c)
    return counter
    
