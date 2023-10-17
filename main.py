# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:6])
# print(s[::2])
# print(s[::3])
# print(s[::-1])
# print(s[::-2])
# print(len(s))


# print(input().count('') +0)


# s = input()
# print(s[(len(s) + 1) // 2:]  + s[: (len(s) + 1) // 2])


# s = input()
# if s.count ('f') ==1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))


# s = input()
# s = s[:s.find('h')] + s[s.rfind('h') + 1:]
# print(s)


# print(input().replace('1','one'))


# print(input().replace('@', ''))


# s = input()
# a = s[s.find('h') + 1]
# b = s[s.find('h') + 1:s.rfind('h')]
# c = s[s.rfind('h'):]
# s = a + b.replace('h', 'H') + c
# print(s)
#

# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# else:
#     print(b)


# x = int(input())
# if x > 0:
#     print(1)
# elif x == 0:
#     print(0)
# else:
#     print(-1)


# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
# if (a1+a2)%2 == (b1+b2)%2:
#     print('yes')
# else:
#     print('no')

# year = int(input())
# if (year % 4 == 0 ) and (year % 100 != 0) or (year %  400 == 0):
#     print('yes')
# else:
#     print('no')


# a = int(input())
# b = int(input())
# c = int(input())
# if (a == b == c):
#     print(3)
# elif (a == b != c or a != b == c):
#     print(2)
# else:
#     print(0)



# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
# if a1==a2 or b1==b2:
#     print('yes')
# else:
#     print('no')


# n = int(input())
# m = int(input())
# k = int(input())
# if k < n*m and ((k % n == 0) or (k % m == 0)):
#     print('yes')
# else:
#     print('no')


# n = int(input())
# m = int(input())
# x = int(input())
# y = int(input())
# if n > m:
#     n, m = m, n
# if x >= n / 2:
#     x = n - x
# if y >= m / 2:
#     y = m - y
# if x < y:
#     print(x)
# else:
#     print(y)