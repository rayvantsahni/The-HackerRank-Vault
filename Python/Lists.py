if __name__ == '__main__':
    N = int(input())
    l_ = []

    for q in range(N):
        query = input()

        if query.split()[0] == "insert":
            l_.insert(int(query.split()[1]), int(query.split()[2]))

        elif query.split()[0] == "print":
            print(l_)

        elif query.split()[0] == "remove":
            l_.remove(int(query.split()[1]))

        elif query.split()[0] == "append":
            l_.append(int(query.split()[1]))

        elif query.split()[0] == "sort":
            l_.sort()

        elif query.split()[0] == "pop":
            l_.pop()

        elif query.split()[0] == "reverse": 
            l_.reverse()
