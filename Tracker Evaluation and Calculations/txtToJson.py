import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', required=True)
parser.add_argument('-o', '--outputfile', required=True)
parser.add_argument('-t', '--typeoffile', required=True, help='hypotheses or annotations')
parser.add_argument('-fps', '--framespersecond', default=60, type=float, help='frames per second of video')

args = parser.parse_args()

if not(args.inputfile.endswith(".txt")):
    print("input file must be of .txt format")
    exit(-1)
if not(args.outputfile.endswith(".json")):
    print("output file must be of .json format")
    exit(-1)
if not(args.typeoffile == "hypotheses" or args.typeoffile == "annotations" ):
    print("wrong type entered")
    exit(-1)


input=args.inputfile
output=args.outputfile
type=args.typeoffile #<< control if file is hypotheses or groundtruth

annotations = {"frames":[],"class":'',"filename":''}  #<< Contains all boxes
annotations['class']="video" # << Set class , at end of json file
annotations['filename']="c:/Desktop/myfile/file.txt" #<< Set file name , at end of json file
list = []

class BOX:   #<< A class that contains a Box object , Think of as a Struct
    def __init__(self,Class,ID,x1,y1,x2,y2,dco):
        self.Class = Class
        self.ID =ID
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.dco=dco


def generate_json(fno, timestamp, list):  #<< Creates our json file

    image_dict = {"timestamp": float, "num": int, "class": '', str(type): []}  #<<This is the bif part of the json file
    coord_dict = {"dco": bool, "height": int, "width": int, "id": '', "y": int, "x": int} #<<here are the boxes
    string=[] #<< used to get around object reference when appending to 'annotations'
    for item1 in list: #<<for boxes i found in frame

        x1 = item1.x1
        y1 = item1.y1
        width =  item1.x2# << x2
        height =  item1.y2# <<y2
        dco = item1.dco
        ID = str(item1.ID)

        coord_dict['x'] = x1   #<<Fill the boxes dictionary
        coord_dict['y'] = y1
        coord_dict['width'] = width
        coord_dict['height'] = height
        coord_dict["dco"] = dco
        coord_dict["id"]=ID

        if (args.typeoffile == "hypotheses"):
            coord_dict.pop("dco")

        string=coord_dict.copy() #<< need copy as when we change coordict it changes everywhere its referenced even if its appended in a list
        image_dict[type].append(string)

    # print(image_dict['annotations'])
    # print("____________________________")


    image_dict["timestamp"] = timestamp  #<< add time stamp
    image_dict["num"] = fno #<< add frame no
    image_dict["class"] = "frame" #<<set class to whatever , here its called frame

    annotations['frames'].append(image_dict)  #<< add the data to frames

with open(input, "r") as file: #open input file and iterate line by line
    for line in file:

        box=line.strip().split(",")[1:]  #if frame contains many boxes add all of them to one line , without frame number appearing again and again

        x = int(line.split(",")[0]) #<<Get frame number for now , can take time stamp here too


        boxesofframe=",".join(box).split('#') #<<< Contain all boxes inside a frame #<<<Get all boxes from frame [Line as of what in the .txt file]

        for i in range (len(boxesofframe)):
            values=boxesofframe[i].split(',')  #<< get values from box
            list.append( BOX(str(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),bool(int(values[6])))) # add the values to list
        fps=60  #<< kinda know what fps we dealing with , can be passed as parameter later
        timestamp=x/fps #<< time in video = frame/fps = time in seconds
        generate_json(x,float(format(timestamp,".4f")),list) #<<take only 4 digits after decimal point, pass the lest and frame no and generate the json file
        list=[]

final=[]  #<< as array to contain the frame class
final.append(annotations) #<< as array

print('Number of Processed Images:', len(annotations["frames"]))  #<< print how many image processed
json_file = json.dumps(final,indent=4) #<<indent makes it look like more readable , set to 0 it becomes a single line
with open(output, 'w') as f:  #<<save to annotations.json ,,, may need to change it as parameter
    f.write(json_file) #<< write the file