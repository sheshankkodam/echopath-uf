# EchoPath User FrontEnd 

EchoPath UF website 

## Setups to run in dev

1. Install `python`
2. Install all required dependencies by running `pip install -r requirements.txt`
3. Launch the application by running `python src/app.py`
4. Navigate to http://localhost:5000/echopath to view the application

## Steps to run inside docker 
1. Install docker https://docs.docker.com/engine/installation/
2. Build docker image by running `docker build --tag=echopath-uf/image .`
3. Remove dangling images `docker rmi $(docker images -f dangling=true -q)`
4. Go in docker bash mode by running `docker run -ti -p 5000:5000 echopath-uf/image bash`
5. Launch the application by running `python src/app.py`
6. Navigate to http://localhost:5000/echopath to view the application


## Author
sheshank kodam 