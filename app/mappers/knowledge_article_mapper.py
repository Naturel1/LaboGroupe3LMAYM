from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.knowledge_article_dto import KnowledgeArticleDTO
from app.models.knowledge_article import KnowledgeArticle
from app.forms.survey.knowledge_article_form import KnowledgeArticleForm


class KnowledgeArticleMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: KnowledgeArticle):
        return KnowledgeArticleDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: KnowledgeArticleForm, entity: KnowledgeArticle):
        entity.knowledge_article_title = form.title.data
        entity.knowledge_article_content = form.content.data
        entity.knowledge_article_category_id = form.category_id.data
        entity.knowledge_article_author_id = form.author_id.data

        return entity
