def count_substring(string, sub_string):
    a = len(sub_string)
    count = 0
    for i in range(len(string)):
        if string[i:i+a]==sub_string:
            #print(string[i:i+a])
            count += 1
    return count

    return count
