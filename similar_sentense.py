words = {
    "like": "love",
    "play": "games",
    "love": "enjoy",
    "food": "meal",
    "enjoy": "happiness"
}

def createmap(k, mymap):
    mymap[k].append(words[k])
    new = words[k]
    while new in words:
        mymap[k].append(words[new])
        new = words[new]
def similar(s1, s2):
    if len(s1.split()) != len(s2.split()):
        return False
    mymap = { k : [] for k,v in words.items()}
    for k, v in words.items():
        createmap(k, mymap)
    """
    a newly formed map with all the matches agisnt each word
        {
        'like': ['love', 'enjoy', 'happiness'],
        'play': ['games'], 
        'love': ['enjoy', 'happiness'], 
        'food': ['meal'], 
        'enjoy': ['happiness']
        }
    """
    words1 = s1.split()
    words2 = s2.split()
    for i in range(len(words1)):
        # print(words2[i], words1[i])
        if words1[i] != words2[i]:
            # print(words1[i], words2[i])
            word1 = words1[i]
            word2 = words2[i]
            if word1 in mymap:
                if word2 in mymap[word1]:
                    return True
            if word2 in mymap:
                if word1 in mymap[word2]:
                    return True
    else:
        return False

print(similar("i like to play", "i enjoy to play"))
print(similar("i like food", "you like food"))
print(similar("i enjoy music", "i love music"))
print(similar("i like food", "i love to eat meal"))
print(similar("love is important", "happiness is important"))
True
False
True
False
