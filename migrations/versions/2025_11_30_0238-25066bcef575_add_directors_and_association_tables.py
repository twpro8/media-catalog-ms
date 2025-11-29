"""add directors and association tables

Revision ID: 25066bcef575
Revises: 237fba5935cb
Create Date: 2025-11-30 02:38:13.035026

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "25066bcef575"
down_revision: Union[str, Sequence[str], None] = "237fba5935cb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "directors",
        sa.Column("id_", sa.UUID(), server_default=sa.text("uuidv7()"), nullable=False),
        sa.Column("first_name", sa.String(length=48), nullable=False),
        sa.Column("last_name", sa.String(length=48), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("bio", sa.String(length=1024), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("TIMEZONE('UTC', now())"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("TIMEZONE('UTC', now())"),
            nullable=False,
        ),
        sa.Column("is_deleted", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id_"),
        sa.UniqueConstraint(
            "first_name", "last_name", "birth_date", name="uq_director"
        ),
    )
    op.create_table(
        "movie_director_associations",
        sa.Column("movie_id", sa.UUID(), nullable=False),
        sa.Column("director_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["director_id"], ["directors.id_"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["movie_id"], ["movies.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("movie_id", "director_id"),
    )
    op.create_table(
        "show_director_associations",
        sa.Column("show_id", sa.UUID(), nullable=False),
        sa.Column("director_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["director_id"], ["directors.id_"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["show_id"], ["shows.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("show_id", "director_id"),
    )
    op.execute(
        sa.text("""
    CREATE TRIGGER update_directors_updated_at
    BEFORE UPDATE ON directors
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS update_directors_updated_at ON directors;")
    op.drop_table("show_director_associations")
    op.drop_table("movie_director_associations")
    op.drop_table("directors")
