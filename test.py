while 1:
    try:
        input()
        s=input().split()
        print(s[-int(input())])
    except:
        raise
        break