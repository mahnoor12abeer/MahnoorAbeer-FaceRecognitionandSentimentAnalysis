import cv2
from facenet_pytorch import MTCNN
import torch
from deepface import DeepFace
from app.sort import Sort

def gen_frames(input_video_path):  # Modified function to yield frames
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)
    tracker = Sort()

    cap = cv2.VideoCapture(input_video_path)
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes, _ = mtcnn.detect(frame_rgb)

        if boxes is not None:
            tracked_objects = tracker.update(boxes)
            
            for toi in tracked_objects:
                x1, y1, x2, y2, obj_id = int(toi[0]), int(toi[1]), int(toi[2]), int(toi[3]), int(toi[4])
                cropped_face = frame[y1:y2, x1:x2]
                
                emotion = "Unknown"
                try:
                    analysis = DeepFace.analyze(cropped_face, actions=['emotion'], enforce_detection=False)
                    emotion = analysis[0]['dominant_emotion']
                except Exception as e:
                    print("Error in emotion recognition:", e)
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f"ID: {obj_id} {emotion}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')