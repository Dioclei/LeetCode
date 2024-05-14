# medium

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        # simulate backward motion
        # what's in the deck doesn't actually matter

        new_deck = []

        # sort original deck
        sorted_deck = sorted(deck)

        # un-reveal last card
        new_deck.insert(0, sorted_deck[-1])

        # starting from second last card, simulate in reverse
        for i in range(len(deck) - 2, -1, -1):
            # put card from bottom of deck on top
            new_deck.insert(0, new_deck.pop(-1))
            # un-reveal card
            new_deck.insert(0, sorted_deck[i])

        return new_deck
        
    
def test():
    s = Solution()
    a = s.deckRevealedIncreasing([4, 5, 6, 7])
    print(a)

test()