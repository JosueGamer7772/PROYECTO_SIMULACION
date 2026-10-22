# PROYECTO SIMULACIÓN - LIMPIADORA DE ARENA EN WEBOTS

## 📌 Descripción del Proyecto
Este proyecto consiste en la simulación 3D de una máquina agrícola/industrial (tractor limpiador de playa) dentro del entorno **Webots R2025a**. Integra el modelado 3D del vehículo, la recreación del entorno costero y el desarrollo de controladores en Python para su desplazamiento e interacción en el mundo virtual.

---

## 🎨 1. Diseños y Entorno 3D

### Modelo 3D de la Máquina
* **Selección del Modelo Base:** Elección del modelo tridimensional del tractor.
* **Modelado y Edición en Blender:**
  * Ajuste de geometrías, jerarquía de componentes y optimización de mallas.
  * Asignación de materiales y texturas.
  * Separación de partes móviles (ruedas, ejes o mecanismos) para su articulación física.
* **Exportación e Importación:** Conversión a formatos compatibles (`.obj` / `.wbt` / PROTO) para su carga e integración en Webots (`DEF TRACTOR Robot`).

### Entorno y Escenario Virtual
* **Playa:** Implementación del terreno irregular mediante el nodo `UnevenTerrain` ("PLAYA") para simular la textura y superficie de la arena.
* **Mar:** Representación inicial de la franja costera/marítima mediante un nodo `UnevenTerrain` ("MAR") ajustado en posición y orientación.

---

## 💻 2. Desarrollo del Código y Controladores

Controlador principal desarrollado en Python (`controllers/C_maquina1/C_maquina1.py`):

* **API de Webots:** Inicialización y control a través de `from controller import Robot`.
* **Vinculación de Actuadores:** Mapeo de los motores de las ruedas (`motor_del_izq`, `motor_del_der`, etc.) mediante `robot.getDevice()`.
* **Modo de Control:** Configuración en **modo de velocidad** (`setPosition(float('inf'))`) con inicialización en reposo.
* **Lógica de Desplazamiento:** Bucle de simulación sincrónico impulsado por `getTimeStep()`, aplicando velocidades angulares dinámicas (`target_speed`) a cada motor asignado.

---

## ⚙️ 3. Estado Actual y Próximos Pasos

### ✅ Logros Alcanzados
- [x] Configuración inicial del mundo en Webots (`PF_MAQUINA.wbt`).
- [x] Integración exitosa del modelo 3D del tractor con sus nodos de movimiento.
- [x] Construcción del escenario ambiental (playa y representación del mar).
- [x] Movimiento y desplazamiento funcional del tractor mediante script en Python.

### ⏳ Pendientes y Próximos Pasos
- [ ] **Mapeo Completo de Motores:** Finalizar la lista explícita de nodos en `motor_names` (`motor_del_izq`, `motor_del_der`, `motor_tra_izq`, `motor_tra_der`) para sincronizar las 4 ruedas.
- [ ] **Mapeo de la Herramienta Recolectora:** 
  - Finalizar en Blender el modelo 3D del mecanismo/rastrillo recolector de basura marina/playera.
  - Acoplar el subsistema recolector al tractor dentro del árbol de nodos de Webots.
- [ ] **Ajuste de Propiedades Físicas:**
  - Configuración fina de masas, centro de gravedad y matrices de inercia para garantizar estabilidad dinámica.
  - Definición de parámetros de fricción (`contactProperties`) entre los neumáticos y la arena.
- [ ] **Sensores y Lógica Avanzada (Opcional):**
  - Implementación de sensores (Cámara, GPS, Lidar o IMU) para navegación o detección de residuos.
  - Control por teclado (`Keyboard`) o rutas autónomas.
