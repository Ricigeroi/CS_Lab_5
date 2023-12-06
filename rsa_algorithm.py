from Crypto.Util.number import getPrime


def gcd(a, h):
    temp = 0
    while True:
        temp = a % h
        if temp == 0:
            return h
        a, h = h, temp


# Generate prime numbers p and q
p = getPrime(1536)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = 65537
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# Calculate d, the modular inverse of e modulo phi
d = pow(e, -1, phi)

# Message to be encrypted
msg = 66971141001051011143265110100114101105

print(f'\np = {p}')
print(f'q = {q}')
print(f'n = {n}')
print(f'e = {e}')
print(f'phi = {phi}')
# Encryption
c = pow(msg, e, n)
print("\nMessage data =", msg)
print("Encrypted data =", c)

# Decryption
m = pow(c, d, n)
print("Original Message Sent =", m)

