from primesense import openni2
from primesense import _openni2 as c_api
import numpy as np
import cv2
openni2.initialize('/home/spadesk/library/OpenNI2/Bin/x64-Release')
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM,
                                               resolutionX=640, resolutionY=480, fps=30))
while True:
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    img = np.frombuffer(frame_data, dtype=np.uint16)
    img.shape = (1, 480, 640)
    img = np.concatenate(img)
    # img = np.concatenate((img, img, img), axis=0)
    # img = np.swapaxes(img, 0, 2)
    # img = np.swapaxes(img, 0, 1)
    cv2.imshow("image", img)
    if cv2.waitKey(34) & 0xFF == ord('q'):
    	break

openni2.unload()