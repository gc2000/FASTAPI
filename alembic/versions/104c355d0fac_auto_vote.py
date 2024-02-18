"""auto-vote

Revision ID: 104c355d0fac
Revises: de2b9e9a4c08
Create Date: 2024-02-18 06:34:02.510683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '104c355d0fac'
down_revision: Union[str, None] = 'de2b9e9a4c08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
