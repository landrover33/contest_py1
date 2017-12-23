name = input()

distinctChar = len(set(name))

if distinctChar % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

