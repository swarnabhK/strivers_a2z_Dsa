# Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.


# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        res = []
        for dir in dirs:
            if dir=="" or dir==".":
                continue
            elif res and dir=="..":
                res.pop()
            elif dir!="..":
                res.append(dir)
        return "/"+"/".join(res);