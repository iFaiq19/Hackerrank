if __name__ == '__main__':
    list_ = []
    list1 = []
    for _ in range(int(input())):
        mylist = []
        name = input()
        mylist.append(name)
        score = float(input())
        mylist.append(score)
        list1.append(score)
        list_.append(mylist)
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    list2 = sorted(list2)
    minimum = list2[1]
    names = []
    for j in list_:
        if j[1]==minimum:
            names.append(j[0])
    names = sorted(names)
    for names in names:
        print(names)

