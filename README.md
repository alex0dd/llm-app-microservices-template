# Microservices Template for LLM-Powered Applications

This is a template repository for building applications using microservices architecture. It includes a basic **frontend**, **backend**, an LLM serving engine (e.g., vLLM), and **nginx** as a reverse proxy. This template is designed to help you quickly set up and deploy applications that use large language models (LLMs) along with traditional web services.

## Architecture

- **Frontend**: Responsible for the frotnend part of the application.
- **Backend**: Handles the business logic and communicates with the LLM server.
- **LLM Server**: A serving engine (such as vLLM) that provides API endpoints for large language model inference.
- **Nginx**: Acts as a reverse proxy to route traffic between the frontend and backend.

## Project Structure

```bash
├── frontend/         # Source code for the frontend application
├── backend/          # Source code for the backend application
├── models/           # Directory for storing models (e.g., huggingface checkpoints)
├── nginx.conf        # Nginx configuration file
├── docker-compose.yml # Docker Compose configuration for orchestrating services
```

## Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/alex0dd/llm-app-microservices-template.git
   cd llm-app-microservices-template
   ```

2. **Configure the environment**:
   - Download a huggingface checkpoint of the model (e.g., [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct))
   - Place your the checkpoint directory in the `models/` directory.
   - Ensure the `nginx.conf` file is correctly configured (especially the llm_server section).

3. **Build and start the services**:

   With `vLLM`:
   ```bash
   docker-compose up --build
   ```

   With `ollama`:
   ```bash
   docker compose -f docker-compose-ollama.yaml up --build
   
   docker compose -f docker-compose-ollama.yaml up --build --force-recreate --remove-orphans
   ```

   This will build and start the following services:
   - `nginx`: Reverse proxy server
   - `frontend`: The web frontend, accessible via `http://localhost`
   - `backend`: The backend API server, accessible via `http://localhost/api`
   - `llm_server`: LLM serving engine, available for backend use, but not exposed to the public.

4. **Access the application**:
   - **Frontend**: `http://localhost`
   - **Backend API**: `http://localhost/api`

## Service Communication

- The **frontend** sends requests to the **backend**.
- The **backend** exposes the LLM via an API, communicates with the **llm_server** for model inference.

- **nginx** handles routing for public requests (i.e., requests to the frontend and backend), but it does not expose the LLM server directly to the outside world.

## Customization

1. **Frontend**: Modify the source code in the `frontend/` folder according to your frontend framework.
2. **Backend**: Implement your business logic in the `backend/` folder. Ensure it properly communicates with the LLM server.
3. **LLM Model**: Replace the model in `models/` with the one you want to use (e.g., Meta-Llama-3.1-8B-Instruct).
4. **LLM Server**: Replace the `llm_server` section in the `docker-compose.yaml` file with other servers such as [ollama](https://ollama.com/).

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Feel free to fork this repository and make contributions.