import cv2
import matplotlib.pyplot as plt
image_path = 'example.jpeg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height,width,_=image_rgb.shape
arrow_end=(50,100)
arrow_start=(width-50,100)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
height_label_position=(arrow_start[0]//2+arrow_end[0]//2,arrow_start[1])
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,f"Width:{width}",height_label_position,font,3,(255,255,0),2,cv2.LINE_AA)
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title('Width of image represented by arrows and text')
plt.show()