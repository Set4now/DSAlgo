# min = 2
# se = ""
# a = "mouse"
# while min < len(a) + 1:
#     se = a[:min]
#     print (se)
#     min += 1
searchWord = "mo"
repository=["mobile", "mouse", "moneypot", "monitor", "mousepad"]
for words in repository:
    if words.lower().startswith(searchWord.lower()):
        print (words)