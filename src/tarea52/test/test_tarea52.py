from main.tarea52 import ADN
import pytest

exveemon = ADN("GAGCCTACTAACGGGAT")
stingmon = ADN("CATCGTAATGACGGCCT")
gatomon = ADN("GGGCCTACTAACGGGAT")
aquilamon = ADN("CTTCGTAATGACGGCCA")
angemon = ADN("TCGACTACTAACGGGAT")
ankylomon = ADN("CATCGTAATGACGGCCT")

def test_function():
    7 == exveemon-stingmon
    9 == gatomon-aquilamon
    10 == angemon-ankylomon
    