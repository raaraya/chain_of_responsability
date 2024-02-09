from typing import Any, Dict
from regla_base import ReglaBase


class ValidadorEdadMayor18(ReglaBase):
    
    def validar(self, solicitud: Dict[str, Any]) -> bool:
        if solicitud['edad'] < 18:
            return False
        else:
            return super().validar(solicitud)
            