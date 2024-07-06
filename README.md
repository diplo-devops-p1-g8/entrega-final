Calidad en el Ciclo de Vida del Desarrollo de Software

Trabajo Práctico Final

Profesor: Lalo Miranda

Grupo 8

Integrantes:

Aiassa Ludmila

del Corro Ignacio

Fernandez Federico


#

# Índice:

[1. Consigna](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.tcb52i3t8x7a)

[2. Planteo](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.bhonle6p0kv1)

[2.1 Branching\
2.2 Flujo de commits](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.mvv6121nzlhi)

[2.3 Uso de Pipelines](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.1oiksom67oz5)

[2.4 Análisis de Código](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.qnoxh4niha4k)

[2.5 Revisión de PRs](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.mixtt726svev)

[2.6 Flujo de Entrega](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.6ik3q7soqhzn)

[2.7 Flujo de Despliegue](https://docs.google.com/document/d/1nmq5kSsv1A1zcvO6ly_Lf4QP4GzCEzoSWILOpp9yQM4/edit#heading=h.95vqxvdr5tg) 


#

# 1. Consigna:

Diseñar un flujo de trabajo completo para el ciclo de vida del desarrollo de software. Se deben planear el flujo de trabajo completo y el recorrido de la información.

 Esto incluye:

- Esquema de branching.

- Flujo de commits.

- Uso de pipelines (PRs, on commits, etc.).

- Análisis de código (cualquiera que se considere oportuno).

- Revisión de PRs.

- Flujo de Entrega.

- Flujo de Despliegue.


# 2. Planteo

El equipo de trabajo forma parte de una startup y está conformado por un equipo de 5 desarrolladores. 

Nos han pedido que agilicemos lo máximo posible las etapas de Integración y de Despliegue para aumentar su capacidad de entregar nuevas features a producción de la manera más estable posible, con los costos de testeos lo más barato posible.


### 2.1 Branching

Para la estrategia de branching se propone un esquema por entornos modificado, donde existiría un entorno productivo **Main** y un entorno no productivo **Dev**. Además de estos se utilizarían **feature** y **hotfix** branches.

Main es una rama protegida y estable, la cual debe mantenerse en un estado permanente de lista para ser desplegada. Dev es el entorno donde los desarrolladores integrarán sus cambios, donde se harán los primeros testeos los cuales serán de análisis estático del código, y la cual deberá tender a estar en un estado de lista para ser desplegada; en caso de que una integración resulte en un fallo del entorno, se hará rollback al estado funcional  más próximo. Cuando se realiza una modificación en la rama main se realiza un tag representando la nueva versión.![](https://lh7-us.googleusercontent.com/docsz/AD_4nXd4ydIieGtXsnYTA7tLjawciyw5K6RlavRCfOzYsTdnWX6o2W0-gbDtUQ1Zxp_2tOE1t3vYzjW4sQHijBXxgqx7q_tjkoUl-cfoih2V7yzleJ09cm4ScVbbKs0_5zlHv3fiUUcEupBiFo2iWNs9zRbqJyjB?key=7Dnbjrm5qz2nwTgBp_i0SA)

 Feature y hotfix se tratan de ramas propias de los desarrolladores, ambas se originan de main pero se integran a dev y main respectivamente. Estas ramas son de característica temporal, esto significa que al momento de las integraciones serán eliminadas.

Se propone este plan debido a lo siguiente:

- Queremos acelerar el proceso de integración y aumentar la cantidad total de integraciones diarias de los desarrolladores.

- Para garantizar la estabilidad, los desarrolladores trabajan sobre Dev, donde allí comprueban la funcionalidad de sus features. Una vez que se valida la funcionalidad mediante tests de funcionalidad y de regresión locales, se hace una PR para integrar a Main.

- NO se propone QA o Staging debido a la necesidad de rapidez en el proceso de integración y despliegue, y para mantener los costos de infraestructura bajos ya que entornos pre productivos elevarían el costo de manera sustancial.


### 2.2 Flujo de commits:

Para esta empresa se eligió un flujo de commits basado en un feature branching, es decir un Github Flow, debido a que se trata de una metodología de trabajo simple, y de entrega continua. Esto se puede aplicar debido a que se trata de una startup con un grupo de trabajo pequeño.

Sin embargo, como también se quieren aplicar buenas prácticas de CI/CD, se agregó una rama DEV para la realización de pruebas. Es por esto que nuestro flujo no es puramente de feature branching sino que se fusiona un poco con Gitlab workflow.

Lo cual, con este sistema híbrido logramos un despliegue continuo , estabilidad y simplicidad.

Para la descripción de commits el equipo se propone seguir en base las convenciones descritas en la [Especificación de “Conventional Commits”](https://www.conventionalcommits.org/en/v1.0.0/#specification) a fin de mejorar la calidad del proyecto en desarrollo, posibilitar la generación de changelogs automáticamente, facilitar la comprensión de las modificaciones realizadas, y favorecer a la escalabilidad del proyecto. Además para los Issues se propone una especificación propia nombrada ["Convención de Issues"](https://pastebin.com/JyEjiDgj) que es adoptada en un tablero Kanban desde la planificación del proyecto con acceso restringido al equipo de desarrollo.\
![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcYJsgHyzyeRheUZCsYzsyE0c111TYNBPI_IXeQTm9-t15-5X13pi-2jXPiRHgwU6fABNz8fds5e99CGJD9RsBNitvt1RsEnjNGwd30UFykIaMf8zCCByqtZ86bEdDPOML67JyX1-qGeme-FsKDJIjqlrc4?key=7Dnbjrm5qz2nwTgBp_i0SA)


### 2.3 Uso de Pipelines:

Para el uso de pipelines se propone un circuito de CI/CD el cual tendrá como objetivo la automatización de tareas de carácter repetitivo. Entiéndase por repetitivo tareas de generación de artefactos, almacenamiento de artefactos, verificación de integridad de dependencias, tests estáticos y/o dinámicos, generación de documentación y/o changelogs, notificaciones de resultados al correr pipelines y releases, y notificaciones de monitoreo.

 Estos pipelines son ejecutados en instancias self hosted, lo cual asegura mantener los costos de automatización bajos. Se levantan 2 (dos) runners para main y dev.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdfXmZ1z9iFkA45mhuE3iTS8TffKWfJy8arqJdxP34N__tUfZP91A44NLzM4gAHSaKdoi-8GUck3tnGgyEIbFsnoMyA-u_zKMn9ycZk9rsHKfl0bFgICcl5xyGrY4bPL8eSt6l1xr7ZWROdCO6zlvopHHk?key=7Dnbjrm5qz2nwTgBp_i0SA)


###

### 2.4 Análisis de Código:

Se realizan análisis estáticos y dinámicos, tanto locales como remotos. Ambos automatizados.

- Code Review: Se recomienda el uso de revisiones estáticas manuales para asegurarse de mantener las convenciones establecidas antes.\
  El code review es obligatorio para las PRs, también es manual.

- Linters: Se establecen parámetros a través de pylint para definir características estéticas y no funcionales como: módulo/función encapsuladas en menos de 200(doscientas) líneas de código; documentación a través de “docstrings”  para cada módulo/función; homogeneidad en el nombramiento de variables, funciones y archivos. Este proceso estará automatizado en el entorno no productivo Dev y Main. Se facilitan las herramientas y se alienta al uso local de este Linter.

- Test Unitarios: Se proporcionan automatizaciones a test unitarios realizados atómicamente con el uso de mocks para agilizar el proceso de validación. Estos se realizan localmente, es responsabilidad del desarrollador asegurar la calidad del código antes de la integración a dev.

- Tests de Funcionalidad y de Regresión: Se ejecutan automáticamente al momento de integrar una PR a main. Estos test son requisito aprobarlos para tener permiso de hacer el despliegue a main.


### 2.5 Revisión de PRs:

Para las distintas branches se asignan distintas triggers necesarios para correr los pipelines.

**Main**: Todos los pipelines que se corran en Main se ejecutarán solamente al ocurrir una PR. Los tests estáticos deberán superar una puntuación de 8 (ocho) en pylint, con excepción de los hotfixes. La PR debe asignarse a alguien distinto al que la genera, examinada (code review) y debe ser aprobada. El pipeline debe tener un código de salida exitoso, de lo contrario la PR no podrá ser aprobada. Se deben superar pruebas automáticas de funcionalidad y regresión para poder ser aceptada.

**Dev**: Los pipelines corren cuando se realiza un push a la branch dev. Puede ser aprobada por cualquier desarrollador y se necesita solo una code review para poder ser aceptada. 2.6 Flujo de Entrega:


#### ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeXDu8-cTJNTN5VQQvTeJgXQwdmhSCDraaeLaTY0Wh2esNceJd6RN1I5luJ0HbydZcSmPwG7H7psGMLca7-XfXn9RIzSyT2pgvCIeWupWlykVY3xVmo-v03yPhf-663qwmdXu6Eu7q4ifXCzMstYQ-p93vJ?key=7Dnbjrm5qz2nwTgBp_i0SA) 2.7 Flujo de Despliegue:

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfKWYF_d27BZr2YZyOzSXETdWW3SnDmQSjE35_-4rILE3HxGiOBxprSRkgmqwDFyn9CW3kxIeaGpVO04_N4tdJNUzyANMEAZyhrM36tG_05AQKta6nuV4zHD--GngNaGcHOzAPoG0lO47cgmE04DWZu9aU8?key=7Dnbjrm5qz2nwTgBp_i0SA)


#### Esquema de versionado:

Para la gestión de versiones  se propone adherir al esquema de Versión Semántica: v(MAJOR).(MINOR).(PATCH)

Con significado respectivo a:

- MAJOR: representa cambios importantes o incompatibles con versiones anteriores.

- MINOR: representa nuevas funcionalidades que son compatibles con versiones anteriores.

- PATCH: representa correcciones de errores que son compatibles con versiones anteriores.
