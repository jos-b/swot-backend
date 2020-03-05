"""Add fullname field

Revision ID: 21cb185c15e6
Revises: 37b1fd641018
Create Date: 2020-03-05 09:24:36.325061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21cb185c15e6'
down_revision = '37b1fd641018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=False)) 
    op.alter_column('users', 'name', new_column_name='username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "full_name")
    op.alter_column('users', 'username', new_column_name="name")
    # ### end Alembic commands ###
