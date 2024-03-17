import subprocess
import sys
import glob

def extractAndSave(inPath, outPath):
    command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(inPath, outPath)
    subprocess.call(command, shell=True)
    
if __name__ == "__main__":
    inPath = str(sys.argv[1])
    outPath = str(sys.argv[2])
    videoFiles = glob.glob(inPath+'/*.mp4')
    for i in videoFiles:
        fileName = i.split('/')[-1].split('.')[0]
        print(i)
        print(outPath+fileName+".wav")
        extractAndSave(i, outPath+fileName+".wav")