from app import db
from app.framework.decorators.injectable import injectable
from app.services.base_service import BaseService
from app.models.knowledge_article import KnowledgeArticle
from app.forms.survey.knowledge_article_form import KnowledgeArticleForm
from app.mappers.knowledge_article_mapper import KnowledgeArticleMapper


@injectable
class KnowledgeArticleService(BaseService):
    def find_all(self):
        return [KnowledgeArticleMapper.entity_to_dto(ka) for ka in KnowledgeArticle.query.filter_by(active=True).all()]

    def find_one(self,knowledge_article_id):
        ka = KnowledgeArticle.query.filter_by(knowledge_article_id=knowledge_article_id, active=True).first()
        return KnowledgeArticleMapper.entity_to_dto(ka) if ka else None

    def find_one_by(self, **kwargs):
        eq = KnowledgeArticle.query.filter_by(active=True, **kwargs).first()
        return KnowledgeArticleMapper.entity_to_dto(eq) if eq else None

    def insert(self, form: KnowledgeArticleForm):
        ka = KnowledgeArticle()
        ka = KnowledgeArticleMapper.form_to_entity(form, ka)
        db.session.add(ka)
        db.session.commit()
        return KnowledgeArticleMapper.entity_to_dto(ka)

    def update(self, knowledge_article_id, form: KnowledgeArticleForm):
        ka = KnowledgeArticle.query.filter_by(knowledge_article_id=knowledge_article_id, active=True).first()
        if ka is None:
            return None
        ka = KnowledgeArticleMapper.form_to_entity(form, ka)
        db.session.commit()
        return KnowledgeArticleMapper.entity_to_dto(ka)

    def delete(self, knowledge_article_id):
            ka = self.find_one(knowledge_article_id)
            if ka is None:
                return None
            ka.active = False
            db.session.commit()
            return ka