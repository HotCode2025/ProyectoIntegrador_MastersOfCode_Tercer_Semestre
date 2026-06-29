# Proyecto integrador Masters Of Code
## MiniMercadoBombal v1.0

_Minimercado Bombal es un sistema de punto de venta diseñado para solucionar un problema muy común en los negocios: el orden y conteo de los productos, así como el control de entradas y salidas. El sistema está estructurado en tres secciones y, además, emite facturas en formato PDF para entregar al cliente al finalizar la compra._

* Clave de registro de usuarios: "1234"

### requisitos 📋
_Para ejecutar nuestro sistema debes instalar ciertas librerias_

```
* [Pillow](https://pypi.org/project/pillow/)
* [reportlab](https://pypi.org/project/reportlab/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [tkcalendar](https://pypi.org/project/tkcalendar/)
* [ttkthemes](https://pypi.org/project/ttkthemes/)

```

### Instalación 🔧

_Aqui estan los comandos para instalar los paquetes necesarios_

```
pip install pillow
pip install reportlab
pip install db-sqlite3
pip instal tkcalendar
pip install ttkthemes

```

luego de instalar las dependecias deberas ejecutar el archivo index.py y se ejecutara el sistema <br/>

## Construido con 🛠️

_Nuestro sistema fue creado con Python y sqlite3_

* [Python](https://www.python.org/) - El lenguaje usado
* [Sqlite3](https://sqlite.org/version3.html) - Base de datos

## Wiki 📖

### 🌟 1. Secciones Principales
* **`ventas.py`**: Interfaz y lógica del punto de venta. Gestiona y procesa los cobros.
* **`inventario.py`**: Control centralizado del stock, ingresos, egresos y herramientas para filtrar o editar artículos.
* **`clientes.py`**: Módulo para el alta, baja y modificación de los datos de los clientes.

### ⚙️ 2. Módulos de Soporte y Administración
* **`proveedor.py`**: Proximamente
* **`pedidos.py`**: Control de las órdenes de compra.
* **`login.py`**: Control de acceso seguro para los usuarios del sistema.
* **`informacion.py`**: Proximamente

### 🗄️ 3. Núcleo del Sistema y Base de Datos
* **`index.py`**: Archivo de arranque principal de la aplicación.
* **`manager.py` / `container.py`**: Controladores de la interfaz gráfica y flujo de ventanas.
* **`database.db`**: Base de datos SQLite que almacena toda la información.

### 📂 4. Directorios de Recursos
* **`/facturas`**: Almacena automáticamente los comprobantes generados en formato PDF por el sistema.
* **`/imagenes` y `/fotos`**: Contienen los recursos visuales.



## Instalación y Ejecución

_Para poner en marcha el sistema localmente, sigue estos pasos:_

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/HotCode2025/ProyectoIntegrador_MastersOfCode_Tercer_Semestre


## Autores ✒️

_Proyecto creado por masters of code compuesto por:_

* **Francisco Knap** 
* **Ximena Tapia**
* **Rafael Pacheco** 
* **Emiliano Bogado** 
* **Joaquin Navea** 
* **Jose Britos**
* **Franco Cala**  