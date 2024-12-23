#rastreamento de tarefas
import json
tarefas={'tarefa':[]}
lista_tarefas=[]





def criar():
    
    while True:
        id=int(input('ID:'))
        descricao=str(input('Descrição:'))
        status=str(input('Status:'))
        dta_criada=float(input('Data criada:'))
        dta_atualizada=float(input('Data atualizada:'))
        break
    while True:
        tarefas['tarefa'].append(
            {
                'id':id,
                'descricao':descricao,
                'status':status,
                'data_criada':dta_criada,
                'data_atualizada':dta_atualizada
            }
        )
        break
    with open("main.json",'w') as file:
        json.dump(tarefas,file, indent=4)
def ver():
    for x in lista_tarefas:
        print(x)
while True:
    print('-'*15)
    print('1-Criar')
    print('2-Atualizar')    
    print('3-Ver')
    print('4-Excluir')
    print('5-Sair')
    print('-'*15)
    
    opcao=int(input('Opção:'))
    if opcao == 1:
        criar()
    if opcao == 3:
        ver()
    if opcao == 5:
        
        break
    