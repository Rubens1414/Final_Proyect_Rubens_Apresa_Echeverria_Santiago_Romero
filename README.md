# Final_Proyect_Rubens_Apresa_Echeverria_Santiago_Romero


@startuml
class creacion_fritos{
  nombra_tu_frito:str
  tipo_frito:str
  tipo_preparacion:str
  interior_del_frito:str
  Pantalla:pantalla
  mostrar(Pantalla:pantalla):none
}
class salsa{
  tipo_salsa:str
  Pantalla:pantalla
  mostrar(Pantalla:pantalla):none
}

class proceso_pago{
  Nombre:str
  Apellido:str
  Tipo_de_pago:str
  Pantalla:pantalla
  mostrar(Pantalla:pantalla):none
}
class envio {
  nombre_pedido:int
  n_pedido:int
  Direccion:str
  Telefono:int
  precio_pedido:int
  cancelar:none
  Pantalla:pantalla
  mostrar(Pantalla:pantalla):none
  
}

class recomendacion {
  mostra_recomendacion_frito:str
  Nombres_fritos_recomendados:str
  Pantalla:pantalla
  mostrar(Pantalla:pantalla):none
}

class pantalla{
  creacion_fritos:List[creacion_fritos]
  envio: List[envio] 
  recomendacion:List[recomendacion] 
  
}
envio *-- proceso_pago: enviar
recomendacion <|-- creacion_fritos:se agrega a recomendaciones
proceso_pago o-- creacion_fritos: Pagar
pantalla o-- creacion_fritos:mostrar
pantalla o-- recomendacion:mostrar
pantalla o-- envio
creacion_fritos <|-- salsa

@enduml
