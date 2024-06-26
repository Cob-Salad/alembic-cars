"""create cars table

Revision ID: 40428140b417
Revises: 
Create Date: 2024-04-25 11:08:27.257165

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40428140b417'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("cars", 
                        sa.Column("id", sa.INTEGER, primary_key=True),
                        sa.Column("vin", sa.Text),
                        sa.Column("model", sa.Text),
                        sa.Column("make", sa.Text),
                        sa.Column("engine", sa.Text),
                        sa.Column("year", sa.Integer)
                    )


def downgrade() -> None:
    op.drop_table("cars")
