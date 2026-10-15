from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas



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
