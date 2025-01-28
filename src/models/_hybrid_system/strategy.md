## Enfoques de recomendación

El motivo de incluir estos enfoques específicos (colaborativo, basado en contenido y popularidad) es que:

1. **Colaborativo**: El contexto indica que hay datos de interacción de los usuarios (`user_id`, `partnumber`, `session_id`) en los datasets de entrenamiento, lo que permite implementar un modelo basado en interacciones previas (e.g., SVD, ALS, NCF).
   
2. **Basado en contenido**: El dataset incluye embeddings de productos y atributos como familia, color y descuento, que son útiles para construir recomendaciones personalizadas incluso si no hay historial de interacciones del usuario.

3. **Popularidad**: Como se especifica que el test incluye usuarios **nuevos** y **no logueados**, un enfoque basado en popularidad asegura que podamos manejar estos casos, ya que no tendremos información de usuario o historial de interacciones.

---

## **Clases de usuarios y enfoques de recomendación**

### **1. Usuario nuevo logueado (presente en `Train`)**
- **Descripción**: Usuario registrado en la plataforma, pero sin interacciones en la sesión actual.
- **Problema**: Aunque sabemos quién es el usuario, no tenemos datos recientes para basar nuestras recomendaciones.
- **Enfoque**:
  - Utilizar modelos **colaborativos** basados en interacciones previas del usuario en el dataset de entrenamiento.
  - Incorporar recomendaciones basadas en contenido utilizando atributos del producto (e.g., familia, descuento, embeddings) si hay un patrón claro en sus compras pasadas.


### **2. Usuario nuevo no logueado (ausente en `Train`)**
- **Descripción**: Usuario sin cuenta registrada o logueado como invitado, por lo que no hay datos históricos disponibles.
- **Problema**: No tenemos información del usuario en absoluto.
- **Enfoque**:
  - Generar recomendaciones de productos populares basadas en métricas globales como:
    - Frecuencia de productos agregados al carrito.
    - Popularidad por país o dispositivo (si está disponible).
  - Incluir productos con descuentos o promociones, que suelen tener mayor probabilidad de conversión.


### **3. Usuario recurrente logueado (presente en `Train`)**
- **Descripción**: Usuario registrado con interacciones tanto en el dataset de entrenamiento como en la sesión actual del dataset de prueba.
- **Problema**: Necesitamos combinar interacciones previas y actuales para optimizar la recomendación.
- **Enfoque**:
  - Usar modelos colaborativos para capturar preferencias históricas y complementarlo con interacciones recientes de la sesión.
  - Priorizar recomendaciones de productos similares a los interactuados en la sesión, utilizando embeddings y atributos (e.g., familia, color).
  - Incorporar productos relacionados (e.g., productos complementarios o en la misma familia).


### **4. Usuario recurrente no logueado (ausente en `Train`)**
- **Descripción**: Usuario que no está logueado, pero que ha interactuado en la sesión actual del dataset de prueba.
- **Problema**: No tenemos datos históricos, pero sí algunas interacciones en la sesión actual.
- **Enfoque**:
  - Generar recomendaciones en tiempo real basándonos en los productos con los que interactuó en la sesión actual.
  - Usar técnicas basadas en contenido (atributos de producto similares o embeddings).
  - Incluir productos relacionados o populares en las categorías de los productos de la sesión actual.


### **Resumen de los enfoques por clase**

| **Clase de Usuario**            | **Datos disponibles**               | **Enfoque principal**                      |
|----------------------------------|-------------------------------------|--------------------------------------------|
| Usuario nuevo logueado          | Datos históricos en `Train`         | Colaborativo + Contenido                   |
| Usuario nuevo no logueado       | Sin datos históricos ni actuales    | Popularidad                                |
| Usuario recurrente logueado     | Históricos en `Train` y actuales    | Colaborativo + Contenido + Interacciones actuales |
| Usuario recurrente no logueado  | Solo interacciones en la sesión     | Contenido + Interacciones actuales         |

---

### **2. Implementar el modelo híbrido (Colaborativo, Contenido, Popularidad):**

#### **Enfoque del modelo híbrido**:

1. **Colaborativo**:
   - **Técnica**: Utilizar matrices de interacción usuario-producto para identificar patrones en las preferencias.
   - **Método**: Aplicar un modelo basado en factores latentes como `SVD` o `NCF`.

2. **Basado en contenido**:
   - **Técnica**: Usar características del producto (como color, familia, embeddings, etc.) y del usuario (RFM, país, etc.).
   - **Método**: Entrenar un modelo como `LightGBM` para predecir interacciones basadas en estas características.

3. **Basado en popularidad**:
   - **Técnica**: Recomendación de los productos más populares.
   - **Método**:
     - Calcular la popularidad como el número de interacciones o compras.
     - Ordenar y recomendar los productos más populares, aplicando filtros según las características del usuario.

---

### **Pipeline para el modelo híbrido**:

1. **Preparación de datos**:
   - Procesar los datos para alimentar los tres enfoques (colaborativo, contenido y popularidad).
   - Asegurar consistencia en las columnas para cada enfoque.

2. **Entrenamiento de modelos**:
   - Entrenar el modelo colaborativo con interacciones usuario-producto.
   - Entrenar el modelo basado en contenido con `LightGBM`.
   - Calcular métricas de popularidad para recomendaciones generales.

3. **Combinación de predicciones**:
   - Crear una estrategia para fusionar los resultados de los tres enfoques:
     - Ponderación fija (e.g., 40% colaborativo, 40% contenido, 20% popularidad).
     - Aprendizaje en cascada: usar el modelo basado en contenido como filtro inicial, seguido de los otros enfoques.

4. **Evaluación final**:
   - Validar las predicciones combinadas utilizando métricas como `NDCG`.

