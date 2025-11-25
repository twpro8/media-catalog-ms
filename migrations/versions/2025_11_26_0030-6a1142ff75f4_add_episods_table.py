"""add episodes table

Revision ID: 6a1142ff75f4
Revises: 1afe96a2f737
Create Date: 2025-11-26 00:30:04.462967

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6a1142ff75f4"
down_revision: Union[str, Sequence[str], None] = "1afe96a2f737"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "episodes",
        sa.Column("show_id", sa.UUID(), nullable=False),
        sa.Column("season_id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("episode_number", sa.Integer(), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=True),
        sa.Column("release_date", sa.Date(), nullable=False),
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
        sa.ForeignKeyConstraint(["season_id"], ["seasons.id_"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["show_id"], ["shows.id_"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id_"),
        sa.UniqueConstraint("season_id", "episode_number", name="uq_episode"),
    )
    op.execute(
        sa.text("""
    CREATE TRIGGER update_episodes_updated_at
    BEFORE UPDATE ON episodes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS update_episodes_updated_at ON episodes;")
    op.drop_table("episodes")
