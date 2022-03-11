import random
dealer_cards = []
player_cards = []

while len(dealer_cards) != 2:
   dealer_cards.append(random.randint(1,11))
   if len(dealer_cards) == 2:
      print('Dealer has X & ', dealer_cards[0])

while len(player_cards) != 2:
   player_cards.append(random.randint(1,11))
   if len(player_cards) == 2:
      print('You have X & ', player_cards)

if sum(dealer_cards) == 21:
   print('Dealer has 21 and wins')
elif sum(dealer_cards) > 21:
   print('Dealer busted')

while sum(player_cards) < 21:
   action_taken = str(input("do you want you hit or stay? H or S"))
   if action_taken == 'h':
      player_cards.append(random.randint(1,11))
      print('You have a total of ' + str(sum(player_cards)) + ' from these cards ', player_cards)
   elif action_taken == 's':
      print('The dealer has a total of ' + str(sum(dealer_cards)) + " with ", dealer_cards)
      print('You have a total of ' + str(sum(player_cards)) + ' with ', player_cards)
      if sum(dealer_cards) > sum(player_cards):
        print('Dealer wins!')
      else:
         print('You win!')
         break

if sum(player_cards) > 21:
   print('You busted! dealer wins')
elif sum(player_cards = 21):
   print('You have 21, you win!')
