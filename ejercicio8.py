class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print(f"Tarea '{tarea}' no está en la lista.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Tareas pendientes:", self.tareas)
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
lista = ListaDeTareas()
lista.agregar_tarea("Estudiar para el examen")
lista.mostrar_tareas()  # Tareas pendientes: ['Estudiar para el examen']
lista.eliminar_tarea("Estudiar para el examen")
lista.mostrar_tareas()  # No hay tareas pendientes.
