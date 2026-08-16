from app.dtos.abstract_dto import AbstractDTO


class SiteDTO(AbstractDTO):
    def __init__(self):
        self.site_id = None
        self.name = None
        self.address = None
        self.city = None

    @staticmethod
    def build_from_entity(entity):
        site_dto = SiteDTO()
        site_dto.site_id = entity.site_id
        site_dto.name = entity.site_name
        site_dto.address = entity.site_address
        site_dto.city = entity.site_city
        return site_dto

    def get_json_parsable(self):
        return dict(self.__dict__)