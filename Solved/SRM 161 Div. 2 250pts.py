class CardCount(object):
    def dealHands(self, numPlayers, deck):
        revdeck = list(deck)
        revdeck.reverse()

        hands = ["" for x in range(numPlayers)]

        while len(revdeck) >= numPlayers:
            for x in range(numPlayers):
                hands[x] += revdeck.pop()
        return hands



print CardCount().dealHands(6, '012345012345012345')
# R: ("000", "111", "222", "333", "444", "555")
print CardCount().dealHands(4, '111122223333')
# R: ("123",  "123",  "123",  "123")
print CardCount().dealHands(1, '012345012345012345')
# R: ("012345012345012345")
print CardCount().dealHands(6, '01234')
# R: ("",  "",  "",  "",  "",  "")
print CardCount().dealHands(2, '')
# R: ("",  "")
