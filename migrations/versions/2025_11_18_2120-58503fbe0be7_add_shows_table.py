"""add shows table

Revision ID: 58503fbe0be7
Revises: 4606c3245ada
Create Date: 2025-11-18 21:20:57.154470

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58503fbe0be7"
down_revision: Union[str, Sequence[str], None] = "4606c3245ada"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "shows",
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.String(length=1024), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=False),
        sa.Column("rating", sa.DECIMAL(precision=3, scale=1), nullable=False),
        sa.Column("id_", sa.UUID(), server_default=sa.text("uuidv7()"), nullable=False),
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
        sa.CheckConstraint("rating >= 0 AND rating <= 10"),
        sa.PrimaryKeyConstraint("id_"),
        sa.UniqueConstraint("title", "release_date", name="uq_show"),
    )
    op.execute(
        sa.text("""
    CREATE TRIGGER update_shows_updated_at
    BEFORE UPDATE ON shows
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS update_shows_updated_at ON shows;")
    op.drop_table("shows")
