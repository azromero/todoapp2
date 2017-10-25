import json
from main import app
from modelo import memdb

def test_criar_tarefa():
    with app.test_client() as c:
        # realiza a requisição utilizando o verbo POST
        resp = c.post('/task', data={'titulo': 'titulo',
                                     'descricao': 'descricao'})
        # é realizada a análise e transformação para objeto python da resposta
        data = json.loads(resp.data.decode('utf-8'))
        # 201 CREATED é o status correto aqui
        assert resp.status_code == 201
        assert data['titulo'] == 'titulo'
        assert data['descricao'] == 'descricao'
        # qaundo a comparação é com True, False ou None, utiliza-se o "is"
        assert data['status'] is False


def test_erro_ao_criar_tarefa():
    memdb.clear()
    with app.test_client() as c:
        resp = c.post('/task', data={'titulo': 'titulo'})
        assert resp.status_code == 400
