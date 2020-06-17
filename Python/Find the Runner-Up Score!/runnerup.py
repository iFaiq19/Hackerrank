if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = []
    for i in arr:
        if i not in mylist:
            mylist.append(i)
    mylist = sorted(mylist)
    print(mylist[len(mylist)-2])
