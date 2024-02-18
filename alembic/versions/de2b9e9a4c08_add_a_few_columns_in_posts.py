"""add a few columns in posts

Revision ID: de2b9e9a4c08
Revises: c0782806fa29
Create Date: 2024-02-18 06:20:21.134842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de2b9e9a4c08'
down_revision: Union[str, None] = 'c0782806fa29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts1', sa.Column('author', sa.String, nullable=False))
    op.add_column('posts1', sa.Column('publisher', sa.String, nullable=False))
    op.add_column('posts1', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts1', 'author')
    op.drop_column('posts1', 'publisher')
    op.drop_column('posts1', 'created_at')
    pass
