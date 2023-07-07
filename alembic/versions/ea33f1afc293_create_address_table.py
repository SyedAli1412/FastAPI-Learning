"""Create address table

Revision ID: ea33f1afc293
Revises: f2c550b08be1
Create Date: 2023-07-07 19:18:58.374365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea33f1afc293'
down_revision = 'f2c550b08be1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('address')
