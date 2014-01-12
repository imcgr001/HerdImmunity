import random


class person:

    '''Creates a vaccinated/infected/unexposed person at a coordinate'''

    def __init__(self, coord,SCALE):
    #initializes the person to be vaccinated or not, infected or not, and coord
        
        self.coord = coord
        self.vaccinated = False
        self.infected = False
        self.contagious = False
        self.scale = SCALE
        self.turns = 0
        #duration of infection
        self.duration = int(random.gauss(4,.5)*SCALE)
        


    def set_vaccinated(self):
    #vaccinates this person
        if not self.infected:
            self.vaccinated = True
        
    def is_vaccinated(self):
    #returns True if vaccinated, False if not
        return self.vaccinated

    def turn(self, xy, d,s):
    #move one square randomly & counts turns infected

        #CHECK THAT MOVE WORKS!!!!!!!!!!!!!!!!!!!!!!!!!
        m = self.coord[xy] + d
        if m >= 0 and m <= s:
            self.coord[xy] = m

        #Count duration of infection and change it to vaccinated if
        #above the duration
        if self.infected and self.turns < self.duration:
            self.turns = self.get_turns() + 1

            #set to contagious after certain # of turns
            if not self.contagious and self.turns >= self.scale:
                self.contagious = True
        # immune after turns passes duration
        elif self.infected and self.turns >= self.duration:
            self.infected = False
            self.vaccinated = True
            self.contagious = False
            
    def get_coord(self):
    #return coordinates    
        return self.coord
    
    def set_infected(self,turns):
    #infect person
        if not self.vaccinated:
            self.infected = True
            self.turns = turns
            if turns > 0:
                self.contagious = True

    def is_infected(self):
    #return True if infected, False if not
        return self.infected
    
    def is_contagious(self):
    #return True if infected and contagious, False otherwise
        return self.contagious

    def get_turns(self):
    #return # of turns
        return self.turns
