# x18. C - Dynamic libraries

## Project Objectives

- What is a dynamic library, how does it work, how to create one, and how to use it
- What is the environment variable $LD_LIBRARY_PATH and how to use it
- What are the differences between static and shared libraries
- Basic usage nm, ldd, ldconfig

## Files and there purposes

1. libdynamic.so; C dynamic library containing the function definitions

2. main.h; Header files containing the function prototypes

3. 1-create_dynamic_lib.sh; Bash script that creates a dynamic library called liball.so from all the .c files that are in the current directory

4. 100-operations.so; C dynamic library that contains C functions that can be called from Python

5. random.so; C dynamic library to inject in a giga million program

6. 101-make_me_win.sh; Bash script to inject the libmask.so library, using LD_PRELOAD, in the giga million program
