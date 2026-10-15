from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas

class AdministracionEquipos(MonitoreoDeCargas):
    # Clase hija encargada de la administración y parámetros de equipos 
    def mostrar_parametros(self):
        print("\n--- Administración y parámetros de equipos ---")
        parametro_equipos = {
            "Transformador_#1": {"VoltajeNominal": 13200, "CapacidadMax": 500},
            "Transformador_#2": {"VoltajeNominal": 13200, "CapacidadMax": 450},    
            "Transformador_#3": {"VoltajeNominal": 13200, "CapacidadMax": 350},
            "Transformador_#4": {"VoltajeNominal": 13200, "CapacidadMax": 780},
            "Celda_C1": {"VoltajeNominal": 415, "CapacidadMax": 200}
        }  

        opcion = 0
        while opcion != 7:
            try:
                opcion = int(input("""\nSeleccione una de las opciones:
1. Mostrar "Transformador_#1"
2. Mostrar "Transformador_#2"
3. Mostrar "Transformador_#3"
4. Mostrar "Transformador_#4"
5. Mostrar "Celda_C1"
6. Mostrar todos los parámetros
7. Regresar al menú principal
Opción: """))
            except ValueError:
                print("Error introduce un número válido")
                continue

            if opcion in [1, 2, 3, 4, 5]:
                claves = list(parametro_equipos.keys())
                equipo_seleccionado = claves[opcion - 1]
                datos = parametro_equipos[equipo_seleccionado]
                print(f"\nEquipo: {equipo_seleccionado} Voltaje Nominal: {datos['VoltajeNominal']}V  Capacidad Máx: {datos['CapacidadMax']}A")
            elif opcion == 6:
                print("\n--- Todos los equipos ---")
                for equipo, datos in parametro_equipos.items():
                    print(f"Equipo: {equipo} Voltaje Nominal: {datos['VoltajeNominal']}V Capacidad Máx: {datos['CapacidadMax']} A")  
            elif opcion == 7:
                print("\nSaliendo del menú de administración")
            else:
                print("\nOpción no registrada intente con un número del 1 al 7.")

        return parametro_equipos
