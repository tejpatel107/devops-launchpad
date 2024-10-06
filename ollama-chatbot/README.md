
# Chatbot with Ollama

This repository contains a simple chatbot application built using OpenWebUI and an [Ollama](https://ollama.ai/) model backend for generating responses. The application takes user inputs via a text box and sends them to the Ollama backend to generate responses using a specified model.

## Features

- **Interactive Chatbot Interface**: Built with OpenWebUI to provide a simple UI for interactions.
- **Ollama Backend Integration**: Connects to the Ollama backend server for LLM-based responses.
- **Environment Configuration**: Easily configure the Ollama backend server IP using an environment variable.


## Option 1: On your local Laptop

### Step 1: Ensure Docker Destop is installed and Running

https://www.docker.com/products/docker-desktop/

```
bcr@Surface:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bcr@Surface:~$
```

### Step 2: Download Ollama Image 

```
sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Output

```
sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
Unable to find image 'ollama/ollama:latest' locally
latest: Pulling from ollama/ollama
6414378b6477: Pull complete
565ec4b441fe: Pull complete
f159bfc8d800: Pull complete
f9aa9bba7fad: Pull complete
450c78a4a605: Pull complete
d7e3ad6c5000: Pull complete
9901a35ab7cb: Pull complete
e961bfcbe854: Pull complete
Digest: sha256:e458178cf2c114a22e1fe954dd9a92c785d1be686578a6c073a60cf259875470
Status: Downloaded newer image for ollama/ollama:latest
e276c51f880190c6fbfebe882acb13be06a77abbcabbf25cc19fd339621cd896
```

### Step 3: Download Llama 3.2 Model

```
sudo docker exec -it ollama ollama run llama3.2:1b
```
Output

```

```

### Step 4: Run Open Web UI

```
sudo docker run -d -p 8080:8080 -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Output

```
sudo docker run -d -p 8080:8080 -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
Unable to find image 'ghcr.io/open-webui/open-webui:main' locally
main: Pulling from open-webui/open-webui
a2318d6c47ec: Pull complete
40d734479f14: Pull complete
0b61b7b259eb: Pull complete
081a3493c0e7: Pull complete
e8027c27b65b: Pull complete
4f4fb700ef54: Pull complete
a211859e0845: Pull complete
3b28612a0571: Pull complete
cdf3f759b3fe: Pull complete
e87b4dba0a22: Pull complete
ff39ce906d48: Pull complete
bfef8e5c9c46: Pull complete
a544a30bf073: Pull complete
aa4fd87f36bc: Pull complete
ee8afd7ae231: Pull complete
Digest: sha256:b2262995f1dceed066324f4dbcca6f0971a197a66cfb5c55bfbe362242d4c1d2
Status: Downloaded newer image for ghcr.io/open-webui/open-webui:main
ac0f5a1751025a23cc60140602337b88a19d43f6dc8885525dcd3d69dc45b202
```

Check all Running containers

bcr@Surface:~$ sudo docker ps
CONTAINER ID   IMAGE                                COMMAND               CREATED         STATUS                            PORTS                      NAMES
ac0f5a175102   ghcr.io/open-webui/open-webui:main   "bash start.sh"       7 seconds ago   Up 5 seconds (health: starting)   0.0.0.0:8080->8080/tcp     open-webui
4ee4d125eeca   ollama/ollama                        "/bin/ollama serve"   5 minutes ago   Up 5 minutes                      0.0.0.0:11434->11434/tcp   ollama
bcr@Surface:~$
```

Open the Web UI at http://localhost:8080



## Option 2: On Denvr AI Cloud

### Step 1: Denvr Cloud Account

Setup your account to launch your GPU of choice ( A100-40G, A100-80G, H100, Gaudi2 )

https://console.cloud.denvrdata.com/account/login

### Step 2: Launch the VM

<img width="1126" alt="image" src="https://github.com/user-attachments/assets/0b226da0-0b1c-4551-a561-9032d30b48f1">



### Step 3: Install/Update packages

```
sudo apt update -y

```


### Step 4: Install Ollama and server Llama 3.2 1B model

```
sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
sudo docker exec -it ollama ollama run llama3.2
```

### Open Web UI

Alternatively you can deploy Open web UI too, if you are only interested in chatbot but not Coding

```
sudo docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

## Troubleshooting

- **Environment Variable Not Set**: If the application is not connecting to the Ollama backend, ensure that the `OLLAMA_IP` variable is set correctly and that the server is reachable.
- **Port Issues**: Ensure that port `11434` (or the port you specified) is open and accessible.


## Contributing

If you would like to contribute, please fork the repository and submit a pull request with your changes.

