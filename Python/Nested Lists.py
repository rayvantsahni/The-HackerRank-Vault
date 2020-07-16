if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        lis = []
        name = input()
        score = float(input())

        lis.append(name)
        lis.append(score)

        a.append(lis)

    b = []
    for i in range(len(a)):
        b.append(a[i][1])
    
    x = list(sorted(set(b)))[1]

    c = []
    for i in range(len(a)):
        if a[i][1] == x:
            c.append(a[i][0])

    c.sort()
    for i in c:
        print(i)
