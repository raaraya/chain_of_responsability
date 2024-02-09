from typing import Any, Dict
from regla import Regla

class ReglaBase(Regla):
    '''
    La clase base "ReglaBase" implementa una regla que determinará el comportamiento de todas las reglas.
    Notese la creación de la propiedad "_siguiente" que almacena la referencia a la siguiente regla en la cadena.
    '''
     
    def __init__(self):
        # inicializa la siguiente regla con None (null)
        self._siguiente: Regla = None
   
     
    def set_siguiente(self, siguiente_regla: Regla) -> None:
        # asigna la regla provista como parametro como la siguiente regla en la cadena
        self._siguiente = siguiente_regla


    def validar(self, solicitud: Dict[str, Any]) -> bool:
        if self._siguiente:
            # si la siguiente regla fue asignada, ejecuta el metodo validar de dicha regla
            return self._siguiente.validar(solicitud)
        
        else:
            # en caso contrario retorna True, indicando que todas las validaciones hasta
            # la ultima cadena han sido satisfactorias
            return True
