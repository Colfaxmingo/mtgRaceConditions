#Determine the rank of card based on the number of turns it will take to win the game
#Base case is a 1 power, 1 toughness creature attacks each turn and is not blocked

#Players start with 20 life
opLife = 20
#Creatures reduce opposing players life by 1 each combat
creaturePower = 1
#Creatures that are dealt damage equal to or greater than its toughness die
creatureToughness = 1
#Creatures cannot attack the first turn they are in play unless they have Haste
creaureHaste = 0
#Creatures require mana to put into play
creatureCost = 1

#damage per turn is the unblocked creature power plus other effects
totalDamagePerTurn = creaturePower


#rank determined by the number of turns it takes to reduce opponents life to 0
creatureRank = opLife % totalDamagePerTurn
