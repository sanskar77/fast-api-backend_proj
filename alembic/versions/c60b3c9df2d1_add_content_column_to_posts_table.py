"""add content column to posts table

Revision ID: c60b3c9df2d1
Revises: 667158f63feb
Create Date: 2024-07-22 23:28:41.387512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c60b3c9df2d1'
down_revision: Union[str, None] = '667158f63feb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
