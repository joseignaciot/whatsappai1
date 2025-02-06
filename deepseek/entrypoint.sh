#!/bin/sh
# Lee la variable de entorno MODEL; si no está definida, usa el valor por defecto.
MODEL_NAME=${MODEL:-"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"}

# Ejecuta el servidor de vLLM con los parámetros deseados:
# - Usa CPU (--device cpu) y confía en el código remoto (--trust-remote-code).
# - Limita el espacio de swap a 2 GiB (--swap-space 2).
# - Desactiva el procesamiento asíncrono (--disable-async-output-proc).
# - Especifica el worker de uniproc para evitar errores en la resolución (–-worker-cls).
exec vllm serve "$MODEL_NAME" \
  --tensor-parallel-size 1 \
  --max-model-len 32768 \
  --disable-async-output-proc \
  --device cpu \
  --trust-remote-code \
  --swap-space 2 \
  

