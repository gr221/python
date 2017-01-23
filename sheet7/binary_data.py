import array

f = open("bin.dat", "br")
s = f.read()
f.close()
numbers = array.array('d')
numbers.frombytes(s)
value = 0
for i in range(0,len(numbers)):
    value += numbers[i]

print(value)
