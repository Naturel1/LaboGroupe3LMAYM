from app import app, db
from app.dtos.team_dto import TeamDTO
from app.forms.team.team_create_form import TeamCreateForm
from app.forms.team.team_update_form import TeamUpdateForm
from app.framework.decorators.injectable import injectable
from app.mappers.team_mapper import TeamMapper
from app.models.team import Team
from app.models.user import User
from app.services.base_service import BaseService


@injectable
class TeamService(BaseService):
    """CRUD and members assignment for teams."""

    def find_all(self) -> list[TeamDTO]:
        return [TeamMapper.entity_to_dto(team)
                for team in Team.query.filter_by(active=True).order_by(Team.team_id).all()]

    def find_one(self, entity_id: int) -> TeamDTO | None:
        team = self.find_one_entity(entity_id)
        return TeamMapper.entity_to_dto(team) if team else None

    def find_one_entity(self, entity_id: int) -> Team | None:
        return Team.query.filter_by(team_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Team | None:
        return Team.query.filter_by(**kwargs).first()

    def insert(self, form: TeamCreateForm) -> TeamDTO | None:
        team = Team()
        TeamMapper.form_to_entity(form, team)

        try:
            db.session.add(team)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert team: {e}")
            db.session.rollback()
            return None

        return TeamMapper.entity_to_dto(team)

    def update(self, entity_id: int, form: TeamUpdateForm) -> TeamDTO | None:
        team = self.find_one_entity(entity_id)

        if team is None:
            return None

        TeamMapper.form_to_entity(form, team)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update team {entity_id}: {e}")
            db.session.rollback()
            return None

        return TeamMapper.entity_to_dto(team)

    def update_members(self, entity_id: int, member_ids: list[int]) -> TeamDTO | None:
        team = self.find_one_entity(entity_id)

        if team is None:
            return None

        wanted = set(member_ids or [])
        users = User.query.filter(User.user_id.in_(wanted), User.active == True).all() if wanted else []

        if len(users) != len(wanted):
            return None

        for member in list(team.members):
            if member.user_id not in wanted:
                member.user_team_id = None

        for user in users:
            user.user_team_id = team.team_id

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update team members {entity_id}: {e}")
            db.session.rollback()
            return None

        return TeamMapper.entity_to_dto(team)

    def delete(self, entity_id: int) -> int | None:
        team = self.find_one_entity(entity_id)

        if team is None:
            return None

        for member in list(team.members):
            member.user_team_id = None

        team.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete team {entity_id}: {e}")
            db.session.rollback()
            return None

        return team.team_id
