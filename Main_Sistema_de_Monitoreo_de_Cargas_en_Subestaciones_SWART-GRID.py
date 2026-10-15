from Clase_Hija_Niveles_Voltajes import NivelesVoltaje
from Clase_Hija_Historial_Corriente import HistorialCorriente
from Clase_Hija_Administracion_Equipos import AdministracionEquipos
from Clase_Hija_Registro_Interruptores import RegistroInterruptores
from Clase_Hija_Consumo_Energetico import ConsumoEnergetico
from Clase_Hija_Persistencia_Sistema import PersistenciaSistema


if __name__ == "__main__":
    print("===== Sistema de Monitoreo de Cargas en Subestaciones SMART GRID =====")
    
    # Instanciamos los objetos necesarios
    voltajes_obj = NivelesVoltaje()
    corriente_obj = HistorialCorriente()
    equipos_obj = AdministracionEquipos()
    interruptores_obj = RegistroInterruptores()
    energia_obj = ConsumoEnergetico()
    persistencia_obj = PersistenciaSistema()

    # Variables1 para almacenar los datos generados durante la ejecución
    matriz_voltajes = []
    lista_corriente = []
    cargas_ordenadas = []

    opcion_principal = 0
    while opcion_principal != 7:
        try:
            opcion_principal = int(input("""
      Menu principal SMART GRID
      
1. Registrar niveles de voltaje 
2. Registrar historial de corriente 
3. Administrar parámetros de equipos 
4. Registrar interruptores disparados
5. Registrar y analizar consumo energético
6. Guardar datos en archivos 
7. Salir del sistema
Seleccione una opción: """))
        except ValueError:
            print("Error intente de nuevo con un número entero válido")
            continue

        if opcion_principal == 1:
            matriz_voltajes = voltajes_obj.registrar_niveles()
        elif opcion_principal == 2:
            lista_corriente = corriente_obj.registrar_historial()
        elif opcion_principal == 3:
            equipos_obj.mostrar_parametros()
        elif opcion_principal == 4:
            interruptores_obj.registrar_interruptor()
        elif opcion_principal == 5:
            cargas_leidas = energia_obj.Lecturas_de_Consumo_de_Cargas()
            cargas_ordenadas = energia_obj.Organizador_de_RCE(cargas_leidas)
            print("\nConsumo energético ordenado de mayor a menor:", cargas_ordenadas)
            while True:
                try:
                    umbral_referencia = int(input("\nIngrese el umbral de consumo para detectar picos críticos: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
            energia_obj.buscar_picos_sobrecarga(cargas_leidas, umbral_referencia)
        elif opcion_principal == 6:
            persistencia_obj.guardar_datos(
                niveles_voltaje=matriz_voltajes,
                historial_corriente=lista_corriente,
                interruptores=interruptores_obj.interruptores_disparados,
                consumo_ordenado=cargas_ordenadas
            )
        elif opcion_principal == 7:
            print("\nSaliendo del sistema de monitoreo de cargas")
        else:
            print("\nOpción no válida intente con un número del 1 al 7.")