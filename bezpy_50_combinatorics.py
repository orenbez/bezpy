# TRY THIS: https://medium.com/i-math/combinations-permutations-fa7ac680f0ac

from sre_constants import SUCCESS
import numpy as np
from math import *
from itertools import permutations, combinations, combinations_with_replacement, product  # itertools is in the Standard Library

# Combinatoric generators from itertools:
# product(p, q, ... [repeat=1]) --> cartesian product of two or more sets i.e. every possible pair combination of elements
# permutations(p[, r]) default of permutations(p) is just the arrangments of all of the objects in p
# combinations(p, r)
# combinations_with_replacement(p, r)

# ==================================================================================================================
# How many ways to arrange 'n' objects
# ==================================================================================================================
def arrange(n):
    return int(factorial(n))

# ==================================================================================================================
# Pick 'r' from 'n' Without Replacement.  Note you can use math.perm(n,k) as of python 3.8
# ==================================================================================================================
def perms(n, r):
    return int(factorial(n)/factorial(n - r))

# ==================================================================================================================
# Pick 'r' from 'n' with Replacement / Repetition
# ==================================================================================================================
def perms_with_replacement(n, r):
    return pow(n, r)

# ==================================================================================================================
# Pick 'r' from 'n' objects where one of the objects has x repeats => divide by x!
# e.g. arrangements of   A,B1,B2,B3,C,D,E
# ==================================================================================================================
def perms_with_duplicates(n, r, x):
    return int(factorial(n) / (factorial(x) * factorial(n - r)))

# ==================================================================================================================
# Pick 'r' from 'n' with where two  the objects has 2-sets of repeats  x-times and y-times => divide by x!y!
# e.g. arrangements of   A,B1,B2,B3,C,D1,D2,E
# ==================================================================================================================
def perms_with_duplicates2(n, r, x, y):
    return int(factorial(n)/(factorial(x) * factorial(y) * factorial(n-r)))


# ==================================================================================================================
# Cyclical Permutations  e.g.   ABCDE = BCDEA  => divide perms by 'r'
# Pick 'r' from 'n' around a table
# ==================================================================================================================
def perms_cyclical(n, r):
    return int(factorial(n)/(r * factorial(n-r)))

# ==================================================================================================================
# Note:
# nCr ≡ nC(n-r)
# (n+1)Cr = nCr + nC(r−1)
# nC0 + nC1 + . .. nCn−1 + nCn = 2^n 
# (1 + x) n = nC0 + nC1x +nC2 x^2 + . .. + nCn−1 x^n−1 + nCn x^n    Binomial Expansion


# ==================================================================================================================

# ==================================================================================================================
# Combine 'r' from 'n' object without Replacement or Repetition. Note you can use math.comb(n,k) as of python 3.8
# ==================================================================================================================
def combs(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

# ==================================================================================================================
# Combine 'r' from 'n' object  with replacement or repetition
# Derivation: Consider that you are adding r-1 objects back to the pot for repeated selection
# ==================================================================================================================
def combs_with_replacement(n, r):
    return combs(n + r - 1, r)




# Independent perms or combs are multiplied to give total  e.g. P1 and P2 = P1 x P2
# Mutually exclusive perms or combs are added e.g. C1 or C2 = C2 + C2


if __name__ == '__main__':


    arr1 = [1, 2, 3]
    arr2 = [5, 6]
    cartesian_product = list(product(arr1, arr2))   # [(1, 5), (1, 6), (2, 5), (2, 6), (3, 5), (3, 6)]

    list(product((0,1), (0,1), (0,1))) # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

    objects = ['a','b','c']
    n = len(objects)
    
    x = list(permutations(objects, r=2))                   # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
    y = list(combinations(objects, r=2))                   # [('a', 'b'), ('a', 'c'), ('b', 'c')]
    z = list(combinations_with_replacement(objects, r=2))  # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

    list(permutations(objects, 3))   #  = list(permutations(objects)
    # [('a', 'b', 'c'),
    #  ('a', 'c', 'b'),
    #  ('b', 'a', 'c'),
    #  ('b', 'c', 'a'),
    #  ('c', 'a', 'b'),
    #  ('c', 'b', 'a')]

    assert perms(n, 2) == len(x)
    assert combs(n, 2) == len(y)
    assert combs_with_replacement(n, 2) == len(z)


   # Permutaions of 'PENNY' i.e  P-E-N1-N2-Y
    assert perms_with_duplicates(5, 3, 2) == 30


    # For selecting cards from a pack we consider 'combinations' since ('3♠,'4♥','5♦','6♣','7♥') is the same in any
    # sequence.  The individual object of a card is fixed.
    # see https://medium.com/intuition/math-of-poker-a353c0d3586e
    # Set of 52 cards
    suits = {'♠','♥','♦','♣'}
    values = {'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
    cards = [v + s for s in suits for v in values]

    # OR
    cards = list(product(values, suits))

    # Display 52 Cards in the pack
    for (idx, card) in enumerate(cards, 1):
        print(idx, card)

    # ==================================================================================================================
    # Combinations of Poker Hand = 2598960
    # ==================================================================================================================
    combs_poker_hand = list(combinations(cards, r=5))
    assert(len(combs_poker_hand) == combs(52, 5) == 2598960)

    # ==================================================================================================================
    # ROYAL FLUSH e.g. A♦ K♦ Q♦ J♦ 10♦
    # ==================================================================================================================
    royal_flush = combs(4, 1) # Choose one suit out of 4  (A, K, Q, J, 10, all the same suit.)
    assert royal_flush == 4

    # ==================================================================================================================
    # STRAIGHT FLUSH e.g. 5♦ 4♦ 3♦ 2♦ A♦
    # ==================================================================================================================
    # Choose Suit and then choose start card from  A to 10
    # excludes the royal flush
    straight_flush = combs(4, 1) * combs(10, 1) - royal_flush
    assert straight_flush == 36

    # ==================================================================================================================
    # FOUR OF A KIND e.g. 2♦ A♣ A♥ A♦ A♠
    # ==================================================================================================================
    # Choose any card A to K and then chose last card out of the 48 cards left
    four_of_a_kind = combs(13, 1) * combs(48, 1)
    assert four_of_a_kind == 624

    # ==================================================================================================================
    # FULL HOUSE e.g. 2♦ 2♣ A♥ A♦ A♠
    # ==================================================================================================================
    # Choose any card A to K, then choose 3 out of the 4 of that value
    # Then Choose 1 of the 12 numbers left and choose two of that value
    full_house = combs(13, 1) * combs(4, 3) * combs(12, 1) * combs(4, 2)
    assert full_house == 3744

    # ==================================================================================================================
    # FLUSH e.g. 9♦ 4♦ J♦ 2♦ A♦
    # ==================================================================================================================
    # Any five cards of the same suit
    # Choose a suit, then chose 5 from 13 cards of that suit
    # exclude straight flush or royal flush
    flush =  combs(4, 1) * combs(13, 5) - straight_flush - royal_flush
    assert flush == 5108

    # ==================================================================================================================
    # STRAIGHT e.g. 10♦ J♣ Q♥ K♣ A♦
    # ==================================================================================================================
    # Five cards in a sequence can choose starting card from {A, 2, 3, ..., 10} (10 starter choices)
    # Then choose a suit (x 4 choices)
    # 2nd card is one of 4 and so on for 3rd, 4th, 5th
    straight = combs(10, 1) * combs(4, 1) * combs(4, 1) ** 4 - straight_flush - royal_flush
    assert straight == 10200

    # ==================================================================================================================
    # THREE OF A KIND e.g 7♦ 7♣ 7♥ K♣ A♦
    # ==================================================================================================================
    # Three cards of the same rank.
    # First choose 1 of the 13 cards and then 3 out of 4 for that suit
    # Second choose 2 of 48 eligible cards left subtract the full_house possibilities
    three_of_a_kind = combs(13, 1) * combs(4, 3) * combs(48, 2) - full_house
    assert three_of_a_kind == 54912
    
    # alternatively
    # First choose 1 of the 13 cards and then 3 out of 4 for that suit
    # Second chose 2 different cards from 12 cards left, each card could be one of 4 suits
    three_of_a_kind = combs(13, 1) * combs(4, 3) * combs(12, 2) * combs(4, 1) * combs(4, 1)
    assert three_of_a_kind == 54912


    # ==================================================================================================================
    # TWO PAIR
    # ==================================================================================================================
    # Choose 2 cards from the 13 available and 2 out of 4 for each of those cards
    # For the last card you need to choose 1 from the 11 left and 1 of 4 suits for that card
    two_pair = combs(13, 2) * combs(4, 2) * combs(4, 2) * combs(11, 1) * combs(4, 1)

    # Alternatively ...
    # Choose first pair from 13 ranks, for which you need to choose 2 out of the 4
    # Choose 2nd pair from 12 ranks , for which you need to choose 2 out of the 4
    # halve the result so that AAKK & KKAA are not counted twice (due to the symmetry of two pairs)
    # For the last card you need to choose 1 from the 44 left
    two_pair = combs(13, 1) * combs(4, 2) * combs(12, 1) * combs(4, 2) * 0.5 * combs(44, 1)
    assert two_pair == 123552

    # ==================================================================================================================
    # ONE PAIR
    # ==================================================================================================================
    # Chose one of the 13 values, each choice requires you to choose 2 of the 4 available of that value
    # Then choose the 3 other values from the 12 left and each of those requires you to choose one of 4 viable
    one_pair = combs(13, 1) * combs(4, 2) * combs(12, 3) * combs(4, 1) ** 3
    assert one_pair == 1098240

    # ==================================================================================================================
    # HIGH CARD
    # ==================================================================================================================
    # First choose 5 values from 13 and select 1 suit of 4 for each card subtract the exclusions
    high_card = combs(13, 5) * combs(4, 1) ** 5 - royal_flush - straight_flush - flush - straight
    assert high_card == 1302540

    # Note: If you are throwing Five Dice ultimately each specific die
    # is considered individually and hence we must use 'permutations' for the correct possibility space

    # ==================================================================================================================
    # Simplified Birthday Problem  is throwing multiple dice e.g. 3 and seeing if any two dice land on same number
    # using the dice should give you an intuition of why you need permutations not combinations as we are dealing with
    # individual dice, therefore throwing (1,1,6) and (6,1,1) need to be counted separately in the possibility space

    a = 1, 2, 3, 4, 5, 6
    b = 1, 2, 3, 4, 5, 6
    c = 1, 2, 3, 4, 5, 6
    values = [(i, j, k) for i in a for j in b for k in c]  # All permutations of 3 dice
    # alternatively
    # values = product((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6))
    total = len(values)  # 216 = 6 ** 3
    count_same = 0
    count_diff = 0
    for i,j,k in values:
        if i == j or j == k or i == k:
            count_same +=1
        if i != j and j != k and i != k :
            count_diff +=1
    print('P(2 or 3 same):', count_same/total)
    print('P(All Different):', count_diff/total, perms(6, 3)/6**3)

    total = 6 ** 3                     # 216 permutations
    _3_diff = 6 * 5 * 4                # 120 permutations = perms(6, 3)
    _2_same = combs(3, 2) * 6 * 1 * 5  # 90 permutations
    # Calculation for _2_same ...
    # choose two dice of the three to be the same combs(3, 2) = 3 ways
    # choose the number to be the same in  6 ways, 2nd digit in 1 way  and the last number in 5 ways = 6*1*5
    _3_same = perms(6, 1)              # 6 permutations (1,1,1), ... , (6,6,6)



    # Consider b'day problem with 4 dice
    total = 6 ** 4  # permutations of 4 dice        # 1296
    _4_diff = 6 * 5 * 4 * 3   # = perms(6,4)        # 360
    _2_same_2_diff = combs(4, 2) * 6 * 1 * 5 * 4    # 720
    _2_same_2_same = combs(4, 2) * 6 * 1 * 5 * 1    # 90
    _3_same_1_diff = combs(4, 3) * 6 * 1 * 1 * 5    # 120
    _4_same_0_diff = combs(4, 4) * 6 * 1 * 1 * 1    # 6



    #  Consider b'day problem with 5 dice
    total = 6 ** 5  # permutations of 5 dice
    _6_diff = 6 * 5 * 4 * 3 * 2 # = perms(6,5)
    _2_same_3_diff = combs(5, 2) * 6 * 1 * 5 * 4 * 3  # choose 2 same in combs(5,2) ways x 6 ways to chose its value,  last 3 dice in 5 * 4 * 3 ways
    _3_same_2_diff = combs(5, 3) * 6 * 1 * 1 * 5 * 4  # choose 3 dice in combs(5,3) ways x 6 ways to chose its value,  last 2 dice in 5 * 4 ways
    _4_same_1_diff = combs(5, 4) * 6 * 1 * 1 * 1 * 5
    _5_same = perms(6, 1)

    # ==================================================================================================================
    # The Birthday Problem
    # ==================================================================================================================
    # P(at least 2 out of 23 sharing a birthday) = 0.507
    # Note: use perms since each individual is assigned a birthday like the die
    print(1 - factorial(365) / (factorial(365 - 23) * (365 ** 23)))  # = 0.507
    print(1 - perms(365, 23) / perms_with_replacement(365, 23))      # = 0.507 

    # Now consider 23 dice with 365 sides
    total = 365 ** 23  # Total Permutations of 23 dice

    _23_diff = perms(365, 23)
    _2_same_21_diff = combs(23, 2)  * 365 * perms(364, 21)
    _3_same_20_diff = combs(23, 3)  * 365 * perms(364, 20)
    _21_same_2_diff = combs(23, 21) * 365 * perms(364, 2)
    _22_same_1_diff = combs(23, 22) * 365 * perms(364, 1)
    _23_same = perms(365, 1)


    # ==================================================================================================================
    # The 1000 poisoned bottles problem - simplify with 4 bottles and two prisoners,  8 bottles and three prisoners
    # ==================================================================================================================
    # https://medium.com/mathadam/the-poisoned-wine-bottle-puzzle-5d45da075453
    # ==================================================================================================================
    # With 10 prisoners you can discern the poison in 1024 bottles = 2 ** 10
    # Consider any 10 digit binary number 1=prisoner dies, 0=prisoner lives
    # e.g. b'0000000000' => no prisoner dies  (don't give any prisoners the bottle labeled 0000000000)
    # e.g. b'0000000001' => prisoner #1 dies        (only give prisoner one bottle labeled 0000000001)
    # e.g. b'1111111111' => all prisoner dies       (give all prisoners the bottle labeled 1111111111)
    for i in range(1024):
        bottle_label = bin(i)

    # combs(10,10) = 1  bottle is given to all 10   => if all prisoners die you know it was that bottle
    # combs(10,9)  = 10 bottles given to 9 prisoners => if that combination of 9 prisoners die you know it was that bottle
    # combs(10,8)  = 45 bottles given to 8 prisoners
    # ...
    # combs(10,0) = 1 bottle is given to 0 prisoners
    max_bottles = 0
    for i in range(11):
        max_bottles += combs(10, i)  # = 1024 bottles can be tested

    # CONSIDER 3 Prisoners 1,2,3  8 bottles (A,B,C,D,E,F,G,H)

    # A|A|A  => All drink bottle  'A'
        # Total = combs(3,3) = 1
    # B|B|X  => Two drink bottle  'B'
    # C|X|C  => Two drink bottle  'C'
    # X|D|D  => Two drink bottle  'D'
        # Total = combs(3,2) = 3
    # E|X|X  => One drink bottle  'E'
    # X|F|X  => One drink bottle  'F'
    # X|X|G  => One drink bottle  'G'
        # Total = combs(3,1) = 3
    # X|X|X  => None drink bottle 'H'
        # Total = combs(3,0) = 1


    # ==================================================================================================================

    # =========================
    # Monty Hall Problem
    # =========================
    from random import shuffle, choice


    def monty_hall_trial(initial_door_number, should_switch):
        shuffle(awards)
        doors = dict(zip(door_numbers, awards))
        remaining_door_numbers = [x for x in door_numbers if x != initial_door_number]
        for door_number in remaining_door_numbers:
            if doors[door_number] == unwanted_award:
                remaining_door_numbers.remove(door_number)
                break

        switched_door_number = remaining_door_numbers[0]
        final_door_number = switched_door_number if should_switch else initial_door_number
        won_car = doors[final_door_number] == wanted_award
        return won_car


    def simulate_monty_hall(trial_number, should_switch):
        winning_counts = 0
        for trial_i in range(trial_number):
            initial_pick = choice(door_numbers)
            won_car = monty_hall_trial(initial_pick, should_switch)
            winning_counts += int(won_car)
        winning_prob = winning_counts / trial_number
        print(f"Trial Times: {trial_number} times\n"
              f"Switching: {should_switch}\n"
              f"Probability: {winning_prob:.2%}")


    door_numbers = [1, 2, 3]
    wanted_award = "car"
    unwanted_award = "goat"
    awards = [wanted_award, unwanted_award, unwanted_award]

    simulate_monty_hall(10000, True)
    # Trial Times: 10000 times
    # Switching: True
    # Probability: 66.05%

    simulate_monty_hall(10000, False)
    # Trial Times: 10000 times
    # Switching: False
    # Probability: 33.54%


    # ===============================================================================================================
    # Coins Analysis.  P(two Tails together, 4 coin toss) = 12/24
    # 3 positions for starter Tail Coin x 2! arrangements of heads x 2! arrangements for tails / 4! arrangements
    # ===============================================================================================================
    x = list(permutations(['T1', 'T2', 'H1', 'H2']))
    print(len(x))
    for i in x: 
        print(i)
    p = 3 * factorial(2) * factorial(2) / factorial(4)
    # ('T1', 'T2', 'H1', 'H2')
    # ('T1', 'T2', 'H2', 'H1')
    # ('T1', 'H1', 'T2', 'H2')
    # ('T1', 'H1', 'H2', 'T2')
    # ('T1', 'H2', 'T2', 'H1')
    # ('T1', 'H2', 'H1', 'T2')
    # ('T2', 'T1', 'H1', 'H2')
    # ('T2', 'T1', 'H2', 'H1')
    # ('T2', 'H1', 'T1', 'H2')
    # ('T2', 'H1', 'H2', 'T1')
    # ('T2', 'H2', 'T1', 'H1')
    # ('T2', 'H2', 'H1', 'T1')
    # ('H1', 'T1', 'T2', 'H2')
    # ('H1', 'T1', 'H2', 'T2')
    # ('H1', 'T2', 'T1', 'H2')
    # ('H1', 'T2', 'H2', 'T1')
    # ('H1', 'H2', 'T1', 'T2')
    # ('H1', 'H2', 'T2', 'T1')
    # ('H2', 'T1', 'T2', 'H1')
    # ('H2', 'T1', 'H1', 'T2')
    # ('H2', 'T2', 'T1', 'H1')
    # ('H2', 'T2', 'H1', 'T1')
    # ('H2', 'H1', 'T1', 'T2')
    # ('H2', 'H1', 'T2', 'T1')


    # ===============================================================================================================
    # Coins Analysis.  P(3 Tails together, 6 coin toss) = 12/24
    # 4 positions for starter Tail Coin x 3! arrangements of heads x 3! arrangements for tails / 6! arrangements
    # Assume 50% of coins land tails (accurate for large numbers)
    # ===============================================================================================================    

    # NOT CORRECT see https://www.youtube.com/watch?v=TX-wicOIjGA&ab_channel=LearnwithSreyas
    def coins_analysis(number_of_coins, tails_together):
        if number_of_coins % 2 != 0:
            print('Require even number of tosses')
            return
        number_of_tails = number_of_coins / 2
        starter_postitions = number_of_coins + 1 - tails_together
        return starter_postitions * perms(number_of_tails, tails_together) * factorial(number_of_coins - tails_together) / factorial(number_of_coins)


    x = list(permutations(['T', 'T', 'T', 'H', 'H', 'H']))
    total = len(x)
    success = 0
    for i in x: 
        if i in (('T', 'T', 'T', 'H', 'H', 'H'), 
                 ('H', 'T', 'T', 'T', 'H', 'H'), 
                 ('H', 'H', 'T', 'T', 'T', 'H'), 
                 ('H', 'H', 'H', 'T', 'T', 'T')):
            success += 1

    print(success/total)     # = 20% 
    print(coins_analysis(6, 3))    # = 20%

    print(coins_analysis(10, 3))   # = 66.7%
    print(coins_analysis(100, 5))

# ==================================================================================================================
# Sample Space Vs Event Space
# e.g. two coins tossed. sample space has 4 elements.
# Event space is a union of all possible events = 4C0 + 4C1 + 4C2 + 4C3 + 4C4 = 16 subsets of the sample space
# e.g the event that at least one of the coins is a tail is {('T', 'T'), ('T', 'H'), ('H', 'T')} - this is one of the 16 subsets of the event space
# ==================================================================================================================
sample_space = set(product(('H', 'T'), ('H', 'T')))  #  {('T', 'T'), ('H', 'H'), ('T', 'H'), ('H', 'T')}
event_space_0= set(combinations(sample_space, 0))    #  {()}
event_space_1 = set(combinations(sample_space, 1))   #  {(('T', 'H'),), (('H', 'H'),), (('T', 'T'),), (('H', 'T'),)}
event_space_2 = set(combinations(sample_space, 2))   #  {(('T', 'T'), ('H', 'H')), (('H', 'H'), ('T', 'H')), (('H', 'H'), ('H', 'T')), (('T', 'H'), ('H', 'T')), (('T', 'T'), ('H', 'T')), (('T', 'T'), ('T', 'H'))}
event_space_3 = set(combinations(sample_space, 3))   #  {(('T', 'T'), ('H', 'H'), ('H', 'T')), (('H', 'H'), ('T', 'H'), ('H', 'T')), (('T', 'T'), ('T', 'H'), ('H', 'T')), (('T', 'T'), ('H', 'H'), ('T', 'H'))}
event_space_4 = set(combinations(sample_space, 4))   #  {(('T', 'T'), ('H', 'H'), ('T', 'H'), ('H', 'T'))}
event_space = event_space_0 | event_space_1 | event_space_2 | event_space_3 | event_space_4  # Take Union of event spaces
assert len(event_space) == 16
