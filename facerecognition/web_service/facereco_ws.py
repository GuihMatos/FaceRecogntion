
import face_recognition
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/<string:img_name1>/<string:img_name2>')
def upload_images(img_name1, img_name2):
    # Load the uploaded image file
    img1 = face_recognition.load_image_file(img_name1)
    # Get face encodings for any faces in the uploaded image
    known_face_encoding = face_recognition.face_encodings(img1)[0]

    known_faces = [
        known_face_encoding
    ]

    # Load the uploaded image file
    img2 = face_recognition.load_image_file(img_name2)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encoding = face_recognition.face_encodings(img2)[0]

    face_found1 = False
    face_found2 = False
    is_the_same = False

    if len(known_face_encoding) > 0 and len(unknown_face_encoding) > 0:
        face_found1 = True
        face_found2 = True

        match_results = face_recognition.compare_faces(
            known_faces, unknown_face_encoding)
        if match_results[0]:
            is_the_same = True

    # Return the result as json
    result = {
        "face_found_in_image1": face_found1,
        "face_found_in_image2": face_found2,
        "is_same_person": is_the_same
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
