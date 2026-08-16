from app.dtos.abstract_dto import AbstractDTO


class SatisfactionSurveyDTO(AbstractDTO):
    def __init__(self):
        self.satisfaction_survey_id = None
        self.rating = None
        self.comment = None
        self.ticket_id = None
        self.client_id = None

    @staticmethod
    def build_from_entity(entity):
        sas_dto = SatisfactionSurveyDTO()
        sas_dto.satisfaction_survey_id = entity.satisfaction_survey_id
        sas_dto.satisfaction_survey_rating = entity.satisfaction_survey_rating
        sas_dto.satisfaction_survey_comment = entity.satisfaction_survey_comment
        sas_dto.satisfaction_survey_ticket_id = entity.satisfaction_survey_ticket_id
        sas_dto.satisfaction_survey_client_id = entity.satisfaction_survey_client_id
        return sas_dto

    def get_json_parsable(self):
        return dict(self.__dict__)
