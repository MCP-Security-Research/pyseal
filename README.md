# vurze

version control your python functions

high level overview:

A rust based pypi package that automatically adds decorators to all functions in a python file.
Also supports command line arguments for checking the version of functions ---> clap cli package
x
Have an decorator for every function and class in a python file ---> py03 rust python language bindings and use the python ast module
The decorator will use asymmetric encryption to ensure that the functions do not get updated ---> ____decide later_____
The private key could be stored in the users .env file
Basically it will act as a checksum to help detect potential security threats
x
For example: @toolname-9875348975
In the end, I would evaluate this based on how it prevents an attack from occuring
Attack → anything that involves changing the functions docstring or underlying code
Ex. Tool Poisoning Attack
ALSO: Could measure performance in the end!!!

1. start rust project
2. create test python files.
3. be able to parse and grab all functions in the file
