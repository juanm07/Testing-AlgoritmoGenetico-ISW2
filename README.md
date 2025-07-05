# Trabajo sobre algoritmos genéticos y testing
En este trabajo desarrollamos un algoritmo genético para generar casos de test automáticamente para la funcion `cgi_decode`, que decodifica un string codificado con el protocolo CGI

## Resumen del trabajo

* Version instrumentada de `cgi_decode` para medir *branch distance*
* Función de fitness basada en las *branch distance* normalizadas
* Implementacion de un algoritmo genético usando:
    * *Tournament selection*
    *  *single-point cross-over*
    *  Operadores de mutación
* Test suite buscando cobertura de branches y lineas del 100%

## Setup e Instalación

1. Clonar el repositorio y navegar hasta él
2. Crear un ambiente virtual de Python:
     ```bash
     python3 -m venv venv
    ```
     Si el comando no funciona, probar `virtualenv venv`
3. Activar el ambiente virtual
     ```bash
     source venv/bin/activate
     ```
4. Instalar las dependencias
  ```bash
   pip install -r requirements.txt
  ```
## Correr los tests

Para ejecutar toda la test suite con reporte de *coverage*:

```bash
  ./run_tests.sh
```
Para ejecutar los test de algun modulo en especifico pasar el nombre del modulo como primer argumento del script.

Por ejemplo para ejecutar los tests del archivo `test_cgi_decode.py`:
```bash
  /run_tests.sh test.test_cgi_decode.
```

Como alternativa, si se utiliza algun IDE como Pycharm, asegurarse de que la variable *PYTHONHASHSEED* sea igual a 0

## Estructura del trabajo

### src

```bash
  src/
├── cgi_decode.py                # Implementacion original del CGI decode
├── cgi_decode_instrumented.py   # Version instrumentada para contar branch distances
├── evaluate_condition.py        # Evaluacion de condiciones para actualizar branch distances
├── get_fitness_cgi_decode.py    # Calculadora de la funcion de fitness para los tests
├── create_population.py         # Inicializacion de la población para el algortimo genético
├── evaluate_population.py       # Evaluación del fitness de la población
├── selection.py                 # Implementacion del Tournament selection
├── crossover.py                 # Implementación del single-point cross-over
├── mutate.py                    # Operadores de mutación
└── genetic_algorithm.py         # Implementacion del algoritmo genético (standard sin elitismo)
```
### test

```bash
test/
├── test_cgi_decode.py
├── test_evaluate_condition.py
├── test_evaluate_condition_for_cgi_decode_instrumented.py
├── test_get_fitness_cgi_decode.py
└── test_genetic_algorithm.py
```

## Detalles de implementación

### Operadores de mutación utilizados

  * Agregar un nuevo caso de test aleatorio
  * Remover un caso de test existente
  * Modificar casos de test a traves de:
      * Agregar un caracter
      * Eliminar un caracter
      * Modificar un caracter

### Operadores genéticos
  * Selección  (*Tournament selection*)
  * Crossover (*single-point cross-over*)
  * Mutación
