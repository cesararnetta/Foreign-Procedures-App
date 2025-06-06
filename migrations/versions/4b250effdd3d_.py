"""empty message

Revision ID: 4b250effdd3d
Revises: 53063402f5e9
Create Date: 2025-06-01 20:47:00.576735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b250effdd3d'
down_revision = '53063402f5e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('follow_up', schema=None) as batch_op:
        batch_op.add_column(sa.Column('documentation', sa.String(length=2038), nullable=True))
        batch_op.add_column(sa.Column('description', sa.String(length=2038), nullable=True))
        batch_op.drop_column('descripcion')
        batch_op.drop_column('documentacion')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('follow_up', schema=None) as batch_op:
        batch_op.add_column(sa.Column('documentacion', sa.VARCHAR(length=2038), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('descripcion', sa.VARCHAR(length=2038), autoincrement=False, nullable=True))
        batch_op.drop_column('description')
        batch_op.drop_column('documentation')

    # ### end Alembic commands ###
