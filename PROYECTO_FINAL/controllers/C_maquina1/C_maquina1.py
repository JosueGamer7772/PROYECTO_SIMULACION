import math
from controller import Supervisor

# Inicializar como Supervisor para poder manipular objetos del mundo
robot = Supervisor()
TIME_STEP = int(robot.getBasicTimeStep())

# 1. Motores del tractor
motor_names = ['motor_del_izq', 'motor_del_der', 'motor_tra_der', 'motor_tra_izq']
motors = []
for name in motor_names:
    motor = robot.getDevice(name)
    if motor:
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        motors.append(motor)

# 2. Motores de la limpiadora
motor_rotor = robot.getDevice('ROTOR')
if motor_rotor:
    motor_rotor.setPosition(float('inf'))
    motor_rotor.setVelocity(0.0)

motor_llmd = robot.getDevice('LLMD')
if motor_llmd:
    motor_llmd.setPosition(float('inf'))
    motor_llmd.setVelocity(0.0)

motor_llmi = robot.getDevice('LLMI')
if motor_llmi:
    motor_llmi.setPosition(float('inf'))
    motor_llmi.setVelocity(0.0)

# 3. Referencia a la arena (efecto visual)
nodo_arena = robot.getFromDef('NUBE_ARENA')
campo_transparencia = nodo_arena.getField('transparency') if nodo_arena else None

# 4. Referencia al rotor y a la basura en la escena
nodo_rotor = robot.getFromDef('ROTOR_MECANISMO')  # DEF del rotor
nodo_basura = robot.getFromDef('BASURA1')          # DEF del objeto en la playa

field_pos_basura = nodo_basura.getField('translation') if nodo_basura else None
field_pos_rotor = nodo_rotor.getField('translation') if nodo_rotor else None

# Estado para controlar si ya fue recolectada
recolectado = False

target_speed = 10.0

# 5. Bucle principal de simulación
while robot.step(TIME_STEP) != -1:
    # Mover ruedas del tractor
    for motor in motors:
        motor.setVelocity(target_speed)
    
    if motor_llmd:
        motor_llmd.setVelocity(-target_speed)
    if motor_llmi:
        motor_llmi.setVelocity(-target_speed)

    # Activar rotor y animación de arena
    if motor_rotor:
        motor_rotor.setVelocity(target_speed)
        if target_speed > 0 and campo_transparencia:
            variacion = 0.35 + 0.10 * math.sin(robot.getTime() * 12.0)
            campo_transparencia.setSFFloat(variacion)

    # --- LÓGICA DE RECOLECCIÓN DE OBJETOS ---
    if nodo_basura and nodo_rotor and not recolectado:
        # Obtener posiciones 3D actuales [x, y, z]
        pos_basura = field_pos_basura.getSFVec3f()
        pos_rotor = field_pos_rotor.getSFVec3f()

        # Calcular distancia euclidiana entre el rotor y el objeto
        distancia = math.sqrt(
            (pos_basura[0] - pos_rotor[0])**2 +
            (pos_basura[1] - pos_rotor[1])**2 +
            (pos_basura[2] - pos_rotor[2])**2
        )

        # Si el rotor entra en contacto/cercanía (distancia menor a 0.6 metros)
        if distancia < 0.6:
            # Teletransportar el objeto a la tolva superior de la limpiadora
            # (Ajusta estos deltas relative +0.0, +1.2, +0.8 según tu modelo)
            nueva_posicion = [
                pos_rotor[0],          # Alineado en X
                pos_rotor[1] + 1.2,    # Detrás (sobre el depósito)
                pos_rotor[2] + 0.8     # Elevado en Z dentro del contenedor
            ]
            field_pos_basura.setSFVec3f(nueva_posicion)
            recolectado = True
            print("¡Objeto recolectado y transportado al contenedor!")