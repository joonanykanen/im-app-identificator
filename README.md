# Identity Manager App

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

This repository contains mainly two files: Identificator.py that has Identificator-class for uri-parsing and -validation, and manager.py that contains Client-class for uri input.

Accepted sample uris:

- "visma-identity://login?source=severa"
- "visma-identity://confirm?source=netvisor&paymentnumber=102226"
- "visma-identity://sign?source=vismasign&documentid=105ab44"

## The problem

To me, the assignment was clear and well contstructed. I needed to implement a class that parses and validates uri-requests based on different criteria. The main focus for me was to make the validation as strict as possible so that no false positives would be going through, and the most importantly, code that works. This meant using no libraries that I don't know for certain.

I chose to go with Python since it is very flexible, follows OOP-practices and is easy to code with.

## Challenges

Even when the code-writing-part was pretty easy and straightforward, I wasn't completely sure if I was allowed to use any external libraries, what sort of error handling I should've chosen or what kind of specific criteria was allowed to go through the validation (e.g. does the order of params matter). I ended up making a solution, where it is easy to see the structure of the whole code and make changes accordingly if needed.

## Further Improvements

There is definitely room for improvement in the code:

- I might consider using `urllib` library for uri parsing to make the code more intuitive and readable
- I could raise custom exceptions instead of the current way of setting instance variables to None
- Refactoring the logic of param validation into separate methods in order to make the code even more readable and modular

For a real-life-opportunity I would be highly encouraged to ask delineate questions on the specific task for added certainty, and would be ready to take feedback that I could utilize accordingly.

## Added Notes

I wanted to make this assignment completely by my own without no use of trained A.I. models since I wanted to convey my thought process on producing code, not some A.I.'s. More importantly, I don't trust in them in production environment. I recognize that there could be better/more concise code to be written when using such tools or putting more than 2-3 hours of time/effort into the project, however I'm pretty happy with my result and feel like the assignment suits the given requirements.
