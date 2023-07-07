"""create address_id to users

Revision ID: e4b449a69902
Revises: ea33f1afc293
Create Date: 2023-07-07 19:24:27.569713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4b449a69902'
down_revision = 'ea33f1afc293'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column(
        'address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
