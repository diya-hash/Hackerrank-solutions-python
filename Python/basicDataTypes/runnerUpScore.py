if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(arr)
    mylist.sort()
    s = set(mylist)
    
    print(list(s)[-2])