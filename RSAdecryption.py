from Crypto.Util.number import inverse, long_to_bytes

n=
e=
c=
p=
q=

phi = (p-1)*(q-1)
d= inverse(e, phi)
message=pow(c, d, n)
print(long_to_bytes(message))
