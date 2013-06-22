from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
comite = Table('comite', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=64)),
    Column('cant_miembros', Integer),
    Column('id_proyecto', Integer),
)

solicitud = Table('solicitud', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=64)),
    Column('impacto_total', String(length=50)),
    Column('costo_total', Integer),
    Column('estado', String(length=50)),
    Column('id_comite', Integer),
    Column('id_usuario', Integer),
    Column('cantidad_votos', Integer),
)

usr_comite = Table('usr_comite', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_comite', Integer),
    Column('id_usr', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comite'].create()
    post_meta.tables['solicitud'].create()
    post_meta.tables['usr_comite'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comite'].drop()
    post_meta.tables['solicitud'].drop()
    post_meta.tables['usr_comite'].drop()
