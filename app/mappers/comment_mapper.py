from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.comment_dto import CommentDTO
from app.forms.comment.comment_form import CommentForm
from app.models.comment import Comment

class CommentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Comment) -> CommentDTO:
        return CommentDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, entity: Comment) -> Comment:

        entity.comment_content = form.content.data
        return entity
