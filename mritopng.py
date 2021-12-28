import os
from typing import final
import png
import pydicom as dicom
import numpy as np
from pydicom.pixel_data_handlers.util import apply_color_lut
from PIL import Image

def mri_to_png(mri_file, png_file,plt):
    """ Function to convert from a DICOM image to png

        @param mri_file: An opened file like object to read te dicom data
        @param png_file: An opened file like object to write the png data
    """

    # Extracting data from the mri file
    plan = dicom.read_file(mri_file)
    shape = plan.pixel_array.shape
    
    ims = plan.pixel_array
    print("Load Dicom image")
    pa = (ims.astype(np.float)-ims.min())*255.0 / (ims.max()-ims.min())
    print("img converting....")
    if plt: # Appling palette 
        rgb = apply_color_lut(pa,palette=plt)
        im = Image.fromarray(rgb)
        im.save(png_file)
    else: # Normal palette
        image_2d = []
        max_val = 0
        for row in  plan.pixel_array:
            pixels = []
            for col in row:
                pixels.append(col)
                if col > max_val: max_val = col
            image_2d.append(pixels)
        # Rescaling grey scale between 0-255
        image_2d_scaled = []
        for row in image_2d:
            row_scaled = []
            for col in row:
                #####
                col_scaled = int((float(col) / float(max_val)) * 255.0)
                row_scaled.append(col_scaled)
            image_2d_scaled.append(row_scaled)
    # Writing the PNG file
        w = png.Writer(shape[1], shape[0], greyscale=True)
        w.write(png_file, image_2d_scaled)
    print("converting Done")

def convert_file(mri_file_path, png_file_path):
    """ Function to convert an MRI binary file to a
        PNG image file.

        @param mri_file_path: Full path to the mri file
        @param png_file_path: Fill path to the png file
    """
    
    # Making sure that the mri file exists
    if not os.path.exists(mri_file_path):
        # raise Exception('File "%s" does not exists' % mri_file_path)
        print('File "%s" does not exists' % mri_file_path)
        return

    # Making sure the png file does not exist
    if os.path.exists(png_file_path):
        # raise Exception('File "%s" already exists' % png_file_path)
        print('File "%s" already exists' % png_file_path)
        return
    print(f"Processing Started : file - {png_file_path}")
    palette_arr=["PET_20_STEP","HOT_IRON","PET","HOT_METAL_BLUE",""]
    png_file_path1=png_file_path
    paths = png_file_path.split("/")
    for plt in palette_arr:

        plt1=plt
        if not plt:
            plt1="Normal"
        if len(paths)==2: 
            try:
                os.makedirs(paths[0]+"/"+plt1)
            except:
                print("Procesing on",paths[0])
            png_file_path=paths[0]+"/"+plt1+"/"+paths[1]
        else:
            png_file_path=plt1+"_"+png_file_path
        print(f"Processing Started : palette - {plt1}")
        mri_file = open(mri_file_path, 'rb')
        png_file = open(png_file_path, 'wb')

        mri_to_png(mri_file, png_file,plt)

        png_file.close()
        print(f"Processing Done : file - {png_file_path}")
        png_file_path=png_file_path1

def convert_folder(mri_folder, png_folder):
    """ Convert all MRI files in a folder to png files
        in a destination folder
    """
    print(f"Processing Started : folder - {mri_folder}")
    try:
        # Create the folder for the pnd directory structure
        os.makedirs(png_folder)
        fc = "y"
    except:
        print("your folder is already. if you replaced your old data with new data enter y")
        fc = input("Enter here :- ")
    if fc =="y" or fc =="Y":
        # Recursively traverse all sub-folders in the path
        for mri_sub_folder, subdirs, files in os.walk(mri_folder):
            for mri_file_path in files:
                file_name,ext=os.path.splitext(mri_file_path)
                if True:
                    png_file_path = png_folder+"/"+file_name+".png"
                    try:
                        # Convert the actual file
                        convert_file(mri_folder+"/"+mri_file_path, png_file_path)
                        print ('SUCCESS>', mri_folder+"/"+mri_file_path, '-->', png_file_path)
                    except Exception as e:
                        print ('FAIL>', mri_file_path, '-->', png_file_path, ':', e)
        print(f"Processing Done : folder - {mri_folder}")
    else:
        print("Please change your floder name and try again")


if __name__ == '__main__': 
   dicom_path = "./dcm_img" # Your DICOM file/folder path
   png_path = "png_folder" # Your PNG file/folder path
   if os.path.isdir(dicom_path):
       print(f"Working with folder' {dicom_path}")
       convert_folder(dicom_path, png_path)
   else:
        try:
            os.makedirs("Dicom_Png_images")
            print("Create Folder :- Dicom_Png_images")
        except:
            print("Folder Exist :- Dicom_Png_images")
        finally:
            png_path="Dicom_Png_images/"+png_path
            print(f"Working with file' {png_path}")
            convert_file(dicom_path, png_path)
