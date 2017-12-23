# https://www.codechef.com/problems/HS08TEST
# Problem Code: HS08TEST

withdraw, balance = input().split("\n")

withdraw = float(withdraw)
balance = float(balance)

# if 0 < withdraw <= 2000 and 0 < balance <= 2000:

validAmount = False
enoughBalance = False
charge = 0.50
if balance >= (withdraw + charge):
    enoughBalance = True
if (withdraw % 5) == 0:
    validAmount = True
if enoughBalance and validAmount:
    balance = balance - (withdraw + charge)

print('{:.2f}'.format(balance))
