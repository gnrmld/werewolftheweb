class Roles(object):

    def Villager(self):
        '''Belongs to the protagonists.
        Does nothing.
        No turns'''
        pass

    def Tanner(self):
        '''Does not belong to any team
        Hates himself/herself, won if he/she dies.
        No turns'''
        pass

    def Hunter(self, is_killed=False):
        '''Belongs to the protagonists.
        If he dies, he can kill whoever 
        he suspects as the werewolf.
        No turns''' 
        pass

    def Doppelganger(self):
        '''Belongs to the team the card he/she picked.
        Copies the role of his picked card.
        1st turn'''
        pass

    def Werewolves(self):
        '''Belongs to the antagonists.
        Opens their eyes to know who's the other werewolf,
        If he's alone, look at one card at the center.
        2nd turn'''
        pass

    def Minion(self):
        '''Belongs to the antagonists.
        They know who the werewolves are, but the werewolves
        has no idea, won if he dies and not the werewolves.
        3rd turn'''
        pass

    def Mason(self):
        '''Belongs to the protagonists.
        They know who the other Mason is.
        4th turn'''
        pass

    def Seer(self):
        '''Belongs to the protagonists.
        Looks at one other player's card or 2 center cards.
        5th turn'''
        pass

    def Robber(self):
        '''Belongs to the team the card he/she picked.
        Swaps card with another player,  and looks at it.
        6th turn'''
        pass

    def Troublemaker(self):
        '''Belongs to the protagonists.
        Swaps two players' card without knowing it.
        7th turn'''
        pass

    def Drunk(self):
        '''Belongs to the team the card he/she picked.
        Exchanges own card at the center,
        does not know what card he/she chose.
        8th turn'''
        pass

    def Insomniac(self):
        '''Belongs to the protagonists.
        Look at their card before the night ends.
        9th turn'''
        pass