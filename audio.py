import pyaudio
import wave
import time
import sys
import numpy as np
##########################
def number_reader(number_string):
    file_name = "audio-numbers\\" + number_string + ".wav"
    print(file_name)
    wf = wave.open(file_name, 'rb')
    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()
    return None
####################################

def number_reader_api(number):
    if number < 100 :
        number_reader(str(number))
        return None
    elif ((number >= 100) and (number < 1000)):
        hund = int(100 * np.floor(number/100))
        rest =  int(number - hund )
        number_reader(str(hund))
        number_reader("and")
        number_reader(str(rest))  
        return None
    elif(number >= 1000) and (number < 10000):
        thousand = int(1000 *  np.floor(number/1000))
        rest1 = int( (number - thousand ))
        hund =int( 100 *  np.floor(rest1/100))
        rest = int( (rest1 - hund ))
        number_reader(str(thousand))
        number_reader("and")
        number_reader(str(hund))
        number_reader("and")
        number_reader(str(rest))  
        return None
    else :
        number_reader(str(10000))
        return None
    return None

###################
number_reader_api(10000)