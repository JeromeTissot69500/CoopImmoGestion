"""Add Inventory table in database

Revision ID: 912e7b75e025
Revises: 312e9942aa1d
Create Date: 2023-04-20 18:07:40.968238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912e7b75e025'
down_revision = '312e9942aa1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Inventory',
    sa.Column('inventory_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type_inv', sa.String(length=50), nullable=False),
    sa.Column('inventory_date', sa.DateTime(), nullable=False),
    sa.Column('observation', sa.String(length=250), nullable=True),
    sa.Column('rental_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rental_id'], ['Rental.rental_id'], ),
    sa.PrimaryKeyConstraint('inventory_id')
    )
    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=4),
               existing_nullable=False)

    with op.batch_alter_table('Price', schema=None) as batch_op:
        batch_op.alter_column('rent',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('charge',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('security_deposit',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)

    with op.batch_alter_table('Rental', schema=None) as batch_op:
        batch_op.alter_column('rental_balance',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)

    with op.batch_alter_table('Tenant', schema=None) as batch_op:
        batch_op.alter_column('annual_salary',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('balance',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tenant', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('annual_salary',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Rental', schema=None) as batch_op:
        batch_op.alter_column('rental_balance',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Price', schema=None) as batch_op:
        batch_op.alter_column('security_deposit',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('charge',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('rent',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.Float(precision=15, decimal_return_scale=4),
               type_=sa.REAL(),
               existing_nullable=False)

    op.drop_table('Inventory')
    # ### end Alembic commands ###
