
# Chatbot with Ollama

This repository contains a simple chatbot application built using OpenWebUI and an [Ollama](https://ollama.ai/) model backend for generating responses. The application takes user inputs via a text box and sends them to the Ollama backend to generate responses using a specified model.

## Features

- **Interactive Chatbot Interface**: Built with OpenWebUI to provide a simple UI for interactions.
- **Ollama Backend Integration**: Connects to the Ollama backend server for LLM-based responses.
- **Environment Configuration**: Easily configure the Ollama backend server IP using an environment variable.


## Option 1: On your local Laptop ( Windows )

### Step 1: Ensure Docker Desktop and `nvidia-smi` are installed and Running

https://www.docker.com/products/docker-desktop/

```
 sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
```
>nvidia-smi.exe
Sat Apr 19 13:35:25 2025
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 538.78                 Driver Version: 538.78       CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                     TCC/WDDM  | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA RTX A2000 8GB Lap...  WDDM  | 00000000:01:00.0  On |                  N/A |
| N/A   44C    P5               7W /  80W |   5570MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
```

### Step 2: Download Ollama with GPU support

```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Output

```
PS C:\beCloudReady> docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
Unable to find image 'ollama/ollama:latest' locally
latest: Pulling from ollama/ollama
f45c5ef3e181: Pull complete
161508c220d5: Pull complete
d9802f032d67: Pull complete
0d15e460e575: Pull complete
Digest: sha256:96b7667cb536ab69bfd5cc0c2bd1e29602218e076fe6d34f402b786f17b4fde0
Status: Downloaded newer image for ollama/ollama:latest
53ff742791ae2aa54b1af8fe16c09e91d730f4f8d753bf14e9a903cc6f13d991
```

### Step 3: Download Llama 3.2 Model

```
PS C:\beCloudReady> docker exec -it ollama ollama run llama3.2
pulling manifest
pulling dde5aa3fc5ff... 100% ▕███████████████████████████████████████▏ 2.0 GB
pulling 966de95ca8a6... 100% ▕███████████████████████████████████████▏ 1.4 KB
pulling fcc5a6bec9da... 100% ▕███████████████████████████████████████▏ 7.7 KB
pulling a70ff7e570d9... 100% ▕███████████████████████████████████████▏ 6.0 KB
pulling 56bb8bd477a5... 100% ▕███████████████████████████████████████▏   96 B
pulling 34bb5ab01051... 100% ▕███████████████████████████████████████▏  561 B
verifying sha256 digest
writing manifest
success
>>> Hello how are you?
I'm just a computer program, so I don't have feelings, but thank you for asking! How can I assist
you today? Is there something on your mind that you'd like to chat about or ask for help with?
I'm all ears (or rather, all text).

>>> Send a message (/? for help)
```

### Step 3.1: Ensure Ollama is using GPU

```
docker exec -it ollama ollama ps
NAME               ID              SIZE      PROCESSOR    UNTIL
llama3.2:latest    a80c4f17acd5    4.0 GB    100% GPU     4 minutes from now
```

### Step 3.2: Find the Bridge (internal IP) of the Ollama container

```
docker inspect  ollama | findstr "IP"
```
Expected Output

```
 docker inspect  ollama | findstr "IP"
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
                    "IPAMConfig": null,
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
```

In this example the IP of Ollama container is `172.17.0.2`

### Step 4: Run Open Web UI with Ollama container IP

```

docker run --network=bridge -d -p 8080:8080 -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Output

```
sudo docker run --network=bridge -d -p 8080:8080 -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
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
```
sudo docker ps
CONTAINER ID   IMAGE                                COMMAND               CREATED         STATUS                   PORTS                      NAMES
4d5971c450cf   ollama/ollama                        "/bin/ollama serve"   5 minutes ago   Up 5 minutes             0.0.0.0:11434->11434/tcp   ollama
238432e6d2dd   ghcr.io/open-webui/open-webui:main   "bash start.sh"       6 minutes ago   Up 6 minutes (healthy)   0.0.0.0:8080->8080/tcp     open-webui
```

Open the Web UI at http://localhost:8080

![image](https://github.com/user-attachments/assets/1aa44484-8327-4947-bf90-0e77d4dd56b7)

"Sign up" with any email ID ( does NOT have to be a valid one )

![image](https://github.com/user-attachments/assets/4c8cf066-8535-4c01-b964-2e0a1b5632c7)

If you are unable to see Ollama backend "Select a model"

![image](https://github.com/user-attachments/assets/32d2cf3d-0206-4037-a689-1dfbae5fb86c)

Then goto "Setting" -> Admin Setting -> Connection

![image](https://github.com/user-attachments/assets/eb05a998-a89a-4351-8587-83b8b307b0a9)

Then goto "Setting" -> Admin Setting -> Connection
![image](https://github.com/user-attachments/assets/0e54b11f-874e-45a9-8de8-9dabd9bdb9ae)

Enter the IP of the Ollama Docker container

```
 sudo docker inspect ollama | grep IPAddress
```

Output

```
 sudo docker inspect ollama | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.3",
                    "IPAddress": "172.17.0.3",
```

### Now you are all set with your Personal Chatbot of your Laptop

![image](https://github.com/user-attachments/assets/b1dd25c4-2f1f-48f2-9ab7-bb10b2e05e58)


## Troubleshooting

- **Environment Variable Not Set**: If the application is not connecting to the Ollama backend, ensure that the `OLLAMA_IP` variable is set correctly and that the server is reachable.
- **Port Issues**: Ensure that port `11434` (or the port you specified) is open and accessible.


## Contributing

If you would like to contribute, please fork the repository and submit a pull request with your changes.

