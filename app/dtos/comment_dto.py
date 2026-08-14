from app.dtos.abstract_dto import AbstractDTO
from app.models.comment import Comment

class CommentDTO(AbstractDTO):
    def __init__(self):
        self.comment_id = None
        self.content = None
        self.ticket_id = None
        self.author_id = None
        self.author_name = None
        self.created_at = None

    @staticmethod
    def build_from_entity(entity: Comment) -> "CommentDTO":
        comment_dto = CommentDTO()

        comment_dto.comment_id = entity.comment_id
        comment_dto.content = entity.comment_content
        comment_dto.ticket_id = entity.comment_ticket_id
        comment_dto.author_id = entity.comment_author_id
        comment_dto.author_name = (
            f"{entity.author.user_first_name} {entity.author.user_last_name}"
            if entity.author else None
        )
        comment_dto.created_at = entity.created_at.isoformat() if entity.created_at else None
                                
        return comment_dto

    def get_json_parsable(self):
        return self.__dict__