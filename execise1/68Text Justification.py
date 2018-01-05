def fullJustify(words, maxWidth):
    """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
    res = []
    v = []
    cnt = 0
    i=0

    while i <len(words):
        w = words[i]
        length = len(w)
        cnt+=length
        print(w,cnt,i)
        if cnt<=maxWidth:
            v.append(w)
            cnt+=1
            i+=1
            if i<len(words):
                continue

        wCnt = len(v)
        if wCnt==1:
            if v[0]=="":
                res.append(" "*maxWidth)
            else:
                res.append(v[0]+" "*(maxWidth-len(v[0])))
        elif  i==len(words):
            word = ""
            for k in range(wCnt-1):
                    word+= v[k]+" "
            word+=(v[-1]+" "*(maxWidth-len(word)-len(v[-1])))
            res.append(word)
        else:
            empty = maxWidth - (cnt-length - wCnt)
            min = empty // (wCnt-1)
            remain = empty % (wCnt-1)
            print("--",empty,min,remain)
            word = ""
            for k in range(wCnt-1):
                if k < remain:
                    word+= (v[k]+" "*(min+1))
                else:
                    word+= (v[k]+" "*min)
            word+=v[-1]
            res.append(word)
        cnt = 0
        v = []


    return res
a = fullJustify(["What","must","be","shall","be."],12)
print(a)
    
