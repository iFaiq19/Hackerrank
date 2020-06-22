import textwrap

def wrap(string, max_width):
    a = len(string)
    outpt = []
    for i in range(0, a, max_width):
        if len(string[i:]) >= max_width:
            outpt.append(string[i:i+max_width])
        else:
            outpt.append(string[i:])
            break
    return '\n'.join(outpt)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)