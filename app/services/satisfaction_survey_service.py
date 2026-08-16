from app import db
from app.models.satisfaction_survey import SatisfactionSurvey
from app.framework.decorators.injectable import injectable
from app.forms.survey.satisfaction_survey_form import SatisfactionSurveyForm
from app.models.user import User
from app.services.base_service import BaseService
from app.mappers.satisfaction_survey_mapper import SatisfactionSurveyMapper


@injectable
class SatisfactionSurveyService(BaseService):
    def find_all(self):
        return [SatisfactionSurveyMapper.entity_to_dto(sas)
                for sas in SatisfactionSurvey.query.filter_by(active=True).order_by(SatisfactionSurvey.satisfaction_survey_id).all()]

    def find_one(self, satisfaction_survey_id):
        sas = self.find_one_entity(satisfaction_survey_id)
        return SatisfactionSurveyMapper.entity_to_dto(sas) if sas else None

    def find_one_entity(self, satisfaction_survey_id: int):
        return SatisfactionSurvey.query.filter_by(satisfaction_survey_id=satisfaction_survey_id, active=True).first()

    def find_one_by(self, **kwargs):
        return SatisfactionSurvey.query.filter_by(active=True, **kwargs).first()

    def insert(self, form: SatisfactionSurveyForm):
        existing_sas = self.find_one_by(survey_name=form.ticket_id.data)
        if existing_sas:
            raise ValueError(f"Satisfaction Survey for '{form.ticket_id.data}' ticket already exists.")
        sas = SatisfactionSurvey()
        sas = SatisfactionSurveyMapper.form_to_entity(form, sas)
        db.session.add(sas)
        db.session.commit()
        return SatisfactionSurveyMapper.entity_to_dto(sas)

    def update(self, satisfaction_survey_id, form: SatisfactionSurveyForm):
        sas = self.find_one_entity(satisfaction_survey_id)
        if sas is None:
            return None
        sas = SatisfactionSurveyMapper.form_to_entity(form, sas)
        db.session.commit()
        return SatisfactionSurveyMapper.entity_to_dto(sas)

    def delete(self, satisfaction_survey_id):
        sas = self.find_one_entity(satisfaction_survey_id)
        if sas is None:
            return None
        sas.soft_delete()
        db.session.commit()
        return sas.satisfaction_survey_id
