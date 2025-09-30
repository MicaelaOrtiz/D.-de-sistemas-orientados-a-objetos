class GuardarReporte:
    def guardar_en_archivo(self, reporte, nombre="reporte.txt"):
        with open(nombre, "w") as f:
            f.write(reporte)
