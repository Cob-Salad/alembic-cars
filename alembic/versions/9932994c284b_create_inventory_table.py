"""create inventory table

Revision ID: 9932994c284b
Revises: 195fda579e80
Create Date: 2024-04-25 11:25:57.274155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9932994c284b'
down_revision: str | None = '195fda579e80'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("inventory", 
                        sa.Column("car_id", sa.Integer, sa. sa.ForeignKey("cars.id")),
                        sa.Column("dealer_id", sa.Integer, sa.ForeignKey("dealerships.id")),
                        sa.Column("cost", sa.Float),
                        sa.Column("is_sold", sa.Boolean),
                        sa.PrimaryKeyConstraint("car_id", "dealer_id", name="inventory_id")
                    )


def downgrade() -> None:
    op.drop_table("inventory")
