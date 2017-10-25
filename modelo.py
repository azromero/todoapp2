from operator import attrgetter

memdb = {}


class Tarefa:

    id = 1

    def __init__(self, titulo, descricao, status=False):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id = Tarefa.id
        Tarefa.id += 1


def listar_tarefas():
    return sorted(memdb.values(), key=attrgetter('status'))


def criar_tarefa(titulo, descricao, status=False):
    tarefa = Tarefa(titulo, descricao, status)
    memdb[tarefa.id] = tarefa
    return tarefa


def remover_tarefa(id_):
    del memdb[id_]


def recuperar_tarefa(id_):
    return memdb[id_]


def editar_tarefa(id_, tarefa):
    editado = memdb[id_]
    editado.titulo = tarefa.titulo or editado.titulo
    editado.descricao = tarefa.descricao or editado.descricao
    editado.status = tarefa.status
    return editado