"""empty message

Revision ID: 5205c78e66eb
Revises: 151232379d0d
Create Date: 2015-03-12 15:30:08.222331

"""

# revision identifiers, used by Alembic.
revision = '5205c78e66eb'
down_revision = '151232379d0d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('market', sa.String(length=1), nullable=True))
    op.add_column('report', sa.Column('processed_rows', sa.Integer(), nullable=True))
    op.add_column('report', sa.Column('reference_month', sa.Integer(), nullable=True))
    op.add_column('report', sa.Column('reference_year', sa.Integer(), nullable=True))
    op.add_column('report', sa.Column('total_rows', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('report', 'total_rows')
    op.drop_column('report', 'reference_year')
    op.drop_column('report', 'reference_month')
    op.drop_column('report', 'processed_rows')
    op.drop_column('report', 'market')
    ### end Alembic commands ###
