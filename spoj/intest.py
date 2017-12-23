# http://www.spoj.com/problems/INTEST/
# problem - Enormous Input Test

n = int(input())
k = int(input())

count = 0
for i in range(n):
    i = int(input())
    if (i % k) == 0:
        count = count + 1
print(count)
