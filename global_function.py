import subprocess # Limpa o console
import os # Complemento da subprocess
 
# Limpa o console
def limpar_console():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

def menu_inicial():
    texto_entrada = '''
  ***************************************
  * Digite a opção desejada para iniciar*
  * o sistema: '''
    
    print('''
  ***************************************
  * 1 - Converter Moedas                *
  * 2 - Valor das cotações atuais       *
  * 3 - Atualiza Cotação das Moedas     *
  * 4 - Versionamento                   *
  * 5 - Desligar                        *
  ***************************************
  ''')
    
    while True:        
        opcao_selecionada = m_chamaValor(texto_entrada, 1)

        if opcao_selecionada.retornoStatus():
          if opcao_selecionada.retornoValor() in [1,2,3,4]:
            return opcao_selecionada.retornoValor()
            break
          else:
            print(''' 
    ***************************************
    * Nenhuma opção foi selecionada!      *
    ***************************************

              ''')
            
 
def qual_moeda_converter():
  textoEntrada = '''
  ***************************************
  * Informe a moeda que você quer       *
  * converter: '''

  print('''
  ---------------------------------------------
  
  ''')
  lista_de_opcoes = [1, 2, 3, 4]
  contador = 1
  print('''
  ***************************************
  * 1 - Peso Argentino                  *
  * 2 - Euro                            *
  * 3 - Dolar                           *
  ***************************************
  ''')
  while contador:

    moeda = m_chamaValor(textoEntrada, 1)
    if moeda.retornoStatus():
      if moeda.retornoValor() == lista_de_opcoes[0]:
        print('''
    ***************************************
    * Moeda selecionada: Peso Argentino   *
    ***************************************
    ''')
        return 1
      elif moeda.retornoValor() == lista_de_opcoes[1]:
        print('''
    ***************************************
    * Moeda selecionada: Euro             *
    ***************************************
        ''')
        return 2
      elif moeda.retornoValor() == lista_de_opcoes[2]:
        print('''
    ***************************************
    * Moeda selecionada: Dolar            *
    ***************************************
        ''')
        return 3
      else:
        print('''
    ***************************************
    * A moeda digitada não está entre as  *
    * opções disponiveis!                 *
    ***************************************
        ''') 

def conversor(quantidade_a_converter, moeda_que_converto):
   
  if moeda_que_converto == 1:
    arquivo = open('cotacoes/peso.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print(f'''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {valor_moeda}                            *
  ***************************************
   ''')
    arquivo.close()
    quantidade_convertida = quantidade_a_converter * valor_moeda
    print(quantidade_convertida)
      
  if moeda_que_converto == 2:
    arquivo = open('cotacoes/euro.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print('''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {0}                             *
  ***************************************
    '''.format(valor_moeda))
    arquivo.close()
    quantidade_convertida = quantidade_a_converter * valor_moeda
    print(quantidade_convertida)

  if moeda_que_converto == 3:
    arquivo = open('cotacoes/dolar.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print(f'''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {valor_moeda}                             *
  ***************************************
    ''')
    arquivo.close()
    quantidade_convertida = quantidade_a_converter * valor_moeda
    print(quantidade_convertida)

def quantidade():
   textoEntrada = '''
  ***************************************
  * Informe a quantidade da moeda que   *
  * deseja converter: '''

   while True:
      valor = m_chamaValor(textoEntrada, 1)

      if valor.retornoStatus():
        if valor.retornoValor() < 0:
          print('''
    ***************************************
    * O valor informado é negativo, assim *
    * não pode ser convertido!            *
    ***************************************
          ''')
        else:
          
          return valor.retornoValor()
          break

def atualiza_cotacao():
    moedas_validas = [1,2,3]
    contador = 1

    peso_arquivo = open('cotacoes/peso.txt', 'r')
    peso = str(peso_arquivo.readline())
    peso_arquivo.close()

    euro_arquivo = open('cotacoes/euro.txt', 'r')
    euro = float(euro_arquivo.readline())
    euro_arquivo.close()

    dolar_arquivo = open('cotacoes/dolar.txt', 'r')
    dolar = str(dolar_arquivo.readline())
    dolar_arquivo.close()

    print('''
  ***************************************
  * 1 - Peso Argentino                  *
  * 2 - Euro                            *
  * 3 - Dolar                           *
  ***************************************
    ''')    
    
    while contador:
       moeda = int(input('''
  ***************************************
  * Informe a moeda que deseja          *
  * atualizar o valor: '''))
       
       if moeda in moedas_validas:
          if moeda == 1:
            print(f'''
  ***************************************
  * Moeda selecionada: Peso Argentino   *
  * A cotação atual da moeda é: {peso}   *
  ***************************************
            ''')

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
               valor = float(valor)
               peso_arquivo = open('cotacoes/peso.txt', 'w')
               peso_arquivo.write(str(valor))
               peso_arquivo.close()
               return True
            except:
               return False

          elif moeda == 2:
            print(f'''
  ***************************************
  * Moeda selecionada: Euro             *
  * A cotação atual da moeda é: {euro}   *
  ***************************************
            ''')

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
               valor = float(valor)
               euro_arquivo = open('cotacoes/euro.txt', 'w')
               euro_arquivo.write(str(valor))
               euro_arquivo.close()
               return True
            except:
               return False

          elif moeda == 3:
            print(f'''
  ***************************************
  * Moeda selecionada: Dolar            *
  * A cotação atual da moeda é: {dolar}   *
  ***************************************
            ''')

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
              document = valor
              valor = float(valor)
              dolar_arquivo = open('cotacoes/dolar.txt', 'w')
              dolar_arquivo.write(document)
              dolar_arquivo.close()
              print(document, valor)
              return True
            except:
               return False

          contador = 0

       else:
          print('''
  ***************************************
  * A moeda informada não               *
  * está disponivel                     *
  ***************************************''')
    
def mostra_cotação():
  peso_arquivo = open('cotacoes/peso.txt', 'r')
  peso = str(peso_arquivo.readline())
  peso_arquivo.close()

  euro_arquivo = open('cotacoes/euro.txt', 'r')
  euro = float(euro_arquivo.readline())
  euro_arquivo.close()

  dolar_arquivo = open('cotacoes/dolar.txt', 'r')
  dolar = str(dolar_arquivo.readline())
  dolar_arquivo.close()

  peso = float(peso)
  euro = float(euro)
  dolar = float(dolar)

  print(f'''
  ***************************************
  *           Cotações atuais           *
  ***************************************
  * Peso Argentino: {peso:.2f}                *
  * Euro: {euro:.2f}                          *
  * Dolar Estadunidense: {dolar:.2f}           *
  ***************************************
  ''')

def inicializador():
  print('''
  Desenvolvido por: Samuel Moraes

  ***************************************
  * Bem vindo ao conversor de valores   *
  ***************************************
  * Moedas disponiveis                  *
  * ------------------------------------*
  * Dolar / Euro / Peso Argentino       *
  ***************************************
  
  '''
  )

def versionamento():
  print('''
  |-------------------------------|
  | Desenvolvido por Samuel Moraes|
  | ----------------------------- |
  | Versão: 1.1    |         2023 |
  |-------------------------------|

  + Existe um erro que aumenta um centavo quando é convertido real para outra moeda, isso foi necessario para corrigir as multiplas casas decimais
  '''
  )

def versionamento_old():
  print('''
  |-------------------------------|
  | Desenvolvido por Samuel Moraes|
  | ----------------------------- |
  | Versão: 1.0    |         2020 |
  |-------------------------------|

  + Existe um erro que aumenta um centavo quando é convertido real para outra moeda, isso foi necessario para corrigir as multiplas casas decimais
  '''
  )

def m_chamaValor(textoEntrada, tipoDado):
  # 1 = Int
  # 2 = Float
  # 3 - Str

  entrada = entrada_generica(valor = 0, status = False)
  if(tipoDado == 1):
    try:
        valor = int(input(textoEntrada))
        entrada.populaValor(valor)
        entrada.populaStatus(True)
        return entrada
    except:
        print('''

    ***************************************
    * Valor informado inválido!           *
    ***************************************
              
              ''')
        entrada.populaStatus(False)
        return entrada
  
  if(tipoDado == 2):
    try:
        valor = float(input(textoEntrada))
        entrada.populaValor(valor)
        entrada.populaStatus(True)
        return entrada
    except:
        print('''

    ***************************************
    * Valor informado inválido!           *
    ***************************************
              
              ''')
        entrada.populaStatus(False)
        return entrada
  
  if(tipoDado == 3):
    try:
        valor = input(textoEntrada)
        entrada.populaValor(valor)
        entrada.populaStatus(True)
        return entrada
    except:
        print('''

    ***************************************
    * Valor informado inválido!           *
    ***************************************
              
              ''')
        entrada.populaStatus(False)
        return entrada

class entrada_generica:
    def __init__(self, valor, status):
      self.valor = valor
      self.status = status

    def populaValor(self, valorRecebido):
      self.valor = valorRecebido
      return self.valor
  
    def populaStatus(self, statusRecebido):
       self.status = statusRecebido
       return self.status

    def retornoValor(self):
      return self.valor
   
    def retornoStatus(self):
      return self.status