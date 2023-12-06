import random

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

a = random.randint(1, p-1)
b = random.randint(1, p-1)

A = pow(g, a, p)
B = pow(g, b, p)


DH_key_alice = pow(B, a, p)
DH_key_bob = pow(A, b, p)

print(f'Alice\'s private key (a) = {a}')
print(f'Bob\'s private key (b) = {b}')

print(f'\nAlice\'s public key (A) = {A}')
print(f'Bob\'s public key (B) = {B}')

print(f'\nALice\'s key = {DH_key_alice}')
print(f'Bob\'s key = {DH_key_bob}')

assert DH_key_bob == DH_key_bob