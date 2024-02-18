"""add user table

Revision ID: 61b4adb846c4
Revises: e2ec5b2304e2
Create Date: 2024-02-18 05:29:49.687558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61b4adb846c4'
down_revision: Union[str, None] = 'e2ec5b2304e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users1',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('email')
    )
        
    pass


def downgrade() -> None:
    op.drop_table('users1')
    pass
