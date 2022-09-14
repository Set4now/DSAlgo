
from collections import defaultdict
from typing import List

"""

World Ladder 2 
Here we need to find all the shortest path from src to dest

"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # 0 if no such sequence exists 
        if endWord not in wordList:
            return 0

        self.g = defaultdict(list)

        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                """

                {'*ot': ['hot', 'dot', 'lot']
                creating a hasp map to store all the words matching to that pattern
                
                """
                pattern = word[:i] + "*" + word[i+1:]
                self.g[pattern].append(word)

        distance, parent = self.bfs(beginWord, wordList)

        paths = []
        path = [endWord]

        if distance[endWord] == float("Inf"):
            return []
        self.get_paths(endWord, path, paths, parent)
        return paths

    
    def get_paths(self, word, path, paths, parent):
        if not parent[word]:
            temp = [i for i in path]
            temp.reverse()
            paths.append(temp)
        
        for prev in parent[word]:
            path.append(prev)
            self.get_paths(prev, path, paths, parent)
        path.pop()
        
    def bfs(self, beginWord, wordList):
        q = []
        q.append(beginWord)
        distance = {v: float("Inf") for v in wordList}
        distance[beginWord] = 1
        parent = {v: [] for v in wordList}
        #parent[beginWord] = []
        # using BFS technique
        # Keep updating the distance map where we store the min distance from source k to the current node
        while q:
            word = q.pop(0)
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                """
                Find neibours of this word (like adjaceny list in a Graph) and add to the queue
                eg.
                hot -> [dot, lot]


                How ?

                We are finding all the paterns this word can be part of 
                and all others words having the same pattern

                {'*ot': ['hot', 'dot', 'lot']}

                means 
                hot: [dot, lot] are 2 neibours of hot
                
                
                """
                for w in self.g[pattern]:
                    if distance[w] > distance[word] + 1:
                        distance[w] = distance[word] + 1
                        q.append(w)
                        parent[w].append(word)

                    # this will track all the min distance paths
                    # if there is already a min distance, we will refer it later to generate the paths
                    elif distance[w] == distance[word] + 1:
                        parent[w].append(word)
        return distance, parent


beginWord = "hit"
endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

s= Solution()




# beginWord = "hot"
# endWord =  "dog"
# wordList = ["hot","dog"]





# beginWord = "leet"
# endWord =  "code"
# wordList = ["lest","leet","lose","code","lode","robe","lost"]


#beginWord = "cet"
#endWord = "ism"
#wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
print(s.findLadders(beginWord, endWord, wordList))