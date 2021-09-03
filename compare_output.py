f1 = open('output.txt')
f2 = open('output1.txt')

output1 = f1.readlines()
output2 = f2.readlines()

for i in range(len(output1)):
    if output1[i] != output2[i]:
        print(i, output1[i], output2[i])