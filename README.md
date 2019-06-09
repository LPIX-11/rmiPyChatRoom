# RMI-Py-ChatRoom
![python picture](https://hdqwalls.com/download/python-qhd-3840x2160.jpg)
Simple RMI ChatRoom in [python](https://www.python.org/) with multi-threading allowing up to 100 clients per server using python3.7 version.

## Set Up
Install python 3.7 environment
* [Install Python 3.7 On Linux](https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/)
* [Install Python 3.7 On Windows](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Install Python 3.7 On Mac](https://wsvincent.com/install-python3-mac/)

### Start The Program
```sh
  # Enter in the project
  cd rmiPyChatRoom

  # Start the server first by specifying the ip adress and the port number
  python3.7 server.py 127.0.1.1 5000

  # Or if your defaut python instace is  set to 3.7 just type
  python server.py 127.0.1.1 5000

  # Then you can start as many client as you want by just starting the client specifying the ip and the port
  python3.7 client.py 127.0.1.1 5000

  # Or
  python client.py 127.0.1.1 5000
```
