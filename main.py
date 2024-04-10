import os   # 导入os模块
import imagesize
import easyocr
import cv2
from PIL import Image

def get_image_size(image_path):
    try:
        width, height = imagesize.get(image_path)
        return width, height
    except:
        # print('文件损坏')
        return 0,0

#猫猫bot
def check_desu_image(width, height):
    # 谱面分数, ppvs, 个人信息, 个人信息v2
    if (width == 1950 and height == 1088 or width == 1134 and height == 1553 or width == 1200 and height == 857 or width == 1920 and height == 1267):
        return True
    else:
        return False
#白菜bot
def check_cabbage_image(width, height):
    #pptth, 
    if (width == 736 and height == 421):
        return True
    else:
        return False
#雨沐bot
def check_yumu_image(filename):
    #pptth, 
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cropped = img[8:33, 150:220]
    ret1, thresh1 = cv2.threshold(cropped, 252, 255, cv2.THRESH_BINARY_INV)
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(thresh1)
    for detection in result:
        text = detection[1]
        confidence = detection[2]
        print(f'Text: {text}, Confidence: {confidence}')
        if "yumu" in text.lower():
            return True
    return False

def check_image(filename):
    width, height = get_image_size(filename)
    if check_desu_image(width,height) or check_cabbage_image(width,height):
        return True
    elif (width == 1920 and height == 1080):
        return check_yumu_image(filename)
    else:
        return False
    
if __name__ == "__main__":
    path = ""       # 指定要遍历的根目录
    full_size = 0
    
    print("【",path,"】 目录下包括的文件和目录：")
    for root, dirs, files in os.walk(path, topdown=True):  # 遍历指定目录
        """
        for name in dirs:            # 循环输出遍历到的子目录
            pass
            #print("∏",os.path.join(root, name))
        """
        for name in files:           # 循环输出遍历到的文件
            if check_image(os.path.join(root, name)):
                print(os.path.join(root, name),end='\t')
                print(os.stat(os.path.join(root, name)).st_size)
                full_size += os.stat(os.path.join(root, name)).st_size
    
    print(full_size)
