from app.models.satisfaction_survey import SatisfactionSurvey
from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.satisfaction_survey_dto import SatisfactionSurveyDTO
from app.forms.survey.satisfaction_survey_form import SatisfactionSurveyForm


class SatisfactionSurveyMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: SatisfactionSurvey):
        return SatisfactionSurveyDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: SatisfactionSurveyForm, entity: SatisfactionSurvey):
        entity.satisfaction_survey_rating = form.rating.data
        entity.satisfaction_survey_comment = form.comment.data
        entity.satisfaction_survey_ticket_id = form.ticket_id.data
        entity.satisfaction_survey_client_id = form.client_id.data
        return entity
