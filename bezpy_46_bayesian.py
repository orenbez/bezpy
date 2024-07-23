# Try this: https://towardsdatascience.com/an-introduction-to-bayesian-inference-in-pystan-c27078e58d53
# Try this: https://towardsdatascience.com/bayes-theorem-the-holy-grail-of-data-science-55d93315defb?source=bookmarks---------63----------------------------

# MULTIPLICATION RULE
# P(A∩B)=P(B)xP(A|B)

# ADDITION RULE
# P(A∪B)=P(A)+P(B)−P(A∩B)

# MUTUALLY EXCLUSIVE EVENTS
# P(A∩B) = 0.

# INDEPENDENT EVENTS
# P(A|B) = P(A)
# P(B|A) = P(B)
# P(A∩B) = P(A)xP(B)


# BAYES' THM FOR BINARY VARIABLE A
# P(A|B) = P(A∩B)/P(B)
#        = P(B|A)*P(A)/P(B)
#        = P(B|A)*P(A)/[P(B|A)*P(A)+P(B|~A)*P(~A)]
# P(A|B) = posterior,
# P(B|A) = likelihood,
# P(A)   = prior,
# P(B)   = evidence or marginal




#             .
#           /  \
#          /    \
#         /      \
#     ~A /        \ A: P(A)=0.03
#       /          \
#      .            .
#     / \          / \
#  ~B/   \B     ~B/   \B: P(B|A)=0.90
#   /     \      /     \
#  P(B|~A)=0.05


# ===========================================================================
# Bayes’Theorem EXAMPLE - DRUG TEST
# ===========================================================================
# A = Taking the Drug
# B = Tested +ve for the drug
# P(A) BASE RATE  = 3%    (People who are on the drug)
# P(B|A)   = SENSITIVITY = 90%   (True +ve)
# P(~B|~A) = SPECIFICITY = 95%   (True -ve)
# P(B|~A)  = 5%                  (False +ve)
# P(A|B) = 0.03 * 0.90 / (0.03 * 0.90 + 0.97 * 0.05)
p_a_given_b = 0.03 * 0.90 / (0.03 * 0.90 + 0.97 * 0.05)   # THEORETICAL PROBABILITY

from random import randint


sample = 5000

p = int(0.03 * sample)  # drug takers
n = int(0.97 * sample)  # not drug takers

ptp = 0   # positive & tested positive
ptn = 0   # positive & tested negative
ntp = 0   # negative & tested positive
ntn = 0   # negative & tested negative

for _ in range (p):
    result = randint(1,100)
    if result <= 90:
        ptp += 1
    else:
        ptn +=1

for _ in range (n):
    result = randint(1,100)
    if result <= 95:
        ntn += 1
    else:
        ntp +=1

a_given_b = ptp/(ptp + ntp)  # EXPERIMENTAL PROBABILITY

print('By formula we expect P(A|B) =', p_a_given_b)
print('By experiment we get P(A|B) =', a_given_b )

