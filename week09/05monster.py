import numpy as np
X = np.random.RandomState(1)
class prince:
  def __init__(self,hp):
    self.hp=hp
    self.i=0
  def heal(self):
    self.hp+=20
    self.i=0
    return self.hp
  def attack(self,opponent):
    opponent.hp-=10+self.i*2
    self.i+=1
    if opponent.hp>=0:
      return opponent.hp
    else:
      return 0

class monster:
  def __init__(self,hp):
    self.hp=hp
  def attack(self,opponent,atk):
    opponent.hp-=atk
    if opponent.hp>=0: 
      return opponent.hp
    else:
      return 0

hp=int(input('Blood Start: '))
#hp=50
you=prince(hp)
plapud=monster(hp)
while hp!=0:
  choice=input('Attack(a) or Heal(h): ')
  if choice=='a':
    monsterhp=you.attack(plapud)
    print(f"Monster\'s HP left {monsterhp}")
    if monsterhp<=0:
      print("You win.(^_^)")
      break
  elif choice=='h':
    heal=you.heal()
    print(f'Your HP left {heal}')
  atk=X.randint(1,40)
  #print(atk)
  yourhp=plapud.attack(you,atk)
  if yourhp<=0:
    print(f'Monster\'s turn : Your HP left 0')
    print("You lose and die.(T_T)")
    break
  else:
    print(f'Monster\'s turn : Your HP left {yourhp}')
  
  