from abc import ABC, abstractmethod


class BaseService(ABC):
    """CRUD contract for all services."""

    @abstractmethod
    def find_all(self):
        """Return all entites as DTO."""

    @abstractmethod
    def find_one(self, entity_id: int):
        """Return one entity as DTO or None."""

    @abstractmethod
    def find_one_by(self, **kwargs):
        """Return one entity as DTO or None."""

    @abstractmethod
    def insert(self, data):
        """Insert a new entity."""

    @abstractmethod
    def update(self, entity_id: int, data):
        """Update an existing entity."""

    @abstractmethod
    def delete(self, entity_id: int):
        """Delete an existing entity."""
