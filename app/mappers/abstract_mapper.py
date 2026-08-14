from abc import ABC, abstractmethod

class AbstractMapper(ABC):

    @staticmethod
    @abstractmethod
    def entity_to_dto(entity):
        pass

    @staticmethod
    @abstractmethod
    def form_to_entity(form, entity):
        pass