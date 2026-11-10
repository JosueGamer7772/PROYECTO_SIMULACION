# 🚜 Proyecto Final: Simulación de Tractor Agrícola y Limpiadora de Playas en Webots

Este repositorio contiene el proyecto final de simulación automatizada desarrollado en el entorno **Webots** utilizando un controlador de tipo **Supervisor** programado en Python. El proyecto integra el modelado 3D avanzado, la cinemática de maquinaria pesada y la programación de simulación robótica en un entorno dinámico interactivo.

---

## 🛠️ Integración y Edición de Modelos en Blender

Una de las fases críticas del proyecto fue la adaptación de la geometría tridimensional. Los modelos originales del tractor y del mecanismo limpiador no estaban preparados nativamente para los requerimientos físicos de un motor de simulación. El equipo realizó un trabajo exhaustivo de edición en **Blender** centrado en los siguientes pilares técnicos:

### 1. Corrección de Orígenes y Centros de Masa (Origin to Geometry)
- **Problema:** En Webots, los componentes móviles (como las ruedas y los rotores) giran en torno al origen local (`0,0,0`) asignado al archivo `.obj`. Si el origen está desplazado, las piezas oscilan de forma errática o giran de forma excéntrica al aplicarles velocidad.
- **Solución en Blender:** Se separó cada rueda (`CHASIS`, `LLANTADD`, `LLANTADI`, `LLANTAIT`, `LLAMTD`, `LLAMI`) en objetos independientes. Se reposicionó el origen exactamente en el centro geométrico de sus respectivos ejes de revolución mediante el comando *Set Origin -> Origin to Center of Mass*, garantizando un movimiento de rotación concéntrico y libre de vibraciones físicas en Webots.

### 2. Reducción y Optimización de Polígonos (Decimate)
- **Problema:** Los modelos CAD de alta fidelidad ralentizan el motor físico de Webots debido a una carga excesiva de vértices, lo que provoca caídas de frames (FPS) y errores en el cálculo de colisiones.
- **Solución en Blender:** Se aplicaron modificadores de tipo *Decimate* a mallas complejas como la estructura del chasis y el rotor mecánico. Esto redujo el conteo de polígonos a un estándar óptimo para simulación en tiempo real, manteniendo la silueta y los detalles visuales esenciales del vehículo.

### 3. Desenvolvido UV y Mapeo de Texturas (UV Unwrapping)
- **Problema:** Los materiales asignados por defecto no se transferían correctamente al formato `.obj` e imposibilitaban el uso de texturas complejas de desgaste en la playa.
- **Solución en Blender:** Se generaron mapas UV coordinados utilizando herramientas de *Smart UV Project* y costuras manuales (*Mark Seam*). Esto permitió mapear la textura de desgaste metálico y suciedad (`Texture Tractor.jpg`) sobre las superficies correctas del chasis y del mecanismo del rotor, asegurando que las coordenadas de textura (`.mtl`) se leyeran de forma nativa en los nodos de Webots.

### 4. Triangulación y Exportación (.obj / .mtl)
- **Operación:** Webots interpreta de mejor manera las mallas compuestas por triángulos en lugar de cuadriláteros (*Quads*). Al exportar desde Blender, se activó la opción *Triangulate Faces* y se configuró el eje **Y hacia arriba** (Y Up) junto con el eje **-Z hacia adelante** (-Z Forward) para emparejar la orientación espacial con el sistema de coordenadas del simulador.

---

## 🚀 Características y Funcionamiento del Controlador

El script en Python utiliza la interfaz `Supervisor` para interactuar directamente con la API del simulador en pasos de tiempo constantes (`TIME_STEP`):

- **Control de Actuadores del Tractor:** Configura el modo de velocidad infinita (`float('inf')`) en los actuadores del chasis principal (`motor_del_izq`, `motor_del_der`, `motor_tra_der`, `motor_tra_izq`) controlando la velocidad lineal de avance.
- **Sincronización del Mecanismo Limpiador:** Los motores auxiliares de las ruedas de la limpiadora (`LLMD`, `LLMI`) y el rotor central (`ROTOR`) operan a velocidades angulares invertidas y calculadas matemáticamente para contrarrestar el par de fricción y simular el arrastre sobre la arena.
- **Efectos de Partículas Visuales (Nube de Arena):** Mediante la manipulación directa de árboles de nodos (`getFromDef`), el script altera de forma dinámica el campo `transparency` del nodo `NUBE_ARENA`. Al aplicar una función armónica senoidal (`math.sin(robot.getTime() * 12.0)`), se emula visualmente el levantamiento oscilatorio de polvo y arena provocado por el impacto de las aspas del rotor.

---

## 📂 Estructura Final del Repositorio

```text
PROYECTO_FINAL/
├── controllers/          # Scripts de control (Python API de Webots)
│   └── supervisor_code/  # Controlador supervisor principal de la simulación
├── protos/               # Archivos 3D optimizados en Blender (.obj, .mtl, .blend)
├── worlds/               # Archivo de escena de Webots y configuraciones (.wbt, .wbproj)
├── texturas/             # Mapas de texturas e imágenes de materiales (.jpg)
└── README.md             # Documentación técnica del proyecto
```

---
## 👥 Desarrolladores

El diseño, modelado, optimización y programación de esta simulación fue realizado por:
* **JESSICA MEZA**
* **JOSUE RODRIGUEZ**
* **ALAN GOMEZ**
