class Trie:
    def __init__(self) -> None:
        self.key = None
        self.character = [None] * 26

def insert(root, word):
    cur_root = root 
    for char in word:
        index = ord(char) - ord('a')
        node  = cur_root.character[index]
        if not node:
            node = Trie()
            cur_root.character[index] = node
        cur_root = node 
    cur_root.key = word


def preorder(root):
    if not root:
        return
    for i in range(26):
        if root.character[i]:
            if root.character[i].key:
                print (root.character[i].key)
            preorder(root.character[i])

    # given set of keys
words = [
    'lexicographic', 'sorting', 'of', 'a', 'set', 'of', 'keys', 'can', 'be',
    'accomplished', 'with', 'a', 'simple', 'trie', 'based', 'algorithm',
    'we', 'insert', 'all', 'keys', 'in', 'a', 'trie', 'output', 'all',
    'keys', 'in', 'the', 'trie', 'by', 'means', 'of', 'preorder',
    'traversal', 'which', 'results', 'in', 'output', 'that', 'is', 'in',
    'lexicographically', 'increasing', 'order', 'preorder', 'traversal',
    'is', 'a', 'kind', 'of', 'depth', 'first', 'traversal'
]

head = Trie()

# insert all keys of a dictionary into a Trie
for word in words:
    insert(head, word)

# print keys in lexicographic order
preorder(head)