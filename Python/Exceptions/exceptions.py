for i in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        result = a // b
        print(result)
        
    except ZeroDivisionError as x:
        print("Error Code:", x)
    except ValueError as y:
        print("Error Code:", y)