# ml-end-books-recommender-system

# End-to-End-Books-Recommender-System


## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


# How to run?

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
uv venv --python 3.8
```

```bash
conda activate books
source .venv/Scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt


uv init --python 3.8
#copy all the libraries into dependencies of pyproject.toml file
uv sync
```

```bash
#create file  .gitattributes with -> * text=auto eol=lf
git add .  # git restore --staged .
git status
git commit -m "project setup"
git push origin main
```

```bash
#for ipynb
uv add --dev ipykernel
```

```bash
# create template.py file and run
# add into pyproject.toml  
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["."]
include = ["ml_books_recommender_system*"]


# add the logging , exception and util (read yaml)

```





### STEP 03- Run the app.py file
```bash
streamlit run app.py
```

### STEP 04- Create DockerFile and Dockerignore




# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
  create EC2 
   name :books-recommender-dev
   machine : ubuntu machine (Ubuntu Server 26.04 LTS (HVM),EBS General Purpose (SSD) Volume Type.)
   instance : t3a.small (AMD)
   key pair : book
   network settings : shh / https / http
  Instance EC2
   security 
     security groups
       Edit inbound rules
        Add rule
          custom TCP 8501 - source 0.0.0.0.00
  Connect Machine        
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
#Go to github and clone the repo
git clone "your-project"
```

```bash
docker build -t entbappy/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 entbappy/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push entbappy/stapp:latest 
```

```bash
docker rmi entbappy/stapp:latest
```

```bash
docker pull entbappy/stapp
```





