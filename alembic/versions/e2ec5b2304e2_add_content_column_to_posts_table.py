"""add content column to posts table

Revision ID: e2ec5b2304e2
Revises: f588f7cf63d0
Create Date: 2024-02-18 05:22:52.133104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2ec5b2304e2'
down_revision: Union[str, None] = 'f588f7cf63d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts1', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts1', 'content')
    pass
