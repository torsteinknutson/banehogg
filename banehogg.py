#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random # for å gjøre det til et spill. 
import math 
import time # for å sette en random delay så de blir mer spennende å se på matchen. 


class Viking_skaper:
    def __init__(self, navn='', sverd=0, skjold=0, helse=0):
        self.navn = navn
        self.sverd = sverd
        self.skjold = skjold
        self.helse = helse
    
    def angrep(self):
        angrep_mengde = self.sverd * (random.uniform(1.5, 1.9)) #måtte endre fra random.random til uniform som trenger 2 attributter, lekte litt rundt og fant at dette ga aldri negativt skadepåføring noe mange andre gjorde. Vet ikke hvorfor. 
        return angrep_mengde
    
    def forsvar(self):
        skjold_mengde = self.skjold * (random.uniform(1.5, 1.9))
        return skjold_mengde
    

class Kamp:
    def start_kamp(self, viking1, viking2):
        while True:
            if self.angrep_resultat(viking1, viking2) == "Game Over":
                break
            if self.angrep_resultat(viking2, viking1) == "Game Over":
                break
                
    def angrep_resultat(self, vikingA, vikingB):
        viking1_angreps_mengde = vikingA.angrep()
        viking2_forsvars_mengde = vikingB.forsvar()
        skade_paa_vikingB = math.ceil(viking1_angreps_mengde - viking2_forsvars_mengde)
        vikingB.helse = vikingB.helse - skade_paa_vikingB
        print('{} angriper {} og påfører han {} i skade.'.format(vikingA.navn, vikingB.navn, skade_paa_vikingB))
        print('{} har nå {} i helse.'.format(vikingB.navn, vikingB.helse))
        time.sleep(random.uniform(0.4, 3))
        
        if vikingB.helse <= 0:
            print('{} har dødd og {} er den seirende og overlegne viking.'.format(vikingB.navn, vikingA.navn))
            return 'Game Over'
        else:
            return 'slåss igjen' #denne har ikke noe å si
        

def banehogg(): #vanligvis heter denne main, men det er kulere med banehogg på kvantin. 
    ragnar = Viking_skaper('Ragnar', 40, 20, 100) #skaper en viking med Class Viking_skaper og gir den attributtene, og lagrer den i funksjonen. Ragnar er ikke tilgjengelig utenfor denne funksjonen. 
    erik = Viking_skaper('Erik Den Røde', 43, 22, 100)
    kamp = Kamp()
    kamp.start_kamp(ragnar, erik)

