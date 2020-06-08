"""Class name should not be unique

Revision ID: 1836b327112d
Revises: 9391156e3fc0
Create Date: 2020-06-01 09:11:06.443196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1836b327112d'
down_revision = '9391156e3fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('classes_name_key', 'classes', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('classes_name_key', 'classes', ['name'])
    # ### end Alembic commands ###