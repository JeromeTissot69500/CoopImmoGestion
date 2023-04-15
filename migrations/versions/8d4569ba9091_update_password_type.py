"""Update password type

Revision ID: 8d4569ba9091
Revises: a6a3f01e4a7b
Create Date: 2023-04-15 09:50:21.137019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d4569ba9091'
down_revision = 'a6a3f01e4a7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=4),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.Float(precision=15, decimal_return_scale=4),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###