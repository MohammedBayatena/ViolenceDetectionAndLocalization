import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', required=True)
parser.add_argument('-o', '--outputfile', required=True)

args = parser.parse_args()

if not(args.inputfile.endswith(".txt") and args.outputfile.endswith(".txt")):
    print("Files are not correct")
    exit(-1)

input=args.inputfile
output=args.outputfile

writefile = open(output, "w") #outputfile
with open(input, "r") as file: #open input file and iterate line by line
    id=0 #first frame ID
    firsttime=True
    for line in file:

        box=line.strip().split(",")[1:]  #if frame contains many boxes add all of them to one line , without frame number appearing again and again
        x = int(line.split(",")[0]) #check what frame are we in , if still in same frame time to concatinate on same line
        if(x==id and firsttime==False):
            writefile.write('#')
            writefile.write(','.join(box))

        elif(x==id and firsttime==True):
            writefile.write((str(x)+","))
            writefile.write((','.join(box)))
            firsttime = False

        elif (x!=id):
            writefile.write("\n")
            writefile.write(str(x)+','+','.join(box))
            firsttime=False
            id+=1

writefile.close()
print("File processed Succesfully!")