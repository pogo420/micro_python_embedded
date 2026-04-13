# micro_python_embedded
Learning Micro python for SoC


## Pyboard setup
* Install esptool: `pip install esptool`
* Find the port for SoC: `ls /dev/tty.*`
* Erase flash: `esptool.py --port /dev/tty.<soc> erase_flash`
* Upload binary: `esptool.py --port /dev/tty.<soc> --baud 460800 write_flash --flash_size=detect 0 soc.bin`
* Install rshell: `pip install rshell`
* Log into the device: `rshell -p /dev/tty.<soc>`
* Soc file system: `/pyboard/`
* Copy the code: `cp main.py /pyboard/`
* P.S. Execution starts from `main.py`
