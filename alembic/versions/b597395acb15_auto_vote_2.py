"""auto-vote 2

Revision ID: b597395acb15
Revises: 104c355d0fac
Create Date: 2024-02-18 06:44:50.617893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b597395acb15'
down_revision: Union[str, None] = '104c355d0fac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts1.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users1.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    op.alter_column('posts1', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts1', 'content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts1', 'author',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts1', 'publisher',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts1', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts1', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('posts1', 'publisher',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts1', 'author',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts1', 'content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts1', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_table('votes')
    # ### end Alembic commands ###
