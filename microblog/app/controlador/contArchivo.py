"""
    Sigma_System
    @organization:CRF_Proyect
    @authors:
        - U{Cristian Candia<mailto:kandia88@gmail.com>}
        - U{Ruth Centurion<mailto:ruthiccr@gmail.com>}
        - U{Fernando Saucedo<mailto:carlifer.fernando@gmail.com>}
"""
from app.modelo import AtributoPorTI, AtributoPorItem
from app import db

class ControllerAtributo():
    pass

class ControllerAtributoTI():
    
    def regAtributoTI(self, atributoTI):
        """
            Metodo que registra un nuevo Atibuto de un Tipo de item
            @param atributoTI: Recibe el nuevo Tipo de item
            @return: Respuesta de confirmacion o de fallo
        """
        try:
            db.session.add(atributoTI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'
    
    def getAtributoTIId(self, id_TI):
        """
            Metodo para obtener una lista de todos los atributos del TI
            @param id_TI: Id del Tipo de Item que solicita sus atributos
            @return: Lista de Atributos asociados al Id del parametro
        """
        return AtributoPorTI.query.filter_by(id_TI = id_TI).all()
    
    def getAtributoTIIdA(self, id_atr):
        """
            Metodo que retorna un atributo de un TI
            @param id_atr: Id del atributo.
            @return: Objeto atributo.
        """
        return AtributoPorTI.query.filter_by(id_Atrib_TI = id_atr).all()
    
    def modAtributoTI(self, atributoTI):
        """
            Metodo para actualizar un atributo existente en un TI
            @param atributoTI: Atributo actualizado
            @return: Confirmacion o Aborto de la transaccion.
        """
        try:
            db.session.merge(atributoTI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'
    
    def delAtributoTI(self, atributoTI):
        """
            Metodo para eliminar un atributo de un tipo de item.
            @param atributoTI: Atributo a eliminar.
            @return: Confirmacion o Aborto de la transaccion.
        """
        try:
            db.session.delete(atributoTI)
            db.session.commit()
        except Exception, error:
            db.session.rollback()
            return str(error)
        return 'Exito'