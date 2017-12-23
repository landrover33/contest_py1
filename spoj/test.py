# http://www.spoj.com/problems/TEST/
# TEST - Life, the Universe, and Everything




# k = int(input())
# while k != 42:
#     print(k)
#     k = int(input())


k = int(input())
flag = True
while flag:
    if k != 42:
        print(k)
        k = int(input())
    else:
        flag = False
