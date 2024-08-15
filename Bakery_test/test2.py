"""Add Bakery product table

Revision ID: d9dec67e3c57
Revises: 
Create Date: 2024-05-28 12:39:32.213955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9dec67e3c57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=255), nullable=False),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
