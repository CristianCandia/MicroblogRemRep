from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
permiso_rol = Table('permiso_rol', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_rol', Integer),
    Column('id_permiso', Integer),
)

rol_usuario = Table('rol_usuario', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_usuario', Integer),
    Column('id_rol', Integer),
)

rol = Table('rol', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=64)),
    Column('descripcion', String(length=120)),
    Column('id_proyecto', Integer),
    Column('id_fase', Integer),
)

user2 = Table('user2', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('passWord', String),
    Column('role', SmallInteger),
)

user2 = Table('user2', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('passWord', String(length=120)),
    Column('nombre', String(length=64)),
    Column('apellido', String(length=64)),
    Column('telefono', String(length=15)),
    Column('ci', String(length=15)),
    Column('e_mail', String(length=15)),
)

fase = Table('fase', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nombre', String(length=64)),
    Column('posicion', Integer),
    Column('descripcion', String(length=120)),
    Column('cantidadItems', Integer),
    Column('cantidadLB', Integer),
    Column('estado', String(length=64)),
    Column('id_proyecto', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permiso_rol'].create()
    post_meta.tables['rol_usuario'].create()
    post_meta.tables['rol'].columns['id_fase'].create()
    post_meta.tables['rol'].columns['id_proyecto'].create()
    pre_meta.tables['user2'].columns['role'].drop()
    post_meta.tables['user2'].columns['apellido'].create()
    post_meta.tables['user2'].columns['ci'].create()
    post_meta.tables['user2'].columns['e_mail'].create()
    post_meta.tables['user2'].columns['nombre'].create()
    post_meta.tables['user2'].columns['telefono'].create()
    post_meta.tables['fase'].columns['id_proyecto'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permiso_rol'].drop()
    post_meta.tables['rol_usuario'].drop()
    post_meta.tables['rol'].columns['id_fase'].drop()
    post_meta.tables['rol'].columns['id_proyecto'].drop()
    pre_meta.tables['user2'].columns['role'].create()
    post_meta.tables['user2'].columns['apellido'].drop()
    post_meta.tables['user2'].columns['ci'].drop()
    post_meta.tables['user2'].columns['e_mail'].drop()
    post_meta.tables['user2'].columns['nombre'].drop()
    post_meta.tables['user2'].columns['telefono'].drop()
    post_meta.tables['fase'].columns['id_proyecto'].drop()
