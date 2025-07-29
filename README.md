# Bia Energy - Prueba Técnica Data Engineer

## Requisitos
- Docker
- Docker Compose

## Instrucciones
1. Clonar el repositorio
2. Ejecutar `docker-compose up --build`
3. Ejecutar `python src/ingest.py` dentro del contenedor
4. Ejecutar `python src/reports.py` para generar reportes

## Estructura
- `src/ingest.py`: Ingesta y limpieza de datos
- `src/enrich.py`: Llamadas a API postcodes.io
- `src/db.py`: Conexión y creación de tablas PostgreSQL
- `src/reports.py`: Generación de reportes optimizados

## Decisiones
- Se usa asyncio para eficiencia
- Manejo de errores con logs estructurados
- PostgreSQL como base relacional por soporte a índices y consultas complejas

## Diagrama de arquitectura
Ver archivo `architecture_diagram.png`