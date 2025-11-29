"""delete show_id field from episodes table

Revision ID: 237fba5935cb
Revises: 6a1142ff75f4
Create Date: 2025-11-29 02:37:57.366717

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "237fba5935cb"
down_revision: Union[str, Sequence[str], None] = "6a1142ff75f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(op.f("episodes_show_id_fkey"), "episodes", type_="foreignkey")
    op.drop_column("episodes", "show_id")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "episodes", sa.Column("show_id", sa.UUID(), autoincrement=False, nullable=False)
    )
    op.create_foreign_key(
        op.f("episodes_show_id_fkey"),
        "episodes",
        "shows",
        ["show_id"],
        ["id_"],
        ondelete="CASCADE",
    )
