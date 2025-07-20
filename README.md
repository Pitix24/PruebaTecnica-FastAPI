# Backend Project - Hexagonal + CQRS + Bundle-contexts

## Estructura

- `app/contexts/`: Contextos lógicos (users, auth), cada uno con dominio, aplicación e infraestructura.
- `app/core/`: Configuración y utilidades globales.
- `app/main.py`: Punto de entrada FastAPI.
- `tests/`: Pruebas unitarias.
- `requirements.txt`: Dependencias.
- `.env.example`: Variables de entorno de ejemplo.

## Cómo ejecutar

1. Crear entorno virtual y activar:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
2. Instalar dependencias:
    ```
    pip install -r requirements.txt
    ```
3. Ejecutar servidor:
    ```
    uvicorn app.main:app --reload
    ```

## Decisiones arquitectónicas

- Arquitectura hexagonal para independencia del dominio.
- CQRS para separar comandos (RabbitMQ) y consultas (directo a DB).
- Bundle-contexts para modularidad y escalabilidad.
