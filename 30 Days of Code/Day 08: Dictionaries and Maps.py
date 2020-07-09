# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
#print(n)

a={}
for i in range(n):
    name,phoneNumber=input().split()
    a[name]=phoneNumber

while(True):
    try:
        i=input()
        if i in a:
            print(i + "=" + a[i])

        else:
            print("Not found")

    except:
        break

        
    
