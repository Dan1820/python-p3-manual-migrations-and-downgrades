"""Renaming grade to marks

Revision ID: 563085454760
Revises: 72c78a1eb7f6
Create Date: 2023-06-05 10:35:14.306111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563085454760'
down_revision = '72c78a1eb7f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('student') as batch_op:
        batch_op.alter_column('grade', new_column_name='marks')


def downgrade() -> None:
    pass
