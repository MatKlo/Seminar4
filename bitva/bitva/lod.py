#!/usr/bin/env python3

'''
Lod a odvozene tridy pro souboj.
'''

class Lod:
    '''
    Zakladni trida reprezentujici lod.
    '''

    def __init__(self, jmeno, trup, utok, stit, kostka):
        self._jmeno = jmeno
        self._trup = trup
        self._max_trup = trup
        self._utok = utok
        self._stit = stit
        self._kostka = kostka
        self._zprava = ''
    
    def __str__(self):
        return str(self._jmeno)
    
    def je_operacni(self):
        return self._trup > 0
        
    def graficky_trup(self):
        celkem = 20
        pocet  = int(self._trup / self._max_trup * celkem)
        if pocet == 0 and self.je_operacni():
            pocet = 1
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f'{self._jmeno} pali kanony za {uder} hp.'
        self.nastav_zpravu(zprava)
        souper.bran_se(uder)

    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod())
        if poskozeni > 0:
            zprava = f'{self._jmeno} utrpela zasah o sile {poskozeni} hp.'
            self._trup -= poskozeni
            if self._trup < 0:
                self._trup = 0
                zprava = f'{zprava[:-1]} a byla znicena.'
        else:
            zprava = f'{self._jmeno} odrazil utok stity.'
        self.nastav_zpravu(zprava)

    def nastav_zpravu(self, zprava):
        self._zprava = zprava
    
    def vypis_zpravu(self):
        return self._zprava

class Korveta(Lod):
    
    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod() + 2)
        if poskozeni > 0:
            zprava = f'{self._jmeno} utrpela zasah o sile {poskozeni} hp - superstit.'
            self._trup -= poskozeni
            if self._trup < 0:
                self._trup = 0        
        else:
            zprava = f'{self._jmeno} odrazil utok stity.'
        self.nastav_zpravu(zprava)

