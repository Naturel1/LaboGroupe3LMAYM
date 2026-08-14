from app import db
from app.models.site import Site
from app.framework.decorators.injectable import injectable
from app.forms.site.site_form import SiteForm
from app.services.base_service import BaseService
from app.mappers.site_mapper import SiteMapper


@injectable
class SiteService(BaseService):
    def find_all(self):
        """Find all sites."""
        return Site.query.filter_by(active=True).all()

    def find_one(self, site_id):
        """Find one site by id."""
        return Site.query.filter_by(site_id=site_id, active=True).first()

    def find_one_by(self, **kwargs):
        """Find one site by any field."""
        return Site.query.filter_by(**kwargs).first()
    
    def insert(self, form: SiteForm):
        """Create a new site."""
        site = Site()
        site = SiteMapper.form_to_entity(form, site)
        db.session.add(site)
        db.session.commit()
        return site

    def update(self, site_id, form: SiteForm):
        """Update a site attributes."""
        site = self.find_one(site_id)
        if site is None:
            return None
        site = SiteMapper.form_to_entity(form, site)
        db.session.commit()
        return site

    def delete(self, site_id):
        """Soft delete a site"""
        site = self.find_one(site_id)
        if site is None:
            return None
        site.active = False
        db.session.commit()
        return site
