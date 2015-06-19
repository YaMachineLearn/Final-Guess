# coding=utf-8
import os

UTTER_NAME_FILE = "input/utterName.txt"
OUTPUT_FILE = "output/guess_the_is_a_and.csv"
WAV_FOLDER = "../MLDS_Final/wav/"

utterNameFile = open(UTTER_NAME_FILE)
outFile = open(OUTPUT_FILE, 'w')

outFile.write('id,sequence\n')
for utterName in utterNameFile:
    utterName = utterName.rstrip()
    utterFileSize = int(os.stat(WAV_FOLDER + utterName + '.wav').st_size)
    outFile.write(utterName + ',裚寋篕諆\n')
    # if utterFileSize > 50000:
    #     outFile.write(utterName + ',裚寋篕\n')
    # else:
    #     outFile.write(utterName + ',痲\n')

# utterNameFile.close()
# outFile.close()

# you 痲
# the 裚
# i   騿
# and 諆
# is  寋
# a   篕
# it  悱
# to  瘏
