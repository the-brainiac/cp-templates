# import sys

# input     = sys.stdin.readline
# # def print(*args):
# # 	for i in args:
# # 		sys.stdout.write(str(i))
# # 		sys.stdout.write(' ')
# # 	sys.stdout.write('\n')

# for i in range(int(input())):
#     n = input().strip()
#     print(n)


# sem1 = 9.77
# sem2 = 8.2 
# sem3 = 7.77
# sem4 = 8.95
# sem5 = 8.68
# sem6 = 9.67

# sem = f'(17.5*{sem1})+(20.5*{sem2})+(22*{sem3})+(21*{sem4})+(22*{sem5})+(21*{sem6})'
# print(eval(sem)/124)

def minSquares(m, n):
    if m == 0 or n == 0:
        return 0 
    if m == n:
        return 1
    
    m, n = min(m, n), max(m, n)
    return n//m + minSquares(m, n%m)

print(minSquares(3, 5))
print(minSquares(7, 3))