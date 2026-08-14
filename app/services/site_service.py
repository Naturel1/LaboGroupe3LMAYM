from app import app, db
from app.models.site import Site


class SiteService:
    def find_all(self):
        """Find all sites."""
        return Site.query.filter_by(active=True).all()

    def find_one(self, site_id):
        """Find one site by id."""
        return Site.query.filter_by(site_id=site_id, active=True).first()

    def insert(self, form):
        """Create a new site."""
        site = Site()
        site.site_name = form.name.data
        site.site_address = form.address.data
        site.site_city = form.city.data
        db.session.add(site)
        db.session.commit()
        return site

    def update(self, site_id, form):
        """Update a site attributes."""
        site = self.find_one(site_id)
        if site is None:
            return None
        site.site_name = form.name.data
        site.site_address = form.address.data
        site.site_city = form.city.data
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