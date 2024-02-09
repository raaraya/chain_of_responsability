from typing import Any, Dict
from regla_base import ReglaBase


class ValidadorId(ReglaBase):
    
    # Override el metodo "validar" de la clase base para realizar su propia validacion
    def validar(self, solicitud: Dict[str, Any]) -> bool:
        '''
            Si la solicitud no posee un campo "id", retorna False indicando que la solicitud no es valida
            sino, retorna el resultado de la validación de la siguiente cadena
        '''        
        
        if 'id' not in solicitud:
            return False
        else:
            return super().validar(solicitud)
            