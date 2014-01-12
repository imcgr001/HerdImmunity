from person import person
from random import randint, random
import os

#size of space
GRIDSIZE = 500
DENSITY = 1 #persons/coordinate

#time scale turns/day
SCALE = int((3600/36)*24)

#probability a noninfected person in contact with infected will become infected
#1 corresponds to 100% .1 to 10% chance
infectivity = .1

#initial number infected
initialInfected = 50

#run #
run = 0

## of people total in simulation
size = GRIDSIZE*DENSITY



def move(li,s):
    """li is a list of persons that will be moved 1 or 0 spaces"""
    
    for k in li:

        #initialize movement to a value of -1,0, or 1
        m = randint(-1,1) 

        #move the target at a random x or y a value of m  
        k.turn(randint(0,1),m,s)

        
        
    return li
               
def collisions(li,infectivity):
    """check if collision and if necessary infects new person"""
    for i in li:
        if (not i.is_infected()) and (not i.is_vaccinated()):
            a = i.get_coord()
            #print("coord")
            for j in li:
                if a == j.get_coord() and j.is_contagious():
                    if random() <= infectivity:
                        i.set_infected(0)
                        break
                    else:
                        break


def logger(runs,i,s,v,c,infe,r):
    """log into csvfile for data analysis
    runs = number of "move" iterations
    i = number of infected
    s = number sterile
    v = number vaccinated
    infectivity = infectivity
    run = run id #
    """
      
    #fname = "infected{0}_vac{1}_tivity{2}_scale{3}.csv".format(initialInfected,
    #                                    numVaccinated,infectivity,SCALE)
    fname = "V0Scale{0}.csv".format(SCALE)
    if os.path.exists(fname):
        f = open(fname,'a')
    else:
        f = open(fname,'w+')
        f.write("runs,infected,sterile,vaccinated,contagious,infectivity,run#\n")
    
    f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(runs,i,s,v,c,infe,r))

    f.close()



def testCol(li):
    """check collisions for debugging"""
    num = 0
    for i in li:
        a = i.get_coord()
        for j in li:
            if a == j.get_coord() and j.is_infected():
                num += 1
    print("collision {}".format(num))
    
def getInf(li):
    """gets number of infected"""
    num = 0
    for i in li:
        if i.is_infected():
            num += 1
    return num

def getCont(li):
    """gets number of contagious"""
    num = 0
    for i in li:
        if i.is_contagious():
            num += 1
    return num
    
def getVac(li):
    """gets number of vaccinated"""
    num = 0
    for i in li:
        if i.is_vaccinated():
            num += 1
    return num

def runs(num,run,infectivity):

    global numVaccinated
    numVaccinated = num

    #initialize list of people and their coordinates,
    plist = [person([randint(0,GRIDSIZE),randint(0,GRIDSIZE)],SCALE) for i in range(int(size))]

    #create the initial infected
    for infected in range(initialInfected):
        #set starting number of infected
        plist[infected].set_infected(SCALE)

    #create the initial vaccinated
    for vaccinated in range(numVaccinated):
        #initialize the vaccinated persons
        plist[vaccinated+initialInfected].set_vaccinated()
        
    #set runs to 0    
    runs = 0
    inf = getInf(plist)
    v = getVac(plist)
    c = getCont(plist)
    print("infected:{}".format(inf))
    logger(runs,inf,size-(inf+v),v,c,infectivity,run)

    #run program until everyone not vaccinated is infected
    while inf !=(size-v) and not (inf == 0 and c == 0):
        #counts runs
        runs+=1
        
        #move people each turn
        plist = move(plist,GRIDSIZE)
        
        #check for collisions with infected
        collisions(plist,infectivity)
        
        inf = getInf(plist)
        #log every 100 runs
        if runs %1000 == 0:
            print(runs)
            v = getVac(plist)
            c = getCont(plist)
            print("infected:{}".format(inf))
            print("immune: {}".format(v))
            print("contagious: {}".format(c))
            logger(runs,inf,size-(inf+v),v,c,infectivity,run)


    inf = getInf(plist)
    v = getVac(plist)
    c = getCont(plist)
    print("infected:{}".format(inf))
    logger(runs,inf,size-(inf+v),v,c,infectivity,run)

if __name__ == "__main__":
    
    print ("running")
    
    #cycle through infectivity levels
    for j in range(0.1,30,5):
        infectivity = j/100
        run = 0
        #cycle through initial infected levels from 1 - 451
        for k in range(1,500,50):
            initialInfected = k
            #cycle through initial vaccinated levels form 0-460
            for l in range(0,size-initialInfected-20,20):
                run += 1
                runs(0,run,infectivity)
