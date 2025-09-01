#!/usr/bin/env python3

import argparse, re, subprocess
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la direccion MAC de una interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-m", "--mac", dest="mac_address", help="Nueva direccion MAC para la interfaz de red")
    group.add_argument("-r", "--reverse", dest="reverse", action=argparse.BooleanOptionalAction, help="Setear nuevamente la MAC permanente")

    return parser.parse_args()

def is_valid_input(interface, mac_address, is_reverse):
    is_valid_interface = False
    is_valid_mac_address = False

    is_valid_interface = re.match(r"^[e][n|t][s|h]\d{1,2}$", interface)
    
    if not is_reverse:
        is_valid_mac_address = re.match(r"^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$", mac_address)

    return is_valid_interface, is_valid_mac_address

def change_mac_address(interface, mac_address, is_reverse):
    
    is_valid_interface, is_valid_mac_address = is_valid_input(interface, mac_address, is_reverse)

    if is_valid_interface:
        
        if is_reverse:
            subprocess.run(["macchanger", "-p", interface], stdout=subprocess.DEVNULL)

            print(colored(f"\n[+] La MAC se ha restaurado exitosamente!", "green"))
        elif is_valid_mac_address:
            subprocess.run(["ifconfig", interface, "down"])
            subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
            subprocess.run(["ifconfig", interface, "up"])

            print(colored(f"\n[+] La MAC ha sido cambiada exitosamente!\n", "green"))
    else:
        print(colored("\n[!] Los datos introducidos no son correctos\n", "red"))

def main():

    args = get_arguments()

    change_mac_address(args.interface, args.mac_address, args.reverse)

if __name__ == "__main__":
    
    main()