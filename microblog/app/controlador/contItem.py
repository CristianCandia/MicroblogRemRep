"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""
"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""

from app.modelo import Item, TipoItem
from app import db

class ControllerItem():
    
    def regItem(self, **kwargsItem):
        """
            Metodo que registra un nuevo item
            @param kwargsItem: Recibe todos los datos para crear un nuevo item
            @return: Respuesta de confirmacion o de fallo
        """
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
        return Item.query.filter_by(id_fase = id).all()
    
    def getItemAll(self):
        return Item.query.all()
    
    def codigoItem(id_Proyecto, id_Fase, numeroItem):
        cod = ("SS" + str(id_Proyecto) 
               + "_F" + str(id_Fase) + "_I" + str(numeroItem))
        return cod
    

class ControllerTI():
    """
        Controlador de Tipo de Item
    """
    
    def getTIFase(self, id):
        """
            Metodo que devuelve el objeto(s) TI correspondiente a una fase
            @param id: Id de la fase del(los) objeto(s) TI solicitado
            @return: objeto(s) TI de dicha fase
        """
        return TipoItem.query.filter_by(fase_id = id).all()
    
    def getTIAll(self):
        """
            Metodo que devuelve la lista de todos los TI existentes 
            @return: objeto/s TI de dicha fase
        """
        return TipoItem.query.all()
    
    def getTIId(self, id):
        """
            Metodo que retorna el objeto TI por su identificador.
            @param id: Id del TI el cual necesita.
            @return: Objeto TI solicitado.
        """
        return TipoItem.query.filter_by(id_TI = id).all()
    
    def codigoTI(id_Proyecto, id_Fase, numeroItem):
        cod = ("SS" + str(id_Proyecto) + "_F" 
               + str(id_Fase) + "_TI" + str(numeroItem))
        return cod
    
    def regTI(self, TI):
        """
            Metodo que registra un nuevo Tipo de item
            @param TI: Recibe el nuevo Tipo de item
            @return: Respuesta de confirmacion o de fallo
        """
        try:
            db.session.add(TI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'

    def delTI(self, TI):
        """
            Metodo que elimina el tipo de item
            @param TI: Tipo de Itema a eliminar
            @return: Confirmacion o Aborto de la transaccion
        """
        try:
            db.session.delete(TI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'
    
    def modTI(self, TI):
        """
            Metodo que modifica el TI
            @param TI: Objeto de TipoItem a ser modificado
            @return: Confirmacion o aborto de la transaccion
        """
        try:
            db.session.merge(TI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'
    
    