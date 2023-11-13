from PIL import Image, ImageEnhance, ImageFilter
import glob
import os
import shutil
import pillow_heif

# To use this code :
# First run all the HEIC move command to shift all HEIC files to a working space.


user_p = os.environ.get('USERPROFILE')
pictdir = os.path.join(user_p,'Pictures')
Exts = ['HEIC','heic']

def heic_2_jpg():

    pictureFolder = "Beau"
    HEIC_Folder = " HEIC extenstion"
    Working_HEIC_Folder = pictureFolder.strip() + HEIC_Folder

    homepath = os.environ["HOMEPATH"]
    pictures_path = os.path.join(homepath, "Pictures")

    repositoryFolder = os.path.join(pictures_path, pictureFolder)

    if not os.path.exists(repositoryFolder):
        print(f"Photo repository '{pictureFolder}' doesn't exist ")
        print("Please check, and possibly edit this file,variable 'pictureFolder' for correct folder")
        quit()
        # Note I only have 1 grandchild.
        # You may want to edit this for input with an input statement.
        # ie
        # pictureFolder = input('Enter repository: ')
        # sentence case may be an issue.

    # os.chdir(pictures_path)

    pythonFolder = os.path.join(pictures_path, "python")
    if not os.path.exists(pythonFolder):
        os.mkdir(pythonFolder)

    HEIC_dir =os.path.join(pictures_path, Working_HEIC_Folder)
    if not os.path.exists(HEIC_dir):
        os.mkdir(HEIC_dir)

    To_JPG = os.path.join(HEIC_dir, "To JPG")
    if not os.path.exists(To_JPG):
        os.mkdir(To_JPG)

    os.chdir(HEIC_dir)

    pillow_heif.register_heif_opener()

    for i in os.listdir((HEIC_dir)):
        filename, ext = os.path.splitext(i)

        if ext.upper().strip(".") in Exts:
            print (i)

            heif_file = pillow_heif.read_heif(i.upper().strip())

            #             Next Line works
            # heif_file2 = pillow_heif.read_heif(os.path.join(HEIC_dir,heif_file))

            image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
            )

            # This works
            # image.save(os.path.join(To_JPG, i.replace("HEIC", "JPG")))
            # But I decided to sharpen them up..
            sharpened_image = image.filter(ImageFilter.SHARPEN)
            sharpened_image.save(os.path.join(To_JPG, i.upper().replace(".HEIC", ".JPG")))

if __name__ == "__main__":
    heic_2_jpg()
    if __name__ == "__main__":
        heic_2_jpg()
        print("Finished.")

