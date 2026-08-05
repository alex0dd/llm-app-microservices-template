

# Plantilla de Microservicios para Aplicaciones con LLM

Este es un repositorio de plantilla para crear aplicaciones utilizando una arquitectura de microservicios. Incluye un **frontend** básico, un **backend**, un motor de servicio LLM (p. ej., vLLM) y **nginx** como proxy inverso. Esta plantilla está diseñada para ayudarte a configurar y desplegar rápidamente aplicaciones que utilizan modelos de lenguaje grandes (LLM) junto con servicios web tradicionales.

## Arquitectura

- **Frontend**: Responsable de la parte del frontend de la aplicación.
- **Backend**: Gestiona la lógica de negocio y se comunica con el servidor LLM.
- **LLM Server**: Un motor de servicio (como vLLM) que proporciona puntos finales de API para la inferencia de modelos de lenguaje grandes.
- **Nginx**: Actúa como proxy inverso para enrutar el tráfico entre el frontend y el backend.

## Estructura del Proyecto

```bash
├── frontend/         # Source code for the frontend application
├── backend/          # Source code for the backend application
├── models/           # Directory for storing models (e.g., huggingface checkpoints)
├── nginx.conf        # Nginx configuration file
├── docker-compose.yml # Docker Compose configuration for orchestrating services
```

## Requisitos previos

Asegúrate de tener lo siguiente instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Primeros pasos

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/alex0dd/llm-app-microservices-template.git
   cd llm-app-microservices-template
   ```

2. **Configura el entorno**:
   - Descarga un punto de control (checkpoint) del modelo de Hugging Face (p. ej., [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct))
   - Coloca el directorio del checkpoint en el directorio `models/`.
   - Asegúrate de que el archivo `nginx.conf` esté configurado correctamente (especialmente la sección llm_server).

3. **Construye e inicia los servicios**:

   Con `vLLM`:
   ```bash
   docker-compose up --build
   ```

   Con `ollama`:
   ```bash
   docker compose -f docker-compose-ollama.yaml up --build
   
   docker compose -f docker-compose-ollama.yaml up --build --force-recreate --remove-orphans
   ```

   Esto construirá e iniciará los siguientes servicios:
   - `nginx`: Servidor proxy inverso
   - `frontend`: La interfaz web, accesible mediante `http://localhost`
   - `backend`: El servidor de API backend, accesible mediante `http://localhost/api`
   - `llm_server`: Motor de servicio LLM, disponible para uso backend, pero no expuesto al público.

4. **Accede a la aplicación**:
   - **Frontend**: `http://localhost`
   - **Backend API**: `http://localhost/api`

## Comunicación entre servicios

- El **frontend** envía solicitudes al **backend**.
- El **backend** expone el LLM mediante una API y se comunica con el **llm_server** para la inferencia del modelo.

- **nginx** gestiona el enrutamiento para solicitudes públicas (es decir, solicitudes al frontend y backend), pero no expone el servidor LLM directamente al mundo exterior.

## Personalización

1. **Frontend**: Modifica el código fuente en la carpeta `frontend/` según tu marco de trabajo de frontend.
2. **Backend**: Implementa tu lógica de negocio en la carpeta `backend/`. Asegúrate de que se comunique correctamente con el servidor LLM.
3. **Modelo LLM**: Reemplaza el modelo en `models/` con el que desees usar (p. ej., Meta-Llama-3.1-8B-Instruct).
4. **Servidor LLM**: Reemplaza la sección `llm_server` en el archivo `docker-compose.yaml` con otros servidores como [ollama](https://ollama.com/).

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

## Contribuciones

Siéntete libre de bifurcar este repositorio y realizar contribuciones.
