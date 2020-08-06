def no_dups(s):
    # Your code here
    words = s.split()
    count = 0
    
    d = {}
    space = " "
    
    for word in words:
        if word in d:
            continue
        else:
            count += 1
            d[word] = count
    return space.join(d.keys())
    

    
print(no_dups("hello hello"))

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))