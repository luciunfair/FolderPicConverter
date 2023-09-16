import os 
import cv2

def pic_conv(pic_main_dir, pic_target_dir, desired_size = 640, padding = False, pad_color=[0,0,0]):
    """ 
    This function is a picture converter. You provide the address of the folder containing pictures,
    and it will convert all your pictures to your desired size, and save them in your target directory,
    with the option of adding padding or not. You can also choose the color of the padding
    
    arguments:
    pic_main_dir -- picture main directory like "E:/dogs", that dogs is the folder that cotrains pictures of dogs of any size
    pic_target_dir -- picture target directory that you want to save your converted pictures in it like "E:/dogs_fixed_size" 
    desired_size -- the size that want all of your picture to become , the default is 640x640
    padding -- whether having padding or not, 
    note that any pictures that is smaller than desired size in width or height will fill with padding of desired color 
    pad_color -- padding color, note that its in RGB format and it's default is black
    """
    
    all_pic = os.listdir(pic_main_dir) # list all of the pictures name in a list
    for pic in all_pic:
        pic_addr =  pic_main_dir + "/" + pic  # picture address
        pic_read = cv2.imread(pic_addr) # reading a picture
        pic_addr_target = pic_target_dir + "/" + pic 
        if padding == True :
            old_size = pic_read.shape[:2]
            ratio = float(desired_size)/max(old_size)
            new_size = tuple([int(x*ratio) for x in old_size])   
            pic_read = cv2.resize(pic_read, (new_size[1], new_size[0]))   
            delta_w = desired_size - new_size[1]
            delta_h = desired_size - new_size[0]
            top, bottom = delta_h//2, delta_h-(delta_h//2)
            left, right = delta_w//2, delta_w-(delta_w//2)
            pad_color = [0, 0, 0]
            new_pic = cv2.copyMakeBorder(pic_read, top, bottom, left, right, cv2.BORDER_CONSTANT,
                value=pad_color)
        else : # it means that padding is set to  False
            new_pic = cv2.resize(pic_read,(desired_size, desired_size))
        cv2.imwrite(pic_addr_target, new_pic)


""" *****example*****

if __name__ == "__main__":
    pic_main_dir = "E:/dogs"
    pic_target_dir =""E:/dogs_fixed_size"
    pic_conv(pic_main_dir, pic_target_dir, desired_size = 1080, padding = False, pad_color=[0,0,0])
"""