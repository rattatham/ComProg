mancity = input("What's the result of Manchester city's match? ")
liverpool = input("What's the result of Liverpool's match? ")
if mancity=='won' and liverpool=='lost':
  print("Manchester city is the champion of Premier League.")
elif mancity=='lost' and liverpool=='won':
  print("Liverpool is the champion of Premier League.")
elif mancity=='won' and liverpool=='won':
  margincity = int(input("What is the margin that Manchester city won by? "))
  marginliver = int(input("What is the margin that Liverpool won by? "))
  if margincity > marginliver:
    print("Manchester city is the champion of Premier League.")
  elif marginliver>margincity:
    print("Liverpool is the champion of Premier League.")
  elif marginliver==margincity:
    winner = input("Which team won the play-off match?(Manchester city/Liverpool) ")
    if winner == 'Manchester city':
      print("Manchester city is the champion of Premier League.")
    elif winner == 'Liverpool':
      print("Liverpool is the champion of Premier League.")