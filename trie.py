class TrieNode:
    def __init__(self) -> None:
        self.childrenmap = {}
        self.endOfString = None
        self.wordCount = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.wordLists = []

    def insert(self, word):
        rootnode = self.root
        for char in word:
            charPointer = rootnode.childrenmap.get(char)
            if not charPointer:
                charPointer = TrieNode()
                rootnode.childrenmap.update({char: charPointer})
            rootnode =  charPointer
        if not rootnode.endOfString:
            rootnode.endOfString = True
            rootnode.wordCount = 1
        else:
            rootnode.wordCount += 1
        #print("Node inserted successfully")

    def search(self, word):
        rootnode = self.root
        for char in word:
            presentInRoot = rootnode.childrenmap.get(char)
            if not presentInRoot:
                return False
            rootnode = presentInRoot
        if rootnode.endOfString:
            return True
        return False

    def getsuggestions(self, node, word, wordlist):
        if node.endOfString:
            if len(wordlist) < 2:
                wordlist.append(word)
        for char, node in node.childrenmap.items():
            self.getsuggestions(node, word+char, wordlist)

    def printAutoSuggestions(self, prefix):
        root = self.root
        not_found = False
        temp_word = ''

        for char in prefix:
            node = root.childrenmap.get(char)
            if not node:
                not_found = False
                return []
            temp_word += char
            root = node
        wordlist  = []
        self.getsuggestions(root, temp_word, wordlist)
        return wordlist

    def findLCP(self):
        root = self.root
        # if the trie contains any diff string, there cannot be any LCP
        # lcp is the longest common prefix from all the strings
        if len(root.childrenmap) > 1:
            return ""
        temp_char = ""
        while not root.endOfString and len(root.childrenmap) < 2:
            for char, node in root.childrenmap.items():
                temp_char += char
            root = node 
        return temp_char
        
        

def deletestring(root, word, index):
    ch = word[index]
    childnode = root.childrenmap.get(ch)
    canthisnodebedeleted = False 
    
    #Some other prefix of other string also prefix of target string
    if len(childnode.childrenmap) >= 1:
        deletestring(childnode, word, index+1)
        return False

    # case 2 , target string is prefix of another string, 
    # don't delete it, just endofstr to false
    if index + 1 == len(word):
        if len(childnode.childrenmap) >= 1: # multiple dependent nodes
            childnode.endOfString = False
            return False
        else: # no dependent node
            root.childrenmap.pop(ch)
            return True 
    
    #some other string is prefix of this string
    if childnode.endOfString == True:
        deletestring(childnode, word, index+1)
        return False

    # Case 4 , not any nodes depend on this
    canthisnodebedeleted = deletestring(childnode, word, index+1)
    if canthisnodebedeleted:
        root.childrenmap.pop(ch)
        return True
    else:
        return True

trie = Trie()
# trie.insert("App")
# trie.insert("Api")


# trie.insert("hello")
# trie.insert("hell")
# trie.insert("hellfire")
# trie.insert("hello")

# trie.insert("hello")
# trie.insert("hello")

# print(trie.search("hello"))
# trie.insert("Api")
# trie.insert("Api")
# trie.insert("Api")
# deletestring(trie.root, "Api", 0)
# print(trie.search("Api"))
#print(trie.printAutoSuggestions("he"))

# words = [
#     'code', 'coder', 'coding', 'codable', 'codec', 'codecs', 'coded',
#     'codeless', 'codependence', 'codependency', 'codependent',
#     'codependents', 'codes', 'codesign', 'codesigned', 'codeveloped',
#     'codeveloper', 'codex', 'codify', 'codiscovered', 'codrive'
# ]

# for word in words:
#     trie.insert(word)
#print(trie.findLCP())



def findsegmented(trie, word, out=''):
    if not word:
        print(out)
        return
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        
        if trie.search(prefix):
            findsegmented(trie, word[i:], out + ' ' + prefix)

trie = Trie()
words = [
        'self', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r',
        'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'
    ]
words = ["cats", "dog", "sand", "and", "cat","ca"]
for w in words:
    trie.insert(w)
word = 'catsanddog'
# print(trie.search("bre"))
findsegmented(trie, word)