# Toy RSA algo

# Pick two primes
prime1 = 13
prime2 = 7
# Their product is your group
maxp = prime1 * prime2
print "Prime numbers %d, %d make field %d" % (prime1, prime2, maxp)
# arbitrary num in group
pubkey = 5
# how to derive privkey? Extended Euclidian algo?
privkey = 29
print "Your pubkey is %d, your privkey is %d" % (pubkey, privkey)

def encrypt_char(num):
    # multiply num by itself, pubkey times
    r = num ** pubkey
    return r % maxp

def decrypt_char(num):
    # multiply encrypted num by itself, maxp times
    r = num ** privkey
    return r % maxp

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
