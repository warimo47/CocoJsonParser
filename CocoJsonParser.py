import json


def JsonParsing():
    print("Start json parsing")
    jsonFile = open('instances_train2017.json')
    jsonString = json.load(jsonFile)
    imagesList = jsonString.get("images")
    imageDict = {}
    for il in imagesList:
        il_imageID = il.get("id")
        il_imageFileName = il.get("file_name")
        il_width = il.get("width")
        il_height = il.get("height")
        imageDict[il_imageID] = [il_imageFileName, il_width, il_height, [], False]

    annotationsList = jsonString.get("annotations")
    for al in annotationsList:
        al_imageID = al.get("image_id")
        al_categoryID = al.get("category_id")
        bl_class = -1
        if al_categoryID == 1:  # person -> SENU
            bl_class = -1  # bl_class = 13
        elif al_categoryID == 3:  # car -> Vehicle
            bl_class = -1  # bl_class = 0
        elif al_categoryID == 6:  # bus -> Bus
            bl_class = -1  # bl_class = 7
        elif al_categoryID == 8:  # truck -> Truck
            bl_class = -1  # bl_class = 1
        elif al_categoryID == 15:  # bench
            bl_class = -1
        elif al_categoryID == 16:  # bird
            bl_class = -1
        elif al_categoryID == 17:  # cat -> Dog_Cat
            bl_class = 10
            imageDict[al_imageID][4] = True
        elif al_categoryID == 18:  # dog -> Dog_Cat
            bl_class = 10
            imageDict[al_imageID][4] = True
        elif al_categoryID == 19:  # horse -> Dog_Cat
            bl_class = 10
            imageDict[al_imageID][4] = True
        al_bbox = al.get("bbox")
        al_u_center = (al_bbox[0] + al_bbox[2] / 2) / imageDict[al_imageID][1]
        al_v_center = (al_bbox[1] + al_bbox[3] / 2) / imageDict[al_imageID][2]
        al_width = al_bbox[2] / imageDict[al_imageID][1]
        al_height = al_bbox[3] / imageDict[al_imageID][2]
        if bl_class != -1:
            imageDict[al_imageID][3].append([bl_class, al_u_center, al_v_center, al_width, al_height])

    for idi in imageDict.values():
        writeFileName = "../YoloTrain/DataSet/Coco_Train_/" + idi[0][:12] + ".txt"
        if idi[4] is True:
            for bl in idi[3]:
                fi = open(writeFileName, "a")
                fi.write(f"{bl[0]} {bl[1]:.06f} {bl[2]:.06f} {bl[3]:.06f} {bl[4]:.06f}\n")
                fi.close()


if __name__ == '__main__':
    JsonParsing()
    print("Program end")
