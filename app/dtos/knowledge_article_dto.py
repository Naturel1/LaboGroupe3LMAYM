from app.dtos.abstract_dto import AbstractDTO


class KnowledgeArticleDTO(AbstractDTO):
    def __init__(self):
        self.knowledge_article_id = None
        self.knowledge_article_title = None
        self.knowledge_article_content = None
        self.knowledge_article_category_id = None
        self.knowledge_article_author_id = None

    @staticmethod
    def build_from_entity(entity):
        dto = KnowledgeArticleDTO()
        dto.knowledge_article_id = entity.knowledge_article_id
        dto.knowledge_article_title = entity.knowledge_article_title
        dto.knowledge_article_content = entity.knowledge_article_content
        dto.knowledge_article_category_id = entity.knowledge_article_category_id
        dto.knowledge_article_author_id = entity.knowledge_article_author_id
        return dto

    def get_json_parsable(self):
        return dict(self.__dict__)
