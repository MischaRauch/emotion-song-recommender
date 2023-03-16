from deepface import DeepFace
import cv2
import time
import get_songs

moods= {'Sad' : 0, 'Calm' : 1, 'Energetic' : 2, 'Happy' : 3}

# Ele's client ID
client_id = '6e1a09c940a943da95144c6f49a0717b'
client_secret = 'ccc2af43075641f9899eaaac5b716b8b'

sp = get_songs.authenticate(client_id, client_secret)


current_dominant_emotion = []
current_emotion = []
# TODO (LOU): store the tempo of current songs 
tempo_current_song = []
# TODO: How to store the preferences everyone has 3 preferences 
#mischasPreference = [rock,ambient,]


# TODO (LOU): Identify person 
cam = cv2.VideoCapture(0)
time.sleep(3)
_, image = cam.read()
cam.release()
# for image in database:
#    DeepFace.verify(database_image, image)
    

while True:
    cam = cv2.VideoCapture(0)
    # wait to get enough light for image
    time.sleep(3)
    _, image = cam.read()
    cam.release()
    #cv2.imwrite('test.png',image)
    data = DeepFace.analyze(image)
    #print(data[0].keys())
    # --> dict_keys(['emotion', 'dominant_emotion', 'region', 'age', 'gender', 'dominant_gender', 'race', 'dominant_race'])
    print(data[0].get('dominant_emotion'))
    # TODO (MISCHA): refactor the current emotion to our available list --> Sad' : 0, 'Calm' : 1, 'Energetic' : 2, 'Happy' : 3
    current_dominant_emotion.append(data[0].get('dominant_emotion'))
    current_emotion.append(data[0].get('emotion'))

    # TODO (MELI): Check time if time is ready do calculations below (IF not) otherwise collect emotions (go up to the code 'continue')


    # TODO (MELI): get average of current_dominant_emotion and clear the old list

    # get songs based on preference 
    songs = get_songs(sp, 100, get_songs.get_playlist_URI(sp, "genre: "+preference1))
    songs.append(get_songs(sp, 100, get_songs.get_playlist_URI(sp, "genre: "+preference2)))
    songs.append(get_songs(sp, 100, get_songs.get_playlist_URI(sp, "genre: "+preference3)))
    data = get_songs.create_table_songs(sp, songs)

    
    # TODO (MISCHA): Classify on emotion with model (NN or RF) taking into account the current dominant emotion
    # TODO (MISCHA): Play around with NN 
    # returns a df of songs matching the two possible emotion


    # TODO (ELENA): Filter/Order on sad or calm = speechiness --> high speechiness = sad, energetic and happy = loudness --> high loudness = energetic
    # IF time: filter songs based on realeased date matching with the age of the user
    # returns data in a df of songs matching emotion with a filter of < 0.5 based on the emotion

    # TODO (LOOU): Tempo: create a new column (absolut_tempo_error) where the previous tempo .... you will figure it out
    # returns one song

    # TODO (MELI / ALL): Play song 
    
    
    
