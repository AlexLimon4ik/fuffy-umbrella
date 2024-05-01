#pip install opencv-python 


# import cv2 
# image_path = "Materials\\cat.jpeg"
# image = cv2.imread(image_path)
# cv2.imshow("Cat", image)
# cv2.waitKey()

# import cv2

# image_path = 'Materials\\cat.jpeg'
# cat_face_cascade = cv2.CascadeClassifier('Materials\\haarcascade_frontalcatface_extended.xml')
# image = cv2.imread(image_path)
# cat_face = cat_face_cascade.detectMultiScale(image)
# print(cat_face)

# for (x,y,w,h) in cat_face:
#     cv2.rectangle(image, (x, y),(x+w, y+h), (0,0,255), 3)
#     cv2.imshow("Cat", image)
#     cv2.waitKey()

# import cv2
# from PIL import Image

# image_path = 'Materials\\cat.jpeg'
# cat_face_cascade = cv2.CascadeClassifier('Materials\\haarcascade_frontalcatface_extended.xml')
# image = cv2.imread(image_path)
# cat_face = cat_face_cascade.detectMultiScale(image)
# cat = Image.open(image_path)
# glasses = Image.open('Materials\\glasses.png')
# cat = cat.convert("RGBA")
# glasses = glasses.convert("RGBA")

# for (x,y,w,h) in cat_face:
#     glasses = glasses.resize((w, int(h/3)))
#     cat.paste(glasses, (x, int(y+h/4)), glasses)
#     cat.save("Materials\\cat_with_glasses.png")
#     cat_with_glasses = cv2.imread("Materials\\cat_with_glasses.png")
#     cv2.imshow("Cat_with_glasses", cat_with_glasses)
#     cv2.waitKey()



import cv2
from PIL import Image

image_path = 'Materials\\cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('Materials\\haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)

glasses = Image.open('Materials\\glasses.png')

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cat.save("Materials\\cat_with_glasses.png")

    cat_with_glasses = cv2.imread("Materials\\cat_with_glasses.png")

    cv2.imshow("Cat_with_glasses3", cat_with_glasses)
    cv2.waitKey()