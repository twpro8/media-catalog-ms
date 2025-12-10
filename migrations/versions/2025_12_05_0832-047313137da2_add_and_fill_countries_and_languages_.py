"""add and fill countries and languages tables

Revision ID: 047313137da2
Revises: d9d3d5ab4f9e
Create Date: 2025-12-05 08:32:28.561076

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pycountry

# revision identifiers, used by Alembic.
revision: str = "047313137da2"
down_revision: Union[str, Sequence[str], None] = "d9d3d5ab4f9e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "countries",
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("code"),
    )
    op.create_table(
        "languages",
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("code"),
    )
    countries_table = sa.table(
        "countries",
        sa.column("code", sa.String),
        sa.column("name", sa.String),
        sa.column("active", sa.Boolean),
    )
    languages_table = sa.table(
        "languages",
        sa.column("code", sa.String),
        sa.column("name", sa.String),
        sa.column("active", sa.Boolean),
    )
    countries = [
        {
            "code": country.alpha_2,
            "name": country.name,
            "active": True,
        }
        for country in pycountry.countries
    ]
    op.bulk_insert(countries_table, countries)
    languages = [
        {
            "code": language.alpha_2,
            "name": language.name,
            "active": True,
        }
        for language in pycountry.languages
        if hasattr(language, "alpha_2")
    ]
    op.bulk_insert(languages_table, languages)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("languages")
    op.drop_table("countries")
