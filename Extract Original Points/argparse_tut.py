import argparse

parser = argparse.ArgumentParser(description='Atutorial of argparse!')
parser.add_argument("--i", help = "Input file. Should be the picking_list from CC. Make sure to include the whole path to the file along with the file name")
parser.add_argument("--o", help = "Output file. Make sure to include the whole path if you want it in a different directory")

args = parser.parse_args()
input_file = args.i
output_file = args.o
if output_file is None:
    print(input_file)