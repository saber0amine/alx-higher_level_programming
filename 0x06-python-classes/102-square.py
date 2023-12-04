#!/usr/bin/python3
class Robot:
    pas=1

    def __init__(self, nom, position={"x":0,"y":0},direction="Est"):
        self.nom=nom
        self.__position=position
        self.direction=direction
    @property
    def position(self):
        return self. __position
    @position.setter
    def position(self, position):
        self. __position = position
    
    @property
    def direction(self):
        return self.direction
    @direction.setter
    def direction(self, direction):
        self.__direction = direction
    def avance(self):
        if (self.direction=="Est"):
            self.position["x"]+=Robot.pas
        elif (self.direction=="Ouest"):
            self.position["x"]-=Robot.pas
        elif (self.direction=="Nord"):
            self.position["y"]+=Robot.pas
        elif (self.direction=="Ouest"):
            self.position["y"]-=Robot.pas
    def droite(self):
        if (self.direction=="Est"):
            self.direction="Sud"
        elif (self.direction=="Sud"):
            self.direction="Ouest"
        elif (self.direction=="Ouest"):
            self.direction="Nord"
        elif (self.direction=="Nord"):
            self.direction="Est"
    def __str__(self):
        return ("Nom:"+self.nom+ " Position:"+ str(self.position)+
                " Direction :"+ self.direction)
class RobotNG(Robot):
    def __init__(self, nom, position={"x":0,"y":0},direction="Est", turbo=False):
        super().__init__(nom,position,direction)
        self.turbo=turbo
    def avance(self, nombrePas):
        if (self.turbo):
            if (self.direction=="Est"):
                self.position["x"] += 3*nombrePas
            elif (self.direction=="Ouest"):
                self.position["x"] -= 3*nombrePas
            elif (self.direction=="Nord"):
                self.position["y"] += 3*nombrePas
            elif (self.direction=="Ouest"):
                self.position["y"] -= 3*nombrePas
        else:
            if (self.direction=="Est"):
                self.position["x"] += nombrePas
            elif (self.direction=="Ouest"):
                self.position["x"] -= nombrePas
            elif (self.direction=="Nord"):
                self.position["y"] += nombrePas
            elif (self.direction=="Ouest"):
                self.position["y"] -= nombrePas
    def gauche(self):
        if (self.direction=="Est"):
            self.direction="Nord"
        elif (self.direction=="Nord"):
            self.direction = "Ouest"
        elif (self.direction=="Ouest"):
            self.direction = "Sud"
        elif (self.direction=="Sud"):
            self.direction="Est"
    def demiTour(self):
        if (self.direction=="Est"):
            self.direction="Ouest"
        elif (self.direction=="Nord"):
            self.direction = "Sud"
        elif (self.direction=="Ouest"):
            self.direction = "Est"
        elif (self.direction=="Sud"):
            self.direction="Nord"

    def __str__(self):
        return (super().__str__()+" Turbo:"+str(self.turbo))

R = Robot("Amine")
print(R.position()["x"])
# rng=RobotNG("ENSAB")
# rng.turbo=True
# rng.gauche()
# rng.gauche()
# rng.avance(2)
# print(rng)
