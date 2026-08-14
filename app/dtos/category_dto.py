from app.dtos.abstract_dto import AbstractDTO


class CategoryDTO(AbstractDTO):
    """
    Data Transfer Object for Category entity.
    """

    def __init__(self):
        self.category_id = None
        self.name = None
        self.description = None

    @staticmethod
    def build_from_entity(entity) -> "CategoryDTO":
        category_dto = CategoryDTO()
        category_dto.category_id = entity.category_id
        category_dto.name = entity.name
        category_dto.description = entity.description
        return category_dto

    def get_json_parsable(self):
        return self.__dict__