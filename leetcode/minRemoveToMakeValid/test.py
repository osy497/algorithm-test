class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removed_par = set()
        stack = []
        tmp = 0
        for i, c in enumerate(s):
            
            if c == "(":
                tmp += 1
                stack.append(i)
            elif c == ")":
                if tmp > 0:
                    tmp -= 1
                    stack.pop()
                else:
                    removed_par.add(i)
        removed_par = removed_par.union(set(stack))
        answer = ""
        for i, c in enumerate(s):
            if i in removed_par:
                continue
            else:
                answer += c
        return answer
                
