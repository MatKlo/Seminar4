#!/usr/bin/env python3

from kostka import Kostka 
from lod import Lod 

class Sektor:
    """
    Správa souboje dvou lodí
    """

    def __init__(self, lod_1, lod_2, kostka, jmeno="bez nazvu",):
        self._jmeno = jmeno
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])
        
    def _vypis_lod(self, lod):
        print(lod)
        print(f'Trup: {lod._trup}')

    def _vykresli(self):
        self._vycisti()
        print(f'================ Sektor {self._jmeno} ================\n')
        print('Lodě:\n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()


    def souboj(self):
        print(f"Vitej v sektoru {self._jmeno}!")
        print("======================")
        print()
        print(f"Dnes se utkaji lode:")
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print("Zahajit souboj...")
        input()

        import random
        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykresli()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())

            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykresli()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())


    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(0.8)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Queen Marry", 100, 80, 50, k)
    clun = Lod("Gumotex", 140, 20, 30, k)
    l = Lod("Yachta", kostka=k, trup=80, utok=60, stit=70)
    
    orion = Sektor(lodicka, clun, k, "Orion")
    gamma = Sektor(lodicka, l, k, "Gamma")

    orion.souboj()
    gamma.souboj()
