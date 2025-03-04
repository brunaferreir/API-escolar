from flask import Blueprint, jsonify, request
from .professor_model import  ProfessorNaoEncontrado,listar_professores, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor

professor_blueprint = Blueprint('professores', __name__)

@professor_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return jsonify(professores)


@professor_blueprint.route('/professores/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    try:
        professor = professor_por_id(professor_id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'professor não encontrado'}), 404



@professor_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    adicionar_professor(data)
    return jsonify(data), 201

@professor_blueprint.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.json
    try:
        atualizar_professor(professor_id, data)
        return jsonify(professor_por_id(professor_id))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}),404



@professor_blueprint.route('/professores/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    try:
        excluir_professor(professor_id)
        return 'Professor deletado', 204
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404





    # excluir_professor(professor_id)
    # return jsonify({'mensagem': 'Professor removido'})