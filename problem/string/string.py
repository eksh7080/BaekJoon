# import sys
# input = sys.stdin.readline

# import string
# string.ascii_lowercase

# 11654
# a = input()
# print(ord(a))

# 11720
# a = int(input())
# b = map(int,input().strip())
# print(sum(b))

# n = int(input())
# s = str(input()) #list 도 가능
# sum = 0
# for i in range(n):
#     sum += int(n[i])
# print(sum)

# 10809
# word = list(input())
# aski = 97
# pr=[]

# for i in range(26):
#     if chr(aski) in word:
#         pr.append(word.index((chr(aski))))
#     else:
#         pr.append("-1")
#     aski+=1

# for i in range(26):
#     print(pr[i],end=" ")

# word = input()
# aski = list(range(97,123))

# for i in aski:
#     print(word.find(chr(i)),end=" ")

# 2675
test = int(input())

for i in range(test):
    r,s = input().split()
    r=int(r)
    for j in range(len(s)):
        print(s[j]*r,end="")
    print()

