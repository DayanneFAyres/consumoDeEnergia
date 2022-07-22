import requests
from datetime import datetime

class TarifasSetorElétrico:

    def __init__(self, concessionaria):
        concessionaria = concessionaria.upper()

        # fazendo apenas para EDP ES inicialmente
        if(concessionaria == 'EDP ES'):

            self.concessionaria = concessionaria.replace(' ', '+')
            # o ano vigente dos valores das tarifas corresponde ao ano anterior
            self.ano = datetime.now().year - 1
            self.__dados_consumidor = self.__consultaTarifas()

        else:
            raise ValueError("Concessionária não cadastrada no sistema.")

    def __consultaTarifas(self):

        url = 'https://apise.way2.com.br/v1/tarifas?agente={}&ano={}&apikey=9eba68dd3d2444e4b0c7e13e17ee2139'.format(self.concessionaria, self.ano)

        req = requests.get(url)

        #retorna uma lista de dicionarios
        dados_json = req.json()

        consumidor_residencial = {}

        for consumidor in dados_json:
            if(consumidor.get('modalidade') == 'CONVENCIONAL' and consumidor.get('subclasse') == 'RESIDENCIAL'):
                consumidor_residencial = consumidor

        return consumidor_residencial

    def getTarifaTUSD(self):

        return self.__dados_consumidor.get('tarifaconsumotusd')

    def getTarifaTE(self):

        return self.__dados_consumidor.get('tarifaconsumote')



