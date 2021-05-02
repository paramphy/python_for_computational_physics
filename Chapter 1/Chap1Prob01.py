import sys


N = sys.argv[1]

print("Number of terms you want to print: " + N)

f = [0, 1]

for i in range(int(N)):

    if i > 1:

        f.append(f[i - 1] + f[i - 2])

print(f)
