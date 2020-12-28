class trie():
    def __init__(self):
        self.val = ""
        self.count = 1
        self.next = []
        self.depth = 1
        self.prev = None
def match(q, a):
    l = len(q)
    if l != len(a):
        return False
    if q[0] == "?":
        for i in range(l):
            if q[l-i-1] == "?":
                break
            if q[l-i-1] != a[l-i-1]:
                return False
    else:
        for i in range(l):
            if q[i] == "?":
                break
            if q[i] != a[i]:
                return False
    return True
            
    
def solution(words, queries):
    result = trie()
    length = [len(word) for word in words]
    tmp_words = [list(word) for word in words]
    M = max(length)
    cur = result
    depth = 0
    answer = []
    leaf = set()

    for word in tmp_words:
        cur = result
        depth = 0
        for c in word:
            depth += 1
            exist = False
            for e in cur.next:
                if e.val == c:
                    e.count += 1
                    exist = True
                    cur = e
                    break
            if not exist:
                tmp = trie()
                tmp.depth = depth
                tmp.val = c
                tmp.prev = cur
                cur.next.append(tmp)
                
                cur = tmp
        leaf.add(tmp)


    for word in list(queries):
        if word[0] == "?":
            tmp = word[::-1]



    for e in leaf:
        print(e.val)

    cur = result
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
