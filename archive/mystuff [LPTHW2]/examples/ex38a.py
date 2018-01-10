#exercise 6: write a script that acts like a real-life list

#example used is a partial deck of cards, want to draw until only 4 cards left

cards = "King Queen Jack Ace 10H 9C 8S 7D 3H"
deck = cards.split(' ')

print "Let's draw until there are 4 cards left.\n"

while len(deck) >=5:
    draw = deck.pop()
    print "Drawing... ", draw
    print "There are %d cards left now.\n" % len(deck)

print "Here's what's left!"
whats_left = ' '.join(deck)
print whats_left
