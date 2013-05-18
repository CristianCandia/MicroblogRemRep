'''
@note: Clase que define el controlador de Item
@authors:
    - U{Cristian Candia<mailto:kandia88@gmail.com>}
    - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
    - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
'''
from app.modelo import Item
from app import db

class ControllerItem():
    '''
        Metodo que registra un nuevo item
        @param kwargsItem: Recibe todos los datos para crear un nuevo item
    '''
    def regItem(self, **kwargsItem):
        item = Item()
        for k, v in kwargsItem.iteritems():
            if (k == 'descripcion'):
                item.descripcion = v
            if (k == 'id_fase'):
                item.numero = len(Item.query.
                                  filter_by(id_fase = v ).first())
                item.id_fase = v
            if (k == 'complejidad'):
                item.complejidad = v
            if (k == 'prioridad'):
                item.prioridad = v
            if (k == 'estado'):
                item.estado = v
            if (k == 'borrado'):
                item.borrado = v
            if (k == 'observaciones'):
                item.observaciones = v
        item.version = 1
        
        try:
            db.session.add(item)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        
        return 'Exito'
    
    def getItemFase(self, id):
        return Item.query.filter_by(id_fase = id ).first()
    
    def getItemAll(self):
        return Item.query.all()    
    