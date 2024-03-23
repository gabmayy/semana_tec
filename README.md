# Juego de Pong Mejorado

Este script de Python mejora el clásico juego de Pong con características adicionales como niveles de dificultad, tamaños de paletas dinámicas y una funcionalidad de pausa. Está diseñado para proporcionar una experiencia de juego más atractiva y personalizable. A continuación, se ofrece una guía completa sobre cómo configurar, jugar y comprender la mecánica del juego.

## Características

- **Niveles de Dificultad Ajustables:** Cambia la dificultad del juego al instante, afectando la velocidad y el color de la bola.
- **Tamaños de Paleta Dinámicos:** Aumenta o disminuye el tamaño de las paletas durante el juego para añadir desafío y estrategia.
- **Funcionalidad de Pausa:** Capacidad para pausar el juego, permitiendo a los jugadores tomar descansos sin cerrar el juego.
- **Seguimiento de Puntuación:** Muestra las puntuaciones de ambos jugadores, actualizándose en tiempo real a medida que avanza el juego.

## Dependencias

- Python 3.x
- Biblioteca de Gráficos Turtle: Para dibujar los gráficos del juego.
- Biblioteca de Python Freegames: Para funcionalidad de vector adicional.

Asegúrate de tener Python instalado en tu sistema y las bibliotecas necesarias antes de ejecutar el juego.

## Configuración y Ejecución del Juego

1. **Instalación:** Si no has instalado Python, descárgalo desde el sitio web oficial de Python. Para instalar la biblioteca `freegames`, usa pip:

   ```bash
   pip install freegames
   ```

2. **Ejecución del Juego:** Guarda el script como `pong_game.py` y ejecútalo usando Python:

   ```bash
   python pong_game.py
   ```

3. La ventana del juego se abrirá y podrás comenzar a jugar inmediatamente.

## Controles

- **Jugador 1:**
  - Mover hacia arriba: `W`
  - Mover hacia abajo: `S`
- **Jugador 2:**
  - Mover hacia arriba: `I`
  - Mover hacia abajo: `K`
- **Ajustar Dificultad:**
  - Fácil: `1`
  - Medio: `2`
  - Difícil: `3`
- **Ajustar Tamaño de la Paleta:**
  - Aumentar tamaño: `4`
  - Disminuir tamaño: `6`
  - Restablecer al tamaño original: `5`
- **Pausar Juego:** Alternar pausa con `T`.

## Mecánica del Juego

- La bola comienza a moverse automáticamente al inicio del juego.
- Los jugadores controlan sus paletas para golpear la bola de ida y vuelta.
- Si la bola pasa la paleta de un jugador, el jugador contrario anota un punto.
- El juego se pausa automáticamente cuando se anota un punto, permitiendo a los jugadores prepararse para la siguiente ronda.
- La dificultad afecta la velocidad y el color de la bola, haciéndola más fácil o difícil de golpear.
- El tamaño de la paleta puede cambiarse durante el juego, afectando la estrategia de juego.

## Personalización del Juego

Siéntete libre de modificar el código para agregar nuevas características o cambiar las mecánicas existentes. Algunas ideas incluyen añadir efectos de sonido, crear un sistema de puntuación más sofisticado o introducir power-ups.

## Conclusión

Este juego de Pong mejorado ofrece una experiencia personalizable e interactiva para dos jugadores. Con controles fáciles de entender y dificultad ajustable, es adecuado para jugadores de todas las edades. 

## Video
https://youtu.be/p7wXpiXEoJU

## Integrantes
- Cleber Gerardo Pérez Galicia    	A01236390
- Gabriel Máynez Garcia 		      A01236355
- Fabián Treviño Villarreal 		   A01369765
