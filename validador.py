# importamos el protocolo, esto no es requerido per se, solo es para especificar el typing
from typing import List
from regla import Regla

# importamos las reglas que hemos implementado
from reglas.validador_id import ValidadorId
from reglas.validador_edad import ValidadorEdad
from reglas.validador_edad_mayor_18 import ValidadorEdadMayor18


json_solicitud = {
	"id": "a6a77710-cd45-4b40-92c3-3589ebf727a6",
	"nombre": "Ria Benton",
	"pais_origen": "Seyabar",
    "edad": 18
}

# inicializa las reglas

# la cadena debería de verse conceptualmente de la siguiente manera:
# validador_id -> validador_edad -> validador_edad_mayor_18

reglas: List[Regla] = [
    ValidadorId(),
    ValidadorEdad(),
    ValidadorEdadMayor18()
]

# recorre la lista de reglas encadenandolas entre ellas, 
# ignorando la ultima regla en la cadena
for index, regla in enumerate(reglas):
    if index == len(reglas)-1:
        break
    
    regla.set_siguiente(reglas[index+1])
    


if __name__ == '__main__':

    # basta con iniciar la primera validación para iniciar todas las validaciones
    solicitud_es_valida = reglas[0].validar(json_solicitud)
    
    if solicitud_es_valida:
        print('Solicitud Valida')
    else:
        print('Solicitud No Valida')
