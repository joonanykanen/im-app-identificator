#!/usr/bin/python3

# Made by: Joona Nykänen
# Date: 28.01.2023

from Identificator import Identificator


class Client:
    def __init__(self, uri: str):
        identity = Identificator(sampleURI)

        # None if path is invalid
        if identity.path != None:
            print(f"Path: {identity.path}")

        # None if parameters are invalid
        if identity.params != None:
            print(f"Parameters: {identity.params}")

        if identity.path == None:
            print(f"Invalid URI. Please try again.")
        elif identity.params == None:
            print(f"Invalid {identity.path}-parameters. Please try again.")


if __name__ == '__main__':
    sampleURI = "visma-identity://confirm?source=netvisor&paymentnumber=102226"
    client = Client(sampleURI)


# eof
