import global_function
import time


# 1 - Corversor
# 2 - Mostra Cotação
# 3 - Atualiza Cotação
# 4 - Versionamento
# 5 - Desligar
global_function.limpar_console()
global_function.inicializador()

while True:
    retorno_menu = global_function.menu_inicial()

    if retorno_menu == 1:
        valor = global_function.quantidade()
        moeda_que_converto = global_function.qual_moeda_converter()
        global_function.conversor(valor, moeda_que_converto)
        time.sleep(1)

    elif retorno_menu == 2:
        global_function.mostra_cotação()
        time.sleep(1)

    elif retorno_menu == 3:
        retorno = global_function.atualiza_cotacao()
        if retorno:
            print(''' 
    ***************************************
    * A cotação foi atualizada com sucesso*
    ***************************************
    ''')
        else:
            print('''
    ***************************************
    * Ocorreu um erro ao atualizar a      *
    * cotação!                            *
    ***************************************
            ''')
        time.sleep(1)

    elif retorno_menu == 4:
        global_function.versionamento()
        time.sleep(1)

    elif retorno_menu == 5:
        break

<<<<<<< HEAD
    else:
        print('Nenhuma opção selecionada')


=======
elif global_function.menu_inicial() == 2:

  retorno = global_function.atualiza_cotacao()
  if retorno:
        print(''' 
  ***************************************
  * A cotação foi atualizada com sucesso*
  ***************************************
  ''')
  else:
        print('''
  ***************************************
  * Ocorreu um erro ao atualizar a      *
  * cotação!                            *
  ***************************************
        ''')

elif global_function.menu_inicial() == 3:
  global_function.mostra_cotação()

elif global_function.menu_inicial() == 4:
  global_function.versionamento()
else:
  print
>>>>>>> 5d1a54c7af4bd01332689c2db0f976b80ca7699c
