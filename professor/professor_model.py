dados = {
    "alunos": [
        {"nome": "lucas", "id": 15},
        {"nome": "cicero", "id": 29},
    ],
    "professores": [
            {"nome": "caio", "id": 15},
    ]
}

professor_id_counter = 1

class ProfessorNaoEncontrado(Exception):
    pass


def professor_por_id(professor_id):
    lista_professores = dados['professores']
    for dicionario in lista_professores:
        if dicionario['id'] == professor_id:
            return dicionario
    raise ProfessorNaoEncontrado

    # for professor in professores:
    #     if professor['id'] == professor_id:
    #         return professor
    # return None

def listar_professores():
    return dados['professores']

def adicionar_professor(professor):
    dados['professores'].append(professor)
    
def atualizar_professor(professor_id, novos_dados):
    professor = professor_por_id(professor_id)
    professor.update(novos_dados)
   

def excluir_professor(professor_id):
    professor = professor_por_id(professor_id)
    dados['professores'].remove(professor)


