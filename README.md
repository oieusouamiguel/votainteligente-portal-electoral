votainteligente-portal-electoral
================================

[![Build Status](https://travis-ci.org/ciudadanointeligente/votainteligente-portal-electoral.png?branch=master)](https://travis-ci.org/ciudadanointeligente/votainteligente-portal-electoral)
[![Coverage Status](https://coveralls.io/repos/ciudadanointeligente/votainteligente-portal-electoral/badge.png?branch=master)](https://coveralls.io/r/ciudadanointeligente/votainteligente-portal-electoral?branch=master)

## Descripción y contexto
---
Votainteligente, la plataforma electoral de la Fundación Ciudadano Inteligente, se utiliza para transparentar las posiciones electorales de los diferentes candidatos a una elección.

![](http://code.iadb.org/sites/default/files/inline-images/votainteligente.gif)
En esta plataforma de participación ciudadana, cualquier persona, u organización puede proponer a los candidatos electorales iniciativas para que estos las añadan a sus compromisos electorales. 
 
Una vez publicadas las propuestas de la ciudadanía, pueden ser apoyadas tanto por las personas u organizaciones registradas para que sean consideradas como compromisos por los candidatos parlamentarios y presidenciales en chile. 
 
Esta herramienta fue desarrolla por la fundación Ciudadano Inteligente para las elecciones chilenas del 2017 en la que se lograron 12 compromisos por parte de los dos candidatos que pasan a la segunda vuelta electoral. 
 
Actualmente 100 organizaciones se encuentran registradas y participando en la plataforma, fueron creadas 700 propuestas ciudadanas y después de la primera vuelta electoral fue visitada por 220 mil personas.  
 
El desarrollo de la herramienta fue la base para crear http://levantalamano.cl/, plataforma que visibiliza las propuestas que niños, niñas y adolescentes tienen para Chile. 

## Instalación
---
### Requerimientos o dependencias

Antes de que se inicie el proceso de instalación, se necesitan los siguientes requisitos:

- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
- [Git](http://git-scm.com/)
- Los requerimientos de [sorl-thumbnail has](http://sorl-thumbnail.readthedocs.org/en/latest/requirements.html)
     - redis (Puedes instalar ejecutando pip install redis, y una vez instalado se debe iniciar sudo service redis start)
     - zlib, zlib-devel, libjpeg, libjpeg-devel para utilizar [Pillow](http://pillow.readthedocs.org/en/3.1.x/installation.html#linux-installation)
     - [PgMagick](http://sorl-thumbnail.readthedocs.io/en/latest/requirements.html#pgmagick-installation) (Puedes instalar PgMagick en Ubuntu ejecutando sudo apt-get install python-pgmagick)
- [ElasticSearch 2.4](https://www.elastic.co/guide/en/elasticsearch/reference/2.4/setup-repositories.html)

### Proceso de instalación

* Clone vota inteligente en algún lugar de tu sistema

`git clone https://github.com/ciudadanointeligente/votainteligente-portal-electoral.git`

Ingresa el directorio de instalación

`cd votainteligente-portal-electoral`

* Crea un ambiente virtual

`mkvirtualenv votainteligente`

Aquí puedes opcionalmente darle al comando la ruta completa al directorio de instalación agregando -a <full_path>. Luego, para ir a este ambiente virtual (y directorio) debes ejecutar `workon votainteligente`
* Si no usaste la opción -a, deberás ingresar al directorio.

`cd votainteligente-portal-electoral`

* Instala los requisitos que vota inteligente necesita en el entorno virtual actual

`pip install -r requirements.txt`

Puede tomar algo de tiempo el tener todo instalado

* Crea la base de datos y tablas.

`python manage.py migrate`


* corre VotaInteligente

`python manage.py runserver`

y entra a  http://localhost:8000/.

## Temas
---

### Temas creados anteriormente

* [votainteligente-venezuela-theme](https://github.com/ciudadanointeligente/votainteligente-venezuela-theme) es el tema para [eligetucandidato.org](http://eligetucandidato.org/)

### Creando tu propio tema personalizado

Si desea crear un nuevo tema, debe crear un directorio que contenga dos subdirectorios, plantillas y elementos estáticos, y copia las plantillas que desea reemplazar.

Y en su proyecto en tu archivo local_settings.py, tienes que agregar lo siguiente

```
 STATICFILES_DIRS = (
     '/full/path/to/your/theme/static/',
 )
 TEMPLATE_DIRS = (
     '/full/path/to/your/theme/templates/',
 )
```
## Testeo
---

Puede ejecutar tests haciendo:
```
$ ./test.sh
```

Y hay un atajo para testear sin migraciones:

```
$ ./t.sh
```

## Licencia
---

VotaInteligente es gratuito y se presenta como software de código abierto bajo los términos de [GNU Public License](http://www.gnu.org/licenses/gpl-3.0.html) (GPL v3)
