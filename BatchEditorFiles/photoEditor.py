import cv2
import os 
import subprocess


def editPhoto(newImageName, photoPath, outputPath):
        print('new im', newImageName)
        outputName = newImageName.split(".")[0]
        print('new imPath', photoPath)


        image = cv2.imread(photoPath)

        if image is not None:
            print("Image loaded, Editing...")
            
            print("OUTPUT PATH: ", outputPath)
            #cv2.imshow("Image to edit", image)

            #cv2.waitKey(0)

            #ReSize Image to be smaller but WAY more server friendly 

            preferedSize = (1252, 1669)

            resizedImage = cv2.resize(image, preferedSize, interpolation=cv2.INTER_AREA)

            cv2.imwrite(os.path.join(outputPath , f'{outputName}.png'), resizedImage)

            

            #Use Subprocess to start cwebp to convert the image to webp AND keep the color profile (hopefully)

            command = f'cwebp -q 80 {outputName}.png -o {outputName}.webp -metadata icc'

            print("PROGRESSING SUBPROCESS")


            #open and close the image 
            from PIL import Image 

            image = Image.open(f"{outputName}.png")
            image.save(f"{outputName}.webp")
            image.close()
            # Run the command
            subprocess.run(command, shell=True, check=True)




            #cv2.destroyWindow()
            
            
            print("COMPLETE")
        else:
            print("FAIL")
