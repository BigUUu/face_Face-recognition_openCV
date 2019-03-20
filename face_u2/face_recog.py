# import face_recognition
# import cv2
# image = face_recognition.load_image_file('E:\\data\\dataset\\images\\dilireba\\dilireba_1.jpg')
# face_locations = face_recognition.face_locations(image)
# cv2.imshow('img',image)
# cv2.waitKey()
# print(face_locations)





import face_recognition
import time

picture_of_me = face_recognition.load_image_file('dilireba_1.jpg')
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

unknown_picture = face_recognition.load_image_file('dilireba_4.jpg')

start = time.clock()
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
end = time.clock()
print(end - start)
if results[0] == True:
    print("迪丽热巴")
