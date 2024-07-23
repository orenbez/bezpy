    # https://medium.com/cantors-paradise/the-history-of-eulers-number-e-8c982994a39b?source=bookmarks---------65----------------------------
# https://medium.com/cantors-paradise/on-understanding-exponents-52d1045af297?source=bookmarks---------67----------------------------
# https://towardsdatascience.com/share-the-%CF%80-honoring-neglected-mathematical-constants-f651d101e87b?source=bookmarks---------69----------------------------
# https://medium.com/however-mathematics/part-of-our-life-the-number-e-8259e84c0b6d?source=bookmarks---------71----------------------------
# https://medium.com/@gautamnag279/what-is-so-special-about-the-number-1-61803-7e0bbc0e89e2?source=bookmarks---------53----------------------------
# https://medium.com/young-polymaths/in-their-20s-bertrand-russell-b2f7eeb594d1?source=bookmarks---------53----------------------------

from math import e, factorial


# Bernoulli's Question on Continuously compounded interest
def euler(n):
    return (1+1/n) ** n

# starts with $1.00 in the bank

# pays 100% interest per year
total = (1 + 1) ** 1

# pays 50% interest paid out twice a year
total = (1 + 1/2) ** 2

# pays 33.33% interest paid out 3-times a year
total = (1 + 1/3) ** 3

# Euler’s Answer
for i in range(1,100):
    print(euler(i))


def euler2(n):
    return sum([ 1/factorial(i) for i in range(0,n)])



