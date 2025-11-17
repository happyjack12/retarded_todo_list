"""Changed name to username in table User

Revision ID: b5266ff5b85a
Revises: f5d484e29522
Create Date: 2025-11-17 14:47:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5266ff5b85a'
down_revision = 'f5d484e29522'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('name', new_column_name='username', existing_type=sa.String(length=255))

    op.drop_index('ix_users_name', table_name='users')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    pass


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username', new_column_name='name', existing_type=sa.String(length=255))

    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    pass