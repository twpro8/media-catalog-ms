"""add seasons table

Revision ID: 1afe96a2f737
Revises: 58503fbe0be7
Create Date: 2025-11-25 21:51:20.027284

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1afe96a2f737"
down_revision: Union[str, Sequence[str], None] = "58503fbe0be7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "seasons",
        sa.Column("show_id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("season_number", sa.Integer(), nullable=False),
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
        sa.ForeignKeyConstraint(["show_id"], ["shows.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id_"),
        sa.UniqueConstraint("show_id", "season_number", name="uq_season"),
    )
    op.execute(
        sa.text("""
    CREATE TRIGGER update_seasons_updated_at
    BEFORE UPDATE ON seasons
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS update_seasons_updated_at ON seasons;")
    op.drop_table("seasons")
