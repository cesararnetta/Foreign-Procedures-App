"""empty message

Revision ID: c42d2d994b0c
Revises: e9adc51688a0
Create Date: 2025-05-27 16:43:37.760058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c42d2d994b0c'
down_revision = 'e9adc51688a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('errand', schema=None) as batch_op:
        batch_op.alter_column('office_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('offices', schema=None) as batch_op:
        batch_op.add_column(sa.Column('office_name', sa.String(length=250), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('offices', schema=None) as batch_op:
        batch_op.drop_column('office_name')

    with op.batch_alter_table('errand', schema=None) as batch_op:
        batch_op.alter_column('office_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
