#rastreamento de tarefas
import json
tarefas={}

def criar():
    
    tarefas['Id']=int(input('Id:'))
    tarefas['Descricao']=str(input('Descrição:'))
    tarefas['Status']=str(input('Status:'))
    tarefas['Dta-Criada']=float(input('Data Criada:'))
    tarefas['Dta_atualizada']=float(input('Data Atualizada:'))
    
    converte=json.dumps(tarefas, indent=4)
        
    with open('main.json','w') as file:
        file.write(converte)
            
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
    if opcao == 5:
        
        break
    