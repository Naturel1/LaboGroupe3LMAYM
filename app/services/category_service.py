from app import app, db
from app.dtos.category_dto import CategoryDTO
from app.forms.category.category_form import CategoryForm
from app.framework.decorators.injectable import injectable
from app.mappers.category_mapper import CategoryMapper
from app.models.category import Category
from app.services.base_service import BaseService


@injectable
class CategoryService(BaseService):
    """
    Provides implementation of category service.
    """

    def find_all(self) -> list[CategoryDTO]:
        return [CategoryMapper.entity_to_dto(category)
                for category in Category.query.filter_by(active=True).order_by(Category.category_id).all()]

    def find_one(self, entity_id: int) -> CategoryDTO | None:
        category = self.find_one_entity(entity_id)
        return CategoryMapper.entity_to_dto(category) if category else None

    def find_one_entity(self, entity_id: int) -> Category | None:
        return Category.query.filter_by(category_id=entity_id, active=True).first()

    def find_one_by(self, **kwargs) -> CategoryDTO | None:
        category = Category.query.filter_by(active=True, **kwargs).first()
        return CategoryMapper.entity_to_dto(category) if category else None

    def insert(self, form: CategoryForm) -> CategoryDTO | None:
        category = Category()
        CategoryMapper.form_to_entity(form, category)
        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert category: {e}")
            db.session.rollback()
            return None
        return CategoryMapper.entity_to_dto(category)

    def update(self, entity_id: int, form: CategoryForm) -> CategoryDTO | None:
        category = self.find_one_entity(entity_id)
        if category is None:
            return None
        CategoryMapper.form_to_entity(form, category)
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update category {entity_id}: {e}")
            db.session.rollback()
            return None
        return CategoryMapper.entity_to_dto(category)

    def delete(self, entity_id: int) -> int | None:
        category = self.find_one_entity(entity_id)
        if category is None:
            return None
        try:
            db.session.delete(category)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete category {entity_id}: {e}")
            db.session.rollback()
            return None
        return entity_id