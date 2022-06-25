import sys
input = sys.stdin.readline

# 10818
# n = int(input())
# a = list(map(int, input().split()))
# print(min(a),max(a))

# 2562

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
# g = int(input())
# h = int(input())
# i = int(input())
# sum = [a,b,c,d,e,f,g,h,i]
# print(sum)
# print(max(sum))
# print(sum.index(max(sum))+1)

# numbers = []
# for i in range(9):
#     a = int(input())
#     numbers.append(a)
# print(max(numbers))
# print(numbers.index(max(numbers))+1)

# num = [int(input()) for i in range(9)]
# print(max(num))
# print(num.index(max(num))+1)

# 2577
a = input()
b = input()
c = input()
sum = [] 
sum.append(int(a)*int(b)*int(c))
sum = str(sum)

string = ''.join(sum)

for i in range(10):
    print(string.count('%d'%i))







































