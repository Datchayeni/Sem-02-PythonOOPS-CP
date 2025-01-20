n=int(input())
l=[] 
for i in range(n): 
    a=int(input())
    l.append(a) 
non_zero = 0
for i in range(len(l)):
    if l[i]!=0:
        l[non_zero],l[i]=l[i],l[non_zero]
        non_zero += 1 
print("Updated array:", l)

n=int(input())
l=[] 
for i in range(n): 
    a=int(input())
    l.append(a) 
non_zero = 0
for i in range(len(l)):
    if l[i]==0:
        l[non_zero],l[i]=l[i],l[non_zero]
        non_zero += 1 
print("Updated array:", l)

n=int(input())
prices=[]
for i in range(n):
    prices.append(int(input()))
max_profit=0
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        max_profit=prices[i]+prices[i-1]
print("Maximum profit:",max_profit)

#16.01.25
d1={"a":2,"b":4,"c":6} 
sum_d=0 
for num in d1.values():
    sum_d+=num 
    print("The sum of elements in the dictionary is:",sum_dict) 

n=int(input("Enter number:")) 
for i in range(1,n+1):
    for  j in range(1,i+1):
        print(i,end=" ")
    print()

#17.01.25
def reverse_string(s): 
    if len(s)<=1: 
        return s 
    return reverse_string(s[1:])+s[0] 
in_str=input() 
reversed_str=reverse_string(in_str) 
print(reversed_str) 
 
 
def cal_power(x,y): 
    if y==0: 
        return 1 
    else: 
        return x*cal_power(x,y-1) 
a=int(input()) 
b=int(input()) 
cal=cal_power(a,b) 
print(cal) 
 
n=int(input()) 
arr=[] 
for _ in range(n): 
    l=list(map(int,input().split())) 
    arr.append(l) 
for i in range(n): 
    for j in range(n): 
        print(arr[i][j], end=" ") 
    print() 
print("transpose matrix is: ") 
for j in range(n): 
    for i in range(n): 
        print(arr[i][j], end=" ") 
    print() 
 
def palindrome(n):
    rev=n[::-1]
    if n==rev:
        print(n,"is a palindrome")
    else:
        print(n,"is not a palindrome")
n=input("Enter a string:")
palindrome(n)

 
n=int(input()) 
arr=[] 
for i in range(n): 
    l=list(map(int,input().split())) 
    arr.append(l) 
total=0 
for row in arr: 
    for col in row: 
        total+=col 
print('The sum of all elements in the 2D array is:',total) 

def sum_dig(n): 
    if n<10: 
        return n
    else:
        return n%10+sum_dig(n//10)
num=int(input()) 
result=sum_dig(num) 
print(result)



