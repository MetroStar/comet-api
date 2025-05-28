# Alembic migrations

## Creating a new Revision

1. To create a revision, run the following:

```sh
alembic revision -m "SOME MESSAGE"
```

2. To specify details of the revision, populate upgrade and downgrade functions in new revision file:

```py
# Add column example
def upgrade() -> None:
  op.add_column('cases', sa.Column('priority', sa.Integer(), nullable=True)

def downgrade() -> None:
  op.drop_column('cases', 'priority')

```

3. To apply the migration, run the following:

```sh
alembic upgrade [REVISION_ID]
```

4. To undo the migration, run the following:

```sh
alembic downgrade -1
```
