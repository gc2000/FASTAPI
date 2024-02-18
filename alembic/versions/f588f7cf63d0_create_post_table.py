"""create post table

Revision ID: f588f7cf63d0
Revises: 
Create Date: 2024-02-17 00:14:53.495072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f588f7cf63d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts1", sa.Column('id', sa.Integer(), nullable=False, 
                    primary_key=True), sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_table("posts1")
    pass
