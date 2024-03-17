# Sistema de Cuenta Bancaria con Monitores - Ejemplo

Este archivo contiene un programa en Python que simula transacciones en una cuenta bancaria utilizando monitores para garantizar la sincronización y la exclusión mutua en operaciones concurrentes.

**Instrucciones de Uso:**

1. Asegúrese de tener Python instalado en su sistema.
2. Ejecute el archivo `main.py` desde la línea de comandos o desde su entorno de desarrollo Python preferido.

**Descripción del Programa:**

El programa define una clase `CuentaBancaria` que representa una cuenta bancaria con métodos para depositar, retirar y consultar saldo. Estos métodos están protegidos por un objeto de bloqueo (`Lock`) de la biblioteca `threading`, que actúa como un monitor para garantizar la exclusión mutua al acceder al saldo compartido.

La función `realizar_transacciones` simula transacciones en la cuenta bancaria, donde se realizan depósitos de 100 unidades seguidos de retiros de 50 unidades, todo esto se repite tres veces.

**Ejecución:**

Al ejecutar el programa, se crean varios hilos para simular transacciones concurrentes en la cuenta bancaria. Después de que todos los hilos hayan terminado, se muestra el saldo final de la cuenta.

**Nota:**

Este programa es un ejemplo simplificado con fines educativos para demostrar el uso de monitores en programación concurrente en Python. En aplicaciones del mundo real, se pueden implementar medidas adicionales para garantizar la seguridad y la integridad de los datos bancarios.
