if __name__ == '__main__':
    my_list = []
    N = int(input())
    for i in range(N):
        command = input().split()
        match(command[0].lower()):
            case "print":
                print(my_list)
            case "remove":
                my_list.remove(int(command[1]))
            case "append":
                my_list.append(int(command[1]))
            case "sort":
                my_list.sort()
            case "pop":
                my_list.pop()
            case "reverse":
                my_list.reverse()
            case "insert":
                my_list.insert(int(command[1]), int(command[2]))
            case _:
                print("Invalid Command")