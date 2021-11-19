import os
import sys
import easygui
from easygui import *
import face_recognition
from face_recognition import *
import cv2
import numpy as np
import glob
import pickle
import os
import random
import json
import pandas as pd
import datetime
from datetime import datetime

loop = 0
while (loop==0):

    def no_identities():
        image = "warning.png"
        msg = "             ATTENTION!: FOR THE CAMERA TO RUN, AT LEAST ONE IDENTITY\n             MUST BE CREATED. SO FAR NO IDENTITIES ARE CREATED YET\n\n\n             PRESS OK TO RETURN TO THE MAIN MENU, AND CREATE ONE"
        title = "NO IDENTITIES CREATED"
        msgbox(msg, title, image=image)


    def exit_program():
        image = "warning.png"
        msg = "Do you want to Quit the Program?"
        title = "Quit Program?"
        choices = ["Yes", "No"]
        choice = buttonbox(msg, title, choices, image=image)
        if choice == "Yes":
            sys.exit(0)
        else:
            pass

    def recognition_program_main():
        image="facial-recognition.png"
        msg = "             >>>>>>>>>>> OPENCV FACE RECOGNITION PROGRAM <<<<<<<<<\n\n"
        title = "FACE AND IDENTITY RECOGNITION SOFTWARE"
        choices = ["Create New Identity", "Start Face Recognition", "EXIT"]
        choice = buttonbox(msg, title, choices, image=image)

        if choice == "EXIT":
            exit_program()

        if choice == "Start Face Recognition":

            if os.path.isfile('./ref_name.pkl'):
                f=open("ref_name.pkl","rb")
                ref_dictt=pickle.load(f)
                f.close()
            else:
                no_identities()
                recognition_program_main()

            if os.path.isfile('./ref_embed.pkl'):
                f=open("ref_embed.pkl","rb")
                embed_dictt=pickle.load(f)
                f.close()
            else:
                no_identities()
                recognition_program_main()

            known_face_encodings = []
            known_face_names = []

            for ref_id , embed_list in embed_dictt.items():
                for my_embed in embed_list:
                    known_face_encodings +=[my_embed]
                    known_face_names += [ref_id]

            video_capture = cv2.VideoCapture(0)

            face_locations = []
            face_encodings = []
            face_names = []
            #document_ids = []
            process_this_frame = True

            while True  :

                ret, frame = video_capture.read()

                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]

                if process_this_frame:

                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                    face_names = []
                    document_ids = []
                    joined_dates = []
                    for face_encoding in face_encodings:

                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                        face_names.append(name)

                    if os.path.isfile('./ref_document.pkl'):
                        f=open("ref_document.pkl","rb")
                        ref_dictt2=pickle.load(f)
                        for item in ref_dictt2:
                            document_ids.append(item)

                process_this_frame = not process_this_frame

                for (top_s, right, bottom, left), name in zip(face_locations, face_names):
                    top_s *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 255, 0), 2)

                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    if name == "Unknown":
                        Unidientified_person = "Unidentified Person"
                        cv2.putText(frame, Unidientified_person, (left + 15, bottom - 15 ), font, 0.7, (255, 255, 255), 1)
                        now=datetime.now()
                        cv2.putText(frame, str(now), (right + 6, bottom - 35), font, 1.0, (0, 0, 0), 1)
                        print(str(now)+": "+Unidientified_person)
                    else:
                        now=datetime.now()
                        cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                        cv2.putText(frame, str(now), (right + 6, bottom - 40), font, 1.0, (0, 0, 0), 1)
                        #cv2.putText(frame, str("D.N.I: ")+str(document_ids), (right + 6 , bottom - 6), font, 1.0, (255, 0, 0), 1)

                        now = datetime.now()
                        print(str(now)+": IDENTIFIED PERSON: "+str(ref_dictt[name]))

                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video_capture.release()
            cv2.destroyAllWindows()

        if choice == "Create New Identity":

            def new_identity():

                face_recognition = ">>>>>>>>>>> OPENCV FACE RECOGNITION PROGRAM <<<<<<<<<\n\n"
                msg = "-----> FACE RECOGNITION PROGRAM\n\n\n* NOTE: ENTER THE DOCUMENT NUMBER ALL TOGETHER,\n  WITH NO SPACES OR SPECIAL CHARACTERS\n\n* MAX AMOUNT OF DIGITS IS LIMITED TO 8.\n\n* MINIMUM AMOUNT OF DIGITS IS 7\n\n- EXAMPLE: 34578901, OR 3457890\n\n\n"
                fieldNames = ["New identity/Person Name:", "ID/Document number: "]
                global fieldValues
                fieldValues = []
                fieldValues = multenterbox(msg, face_recognition, fieldNames)

                if fieldValues == None:
                    recognition_program_main()

                if (not fieldValues[1].isdigit()):
                    title = "ATTENTION"
                    warning = "warning.png"
                    msg = "TYPE ERROR. REMEMBER ONLY INTEGERS ARE ALLOWED IN BOTH THE ID/Document number field\n\n"
                    msgbox(msg, title, image=warning)
                    new_identity()

                if len(fieldValues[1]) > 8 :
                    title = "ATTENTION"
                    warning = "warning.png"
                    msg = "YOU EXCEEDED THE AMOUNT OF 8 NUMBERS REQUESTED FOR THE ID/Document number field\n\n"
                    msgbox(msg, title, image=warning)
                    new_identity()

                if len(fieldValues[1]) > 8 :
                    title = "ATTENTION"
                    warning = "warning.png"
                    msg = "YOU EXCEEDED THE AMOUNT OF 8 DIGITS, REQUIRED FOR THE ID/Document number field\n\n"
                    msgbox(msg, title, image=warning)
                    new_identity()

                if len(fieldValues[1]) < 7 :
                    title = "ATTENTION"
                    warning = "warning.png"
                    msg = "YOU MUST ENTER MORE THAN 7 DIGITS, REQUIRED FOR THE ID/Document number field\n\n"
                    msgbox(msg, title, image=warning)
                    new_identity()


                if fieldValues == None:
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":

                        sys.exit(0)

                    if choice == "No":

                        new_identity()
                    else:
                         new_identity()
                while 1:

                    if fieldValues == None: break
                    errmsg = ""
                    for i in range(len(fieldNames)):
                      if fieldValues[i].strip() == "" :
                          errmsg = errmsg + ('* ATTENTION!, PLEASE COMPLETE THE "%s" FIELD. IT IS EMPTY.\n\n' % fieldNames[i])

                    if errmsg == "": break # no problems found
                    title = "ATTENTION"
                    warning = "warning.png"
                    msgbox(errmsg, title, image=warning)
                    fieldValues = multenterbox(msg, title, fieldNames, fieldValues)

                    try:

                        if (not fieldValues[1].isdigit()):
                            title = "ATTENTION"
                            warning = "warning.png"
                            msg = "TYPE ERROR. REMEMBER ONLY INTEGERS ARE ALLOWED IN BOTH THE ID/Document number field\n\n"
                            msgbox(msg, title, image=warning)
                            new_identity()

                    except:

                        if fieldValues == None:
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":

                                sys.exit(0)

                            if choice == "No":

                                new_identity()

                            else:
                                 new_identity()

                fieldValues[0] #PERSON NAME STRING VALUE
                fieldValues[1] #DOCUMENT INTEGER VALUE
                name=fieldValues[0]
                document_number=fieldValues[1]
                document_string=" - D.N.I: "
                document_number_id=document_string+document_number
                random_number = random.randint(0, 1000000000)
                ref_id= random_number

                try:
                    f=open("ref_name.pkl","rb")

                    ref_dictt=pickle.load(f)
                    print(ref_dictt)
                    f.close()
                except:
                    ref_dictt={}
                ref_dictt[ref_id]=name+document_number_id

                #
                try:
                    f=open("ref_document.pkl","rb")

                    ref_dictt2=pickle.load(f)
                    print(ref_dictt2)
                    f.close()
                except:
                    ref_dictt2={}
                ref_dictt2[document_number]=name

                ref_dictt3={}
                now = datetime.now()
                ref_dictt3[str(now)]=ref_id

                f=open("ref_document.pkl","wb")
                pickle.dump(ref_dictt2,f)
                pickle.dump(ref_dictt3,f)
                f.close()

                f=open("ref_name.pkl","wb")
                pickle.dump(ref_dictt,f)
                f.close()

                try:
                    f=open("ref_embed.pkl","rb")

                    embed_dictt=pickle.load(f)
                    f.close()
                except:
                    embed_dictt={}

                try:
                    f=open("ref_name.pkl","rb")

                    ref_dictt=pickle.load(f)
                    print(ref_dictt)
                    f.close()
                except:
                    ref_dictt={}
                ref_dictt[ref_id]=name+document_number_id

                #
                try:
                    f=open("ref_document.pkl","rb")

                    ref_dictt2=pickle.load(f)
                    print(ref_dictt2)
                    f.close()
                except:
                    ref_dictt2={}
                ref_dictt2[document_number]=name

                ref_dictt3={}
                now = datetime.now()
                ref_dictt3[str(now)]=ref_id

                f=open("ref_document.pkl","wb")
                pickle.dump(ref_dictt2,f)
                pickle.dump(ref_dictt3,f)
                f.close()

                f=open("ref_name.pkl","wb")
                pickle.dump(ref_dictt,f)
                f.close()

                try:
                    f=open("ref_embed.pkl","rb")

                    embed_dictt=pickle.load(f)
                    f.close()
                except:
                    embed_dictt={}

                import face_recognition

                for i in range(1):
                    key = cv2. waitKey(1)
                    webcam = cv2.VideoCapture(0)
                    while True:

                        check, frame = webcam.read()

                        cv2.imshow("SNAPSHOT MODE WINDOW", frame)
                        captura_identidad="ATTENTION: PRESS THE s KEY FROM THE KEYBOARD, TO GET A SCREENSHOT OF YOURSELF..."
                        print(captura_identidad+"...")
                        fontscale=1
                        thickness=2
                        #cv2.putText(frame, captura_identidad, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, fontscale, (0, 255, 255), thickness)
                        now=datetime.now()
                        cv2.putText(frame, name+" - Documnent ID: "+document_number, (100, 50), cv2.FONT_HERSHEY_SIMPLEX, fontscale, (0, 255, 0), thickness)
                        cv2.putText(frame, str(now), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, fontscale, (0, 255, 255), thickness)
                        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                        rgb_small_frame = small_frame[:, :, ::-1]

                        key = cv2.waitKey(1)

                        if key == ord('s') :
                            face_locations = face_recognition.face_locations(rgb_small_frame)
                            if face_locations != []:
                                face_encoding = face_recognition.face_encodings(frame)[0]
                                if ref_id in embed_dictt:
                                    embed_dictt[ref_id]+=[face_encoding]
                                    #embed_dictt[document_number]+=[face_encoding]
                                else:
                                    embed_dictt[ref_id]=[face_encoding]
                                    #embed_dictt[document_number]=[face_encoding]

                                cv2.imwrite('opencv_image_'+str(name)+"_"+str(document_number)+'.png', frame)
                                #Resize image

                                src = cv2.imread('opencv_image_'+str(name)+"_"+str(document_number)+'.png', cv2.IMREAD_UNCHANGED)
                                #percent by which the image is resized
                                scale_percent = 50

                                #calculate the 50 percent of original dimensions
                                width = int(src.shape[1] * scale_percent / 100)
                                height = int(src.shape[0] * scale_percent / 100)

                                # dsize
                                dsize = (width, height)

                                # resize image
                                output = cv2.resize(src, dsize)

                                cv2.imwrite('opencv_image_'+str(name)+"_"+str(document_number)+'.png',output)
                                webcam.release()
                                cv2.waitKey(1)
                                cv2.destroyAllWindows()
                                break
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                        elif key == ord('q'):
                            print("Turning off camera.")
                            webcam.release()
                            print("Camera off.")
                            print("Program ended.")
                            cv2.destroyAllWindows()
                            break

                f=open("ref_embed.pkl","wb")
                pickle.dump(embed_dictt,f)
                f.close()
                image='opencv_image_'+str(name)+"_"+str(document_number)+'.png'
                msg = "THE NEW IDENTITY WAS SAVED WITH THE FOLLOWING DATA:\n\n\n        Person Name: "+str(fieldValues[0])+"\n\n        ID/Document number: "+str(fieldValues[1])+"\n\n\n        CLICK OK TO PROCEED TO THE MAIN WINDOW"
                title = "NEW IDENTITY SAVED"
                msgbox(msg, title, image=image)
                recognition_program_main()

            new_identity()

    recognition_program_main()



    


        
