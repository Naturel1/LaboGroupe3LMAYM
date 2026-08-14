from app.dtos.intervention_dto import InterventionDTO
from app.forms.intervention.intervention_form import InterventionForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.intervention import Intervention

class InterventionMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(intervention: Intervention) -> InterventionDTO:

        return InterventionDTO.build_from_entity(intervention)


    @staticmethod
    def form_to_entity(form, intervention: Intervention) -> Intervention:

        if isinstance(form, InterventionForm):
            intervention.intervention_date = form.intervention_date.data
            intervention.intervention_duration = form.intervention_duration.data
            intervention.intervention_report = form.intervention_report.data
            intervention.intervention_ticket_id = form.intervention_ticket_id.data
            intervention.intervention_technician_id = form.intervention_technician_id.data
            intervention.intervention_type_id = form.intervention_type_id.data

        return intervention
