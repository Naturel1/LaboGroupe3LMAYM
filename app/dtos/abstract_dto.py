from abc import ABC, abstractmethod


class AbstractDTO(ABC):
    """Common contract for all DTOs (Data Transfer Objects)."""

    @staticmethod
    @abstractmethod
    def build_from_entity(entity):
        pass

    @abstractmethod
    def get_json_parsable(self):
        pass