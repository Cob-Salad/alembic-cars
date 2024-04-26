"""create dealerships table

Revision ID: 195fda579e80
Revises: 40428140b417
Create Date: 2024-04-25 11:19:14.542952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '195fda579e80'
down_revision: str | None = '40428140b417'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("dealerships", 
                        sa.Column("id", sa.Integer, primary_key=True),
                        sa.Column("name", sa.Text),
                        sa.Column("address", sa.Text),
                        sa.Column("phone_number", sa.Text))


def downgrade() -> None:
    op.drop_table("dealerships")
