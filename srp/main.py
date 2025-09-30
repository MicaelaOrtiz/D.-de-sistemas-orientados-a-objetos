from fuente_datos import FuenteDatos
from procesador_datos import ProcesadorDatos
from generador_reporte import GeneradorReporte
from guardar_reporte import GuardarReporte

if __name__ == "__main__":
    fuente = FuenteDatos()
    procesador = ProcesadorDatos()
    generador = GeneradorReporte()
    guardador = GuardarReporte()

    datos = fuente.obtener()
    resultado = procesador.calcular_promedio(datos)
    reporte = generador.generar_texto(resultado)
    guardador.guardar_en_archivo(reporte)

