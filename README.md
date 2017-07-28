# EchoPath User FrontEnd 

EchoPath UF website 

## Setups to run in dev

1. Install `python`
2. Install all required dependencies by running `pip install -r requirements.txt`
3. Launch the application by running `sudo python src/app.py`
4. Navigate to http://localhost:5000/echopath to view the application

## Steps to run inside docker 
1. Install docker https://docs.docker.com/engine/installation/
2. Build docker image by running `docker build --tag=echopath-uf/image .`
3. Remove dangling images `docker rmi $(docker images -f dangling=true -q)`
4. Go in docker bash mode by running `docker run -ti -p 5000:5000 echopath-uf/image bash`
5. Launch the application by running `python src/app.py`
6. Navigate to http://localhost:5000/echopath to view the application

## Setups to run in prod
1. Install `python`
2. Install all required dependencies by running `pip install -r requirements.txt`
3. check old running instances of echopath-uf `ps aux| grep python`
4. Kill old running instances of echopath-uf `sudo kill -9 <process_ids>`
5. Remove old echopath-uf directory `rm -rf /home/ec2-user/echopath-uf/`
6. Get the latest release `git clone https://github.com/sheshankkodam/echopath-uf.git`
7. Get in to the directory `cd echopath-uf`
8. Launch the application by running `sudo nohup python src/app.py &`


## Author
sheshank kodam 