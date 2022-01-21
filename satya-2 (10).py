import random
class Die:
    """creating class die with one attribute and two methods""" 
    def __init__(self):
        self.roll()
    def  roll(self):
        self._value=random.randint(1,6)
    def get_value(self):
        return self._value
class DiceCup:
    """creating class dicecup where it handles methods value(), bank(), is_banked(), release(), release_all(), roll()""" 
    def __init__(self,var):
        self._dices=[]
        self._ban=[False,False,False,False,False]
        for i in range(5):
            self._dices.append(Die())
        for i in range(var):
            self._dices.append(Die())
    def roll(self):
        for i in range(0,5):
            if self._ban[i]==False:
                self._dices[i].roll()
    def value(self,index):
        return self._dices[index].get_value()
    def bank(self,index):
        self._ban[index]=True
    def is_banked(self,index):
        if self._ban[index]==True:
            return True
        else:
            return False
    def release(self,index):
        self._ban[index]==False
    def release_all(self):
        self._ban=[False,False,False,False,False]

class PlayerRoom:
    """class player room which handles scores of players"""
    def __init__(self):
        self._players=[]
    def set_game(self,a1):
        self._game=a1
    def add_player(self,a2):
        self._players.append(a2)
    def reset_scores(self):
        for i in range(len(self._players)):
            self._players[i].reset_score()
    def play_round(self):
        for i in self._players:
            i.play_round(self._game)
            if self.game_finished():
                break
            else:
                pass
    def game_finished(self):
        empty=[]
        x=0
        while x<len(self._players):
            if self._players[x].current_score()>=21:
                empty.append(True)
                x=x+1
            else:
                empty.append(False)
                x=x+1
        return any(empty)
    def print_scores(self):
        for i in range(len(self._players)):
            print(self._players[i]._name ,"=", self._players[i].current_score())
    def print_winner(self):
        for i in range(len(self._players)):
            if self._players[i].current_score()>=21:
                print("The winner is:",self._players[i]._name)

class ShipOfFools:
    """class ship of fools with the game logic"""
    def __init__(self):
        self.winningscore=21
        self._cup=DiceCup(5)
    def round(self):
        self._cup.release_all()
        self._cup.roll()
        has_ship = False
        has_captain = False
        has_crew = False
        # The initial cargo score i.e., score of other two dices
        crew = 0
        # three chances for each player in a round
        for rep in range(3):
            repl=[]
            i=0
            while i<5:
                repl.append(self._cup._dices[i].get_value())
                i=i+1
            print(repl)
            if not (has_ship) and (6 in repl):
                for i in range(5):
                    if repl[i]==6:
                        self._cup.bank(i)
                        break
                has_ship = True
            else:
                if has_ship:
                    pass
                else:
                    self._cup.roll()
            if (has_ship) and not (has_captain) and (5 in repl):
            # A ship is banked and not the captain 
                for i in range(5):
                    if repl[i]==5:
                        self._cup.bank(i)
                        break
                has_captain = True
            else:
                if has_captain:
                    pass
                else:
                    self._cup.roll()
            if has_captain and not has_crew and (4 in repl):
            # A captain is banked
                for i in range(5):
                    if repl[i]==4:
                        self._cup.bank(i)
                        break
                has_crew = True
            else:
                if has_crew:
                    pass
                else:
                    self._cup.roll()
            if has_ship and has_captain and has_crew:
            # bank the other dice if you like to save.
                if rep<2:
                        for i in range(5):
                            if self._cup._dices[i].get_value()>3:
                                self._cup.bank(i)
                            else:
                                self._cup.roll()
                elif rep==2:
                    for i in range(5):
                        if self._cup.is_banked(i):
                            pass
                        else:
                            self._cup.bank(i)
            # calculate score.
        if has_ship and has_captain and has_crew:
            crew = sum(repl) - 15
            print("crew:",crew)
            return crew
        else:
            print("crew:",crew)
            return crew
class Player:
    """class player with player information"""
    def __init__(self,name_of_player):
        self._name=self.set_name(name_of_player)
        self._score=0
    def set_name(self,name_string):
        return name_string
    def current_score(self):
        return self._score
    def reset_score(self):
        self._score=0
    def play_round(self, game_round):
        new_round=game_round
        self._score=self._score + new_round.round()

if __name__ == "__main__":
    room = PlayerRoom()
    room.set_game(ShipOfFools())
    room.add_player(Player('sri'))
    room.add_player(Player('vamsi'))
    room.reset_scores()
    print("banking ship, captain and crew")
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()      
