from app.dtos.team_dto import TeamDTO
from app.forms.team.team_create_form import TeamCreateForm
from app.forms.team.team_update_form import TeamUpdateForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.team import Team


class TeamMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Team) -> TeamDTO:
        return TeamDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, team: Team) -> Team:

        if isinstance(form, TeamCreateForm) or isinstance(form, TeamUpdateForm):
            team.team_name = form.name.data
            team.team_description = form.description.data

        return team
