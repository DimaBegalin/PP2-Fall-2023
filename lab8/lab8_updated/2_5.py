l = ['apple', 'banana', 'cherry']

with open('output.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)
