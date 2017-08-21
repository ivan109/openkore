#This converter script is created by windhamwong.

#This script is used for converting non-ASCII character in decompiled lua file generated by unluac into the correct character.

import re, sys, getopt

input_filepath = ''
output_filepath = ''

if (len(sys.argv) < 5):
	print 'luaConverter.py -i <inputfile> -o <outputfile>'
	sys.exit(2)

try:
	opts, args = getopt.getopt(sys.argv[1:],"i:o:")
except getopt.GetoptError:
	print 'luaConverter.py -i <inputfile> -o <outputfile>'
	sys.exit(2)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
	
for opt, arg in opts:
	if opt == '-h':
		print 'luaConverter.py -i <inputfile> -o <outputfile>'
		sys.exit()
	elif opt == "-i":
		input_filepath = arg
		print 'Input file: ', input_filepath
	elif opt == "-o":
		output_filepath = arg
		print 'Output file: ', output_filepath

try:
	input_file = open(input_filepath)
	input_lines = input_file.readlines()
	input_file.close()

	output_file = open(output_filepath, 'w')

	for single_line in input_lines:
		single_line = re.sub(r'\\(\d{3})', lambda match: chr(int(match.group(1))), single_line)
		output_file.write(single_line)
		
	output_file.close()
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise