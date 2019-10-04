# Introduction
This project creates g2p (grapheme to phoneme) as a micro-service inside of a Docker. It uses the https://github.com/sequitur-g2p/sequitur-g2p for g2p and wraps around the functions to serve as a micro-service.


# Dependencies

* Docker
* PyCharm (optional)

# PyCharm setup

* Add the folder "g2pDocker" in the PyCharm project
* You might have to add the docker plugin (PyCharm -> Prefs -> Plugin -> Search for 'Docker' and install)
* Secondary click on ```docker-compose.yaml``` and click run
  
  This should create the docker container with the required dependencies. You can verify that by running ```docker ps```
  
* Add the remote host as the docker container
  * PyCharm -> Preferences -> Build, Execution & Deployment -> Deployment
    * Add SFTP connection with the following details:\
      Host: localhost\
      Port: 7778\
      User name: debugger\
      Password: pwd\
      Click on 'Test Connection' and it should be successful\
      Click Apply and OK.
  
  * PyCharm -> Project:g2pDocker -> Preferences -> Project Interpreter
    * Click on '+' [Add Interpreter for the project]
    * Click on SSH Interpreter -> New Server Configuration\
      Host: localhost\
      Port: 7778\
      User name: debugger\
      Password: pwd\
      Add a mapping from the current working dir in host -> /home/debugger/g2pDocker/mapping [This will automatically sync the files to docker]
    * NOTE: Be careful not to map to /home/debugger/g2pDocker as this will overwrite all the files
  
  
# Non-PyCharm setup

* ```docker-compose docker-compose.yaml up```


# Build

You can now ssh into the docker container from Terminal

```ssh debugger@localhost -p 7778```\
Password: pwd

You should see the g2pDocker folder inside the container. cd in that and build the grpc files
```
cd g2pDocker
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. g2p.proto
```

This will generate ```g2p_pb2.py``` and ```g2p_pb2_grpc.py``` files which are python wrappers for grpc





