import pyaudio
import wave
import time
import datetime
from gpiozero import LED, Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])


azul= LED (14)
verde = LED (15)
branco = LED (18)
vermelho = LED (2)
amarelo = LED (20)

botaocinza = Button (3)
botaopreto = Button (21)
branco.on()
while True:
    t=300
    vermelho.on()
    amarelo.off()
    verde.off()
    time.sleep(0.5)
    if botaopreto.wait_for_press(1):
        
        print ("tempo de gravacao definido como:")
        print (t)
        break
    botaocinza.wait_for_press()
    vermelho.off()
    amarelo.on()
    t=t+300
    time.sleep(0.5)
    if botaopreto.wait_for_press(1):
        print ("tempo de gravacao definido como:")
        print (t)
        break
    botaocinza.wait_for_press()
    amarelo.off()
    verde.on()
    t=t+300
    time.sleep (0.5)
    if botaopreto.wait_for_press(1):
        print ("tempo de gravacao definido como:")
        print (t)
        break
    botaocinza.wait_for_press()
   

azul.on()
branco.off()
tempog = t

while True:
    t=1800
    vermelho.on()
    amarelo.off()
    verde.off()
    time.sleep(0.5)
    if botaopreto.wait_for_press(1):
        print ("tempo de pausa definido como:")
        print (t)
        break
    botaocinza.wait_for_press()
    vermelho.off()
    amarelo.on()
    t=t+1800
    time.sleep(0.5)
    if botaopreto.wait_for_press(1):
        print ("tempo de pausa definido como:")
        print (t)
        break
    botaocinza.wait_for_press()
    amarelo.off()
    verde.on()
    t=t+1800
    time.sleep (0.5)
    if botaopreto.wait_for_press(1):
        print ("tempo de pausa definido como:")
        print (t)
        break
    botaocinza.wait_for_press()

vermelho.off()
amarelo.off()
verde.off()


tempop = t


while True:
    azul.on()
    nome = datetime.datetime.now()
    nome = str (nome)
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = int (tempog) # seconds to record
    dev_index = 2 # device index found by p.get_device_info_by_index(ii)
    wav_output_filename = nome # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
    azul.off()
    time.sleep (int (tempop))

    botaocinza.when_pressed = shutdown
