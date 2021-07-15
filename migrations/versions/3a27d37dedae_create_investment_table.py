"""create investment table

Revision ID: 3a27d37dedae
Revises: 37013825f347
Create Date: 2021-07-15 00:22:33.371345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a27d37dedae'
down_revision = '37013825f347'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chart_dummy',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.Column('value', sa.BigInteger(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chart_dummy')
    # ### end Alembic commands ###
