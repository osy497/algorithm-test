from collections import defaultdict
class Node():
    def __init__(self):
        self.children = dict()
        self.count = 0
class Trie():
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur_node = self.head
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Node()
            cur_node.count += 1
            cur_node = cur_node.children[c]


    def search(self, word):
        cur_node = self.head
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return 0
        return cur_node.count


def solution(words, queries):
    answer = []
    a = defaultdict(Trie)
    b = defaultdict(Trie)

    for word in words:
        a[len(word)].insert(word)
        b[len(word)].insert(word[::-1])

    for q in queries:
        print(q)
        if q[0] == "?":
            flag = True
        else:
            flag = False

        if flag:
            post_word = q[::-1][:q[::-1].index("?")]
            answer.append(b[len(q)].search(post_word))
        else:
            post_word = q[:q.index("?")]
            answer.append(a[len(q)].search(post_word))
    return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "???do"]))
#print(solution(["a", "ab", "b", "bb", "ba", "aa", "ac", "cb"], ["?b", "a?"]))
