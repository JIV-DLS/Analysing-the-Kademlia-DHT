# coding=utf-8

from RoutingTable import *
from Node import *
import random
from random import choice

from hashlib import sha256
from binascii import hexlify
from random import choice
from Exceptions import *

import sys

class Map():
    """
    Classe che viene utilizzata per mantenere il mapping tra l'id di un nodo 
    e un intero e per memorizzare un contatore che viene incrementato ogni volta
    che viene inserito una nuova coppia all'interno del dizionario. 
    """


    def __init__(self):
        self.mapID = {}
        self.count = 0
    
    
    def incrementCounter(self):
        """Incrementa il contatore che indica quanti mapping sono memorizzati 
        """
        self.count += 1

    def getCounter(self):
        """
        Viene restituito il numero di coppie memorizzate nel dizionario che contiene il mapping ID-intero
        
        Returns:
            Int -- Numero di coppie memorizzate nella mappa
        """
        return self.count