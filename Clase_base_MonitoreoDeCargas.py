class MonitoreoDeCargas:
    # Clase base que centraliza los atributos y configuraciones iniciales
    def __init__(self):
        print("=== Sistema de Monitoreo de Cargas Iniciado ===")
        self.interruptores_disparados = {1223, 2344, 2345, 1212, 1231}


class NivelesVoltaje(MonitoreoDeCargas):
    # Clase hija encargada exclusivamente del registro de voltajes
    def registrar_niveles(self):
        niveles_voltaje = []
        print("\n--- Registro de niveles de voltajes ---")
        for i in range(2):
            filas = []
            for j in range(2):
                while True:
                    try:
                        valor = int(input(f"Ingrese voltaje para fase y posición [{i + 1}, {j + 1}]: "))
                        filas.append(valor)
                        break
                    except ValueError:
                        print("Error intenete con un número entero válido")
            niveles_voltaje.append(filas)
        
        print("\nMatriz de niveles de voltaje:")
        for fila in niveles_voltaje:
            print(fila)
        
        return niveles_voltaje


class HistorialCorriente(MonitoreoDeCargas):
    # Clase hija encargada del registro del historial de corriente
    def registrar_historial(self):
        print("\n--- Registro de historial de corriente ---") 
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de registros de corriente que desee evaluar: "))
                break
            except ValueError:
                print("Error intente con un número válido")
        
        historial = []
        for i in range(cantidad):
            while True:
                try:
                    valor = int(input(f"Historial de corriente {i + 1}: "))
                    historial.append(valor)
                    break
                except ValueError:
                    print("Error intente con un número válido.")
            
        print("\nHistorial de corriente:")
        print(historial)
        
        return historial


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


class RegistroInterruptores(MonitoreoDeCargas):
    # Clase hija encargada del control de interruptores disparados
    def registrar_interruptor(self):
        print("\n--- Registro de interruptores disparados ----")
        while True:
            try:
                codigo = int(input("Ingrese el código del interruptor de protección disparado: "))
                break
            except ValueError:
                print("Error intente con un código numérico válido")
        
        if codigo in self.interruptores_disparados:
            print(f"El interruptor {codigo} ya se encontraba registrado")
        else:
            self.interruptores_disparados.add(codigo)
            print(f"Interruptor {codigo} registrado con exito")
            
        print(f"Conjunto de interruptores disparados actuales: {self.interruptores_disparados}")


class ConsumoEnergetico(MonitoreoDeCargas):                     
    def Lecturas_de_Consumo_de_Cargas(self):       
        while True:
            try:
                Cantidad_Consumo = int(input("Ingrese la cantidad de consumo de diferentes zonas: "))    
                break
            except ValueError:
                print("Error intente con un número válido")
                
        Consumo_energetico = []
        for i in range(Cantidad_Consumo):
            while True:
                try:
                    energia = int(input(f"Consumo de energía de la zona [{i + 1}]:  amp"))    
                    Consumo_energetico.append(energia)
                    break
                except ValueError:
                    print("Error vuelva intentarlo con un número válido.")
        return Consumo_energetico
                
    def Organizador_de_RCE(self, cargas):
        n = len(cargas)
        cargas_copia = list(cargas) 
        for i in range(n):
            intercambiado = False
            for j in range(0, n - i - 1):
                if cargas_copia[j] < cargas_copia[j + 1]:
                    cargas_copia[j], cargas_copia[j + 1] = cargas_copia[j + 1], cargas_copia[j]
                    intercambiado = True
            if not intercambiado:
                break         
        return cargas_copia

    def buscar_picos_sobrecarga(self, cargas, limite):
        print(f"\n--- Búsqueda lineal de picos de sobrecarga sobre el límite > {limite}) ---")
        picos_criticos = []
        for i in range(len(cargas)):
            if cargas[i] > limite:
                picos_criticos.append((i + 1, cargas[i]))
        
        if picos_criticos:
            for zona, valor in picos_criticos:
                print(f"¡Advertencia! pico de sobrecarga crítico detectado en la Zona {zona} con {valor} Amp.")
        else:
            print("No se registraron picos de sobrecarga críticos que superen el límite")
        return picos_criticos


class PersistenciaSistema(MonitoreoDeCargas):
    # Clase hija encargada del almacenamiento persistente I/O y Manejo de Excepciones
    def guardar_datos(self, niveles_voltaje, historial_corriente, interruptores, consumo_ordenado):
        print("\n--- Guardando datos en archivos de texto ---")
        
        try:
            with open("bitacora_interruptores.txt", "w", encoding="utf-8") as f:
                f.write("===== Bitácora de interruptores disparados =====\n")
                for codigo in interruptores:
                    f.write(f"Interruptor código: {codigo}\n")
            
            with open("estado_subestacion.txt", "w", encoding="utf-8") as f:
                f.write("===== Matriz de niveles de voltajes =====\n")
                if niveles_voltaje:
                    for fila in niveles_voltaje:
                        f.write(f"{fila}\n")
                else:
                    f.write("Sin registros de voltaje\n")
                
                f.write("\n===== Historial de corriente =====\n")
                f.write(f"{historial_corriente}\n")
                
                f.write("\n===== Registro de consumo de energía (RCE) =====\n")
                f.write(f"{consumo_ordenado}\n")
                
            print("Archivos bitacora_interruptores.txt y estado_subestacion.txt guardados con éxito")
            
        except IOError as e:
            print(f"Error al guardar los archivos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


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