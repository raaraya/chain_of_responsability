from abc import abstractmethod
from typing import Any, Dict, Protocol

class Regla(Protocol):
    '''
    El Protocol "Regla" declara un metodo para crear la cadena de reglas.
    También declara un metodo para validar la solicitud.
    '''

    # Siguiente regla en la cadena
    _siguiente: 'Regla'
    
    @abstractmethod
    def set_siguiente(self, siguiente_regla: 'Regla') -> None:
        ''' Asigna la siguiente regla en la cadena '''
        raise NotImplementedError
    
    
    @abstractmethod
    def validar(self, solicitud: Dict[str, Any]) -> bool:
        ''' Ejecuta la acción de verificación '''
        pass
