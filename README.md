# Genetic algorithm using Cryptography
Research based assignment to decrypt the cipher with a key obtained using Genetic algorithm search

## How to run


* gaAlgo.py is complete code
  - If you are in windows:
	  Just double click gaAlgo.py
	  It is source code also Just open it with text application

* If you are in linux:
	  You can run it on sandcastle/LinuxShell by doing as follows,
	    after getting inside the folder using terminal
      
		python gaAlgo.pr

## How to change parameter

* Open gaAlgo.py using a text file or an IDE
* There are numbered parameter that will be changed from 1 to 5
  I have inserted comments in code as parameter number to identify
  
	i.e #parameter1, #parameter2

* Just search for parameter you want to change, using Ctrl+F or simple scrolling
	i.e search/look for 'parameter4' if you want to change it

* Parameters are,
	- parameter1: intial population
	- parameter2: keysize
	- parameter3: crossover rate and mutation rate (out of 100% not 1% i.e (98 out of 100) not (0.98 out of 1.0)
	- parameter4: Crossover type, Uncomment just one at a time and run
	- parameter5: encrypted string, uncomment one at a time. each string is placed under its keysize. 	


* and run!

## Filenames legend inside generated key String folders

- String 1 is 26 key string all over
- String 2 is 40 key string all over
- files are named on the bases what parameters were while for that file


Crossovers,

co1 : Uniform crossover
co2 : High point crossover
co3 : One point crossover

Given Parameter,

pm1 : given parameter set 1 i.e mutation :0% : crossover 0$
pm2 : given parameter set 2
.
.
pm5 : given (actually self tried) parameter set5

Strings,

str1: String 1 (26 key string)
str2: String 2 (40 key string)

Runs,

run1: run no. 1
.
.
run2: run no. 2

## Pre-requisites

You need to have python installed in the system to run this
