from hands import *

def monteCarlo()

def handStrength(private, public):
    pass

def positivePotential(private, public):
    pass

def negativePotential(private, public):
    pass

def EHS(private, public):
    hs = handStrength(private, public)
    ppot = positivePotential(private, public)
    npot = negativePotential(private, public)
    
    # Hand is ahead and stays ahead OR is behind and catches up
    return hs * (1 - npot) + (1 - hs) * ppot