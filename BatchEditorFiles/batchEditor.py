import cv2
import os 


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


        #Simply Take The Frame and Add it to the output video object 
        output_video.write(frame)

        cv2.imshow("Video Output", frame)

        #Emergency stop if the user presses q 
        if cv2.waitKey(25) == ord('q'):
            break

    
    #Once no more video remains, release the video and break the frames
    video_to_Edit.release()
    cv2.destroyAllWindows()

    