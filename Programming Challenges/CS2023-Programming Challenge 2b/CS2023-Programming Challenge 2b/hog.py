"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll dice equal to num_rolls
    
    
    $ python3 -i hog.py
    >>> roll_dice(1,make_test_dice(4, 2, 1, 3))
    4
    >>> roll_dice(2,make_test_dice(4, 2, 1, 3))
    6
    >>> roll_dice(3,make_test_dice(4, 2, 1, 3))
    1
    >>> roll_dice(4,make_test_dice(4, 2, 1, 3))
    1
    """
    
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    
    # BEGIN Question 1
    scored_points = 0
    roll = 0
    pigout = False
    for i in range(num_rolls):
        roll = dice()
        if(roll == 1): #If pig out. Have to do this to roll both dice if there are two.
            pigout = True
        scored_points += roll
    if(pigout):
        return 1
    return scored_points
            
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    
    $ python3 -i hog.py
    >>> take_turn(2, 0, make_test_dice(4, 6, 1))
    10
    >>> take_turn(3, 0, make_test_dice(4, 6, 1))
    1
    >>> take_turn(0, 35)
    6
    >>> take_turn(0, 71)
    8
    >>> take_turn(0, 7)
    8
    >>> take_turn(0, 0)
    1
    >>> take_turn(0, 9)
    10
    >>> take_turn(2, 0, make_test_dice(6))
    12
    >>> take_turn(0, 50)
    6
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    points_scored = 0
    #Free Bacon
    if(num_rolls == 0):
        points_scored = max([int(i) for i in str(opponent_score)])+1 # Searches through the string of opponents score, then turns the digit into an integer.
                                                   # Throws all values into the max function to find the maximum. Adds 1 per the rules of Free Bacon
    else:
        points_scored = roll_dice(num_rolls, dice)
    return points_scored
        
    
    # END Question 2

def select_dice(score, opponent_score, four_sided, six_sided):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    
    $ python3 -i hog.py
    >>> select_dice(4, 24, four_sided, six_sided) == six_sided
    True
    >>> select_dice(16, 64, four_sided, six_sided) == four_sided
    False
    >>> select_dice(0, 0, four_sided, six_sided) == four_sided
    True
    >>> select_dice(50, 80, four_sided, six_sided) == four_sided
    False
    """
    # BEGIN Question 3
    if(score % 7 == 0 and opponent_score % 7 == 0):
        return four_sided
    else:
        return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    
    $ python3 -i hog.py
    >>> is_swap(19, 91)
    True
    >>> is_swap(20, 40)
    False
    >>> is_swap(41, 14)
    True
    >>> is_swap(23, 42)
    False
    >>> is_swap(55, 55)
    True
    >>> is_swap(114, 41) # We check the last two digits
    True
    """
    # BEGIN Question 4
    score0_last2 = score0 % 100 # Only want to compare tens place and ones place. This gets rid of anything past those.
    score1_last2 = score1 % 100
    score0_swapped = ((score0_last2 % 10) * 10) + score0_last2 // 10
    if(score0_swapped == score1_last2 or score0_last2 == score1_last2):
        return True
    else:
        return False
    
        
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, four_sided, six_sided, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1

    $ python3 -i hog.py
    >>> four_sided = make_test_dice(1)
    >>> six_sided = make_test_dice(3)
    >>> always = always_roll
    >>> s0,s1 = play(always(5), always(3), four_sided, six_sided, score0=91, score1=10)
    >>> s0, s1
    (106, 10)

    >>> s0,s1 = play(always(5), always(5), four_sided, six_sided, goal=10)
    >>> s0, s1
    (1, 15)

    >>> s0,s1 = play(always(5), always(3), four_sided, six_sided, score0=36, score1=15, goal=50)
    >>> s0, s1
    (15, 51)

    >>> # Swine swap applies to 3 digit scores
    >>> s0,s1 = play(always(5), always(3), four_sided, six_sided, score0=98, score1=31)
    >>> s0,s1
    (31, 113)

    >>> # Goal edge case
    >>> s0,s1 = play(always(4), always(3), four_sided, six_sided, score0=88, score1=20)
    >>> s0, s1
    (100, 20)
    
    >>> import random
    >>> four_sided = lambda: random.randrange(1, 5)
    >>> six_sided = lambda: random.randrange(1, 7)
    >>> random_strat = lambda a, b: (random.randrange(11) + b) % 10
    >>> random.seed(4321)
    >>> for _ in range(100):
    ...    s0, s1 = play(random_strat,random_strat, four_sided, six_sided)
        
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while(score0 < goal and score1 < goal):
        if(who == 0):
            score0 += take_turn(strategy0(score0, score1), score1, select_dice(score0, score1, four_sided, six_sided))
        else:
            score1 += take_turn(strategy1(score1, score0), score0, select_dice(score1, score0, four_sided, six_sided))
        if(is_swap(score0, score1)):
                temp = score0
                score0 = score1
                score1 = temp
        who = other(who)
    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)