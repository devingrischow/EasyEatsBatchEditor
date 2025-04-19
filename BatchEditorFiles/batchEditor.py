import cv2
import os 
import colour
import numpy as np

def batchVideoEditor(video_to_edit_File, stepName, stepNumber, output_filePath):
    video_to_Edit = cv2.VideoCapture(video_to_edit_File)


    #Encoding Codec
    mp4CODEC = cv2.VideoWriter_fourcc(*'avc1')

    
    #Output video that the frames are written to
    output_video = cv2.VideoWriter(os.path.join(output_filePath , f'{stepName}-{stepNumber}.mp4'), mp4CODEC, 30, (1080,1920))


    while True:
        ret, frame = video_to_Edit.read()

        if not ret:
            print("No More Video Frames Found, Ending...")
            break


        #convert the taken frame and conver its color space to REC 709
        frame_color_709 = convert_to_rec709(frame)




        # Convert back to BGR for OpenCV compatibility (going to see if optional)
        frame_output = cv2.cvtColor(frame_color_709, cv2.COLOR_RGB2BGR)

        
        #Start Test with normal new frame output, 

        #then try gamma adjusted 

        #Simply Take The Frame and Add it to the output video object 
        output_video.write(frame_output)

        cv2.imshow(f"{stepName}-{stepNumber}", frame_output)

        #Emergency stop if the user presses q 
        if cv2.waitKey(25) == ord('q'):
            break

    
    #Once no more video remains, release the video and break the frames
    video_to_Edit.release()
    cv2.destroyAllWindows()


#Convert a frame from openCVs BGR to REC 709
def convert_to_rec709(image):
    """Convert the image to Rec. 709 color space using colour-science library."""
    # OpenCV uses BGR by default. Convert to RGB first.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Normalize image to float [0, 1] range
    rgb_image = rgb_image / 255.0
    
    # Convert RGB to Rec. 709 using colour-science
    rec709_image = colour.RGB_to_RGB(rgb_image, input_colourspace='sRGB', output_colourspace='ITU-R BT.709')

    # Convert float [0, 1] to uint8 [0, 255]
    rec709_image = np.clip(rec709_image * 255, 0, 255).astype('uint8')
    
    return rec709_image


#Apply a Gamma Correction to the image, allowing to control the tone of the image given a gamma correction value.
def apply_gamma_correction(image, gamma):
    """Apply gamma correction to the given image."""
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)