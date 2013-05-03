from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
proyecto = Table('proyecto', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=64)),
    Column('descripcion', String(length=120), nullable=False),
    Column('fecha_de_creacion', Date),
    Column('complejidad_total', Integer),
    Column('estado', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['proyecto'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['proyecto'].drop()
