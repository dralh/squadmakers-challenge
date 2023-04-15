# SquadMakers Challenge

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

### Consideraciones
Para la estructura del proyecto se escogió Clean Architecture, ya que si bien es un proyecto pequeño,
podría presentarse la oportunidad de estar en el mismo contexto
(con mucha incertidumbre con respecto al alcance y escalamiento de las futuras funcionalidades) en un requerimiento laboral.
Por un lado, Clean Architecture nos da la ventaja de no depender de tecnologías en concreto y, mejor aún, que estas sean intercambiables
con el mínimo esfuerzo sin modificar el código core. Por otro lado, también nos permite que agregar funcionalidades consista en exactamente eso
"agregar" mas no "modificar".

Como "web framework" se escogió Flask, ya que nos proporciona lo mínimo y necesario para poder crear un API REST y, ante la incertidumbre
mencionada anteriormente, nos permite customizar al máximo los requerimientos.

Como motor de base de datos se escogió PostgreSQL. Si bien MongoDB hubiera guardado de manera más práctica los objetos,
ya que estos con poseen una estructura variable dependiendo del proveedor, esto se pudo solucionar fácilmente estableciendo un modelo para el caso de uso
y mapeando cada respuesta del proveedor a este. Además tampoco se tuvo en cuenta Oracle ni SQL server, ya que no se contaba con la información
de si se poseía una licencia para poder aprovechar al máximo sus beneficios. Asimismo, no se optó por Elastic Search debido a que está más orientado
a la optimización de búsqueda de texto. Finalmente, se prefirió PostgreSQL en vez de MariaDB debido a que está muy probado en producción y ofrece
un set interesante de extensiones.



## Stack

Python3.11, SQLAlchemy, Flask, PostgreSQL


## Dependencias

python3.11, postgresql
## Ejecutar localmente

Clonar el repositorio

```bash
  git clone https://github.com/dralh/squadmakers-challenge
```

Ir a la carpeta del projecto

```bash
  cd squadmakers-challenge
```

Crear environment
```bash
  python3 -m pip install virtualenv
  python3 -m virtualenv venv
  source ./venv/bin/activate
```

Instalar projecto
```bash
  python setup.py install ".[dev,test]"
```

Copiar el archivo de configuracion
```bash
  cp config.template.yaml config.yaml
```

Inicializar la base de datos
```bash
  psql -h <host> -p <port> -U postgres < database/create_database.sql
  psql -h <host> -p <port> -U postgres -d squadmakers < database/create_user.sql
  psql -h <host> -p <port> -U postgres -d squadmakers < database/create_schema.sql
  psql -h <host> -p <port> -U postgres -d squadmakers < database/migrations/V1_0__base_migration.sql    
```

Ejecutar tests
```bash
  pytest -sv tests
```

Iniciar el servidor

```bash
  ./run.sh
```


## Uso/Ejemplos

Obtener una broma aleatoria
```bash
  curl http://127.0.0.1:6000/api/joke
```

Obtener una broma de un proveedor
```bash
  curl http://127.0.0.1:6000/api/joke/chuck
  curl http://127.0.0.1:6000/api/joke/dad
```

Crear una broma
```bash
  curl +X POST -H "Content-Type: application/json" -d '{"content": "a basic joke"}' http://127.0.0.1:6000/api/joke
```

Editar una broma
```bash
  curl +X PUT -H "Content-Type: application/json" -d '{"content": "a new joke"}' http://127.0.0.1:6000/api/joke/1
```

Eliminar una broma
```bash
  curl -X DELETE http://127.0.0.1:6000/api/joke/1
```

Calcular el minimo comun multiplo de una lista de numeros
```bash
  curl http://127.0.0.1:6000/api/math/leastcommonmultiple?numbers=1,2,3,4,5
```

Incrementar en uno un numero dado
```bash
  curl http://127.0.0.1:6000/api/math/increment?number=123
```

