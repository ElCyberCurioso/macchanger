# MAC Changer with Python

Python3 tool to change MAC address of an interface (ethX or ensX)

## Setup

```bash
git clone https://github.com/ElCyberCurioso/macchanger
python3 macchanger.py <args>
```

## How to use

```python                        
usage: macchanger.py [-h] -i INTERFACE (-m MAC_ADDRESS | -r | --reverse | --no-reverse)

Tool for changing the MAC address of a network interface

options:
  -h, --help            show this help message and exit
  -i, --interface INTERFACE
                        Network interface name
  -m, --mac MAC_ADDRESS
                        New MAC address for the network interface
  -r, --reverse, --no-reverse
                        Reset the permanent MAC address

```

## Examples

Modifying MAC address:

```python
$ sudo python3 macchanger.py -i eth0 -m 00:50:08:11:22:00

[+] The MAC has been successfully changed!

$ macchanger -s eth0
Current MAC:   00:50:08:11:22:00 [wireless] (Compaq WL100)
```

Recovering original MAC address:

```python
$ sudo python3 macchanger.py -i eth0 -r                  

[+] The MAC has been successfully restored!

$ macchanger -s eth0                                     
Current MAC:   00:0c:29:f4:2b:53 (VMware, Inc.)
```
