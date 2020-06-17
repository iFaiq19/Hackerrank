def swap_case(s):
    ans = ''
    for i in s:
        if  i == i.upper():
            ans+=i.lower()
        else:
            ans+=i.upper()
    return ans
