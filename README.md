# PROYECTO_SIMULACION
**PROYECTO FINAL**

## 📌 Descripción del Proyecto
Este proyecto consiste en la simulación 3D de una máquina (tractor / limpiadora de arena) dentro del entorno **Webots**, integrando el modelado del vehículo y el desarrollo de controladores en **Python** para su manipulación e interacción en el entorno virtual.

1. Búsqueda y Edición del Diseño de la Máquina
Búsqueda del Modelo 3D: Selección y adquisición del modelo tridimensional base adecuado para las especificaciones de la máquina.

Modelado y Edición en Blender:

Ajuste de geometrías, jerarquías de componentes y optimización de mallas.

Asignación de materiales y texturas.

Separación de partes móviles (ruedas, ejes o mecanismos) para permitir su posterior articulación física en el simulador.

Exportación e Importación: Conversión del diseño a formatos compatibles (.obj / .wbt / PROTO) para su correcta carga dentro de Webots.

💻 2. Desarrollo del Código y Controladores
Controlador en Python (C_maquina1.py):

Implementación de la API de controladores de Webots (from controller import Robot).

Vinculación de dispositivos y actuadores mediante robot.getDevice().

Configuración de motores en modo velocidad/posición para la tracción y maniobrabilidad de la máquina.

Lógica de control para el desplazamiento (adelante, atrás, giros o control por teclado).

⚙️ 3. Configuraciones Pendientes y Próximos Pasos
[ ] Ajuste de Propiedades Físicas:

Configuración fina de masas, centros de gravedad y matrices de inercia para evitar volcamiento.

Ajuste de parámetros de fricción (contactProperties) entre las ruedas y la superficie.

[ ] Mapeo de Motores y Sensores:

Definición final de los nombres de los nodos de motor dentro del árbol de Webots para sincronizarlos con C_maquina1.py.

Adición opcional de sensores (distancia, cámara o IMU) según los requerimientos del proyecto.

[ ] Pruebas de Simulación: Validación del comportamiento dinámico en la escena PF_MAQUINA.wbt