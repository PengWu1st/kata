
from typing import Callable, Type
from functools import partial


class Entity:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'


class ValueObject:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value})'


class Repository:
    def __init__(self):
        self.entities = set()

    def __getitem__(self, id):
        for entity in self.entities:
            if entity.id == id:
                return entity
        return None

    def __setitem__(self, id, entity):
        self.entities.add(entity)

    def __iter__(self):
        return iter(self.entities)

    def delete(self, entity):
        self.entities.remove(entity)


def addEntity(repository, id):
    entity = Entity(id)
    repository[id] = entity
    return entity


def getEntity(repository, id):
    return repository[id]


def deleteEntity(repository, id):
    entity = repository[id]
    repository.delete(entity)
    return entity


def updateEntity(repository, entity, id):
    repository.delete(entity)
    entity.id = id
    repository[id] = entity
    return entity


def create_service(repository):

    return {
        "addEntity": partial(addEntity, repository),
        "getEntity": partial(getEntity, repository),
        "deleteEntity": partial(deleteEntity, repository),
        "updateEntity": partial(updateEntity, repository)
    }


def main():
    # app start up
    service = create_service(Repository())

    # requests arrives
    requests = [
        partial(service["getEntity"], 1),
        partial(service["addEntity"], 1),
        partial(service["getEntity"], 1),
        partial(service["deleteEntity"], 1),
        partial(service["getEntity"], 1),
    ]

    for request in requests:
        print(request())


if __name__ == "__main__":
    main()
