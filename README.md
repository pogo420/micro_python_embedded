# micro_python_embedded
Learning Micro python for SoC


## Pyboard setup
### First time
* Install esptool: `pip install esptool`
* Find the port for SoC: `ls /dev/tty.*`
* Erase flash: `esptool.py --port /dev/tty.<soc> erase_flash`
* Upload binary: `esptool.py --port /dev/tty.<soc> --baud 460800 write_flash --flash_size=detect 0 soc.bin`
* Install rshell: `pip install rshell`
### Recurring
* Find the port for SoC: `ls /dev/tty.*`
* Log into the device: `rshell -p /dev/tty.<soc>`
* Soc file system: `/pyboard/`
* Copy the code: `cp main.py others_code.py /pyboard/`
* P.S. Execution starts from `main.py`
* Execute `repl`
* Press reset in board(esp8266)
### Exit process:
* From repl: control + x
* From rshell: control + c
 