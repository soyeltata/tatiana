<div align="center"><img src="./assets/tatiana-logo.png">
<hr width=550>
<i>Un pobre intento de hacer un pequeño motor de videojuegos utilizando Python (≥ 3.10) y pygame</i>
</div>

<br>
<br>

**Tatiana** es un pequeño intento de implementar un motor de videojuegos 2D competente utilizando **Python** (en una versión superior o igual a **3.10**) y el módulo **pygame** como dependencia obligatoria, además de estar construido y regirse enteramente mediante el paradigma **ECS** (en castellano: *sistema entidad-componente*).

Como es obvio debido a la versión en la que actualmente se encuentra este proyecto, debe tratarse por el momento como una prueva de concepto más que como un producto estable y seguro, pues todavía quedan multitud de funcionalidades esenciales en cualquier motor de videojuegos por implementar a la par que muchos errores (que podrían ser considerados como graves) por corregir; por no mencionar el detalle de estar escrito enteramente en **Python**, lo que hace de este motor algo lento en comparación.

No obstante y a causa de los importantes avances que ha estado teniendo este proyecto, he decidido hacer público este proyecto para facilitar su uso y, en caso de tener sugerencias para el mismo o querer asistir en el desarrollo, hacer posible la contribución por parte de cualquiera.


## instalación del paquete
Puede instalar remotamente el paquete **Tatiana** en su entorno local ejecutando el siguiente comando desde su terminal:
```bash
pip3 install git+https://github.com/soyeltata/tatiana
```
Esto, en el caso de que se encuentre en un entorno **UNIX**, si está bajo una máquina **Windows** habrá de reemplazar `pip3` por `pip`, como se muestra a continuación:
```bash
pip install git+https://github.com/soyeltata/tatiana
```

Sin embargo y en el caso de que quiera instalar **Tatiana** manualmente con el fin de modificar su código fuente o con cualquier otro propósito, habrá de seguir las siguientes instrucciones, no sin antes asegurarse de que tiene instalados los paquetes `git` y `make`:
1. Clone el repositorio en su máquina local mediante el siguiente comando (funciona indistintamente de su sistema operativo):
   ```bash
   git clone https://github.com/soyeltata/tatiana.git tatiana-main && cd tatiana-main
   ```
   O, si no posee `git` en su máquina, puede descargar el código fuente como un archivo *.zip* y posteriormente descomprimirlo y moverse al directorio `tatiana-main`.

2. Una vez realizados dichos pasos, proceda a ejecutar el siguiente comando si posee el paquete `make` instalado en su máquina para instalar **Tatiana**:
   ```bash
   make install
   ```
   Si por el contrario sólo quiere compilar el paquete (por cualquier motivo), ejecute el siguiente comando en su lugar:
   ```bash
   make all
   ```
   Los binarios se encontrarán en el directorio `dist/` que se acabará de crear.
   Para configurar correctamente y adaptar la compilación a su dispositivo con precisión, visite y lea el archivo `Makefile` que encontrará en la carpeta en la que se sitúa en el momento.
   En el caso de que no posea `make` instalado en su dispositivo, puede instalar **Tatiana** manualmente con el siguiente comando:
   ```bash
   pip install -e .
   ```

3. Luego de haber completado la instalación de **Tatiana**, puede, ahora sí, eliminar el directorio `tatiana-main` y el archivo *.zip* que haya descargado.

## un pequeño ejemplo del motor
Una vez instalado **Tatiana** en su dispositivo, ya puede empezar a trastear y juguetear con el pequeño motor de videojuegos que acaba de obtener.
Aquí, en esta pequeña sección podrá encontrar varios ejemplos útiles hechos utilizando **Tatiana** que quizás le ayuden en el desarrollo de su proyecto:

#### dibujar una imagen en pantalla
Para este primer ejemplo, necesitará de una imagen cualquiera de formato **PNG** a la que nombraremos como `image.png` dentro del código. Este archivo será nombrado una única vez en el código en la declaración de la constante `SPRITE`, por lo que modifíquela si el nombre de su imagen es otro:
```python
```

## características por implementar
Aún habiéndose implementado varias características dentro del motor **Tatiana**, el desarrollo de este apenas comienza, por lo que la mayoría de las que pensamos como posibles o que nos gustaría ver implementadas aún no lo están.
Por ello, a continuación se muestra el plan de programación que se tiene pensado para el proyecto (aunque sin fecha alguna, puede que no se acaben cumpliendo nuestras intenciones):
- [X] Un *sistema de entidad-componente* (**ECS**) funcional.
- [X] Dibujado de imágenes y sistemas para el escalado, la rotación y la opacidad de las mismas.
- [X] Animaciones funcionales y sistemas para manejar varias a la vez.
- [X] Sistemas para la limitación de FPS en la ejecución.
- [ ] Movimiento fluido mediante interpolaciones.
- [ ] Importación de *"atlas"* y *"spritesheets"*.
- [ ] Físicas realistas mediante el paquete [Pymunk](http://www.pymunk.org/).
- [ ] Clases base para crear rectángulos, círculos, triángulos, texto...

## [licencia del proyecto](./LICENSE)
 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

#### Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

<br>
<br>

> Este proyecto está dedicado, cómo no, a **Tatiana**. Sé que no es mucho, pero es trabajo honrado y, si he podido llevar a cabo esta idea, ha sido pensando en ti **;)**