import subprocess
import os

# Limpa o console
def limpar_console():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
#

def menu_inicial():
    contador = 1
    lista_de_opcoes = [1, 2, 3, 4]
    print('''
  ***************************************
  * 1 - Converter Moedas                *
  * 2 - Alterar Cotação das Moedas      *
  * 3 - Desligar                        *
  * 4 - Informações                     *
  ***************************************
  ''')
    
    while contador:
        opcao_selecionada = int(input('''
  ***************************************
  * Digite a opção desejada para iniciar*
  * o sistema: '''))

        if opcao_selecionada in lista_de_opcoes:
            contador = 0
            return opcao_selecionada

        else:
            print(''' 
  ***************************************
  * Nenhuma opção foi selecionada!      *
  ***************************************

            ''')

# Não utilizado
def qual_tenho_moeda():
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
    moeda = int(input('Informe a moeda que você tem: '))

    if moeda == lista_de_opcoes[0]:
      print('Moeda selecionada: Peso Argentino')
      return 1
    elif moeda == lista_de_opcoes[1]:
      print('Moeda selecionada: Euro')
      return 2
    elif moeda == lista_de_opcoes[2]:
      print('Moeda selecionada: Dolar')
      return 3
    else:
       print('A moeda digitada não está entre as opções disponiveis! ')
  
def qual_moeda_converter():
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
    moeda = int(input('''
  ***************************************
  * Informe a moeda que você quer       *
  * converter: '''))

    if moeda == lista_de_opcoes[0]:
      print('''
  ***************************************
  * Moeda selecionada: Peso Argentino   *
  ***************************************
  ''')
      return 1
    elif moeda == lista_de_opcoes[1]:
      print('''
  ***************************************
  * Moeda selecionada: Euro             *
  ***************************************
      ''')
      return 2
    elif moeda == lista_de_opcoes[2]:
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
    arquivo = open('peso.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print('''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {0}                            *
  ***************************************
   '''.format(valor_moeda))
    arquivo.close()
    quantidade_convertida = quantidade_a_converter / valor_moeda
    print(quantidade_convertida)
      
  if moeda_que_converto == 2:
    arquivo = open('euro.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print('''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {0}                             *
  ***************************************
    '''.format(valor_moeda))
    arquivo.close()
    quantidade_convertida = quantidade_a_converter / valor_moeda
    print(quantidade_convertida)

  if moeda_que_converto == 3:
    arquivo = open('dolar.txt', 'r')
    valor_moeda = float(arquivo.readline())
    print('''
  ***************************************
  * A cotação da moeda selecionada está *
  * em: {0}                             *
  ***************************************
    '''.format(valor_moeda))
    arquivo.close()
    quantidade_convertida = quantidade_a_converter / valor_moeda
    print(quantidade_convertida)

def quantidade():
   contador = 1

   while contador:
      valor = float(input('''
  ***************************************
  * Informe a quantidade de reais que   *
  * deseja converter: '''))

      if valor < 0:
         print('''
  ***************************************
  * O valor informado é negativo, assim *
  * não pode ser convertido!            *
  ***************************************
         ''')
      else:
         contador = 0
         return valor

def atualiza_cotacao():
    print('''
  ---------------------------------------------
  
  ''')
    moedas_validas = [1,2,3]
    contador = 1

    peso_arquivo = open('peso.txt', 'r')
    peso = str(peso_arquivo.readline())
    peso_arquivo.close()

    euro_arquivo = open('euro.txt', 'r')
    euro = float(euro_arquivo.readline())
    euro_arquivo.close()

    dolar_arquivo = open('dolar.txt', 'r')
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
            print('''
  ***************************************
  * Moeda selecionada: Peso Argentino   *
  * A cotação atual da moeda é: {}   *
  ***************************************
            '''.format(peso))

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
               valor = float(valor)
               peso_arquivo = open('peso.txt', 'w')
               peso_arquivo.write(str(valor))
               peso_arquivo.close()
               return True
            except:
               return False

          elif moeda == 2:
            print('''
  ***************************************
  * Moeda selecionada: Euro             *
  * A cotação atual da moeda é: {}   *
  ***************************************
            '''.format(euro))

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
               valor = float(valor)
               euro_arquivo = open('euro.txt', 'w')
               euro_arquivo.write(str(valor))
               euro_arquivo.close()
               return True
            except:
               return False

          elif moeda == 3:
            print('''
  ***************************************
  * Moeda selecionada: Dolar            *
  * A cotação atual da moeda é: {}   *
  ***************************************
            '''.format(dolar))

            valor = input('''
  ***************************************
  * Informe a cotação atual: ''')
            try:
              document = valor
              valor = float(valor)
              dolar_arquivo = open('euro.txt', 'w')
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
  print('''
  ---------------------------------------------
  
  ''')
  peso_arquivo = open('peso.txt', 'r')
  peso = str(peso_arquivo.readline())
  peso_arquivo.close()

  euro_arquivo = open('euro.txt', 'r')
  euro = float(euro_arquivo.readline())
  euro_arquivo.close()

  dolar_arquivo = open('dolar.txt', 'r')
  dolar = str(dolar_arquivo.readline())
  dolar_arquivo.close()

  print('''
  ***************************************
  *           Cotações atuais           *
  ***************************************
  * Peso Argentino: {}               *
  * Euro: {}                          *
  * Dolar Estadunidense: {}           *
  ***************************************
  '''.format(peso, euro, dolar))
   


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