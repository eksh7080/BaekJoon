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
#         pr.append(word.index(chr(aski)))
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
# test = int(input())

# for i in range(test):
#     r,s = input().split()
#     r=int(r)
#     for j in range(len(s)):
#         print(s[j]*r,end="")
#     print()

# 1157

# alpa = input().upper()       
# set_list = list(set(alpa))    
# al_arr = []

# for i in set_list:
#     al_arr.append(alpa.count(i))   

# if  al_arr.count(max(al_arr)) > 1:    
#     print("?")
# else:
#     print(set_list[al_arr.index(max(al_arr))])

# print(set_list)
# print(al_arr,max(al_arr))
# print(al_arr.count(max(al_arr)))
# print(al_arr.index(max(al_arr)))

# 1152
# string_list = input().split()
# print(len(string_list))

# 2908
# sang = list(input().split())
# sang_arr = []
# for i in range(len(sang)):
#     sang_re = sang[i][::-1]
#     sang_arr.append(sang_re)
# print(max(sang_arr))

# su,sang = input().split()
# su = int(su[::-1])
# sang = int(sang[::-1])
# print(max(su,sang))

# 5622
# distr = input()

# dial = {2: ['A','B','C'], 3: ['D','E','F'], 4: ['G','H','I'], 5: ['J','K','L'], 6: ['M','N','O'], 7: ['P','Q','R','S'], 8: ['T','U','V'], 9: ['W','X','Y','Z']}

# cnt = 0

# dial_list = list(dial.values())
# dial_key = list(dial.keys())
# dial_items = (dial.items())

# for i in distr:
#     if i in dial_list[0]:
#         cnt += 3
#     elif i in dial_list[1]:
#         cnt += 4
#     elif i in dial_list[2]:
#         cnt += 5
#     elif i in dial_list[3]:
#         cnt += 6
#     elif i in dial_list[4]:
#         cnt += 7
#     elif i in dial_list[5]:
#         cnt += 8
#     elif i in dial_list[6]:
#         cnt += 9
#     elif i in dial_list[7]:
#         cnt += 10

# print(cnt)

# for i in distr:
#     for j,k in dial_items:
#         if i in k:
#             cnt += j+1

# print(cnt)


# 2941
# croatia = input()
alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpa = list(range(97,123))
cnt = 0
alpa_arr = []

for i in alpa:
    alpa_arr.append(chr(i))

print(alpa_arr)
# for i in croatia:
#     for j in range(len(alpabet)):
#         if i in alpabet[j]:
#             cnt+=1

# print(cnt)


