# Scripts Python

* El comando almacenará contenedores de instrucciones
* Las instrucciones son comandos disponibles en sh  (No Alias)

* Habrá Una lista de contenedores con los comandos necesarios
* Habrá un contenedor configurado como si fuera un cursor

## Contenedores
Un contenedor es una estructura que almacena la lista de comandos ejecutadas
en una sesión.

### Información a almacenar un contenedor
* Nombre (Identificador único)
* Lista de comandos
## Acciones disponibles para un contenedor:

* obtener el nobre del contenedor actual
* eliminar el contenedor actual
* eliminar un contenedor
* crear un contenedor
* configurar un contenedor (en base al nombre)
* ver la lista de comandos en un contenedor
* ver la lista de comandos en el contenedor actual
* ver la lista de contenedores
* correr un contenedor

### Acciones extras a considerar
* vaciar contenedor (actual o especifico)
* vaciar lista de contenedores

### Como se almacena los contenedores
Para almacenar contenedores, se usara un archivo oculto (unix like) donde están
todas  las configuraciones necesarias.

**Advertencia** : Al tratarse de un archivo en texto plano (JSON)
no debe ingresarse información sensible.

**A VER**: Comprobar si se puede ejecutar cosas con permisos administrativos