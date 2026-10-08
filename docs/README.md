<div align="center">
    <img
    src="/docs/assets/logo.png"
    alt="Logo 'El Ahorcado'"
    width="230"
/>
  <h1 align="center">El Ahorcado</h1>
  <h4 align="center">Juego en terminal elaborado en Python.</h4>
</div>


## Acerca de
Este pequeño proyecto de Python se elaboró para probar mi conocimiento sobre los módulos, las listas y los ciclos de una manera entretenida. Programado en un corto período de tiempo, me sirve para jugar en tiempos de ocio en la Universidad.

## Dependencias
* Python 3.14.7

## Uso
1. Descargar la versión más reciente de [Python](https://www.python.org/downloads/).
2. Clonar el repositorio.
```
git clone https://github.com/Andyy10/el-ahorcado.git
```
[!NOTE] Si no puedes clonar el repositorio, puedes descargar el archivo ZIP.
3. En una terminal (CMD, Terminal, Powershell) ejecutar el archivo main.py que se encuentra en la carpeta 'src'.
```
cd src
python main.py
```
4. Ingresar letras hasta adivinar la palabra o perder.

## Estructura del proyecto
```text
el-ahorcado: Juego de terminal.
├── src: Archivos necesarios para que el proyecto funcione.
│   ├── main.py: Programa principal donde se maneja la lógica del juego.
│   ├── palabras_ahorcado: Módulo donde se almacenan las palabras del juego. Se pueden agregar y quitar tantas como se deseen.
│   └── arte_ahorcado: Módulo donde se guarda el arte ASCII del juego, como los monitos de palo y el logo.
├── docs: Documentación del proyecto e imágenes.
```
## Capturas de pantalla
![Ejecución del juego](/docs/assets/Screenshot1.png?raw=true "Ejecución del juego.")
![Adivinar una letra](/docs/assets/Screenshot2.png?raw=true "Adivinar una letra.")
![Victoria](/docs/assets/Screenshot3.png?raw=true "Victoria. Fin del juego.")
![Derrota](/docs/assets/Screenshot4.png?raw=true "Derrota. Fin del juego.")