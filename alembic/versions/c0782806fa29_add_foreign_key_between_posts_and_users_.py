"""add foreign key between posts and users table

Revision ID: c0782806fa29
Revises: 61b4adb846c4
Create Date: 2024-02-18 05:49:54.314507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0782806fa29'
down_revision: Union[str, None] = '61b4adb846c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts1', sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',       # Constraint name
        source_table='posts1',                  # Table name
        referent_table='users1',                 # Referenced table name
        local_cols=['owner_id'],                # Local column(s)
        remote_cols=['id'],                     # Referenced column(s)
        ondelete='CASCADE'
    )
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts1')
    op.drop_column('posts1', 'owner_id')

    pass
