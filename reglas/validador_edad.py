from typing import Any, Dict
from regla_base import ReglaBase


class ValidadorEdad(ReglaBase):
    
    def validar(self, solicitud: Dict[str, Any]) -> bool:
        if 'edad' not in solicitud:
            return False
        else:
            return super().validar(solicitud)
            