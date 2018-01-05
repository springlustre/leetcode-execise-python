def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    dot = 0
    dirName = ""
    for x in path:
        print(stack)
        if x=="/":
            print("dir",dirName)
            if dirName==".." and len(stack) > 0:
                stack.pop()
            elif dirName!="." and dirName!="" and dirName!="..":
                stack.append(dirName)
            dirName = ""
            continue
        else:
            dirName+=x
    print("dir",stack)
    if dirName==".." and len(stack) > 0:
        stack.pop()
    if dirName!="" and dirName!="." and dirName!="..":
        print("stack",stack)
        stack.append(dirName)
    print("stack",stack)
    if len(stack)==0:
        return "/"
    res = ""
    for x in stack:
        res+="/"+x
    return res

a = simplifyPath("///eHx/..")
print(a)
    
