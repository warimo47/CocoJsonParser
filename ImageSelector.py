import os
import os.path
import shutil


def ImageSelecting():
    print("Image selecting start")
    txtPathDir = "C:/Users/Dell2/Desktop/YoloTrain/DataSet/Coco_Train_"
    txtFileList = os.listdir(txtPathDir)

    imgPathDir = "C:/Users/Dell2/Desktop/YoloTrain/DataSet/Coco_Train_118287"

    for tfl in txtFileList:
        imgFileName = tfl[:12] + ".jpg"
        isFileExist = os.path.isfile(imgPathDir + "/" + imgFileName)
        if isFileExist is True:
            shutil.copy2(imgPathDir + "/" + imgFileName, txtPathDir + "/" + imgFileName)
        else:
            print("Error] 파일 없음")


if __name__ == '__main__':
    ImageSelecting()
    print("Program end")
