"""add actors and association tables

Revision ID: d9d3d5ab4f9e
Revises: 25066bcef575
Create Date: 2025-11-30 06:46:04.583519

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d9d3d5ab4f9e"
down_revision: Union[str, Sequence[str], None] = "25066bcef575"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "actors",
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
        sa.UniqueConstraint("first_name", "last_name", "birth_date", name="uq_actor"),
    )
    op.create_table(
        "movie_actor_associations",
        sa.Column("movie_id", sa.UUID(), nullable=False),
        sa.Column("actor_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["actor_id"], ["actors.id_"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["movie_id"], ["movies.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("movie_id", "actor_id"),
    )
    op.create_table(
        "show_actor_associations",
        sa.Column("show_id", sa.UUID(), nullable=False),
        sa.Column("actor_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["actor_id"], ["actors.id_"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["show_id"], ["shows.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("show_id", "actor_id"),
    )
    op.execute(
        sa.text("""
    CREATE TRIGGER update_actors_updated_at
    BEFORE UPDATE ON actors
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS update_actors_updated_at ON actors;")
    op.drop_table("show_actor_associations")
    op.drop_table("movie_actor_associations")
    op.drop_table("actors")
