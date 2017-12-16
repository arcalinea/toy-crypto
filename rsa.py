# Toy RSA algo

from rsaKeyGen import gen_keypair

# Pick two primes, i.e. 13, 7. Try substituting different small primes
prime1 = 13
prime2 = 7
# Their product is your modulus number
modulus = prime1 * prime2
print "Take prime numbers %d, %d make composite number to use as modulus: %d" % (prime1, prime2, modulus)
print "RSA security depends on the difficulty of determining the prime factors of a composite number."

# Key generation is the most complicated part of RSA. See rsaKeyGen.py for algorithms
print "\n*~*~*~ Key Generation *~*~*~"
keys = gen_keypair(prime1, prime2)
print "All possible keys:", keys
# We'll go with the first keypair: pub 5, priv 29
pubkey = keys[0]['pub']
privkey = keys[0]['priv']
print "Your pubkey is %d, your privkey is %d\n" % (pubkey, privkey)


def encrypt_char(num):
    # multiply num by itself, pubkey times
    r = num ** pubkey
    return r % modulus

def decrypt_char(num):
    # multiply encrypted num by itself, modulus times
    r = num ** privkey
    return r % modulus

def encrypt_word(word):
    encwd = ''
    for char in word:
        n = ord(char)
        enc = encrypt_char(n)
        encwd += chr(enc)
    return encwd

def decrypt_word(word):
    decwd = ''
    for char in word:
        n = ord(char)
        dec = decrypt_char(n)
        decwd += chr(dec)
    return decwd

encwd = encrypt_word('CLOUD')
print "Encrypted word: ", encwd
decwd = decrypt_word(encwd)
print "Decrypted word: ", decwd
