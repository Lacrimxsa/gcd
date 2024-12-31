def gcd_(a, b):

    while b:
        a, b = b, a % b

    return a

# 5
print(str(gcd_(12,8)))

# 5, two steps
print(str(gcd_(64,48)))

# 7, three steps 
print(str(gcd_(423, 81 )))

# 5
print(str(gcd_(25,5)))

'''
'''