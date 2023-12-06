import random

# Message to be encrypted
msg = 66971141001051011143265110100114101105

# Large prime number 'p' and generator 'g' for the group
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

# Generating a random private key 'a'
a = random.randint(1, p - 2)

# Calculating the public key 'r' using the private key 'a'
r = pow(g, a, p)

# Generating another random number 'k' used for the encryption process
k = random.randint(1, p - 2)

# Computing another public key 'gamma' using 'k'
gamma = pow(g, k, p)
print("\nOriginal message:", msg)
print("\nRandom private key (a):", a)

print("Computed public key (r):", r)

print("\nRandom secret key (k):", k)
print("Computed public key (gamma):", gamma)

# Encrypting the message. The ciphertext is the product of the message and 'r' raised to the power 'k', modulo 'p'
ciphertext = msg % p * pow(r, k, p)
print("\nCiphertext:", ciphertext)

# Decrypting the message. It involves using 'gamma', 'a', and the ciphertext The decrypted message is obtained by
# multiplying the ciphertext with 'gamma' raised to the power of 'p-1-a', modulo 'p'
decrypted = (pow(gamma, p - 1 - a, p) * ciphertext) % p
print("Decrypted message:", decrypted)

assert msg == decrypted
