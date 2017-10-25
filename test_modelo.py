import pytest
from modelo import (Tarefa, listar_tarefas, memdb, criar_tarefa,
                    remover_tarefa, recuperar_tarefa, editar_tarefa)


def test_define_tarefa():
    tarefa = Tarefa('titulo', 'descrição', False)
    assert tarefa.titulo == 'titulo'
    assert tarefa.descricao == 'descrição'
    assert tarefa.status is False


def test_status_nao_obrigatorio():
    tarefa = Tarefa('titulo', 'descrição')
    assert tarefa.status is False
    tarefa = Tarefa('titulo', 'descrição', True)
    assert tarefa.status is True


def test_toda_tarefa_tem_identificador_unico():
    tarefa1 = Tarefa('titulo', 'descrição')
    tarefa2 = Tarefa('titulo', 'descrição')
    tarefa1.id != tarefa2.id


def test_listar_tarefas():
    tarefa1 = Tarefa('titulo 1', 'descrição')
    tarefa2 = Tarefa('titulo 2', 'descrição')
    memdb[tarefa1.id] = tarefa1
    memdb[tarefa2.id] = tarefa2
    for indice, tarefa in enumerate(listar_tarefas(), 1):
        assert tarefa.titulo == 'titulo {}'.format(indice)


def test_ordem_tarefas():
    memdb.clear()
    tarefa1 = Tarefa('titulo 1', 'descrição', True)  # tarefa já finalizada
    tarefa2 = Tarefa('titulo 2', 'descrição')  # não finalizada
    memdb[tarefa1.id] = tarefa1
    memdb[tarefa2.id] = tarefa2
    tarefas = list(listar_tarefas())
    assert tarefas[0].titulo == 'titulo 2'
    assert tarefas[1].titulo == 'titulo 1'


def test_criar_tarefa():
    memdb.clear()
    tarefa = criar_tarefa('titulo', 'descrição')
    assert tarefa.titulo == 'titulo'
    assert tarefa.descricao == 'descrição'
    assert tarefa.status is False
    assert len(memdb) > 0


def test_remover_tarefa():
    memdb.clear()
    tarefa = Tarefa('titulo', 'descricao')
    memdb[tarefa.id] = tarefa
    remover_tarefa(tarefa.id)
    assert len(memdb) == 0


def test_tarefa_nao_existente():
    memdb.clear()
    with pytest.raises(KeyError):
        remover_tarefa(1)


def test_recuperar_tarefa():
    memdb.clear()
    tarefa = Tarefa('titulo', 'descricao')
    memdb[tarefa.id] = tarefa
    recuperado = recuperar_tarefa(tarefa.id)
    assert tarefa.id == recuperado.id
    assert tarefa.titulo == recuperado.titulo
    assert tarefa.descricao == recuperado.descricao


def test_recuperar_tarefa_nao_existente():
    memdb.clear()
    with pytest.raises(KeyError):
        remover_tarefa(1)


def test_editar_tarefa():
    memdb.clear()
    tarefa = Tarefa('titulo', 'descricao')
    memdb[tarefa.id] = tarefa
    modificado = Tarefa('titulo modificado', 'descricao')
    editar_tarefa(tarefa.id, modificado)
    assert memdb[tarefa.id].titulo == 'titulo modificado'