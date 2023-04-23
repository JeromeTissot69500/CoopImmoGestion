"""Add Payment and SecurityDeposit table  in database V3

Revision ID: 1d683921c231
Revises: 82240e029c4f
Create Date: 2023-04-22 12:45:11.342421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d683921c231'
down_revision = '82240e029c4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SecurityDeposit',
    sa.Column('security_deposit_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['payment_id'], ['Payment.payment_id'], ),
    sa.PrimaryKeyConstraint('security_deposit_id')
    )
    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=4),
               existing_nullable=False)

    with op.batch_alter_table('Payment', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
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

    with op.batch_alter_table('Payment', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.Float(precision=15, decimal_return_scale=4),
               type_=sa.REAL(),
               existing_nullable=False)

    op.drop_table('SecurityDeposit')
    # ### end Alembic commands ###