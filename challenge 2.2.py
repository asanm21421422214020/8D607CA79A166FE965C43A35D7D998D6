#Define the base class Player
class Player:

  def Play(self):
    print("the player is playing cricket.")


#Define the derived class Batsman
class Batsman(Player):

  def Play(self):
    print("the batsman is batting.")


#Define the derived class Bowler
class Bowler(Player):

  def Play(self):
    print("the bowler is bowling.")


#Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play() method for each object
batsman.Play()
bowler.Play()
