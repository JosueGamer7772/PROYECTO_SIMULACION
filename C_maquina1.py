from controller import Robot

# Inicializar el robot
robot = Robot()

# Obtener el tiempo de paso de la simulación
TIME_STEP = int(robot.getBasicTimeStep())

# Obtener los motores de las ruedas (reemplaza los nombres por los de tu árbol de nodos)
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Configurar posición en infinito para control de velocidad continuo
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Asignar velocidad a las ruedas (rad/s)
left_motor.setVelocity(5.0)
right_motor.setVelocity(5.0)

# Bucle principal de simulación
while robot.step(TIME_STEP) != -1:
    pass