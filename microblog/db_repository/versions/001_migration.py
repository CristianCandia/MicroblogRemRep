from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
atributo_porTI = Table('atributo_porTI', post_meta,
    Column('id_Atrib_TI', Integer, primary_key=True, nullable=False),
    Column('id_TI', Integer, nullable=False),
    Column('nombre', String(length=64)),
    Column('tipo', String(length=64)),
    Column('valorDefault', String(length=100)),
)

tipo_item = Table('tipo_item', post_meta,
    Column('id_TI', Integer, primary_key=True, nullable=False),
    Column('codigo', String(length=100)),
    Column('descripcion', String(length=100)),
    Column('proyecto_id', NullType),
    Column('fase_id', NullType),
)

item = Table('item', post_meta,
    Column('id_item', Integer, primary_key=True, nullable=False),
    Column('descripcion', String(length=200)),
    Column('numero', Integer),
    Column('num_x_TI', Integer),
    Column('id_TI', Integer),
    Column('id_fase', Integer),
    Column('version', Integer),
    Column('complejidad', Integer),
    Column('prioridad', Integer),
    Column('estado', String(length=64)),
    Column('borrado', Boolean),
    Column('observaciones', String(length=200)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['atributo_porTI'].create()
    post_meta.tables['tipo_item'].create()
    post_meta.tables['item'].columns['id_TI'].create()
    post_meta.tables['item'].columns['num_x_TI'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['atributo_porTI'].drop()
    post_meta.tables['tipo_item'].drop()
    post_meta.tables['item'].columns['id_TI'].drop()
    post_meta.tables['item'].columns['num_x_TI'].drop()
