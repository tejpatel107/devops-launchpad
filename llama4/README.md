

# Deploy with docker on Linux:
docker run --runtime nvidia --gpus all \
	--name my_vllm_container \
	-v ~/.cache/huggingface:/root/.cache/huggingface \
 	--env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
	-p 8000:8000 \
	--ipc=host \
	vllm/vllm-openai:latest \
	--model meta-llama/Llama-4-Scout-17B-16E-Instruct
