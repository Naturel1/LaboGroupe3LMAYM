from app.dtos.abstract_dto import AbstractDTO


class TeamDTO(AbstractDTO):
    """A team as seen by the views (templates, JSON responses...)."""

    def __init__(self):
        self.team_id = None
        self.name = None
        self.description = None
        self.member_ids = []

    @staticmethod
    def build_from_entity(team) -> "TeamDTO":
        """Build a TeamDTO from a Team entity."""

        team_dto = TeamDTO()

        team_dto.team_id = team.team_id
        team_dto.name = team.team_name
        team_dto.description = team.team_description
        team_dto.member_ids = [member.user_id for member in (team.members or [])]

        return team_dto

    def get_json_parsable(self):
        """Return a dict of base types, ready for jsonify()."""

        data = dict(self.__dict__)
        return data
