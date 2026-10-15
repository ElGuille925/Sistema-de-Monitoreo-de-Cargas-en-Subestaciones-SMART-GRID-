from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas

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
