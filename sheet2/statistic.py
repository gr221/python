import string
import grundgesetz
alphabet = dict.fromkeys(string.ascii_lowercase, 0)
gesetz = str(grundgesetz.text.lower())

for i in alphabet.keys():
    print(i, "  ", alphabet[i])

for i in range(0, len(gesetz)):
    if gesetz[i] in alphabet.keys():
        alphabet[gesetz[i]] = alphabet[gesetz[i]] + 1

print(alphabet)
