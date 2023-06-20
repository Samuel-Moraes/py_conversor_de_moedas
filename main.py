import global_function

global_function.limpar_console()
global_function.inicializador()
retorno_menu = global_function.menu_inicial()

if retorno_menu == 1:
  # moeda_que_tenho = global_function.qual_tenho_moeda()
  valor = global_function.quantidade()
  moeda_que_converto = global_function.qual_moeda_converter()
  global_function.conversor(valor, moeda_que_converto)

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