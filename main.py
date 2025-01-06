import json
from datetime import date
lista_tarefa=[]
tarefa=dict()
data=date.today()
lista_concluida=[]
lista_andamento=[]
lista_naofeito=[]

dta_atual=str(data)
dta_atualizada=str(data)
def criar():
    while True:
        tarefa.clear()
        tarefa['id']=int(input('ID:'))
        tarefa['Descricao']=str(input('Descrição:'))
        while True:
            print('DIGITE O COD DO STATUS:')
            print('C - Concluido')
            print('A - Andamento')
            print('N - Não Feito')
            cod_status=str(input('Codigo Status:')).upper()
            if cod_status == 'C':
                tarefa['status']='Concluido'
                break
            elif cod_status == 'A':
                tarefa['status']='Andamento'
                break
            elif cod_status == 'N':
                tarefa['status']='Não Feito'
                break
            print('Erro! Por favor digite um dos codigos acima.')
        tarefa['Data_criada']=dta_atual
        tarefa['Data_atualizada']=dta_atualizada
        break
    lista_tarefa.append(tarefa.copy())
    with open('main.json','w') as file:
        json.dump(lista_tarefa, file, indent=4)
    if tarefa['status'] == 'Andamento':
        lista_andamento.append(tarefa.copy())
    print(lista_andamento)
    if tarefa['status'] == 'Concluido':
        lista_concluida.append(tarefa.copy())
    print(lista_concluida)
    if tarefa['status'] == 'Não Feito':
        lista_naofeito.append(tarefa.copy())
    print(lista_naofeito)
def vizualizar():
    print('1-Toda a lista')
    print('2 - Tarefas em andamento')
    print('3 - Tarefas concluidas')
    print('4 - Tarefas não feitas')
    opcao_visualizar = int(input('Opcão:'))
    
    if opcao_visualizar == 1:
        for toda_lista in lista_tarefa:
            print(toda_lista)
    elif opcao_visualizar == 2:
        for tarefa_andamento in lista_andamento:
            print(tarefa_andamento)
    elif opcao_visualizar == 3:
        for tarefa_concluida in lista_concluida:
            print(lista_concluida)
    elif opcao_visualizar == 4:
        for tarefa_naofeita in lista_naofeito:
            print(tarefa_naofeita)
    else:
        print('Erro! Codigo não encontrado.')
#
def atualizar():
    opcao=int(input('indice para atualizar:'))
    for c in lista_tarefa[opcao]:
        print(c)
    
while True:
    opcao=int(input('Opção:'))
    if opcao == 1:
        criar()
    if opcao == 2:
        vizualizar()
    if opcao == 3:
        atualizar()
    if opcao == 0:
        break