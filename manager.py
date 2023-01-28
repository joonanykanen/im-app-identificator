#!/usr/bin/python3

# Made by: Joona Nykänen
# Date: 28.01.2023

from Identificator import Identificator

if __name__ == '__main__':
    sampleURI = "visma-identity://confirm?source=netvisor&paymentnumber=102226"
    identity = Identificator(sampleURI)

    # None in case of an invalid path
    if identity.path != None:
        print(f"Path: {identity.path}")

    # None in case of invalid parameters
    if identity.params != None:
        print(f"Parameters: {identity.params}")

    if identity.path == None:
        print(f"Invalid URI. Please try again.")
    elif identity.params == None:
        print(f"Invalid {identity.path}-parameters. Please try again.")

# eof
