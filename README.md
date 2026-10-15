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
#updates libraries
sudo apt-get update -y
sudo apt-get upgrade

#Install Docker

# Download the official Docker installation script and save it as get-docker.sh
curl -fsSL https://get.docker.com -o get-docker.sh
# Run the script with admin privileges: installs Docker and starts it
sudo sh get-docker.sh
# Add the "ubuntu" user to the docker group to run Docker without sudo
sudo usermod -aG docker ubuntu
# Apply the new group to the current session without logging out and back in
newgrp docker

```

```bash
#Go to github and clone the repo
git clone "your-project"
#Then -->>>> cd to the folder
```

```bash
#build on ec2 the image
docker build -t pcsiemat/bookapp:latest . 
```

```bash
#check the image
docker images -a  
```

```bash
#execute the image as a container
docker run -d -p 8501:8501 pcsiemat/bookapp 
```

```bash
#check the container running in a browser (Public IPv4 address on aws)
http://ip:8501
```bash

```bash
#check container is running
docker ps  
```

```bash
#stop and check de container stop
docker stop container_id
docker ps  -a
```

```bash
#remove all container that are stopped
docker rm $(docker ps -a -q)
```

## 3. Publish image on dockerhub (First log in)
```bash
#On EC2
docker login
#Copy link to browser 
```

```bash
#publish on docker hub
docker push pcsiemat/bookapp:latest 
```

```bash
#remove image form ec2
docker rmi pcsiemat/bookapp:latest
```

```bash
$get images from dockerhub
docker pull pcsiemat/bookapp
```





