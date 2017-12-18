
# Greatest Common Denominator
def gcd(a, b):
    if a is 0:
        return b
    return gcd(b % a, a)

def is_prime(x):
  if x == 1:
    return False
  else:
    for a in range(2,x):
      if x % a == 0:
        return False
  return True

# Euler's Totient Function
# Count of numbers up to n which are relatively prime to n
# Finding phi from composite for large numbers is hard
def phi_hard(composite):
    count = 1
    for num in range(2, composite):
        if gcd(num, composite) is 1:
            count += 1
    return count

# If you know prime factors of composite, finding phi becomes easy
def phi_easy(p1, p2):
    return (p1 - 1) * (p2 - 1)

####### Key Generation #######
# For key generation, we have the 2 prime factors that form the composite, so we can use phi_easy() to find the totient
# To break RSA, you would only have the composite, thus would have to use phi_hard() to derive totient -> privkey.

# pubkeys are a coprime of the composite modulus
def find_pubkeys(p1, p2):
    pubkeys = []
    totient = phi_easy(p1, p2)
    # start from 3, smallest prime. in practice, starts at bigger prime (65537)
    for pub in range(4, totient):
        if is_prime(pub):
            pubkeys.append(pub)
    return pubkeys

# Extended Euclidean Algorithm
# privkey is modular multiplicative inverse of pubkey
def find_privkey(pubkey, p1, p2):
    composite = p1 * p2
    totient = phi_easy(p1, p2)
    for priv in range(1, composite):
        if ((pubkey * priv) - 1) % totient is 0:
            return priv

def gen_keypair(p1, p2):
    keys = []
    pubkeys = find_pubkeys(p1, p2)
    for pub in pubkeys:
        priv = find_privkey(pub, p1, p2)
        if priv is not None:
            keys.append({"pub": pub, "priv": priv})
    return keys
