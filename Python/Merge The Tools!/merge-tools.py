def merge_the_tools(string, k):
    temp = []
    len_temp = 0
    for i in string:
        len_temp += 1
        if i not in temp:
            temp.append(i)
        if len_temp == k:
            print(''.join(temp))
            temp = []
            len_temp = 0
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)