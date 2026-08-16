from app.models.site import Site
from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.site_dto import SiteDTO
from app.forms.site.site_form import SiteForm


class SiteMapper(AbstractMapper):
   
    @staticmethod
    def entity_to_dto(entity: Site) -> SiteDTO:
        return SiteDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: SiteForm, entity: Site):
        entity.site_name = form.name.data
        entity.site_address = form.address.data
        entity.site_city = form.city.data
        return entity
