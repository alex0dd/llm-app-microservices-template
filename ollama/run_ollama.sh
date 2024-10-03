#!/bin/bash

echo "Starting Ollama server..."
ollama serve &  # Start Ollama in the background

sleep 6s

echo "Ollama is ready, creating the model..."

# Pull the model (needs ollama to be running as well)
ollama create your_model -f /ollama/Modelfile
ollama run your_model

# Kill the process after the model has been downloaded
ps -ef | grep 'ollama serve' | grep -v grep | awk '{print $2}' | xargs -r kill -9
# Do the actual serving
ollama serve