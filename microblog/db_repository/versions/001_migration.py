from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
<<<<<<< HEAD
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
=======
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
>>>>>>> branch 'master' of ssh://git@github.com/CristianCandia/MicroblogRemRep.git
