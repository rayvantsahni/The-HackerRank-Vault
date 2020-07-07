# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
#print(n)

a=[]
for i in range(n):
    a.append(input())

#print(a)

for i in a:
    o=''
    e=''
    #print(type(o));print(type(e))
    for j in range(len(i)):
        if j%2==0:
            e=e+list(i)[j]
            #e.append(list(i)[j])

        if j%2==1:
            o=o+list(i)[j]
            #o.append(list(i)[j])

    '''e=tuple(e)
    o=tuple(o)'''
    
    print(e,o)
