from controller import Robot

# Inicializar el robot
robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())

# Nombres exactos declarados en los nodos RotationalMotor
motor_names = ['motor_del_izq', 'motor_del_der', 'motor_tras_izq', 'motor_tras_der']
motors = []

for name in motor_names:
    motor = robot.getDevice(name)
    if motor:
        motor.setPosition(float('inf'))  # Activa el modo de velocidad continua
        motor.setVelocity(0.0)
        motors.append(motor)

# Velocidad angular deseada en rad/s
target_speed = 10.0

# Bucle principal de simulación
while robot.step(TIME_STEP) != -1:
    for motor in motors:
        motor.setVelocity(target_speed)
