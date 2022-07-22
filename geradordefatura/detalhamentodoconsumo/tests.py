from django.test import TestCase
from setor_eletrico_api import TarifasSetorElétrico
import json

tarifas = TarifasSetorElétrico('Edp ES')

print( tarifas.getTarifaTE(), tarifas.getTarifaTUSD())
