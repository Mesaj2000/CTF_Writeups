When you run the netcat, you are presented with the following:
```
c: 10969609155267016506269562337303125979933921109305154074098006761236025359697508
n: 15782823759852742232432148741595588439623353185497593659674214629755156235049263
e: 65537
```
The specific numbers are always different, but the method is always the same: n is small (only 80 digits)

Throwing this into a [factoring calculator](https://www.alpertron.com.ar/ECM.HTM), we get the factors of n are:
```
p: 125011602163538448153186739667457952549
q: 126250871812728794389752525761714997947587
```

At this point, we can just use the RSA equations:
```
phi = (p-1) * (q-1)
d = modular inverse of e mod phi
plaintext = (c ^ d) % n
```

We can do the second step with gmpy2.invert, and the third with python's pow function

Converting plaintext (a decimal number) into hex, then ascii, gives: `picoCTF{us3_l@rg3r_pr1m3$_2461}`

The [full python script](SuperSafeRSASolution.py) is as follows:
```
from gmpy2 import invert

# Given values
n = 15782823759852742232432148741595588439623353185497593659674214629755156235049263
p = 125011602163538448153186739667457952549
q = 126250871812728794389752525761714997947587
c = 10969609155267016506269562337303125979933921109305154074098006761236025359697508
e = 65537

# Solve for plaintext
phi = (p - 1) * (q - 1)	
d = invert(e, phi)
plaintext = pow(c, d, n)
	
# Convert plaintext (a decimal number) into hex, then ascii
hex = hex(plaintext)[2:]
if hex[-1] == "L":
    hex = hex[:-1]
print(bytearray.fromhex(hex).decode())
```
