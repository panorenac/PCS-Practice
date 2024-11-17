import random
import time
import matplotlib.pyplot as plt

from Hospital import imprimirHospital
from Paciente import imprimirPaciente
from Recepcionita import imprimirRecepcionista
from RelojInteligente import imprimirRelojInteligente

# Condiciones iniciales y parámetros globales
TIEMPO_SIMULACION = 72  # Horas
UMBRAL = 0.7  # Probabilidad en el rango [0 - 1]

# Variables globales
TIEMPO = 0  # Horas
MARCA_TIEMPO = "Siga"  # Puede ser "Siga" o "Pare"
ESTADOSENSOR_RITMOCARDIACO = "Activo"  # Activo o Inactivo
PROMEDIO_RITMOCARDIACO = 0
TASA_RIESGOFRAGILIDAD = 0


def PACIENTE_LLEGA():
    """Determina si un paciente llega basándose en un valor aleatorio."""
    global ALEATORIO, OCURRENCIA

    if 0 < TIEMPO <= TIEMPO_SIMULACION:
        ALEATORIO = random.random()
        OCURRENCIA = "Activa" if ALEATORIO >= UMBRAL else "Inactiva"
        print(f"[Evento PACIENTE_LLEGA] Ocurrencia: {OCURRENCIA}, Aleatorio: {ALEATORIO:.2f}")


def TIEMPO_PASA():
    """Controla el avance del tiempo dentro de la simulación."""
    global TIEMPO, MARCA_TIEMPO

    if TIEMPO <= TIEMPO_SIMULACION:
        if MARCA_TIEMPO == "Siga":
            TIEMPO += 1
            MARCA_TIEMPO = "Pare"
            print(f"[Evento TIEMPO_PASA] Tiempo actual: {TIEMPO} horas")
        else:
            print(f"[TIEMPO_PASA] Esperando marca de tiempo 'Siga'. Tiempo: {TIEMPO}")

registro_eventos = []

def RITMOCARDIACO_APARECE():
    """Genera y registra un valor de ritmo cardiaco."""
    global PROMEDIO_RITMOCARDIACO, TASA_RIESGOFRAGILIDAD, MARCA_TIEMPO

    if TIEMPO <= TIEMPO_SIMULACION and MARCA_TIEMPO == "Pare" and ESTADOSENSOR_RITMOCARDIACO == "Activo":
        valor = random.randint(50, 120)  # Ritmo aleatorio
        riesgo = "Alto" if valor > 100 else "Bajo"

        # Actualizar métricas
        if TIEMPO > 1:  # Evita dividir por 0
            PROMEDIO_RITMOCARDIACO = ((PROMEDIO_RITMOCARDIACO * (TIEMPO - 1)) + valor) / TIEMPO

        if riesgo == "Alto":
            TASA_RIESGOFRAGILIDAD += 1
        
         # Registrar el evento
        evento = {
            'Tiempo': TIEMPO,
            'Ritmo Cardiaco': valor,
            'Riesgo': riesgo
        }
        registro_eventos.append(evento)

        # Registrar datos
        print(f"[Evento RITMOCARDIACO_APARECE] Tiempo: {TIEMPO} horas, Ritmo: {valor} lpm, Riesgo: {riesgo}")
        print(f"[Estado] Promedio ritmo cardiaco: {PROMEDIO_RITMOCARDIACO:.2f} lpm, Tasa riesgo fragilidad: {TASA_RIESGOFRAGILIDAD}")
        MARCA_TIEMPO = "Siga"
    else:
        print(f"[RITMOCARDIACO_APARECE] No se cumplen las condiciones para generar ritmo cardiaco.")


def main():
    """Controla la ejecución de la simulación."""
    print("Hospitales:")
    imprimirHospital()

    print("Recepcionistas:")
    imprimirRecepcionista()

    print("Relojes Inteligentes:")
    imprimirRelojInteligente()

    print("Pacientes:")
    imprimirPaciente()

    while TIEMPO <= TIEMPO_SIMULACION:
        PACIENTE_LLEGA()
        TIEMPO_PASA()
        RITMOCARDIACO_APARECE()
        print(f"Fin del ciclo para el tiempo {TIEMPO} horas\n")
        time.sleep(0.5)  # Pausa de medio segundo
    
    print("\n--- Resumen de Eventos ---")
    for evento in registro_eventos:
        print(evento)
    print("registro_eventos:", registro_eventos)

  # Simulación terminada, graficar resultados
    tiempos = [evento['Tiempo'] for evento in registro_eventos]
    ritmos = [evento['Ritmo Cardiaco'] for evento in registro_eventos]
    
    # Graficar el ritmo cardiaco a lo largo del tiempo
    plt.plot(tiempos, ritmos, marker='o', label='Ritmo Cardiaco (lpm)')
    plt.title("Ritmo Cardiaco a lo Largo del Tiempo")
    plt.xlabel("Tiempo (horas)")
    plt.ylabel("Ritmo Cardiaco (lpm)")
    plt.grid(True)

    # Si deseas, puedes también graficar la tasa de riesgo de fragilidad
    tasa_riesgo = [evento['Riesgo'] for evento in registro_eventos]
    plt.plot(tiempos, tasa_riesgo, marker='x', linestyle='--', label="Riesgo de Fragilidad")

    plt.legend()
    plt.show()     

if __name__ == "__main__":
    main()