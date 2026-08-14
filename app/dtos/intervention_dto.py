from app.dtos.abstract_dto import AbstractDTO

class InterventionDTO(AbstractDTO):

    def __init__(self):
        self.intervention_id = None
        self.intervention_date = None
        self.intervention_duration = None
        self.intervention_report = None
        self.intervention_ticket_id = None
        self.intervention_technician_id = None
        self.technician_name = None
        self.intervention_type_id = None
        self.intervention_type_name = None


    @staticmethod
    def build_from_entity(intervention) -> "InterventionDTO":
        intervention_dto = InterventionDTO()

        intervention_dto.intervention_id = intervention.intervention_id
        intervention_dto.intervention_date = intervention.intervention_date.isoformat()
        intervention_dto.intervention_duration  = intervention.intervention_duration
        intervention_dto.intervention_report = intervention.intervention_report
        intervention_dto.intervention_ticket_id = intervention.intervention_ticket_id
        intervention_dto.intervention_technician_id = intervention.intervention_technician_id
        intervention_dto.technician_name = (f"{intervention.technician.user_firstname} {intervention.technician.user_lastname}" if intervention.technician else None)
        intervention_dto.intervention_type_id = intervention.intervention_type_id
        intervention_dto.intervention_type_name = (intervention.intervention_type.intervention_type_name if intervention.intervention_type else None)

        return intervention_dto


    def get_json_parsable(self):

        data = dict(self.__dict__)
        return data