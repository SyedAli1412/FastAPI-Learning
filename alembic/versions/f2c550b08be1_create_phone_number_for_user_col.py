"""create phone number for user  col

Revision ID: f2c550b08be1
Revises: 
Create Date: 2023-07-07 19:10:56.196749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2c550b08be1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column(
        'phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
