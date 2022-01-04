# Explanation:


# 1 5 9 13

# 2 6 10 14

# 3 7 11 15

# 4 8 12 16

def Amazing_Pattern_Drawing():
    constant_term=3
    for i in range(1,5):
        for j in range(1,5):
            print(4*j-constant_term,end='  ')
        print(end='  ')
        print("\n")
        constant_term=constant_term-1

print(Amazing_Pattern_Drawing())