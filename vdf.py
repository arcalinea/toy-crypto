# Verifiable Delay Functions
import time 

def benchmark(func):
    start = time.time()
    res = func() 
    stop = time.time()
    return res, stop - start

# Prover:
# h = g^(2^T)
# g is thing you've hashed into the group
# T is network parameter, how long you want it to take
# h is output when prover finishes VDF

g = 3
T = 22
 
def run_delay():
     h = g**(2**T)
     return h

print "Running VDF => h = g^(2^T)"
h, h_time = benchmark(run_delay)
print "Time to run VDF:", h_time

# Verifier:
# Picks L (challenge prime), sends to Prover

L = 23

# Prover:
# Because 2^T = L*q + r, solves for q and r by dividing by L =>  (2^T) / L = (q,r)
# Computes proof (pi) =>  pi = g^q
# Sends pi (proof) and h (output) to the verifier

(q, r) = divmod((2**T), L)

print "Finding quotient, remainder => (q, r) = (2^T) / L =>", (q, r) 

def create_proof():
    pi = g ** q
    return pi

print "Creating proof => proof = g^q"
pi, pi_time = benchmark(create_proof)
print "Time to create proof:", pi_time
print "Ratio of proof to delay time: 1 /", h_time / pi_time

# Verifier:
# Knows g, picked L, and just got pi
# Gets r through 2^t % L
# g^(2^T) = pi^L * g^r
# = (g^q)^L * g^r
# = g^(Lq + r)
# = g^(2^T)

print "Checking proof => h == pi^L * g^r =>", h == pi**L * g**r