"""demo data

Revision ID: a3b1c9d4e6f7
Revises: 76c56ea45e73
Create Date: 2026-08-12 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import os


def _is_production_env() -> bool:
    return os.getenv('DEBUG', '').lower() not in ('True', 'true', '1', 'Yes', 'yes')


# revision identifiers, used by Alembic.
revision = 'a3b1c9d4e6f7'
down_revision = '76c56ea45e73'
branch_labels = None
depends_on = None


def upgrade():
    if _is_production_env():
        print('Skipping demo data insertion in production environment.')
        return

    bind = op.get_bind()
    conn = bind

    # Insert roles
    roles = ['demo_admin', 'demo_technician', 'demo_client']
    for r in roles:
        res = conn.execute(sa.text("SELECT role_id FROM roles WHERE role_name = :name"), {'name': r}).fetchone()
        if not res:
            conn.execute(sa.text("INSERT INTO roles (role_name, created_at, active) VALUES (:name, now(), true)"), {'name': r})

    # Insert admin
    admin = [('DEMO_ADMIN', 'Fabien', 'Pinckaers', 'admin@example.com', '1234')]
    for username, first, last, email, pwd in admin:
        res = conn.execute(sa.text("SELECT user_id FROM users WHERE user_email = :email"), {'email': email}).fetchone()
        if not res:
            conn.execute(sa.text(
                """
                INSERT INTO users (user_username, user_firstname, user_lastname, user_email, user_password, created_at, active)
                VALUES (:username, :first, :last, :email, :pwd, now(), true)
                """),
                {'username': username, 'first': first, 'last': last, 'email': email, 'pwd': pwd}
            )

    # Insert Technician
    technician = [('DEMO_TECH', 'John', 'Doe', 'tech@example.com', '1234')]
    for username, first, last, email, pwd in technician:
        res = conn.execute(sa.text("SELECT user_id FROM users WHERE user_email = :email"), {'email': email}).fetchone()
        if not res:
            conn.execute(sa.text(
                """
                INSERT INTO users (user_username, user_firstname, user_lastname, user_email, user_password, created_at, active)
                VALUES (:username, :first, :last, :email, :pwd, now(), true)
                """),
                {'username': username, 'first': first, 'last': last, 'email': email, 'pwd': pwd}
            )

    # Insert Client
    client = [('DEMO_CLIENT', 'Alice', 'Smith', 'client@example.com', '1234')]
    for username, first, last, email, pwd in client:
        res = conn.execute(sa.text("SELECT user_id FROM users WHERE user_email = :email"), {'email': email}).fetchone()
        if not res:
            conn.execute(sa.text(
                """
                INSERT INTO users (user_username, user_firstname, user_lastname, user_email, user_password, created_at, active)
                VALUES (:username, :first, :last, :email, :pwd, now(), true)
                """),
                {'username': username, 'first': first, 'last': last, 'email': email, 'pwd': pwd}
            )

    # Insert sites
    sites = [
        ('Odoo Farm 1', 'Chaussée de Namur 40', 'Ramillies'),
        ('Odoo Farm 2', 'Rue des Bourlottes 9', 'Ramillies'),
        ('Odoo LLN', 'Rue du Laid Burniat 5', 'Ottignies-LLN'),
    ]
    for site_name, site_address, site_city in sites:
        res = conn.execute(sa.text("SELECT site_id FROM sites WHERE site_name = :name"), {'name': site_name}).fetchone()
        if not res:
            conn.execute(sa.text("INSERT INTO sites (site_name, site_address, site_city, created_at, active) VALUES (:name, :addr, :city, now(), true)"), {'name': site_name, 'addr': site_address, 'city': site_city})

    # Insert team
    team_name = [('DEMO_Team', 'Team for demo')]
    for name, desc in team_name:
        res = conn.execute(sa.text("SELECT team_id FROM teams WHERE team_name = :name"), {'name': name}).fetchone()
        if not res:
            conn.execute(sa.text("INSERT INTO teams (team_name, team_description, created_at, active) VALUES (:name, :desc, now(), true)"), {'name': name, 'desc': desc})

    # Insert categories
    categories = [
        ('DEMO_Hardware', 'Hardware related issues'),
        ('DEMO_Software', 'Software related issues'),
        ('DEMO_Network', 'Network related issues'),
    ]
    for name, desc in categories:
        res = conn.execute(sa.text("SELECT category_id FROM categories WHERE category_name = :name"), {'name': name}).fetchone()
        if not res:
            conn.execute(sa.text("INSERT INTO categories (category_name, category_description, created_at, active) VALUES (:name, :desc, now(), true)"), {'name': name, 'desc': desc})

    # Insert priorities
    priorities = [
        ('DEMO_Low', 1, 72),
        ('DEMO_Medium', 2, 24),
        ('DEMO_High', 3, 4),
    ]
    for name, level, delay in priorities:
        res = conn.execute(sa.text("SELECT priority_id FROM priorities WHERE priority_name = :name"), {'name': name}).fetchone()
        if not res:
            conn.execute(sa.text("INSERT INTO priorities (priority_name, priority_level, priority_delay_hours, created_at, active) VALUES (:name, :level, :delay, now(), true)"), {'name': name, 'level': level, 'delay': delay})

def downgrade():
    if _is_production_env():
        print('Skipping demo data cleanup in production environment.')
        return

    bind = op.get_bind()
    conn = bind

    # Remove role from admin
    user = conn.execute(sa.text("SELECT user_id FROM users WHERE user_username = :username"), {'username': 'DEMO_ADMIN'}).fetchone()
    if user:
        conn.execute(sa.text('DELETE FROM user_roles WHERE "UserRole_user_id" = :uid'), {'uid': user[0]})
    # Remove admin
    conn.execute(sa.text("DELETE FROM users WHERE user_username = :username"), {'username': 'DEMO_ADMIN'})

    # Remove role from technician
    user = conn.execute(sa.text("SELECT user_id FROM users WHERE user_username = :username"), {'username': 'DEMO_TECH'}).fetchone()
    if user:
        conn.execute(sa.text('DELETE FROM user_roles WHERE "UserRole_user_id" = :uid'), {'uid': user[0]})
    # Remove technician
    conn.execute(sa.text("DELETE FROM users WHERE user_username = :username"), {'username': 'DEMO_TECH'})

    # Remove role from client
    user = conn.execute(sa.text("SELECT user_id FROM users WHERE user_username = :username"), {'username': 'DEMO_CLIENT'}).fetchone()
    if user:
        conn.execute(sa.text('DELETE FROM user_roles WHERE "UserRole_user_id" = :uid'), {'uid': user[0]})
    # Remove client
    conn.execute(sa.text("DELETE FROM users WHERE user_username = :username"), {'username': 'DEMO_CLIENT'})

    # Remove roles only if no users reference them
    role_names = ['demo_admin', 'demo_technician', 'demo_client']
    for r in role_names:
        conn.execute(sa.text(
            'DELETE FROM roles WHERE role_name = :name AND NOT EXISTS (SELECT 1 FROM user_roles ur WHERE ur."UserRole_role_id" = roles.role_id)'
        ), {'name': r})

    # Remove demo priorities only if no tickets reference them
    priority_names = ['DEMO_Low', 'DEMO_Medium', 'DEMO_High']
    for p in priority_names:
        conn.execute(sa.text(
            "DELETE FROM priorities WHERE priority_name = :name AND NOT EXISTS (SELECT 1 FROM tickets t WHERE t.ticket_priority_id = priorities.priority_id)"
        ), {'name': p})

    # Remove demo categories only if no tickets reference them
    category_names = ['DEMO_Hardware', 'DEMO_Software', 'DEMO_Network']
    for c in category_names:
        conn.execute(sa.text(
            "DELETE FROM categories WHERE category_name = :name AND NOT EXISTS (SELECT 1 FROM tickets t WHERE t.ticket_category_id = categories.category_id)"
        ), {'name': c})

    # Remove demo team if no users attached
    conn.execute(sa.text(
        "DELETE FROM teams WHERE team_name = :name AND NOT EXISTS (SELECT 1 FROM users u WHERE u.user_team_id = teams.team_id)"
    ), {'name': 'DEMO_Team'})

    # Remove demo sites if no users attached
    sites = ['Odoo Farm 1', 'Odoo Farm 2', 'Odoo LLN']
    for s in sites:
        conn.execute(sa.text(
            "DELETE FROM sites WHERE site_name = :name AND NOT EXISTS (SELECT 1 FROM users u WHERE u.user_site_id = sites.site_id)"
        ), {'name': s})