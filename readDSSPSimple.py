#!/usr/bin/python
# The line above tells the system which python command it should use

### RUNNING THE SCRIPT ####
# your can run the script by typing:
# > ./readDSSPSimple.py dssp_file_name
# or by typing
# > python readDSSPSimple.py directory_name
# Note: you first need to make your script executable by the user with:
# > chmod u+rx readDSSPSimple.py


### PACKAGES ####
# First we import some packages that we may  need
import sys  # system
import os   # operating system
import re   # regular expression
import math # math modules

### FILE NAMES ###
# Here we set the filenames that the program uses.

# output file
fn_out = "secondary_structure.txt"


### GLOBAL VARIABLES ###
# Here we put the "Global Variables" - variables that maybe accessed by all functions in this script

# stores the secondary structure element (sse) for each residue
# indexed by chain and residue number: dict_sse[chain][residue]=sse
dict_sse = dict()

# stores the amino acids (aa) for each residue
# indexed by chain and residue number: dict_aa[chain][residue]=aa
dict_aa = dict()


############## FUNCTION DEFINITIONS ####################
# It is important to keep your code modular,
# i.e. split the code into different funtions
# so that it is easy to interpret, read and debug




#########################################
### readDSSP, reads the DSSP file given as a command line argument
### and stores the information in dict_sse and dict_aa

def readDSSP(filename):

	#open file for reading
	print("opening file ", filename)
	# "r" indicates you open the file to read
	#try opening the file, and give warning if not possible
	try:
		infile = open(filename, 'r')
	except IOError: # In case of IOError return empty collection
		print("Error: Cannot open DSSP file " + filename + ".")
		exit(1)

        # keep track of the first line starting with "   #"
	start_reading = False

	# Loop over all the lines in the file:
	# "readlines()" will return a list with all the lines
	list = infile.readlines()

	for line in list:


		# rstrip remove the "\n" from the end of the line
		line =  line.rstrip()
		#print(f"---{line}---")
		#print(line.find("#"))

		index = line.find("#")

		# set the start_reading flag to True
		if index != -1: 
			print(f"Found '#' at indexin the list.")
			start_reading = True
		

		# START CODING
		# You need to set a condition when you can start
		# processing the lines. Have a look in the DSSP files
		# to see where you would like to start reading
		# # END CODING


		# #  only start processing if start_reading == True
		elif(start_reading):
			# print('start reading')

			# get information from the DSSP file, see
			# http://swift.cmbi.ru.nl/gv/dssp/

			# get amino acid type
			aa = line[13]
			# print(aa)

			# skip amino acids marked '!'
			if(aa == '!'):
				continue

			# get residue number
			res_num  = int(line[5:10].strip())

			# START CODING
			# obtain the 'chain' and 'sse' (secondary structure)
			# from the line, as above
			# chain ID

			chain = line[11]
			sse = line[9]





		# 	# END CODING


		# 	# check if chain has been seen before,
		# 	# if not create new dictionary for chain
			if(chain not in dict_sse):
				dict_sse[chain] = dict()
				dict_aa[chain] = dict()

			# store sse and aa in dictionaries
			dict_sse[chain][res_num]=sse
			dict_aa[chain][res_num]= aa


		#end if start reading
	# end loop readlines()

	# close the infile
	infile.close()

# end function readDSSP


###########################################
# This function prints the propensities, based on the counts

def printSecondaryStructure(fn_out):
	print('print secondary structure')

	# open outfile, to write
	outfile = open(fn_out,'w')

	# print column names to outfile
	print("chain","resnum","aa","sse", file=outfile)

	# obtain all chains
	list_chains = sorted(dict_sse.keys())

	# loop over all the chains
	for chain in list_chains:

		# obtain all residues numbers in chain
		list_resnum =  sorted(dict_sse[chain].keys())

		# print(list_resnum)

		#print(dict_aa)


		# START CODING HERE
		# print the chain, residue number, amino acid and
		# secondary structure type to the outfile

		print(chain, list_resnum, dict_aa[chain], dict_sse[chain],  file=outfile)

		

		# END CODING HERE

	# end for loop over chains

	# close outfile
	outfile.close()
	print("written file", fn_out)

# end function printSecondaryStructure


############## PROGRAM ##################


#read DSSP file
# sys.argv1 contains a command line argument
readDSSP(sys.argv[1])

# Print out secondary structure
printSecondaryStructure(fn_out)
