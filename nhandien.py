import cv2
import face_recognition

# Load the reference image (the image of the face to unlock)
reference_image = face_recognition.load_image_file("person2.jpg")
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

# Start capturing video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to RGB (OpenCV uses BGR by default)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # Check if the face is recognized by comparing it to the reference face
        recognized = face_recognition.compare_faces([reference_face_encoding], face_encoding)

        if recognized[0]:
            # If recognized, perform the action to unlock the screen (e.g., press a key)
            # Replace this part with your actual unlocking mechanism
            print("Face recognized - Unlocking...")
            # Here you can add your unlock logic

    # Show the frame with faces detected
    cv2.imshow('Face Unlock', frame)

    # Check for the 'q' key to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
