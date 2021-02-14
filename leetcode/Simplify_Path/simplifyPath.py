class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        
        stack = []
        for p in path:
            if p == "." or not p:
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        answer = ''.join([ e + "/" for e in stack])
        return "/" + answer[:-1]
                
        
