'''
COURSE: CST 205 Multimedia Design and Programing
TITLE:  FreeHand
AUTHORS:
            Iris Manriquez | Daniel Morales | Edgar Reyes
DATE:   May 13th, 2018
ABSTRACT:

This notes file creates the individual notes for the piano to access. The notes are saved to the computer in wav files,
there are different frequencies for each note which gives it a unique sound.

'''



from scipy.io.wavfile import write
from pylab import plot,show,axis
from numpy import linspace,sin,pi,int16

# tone synthesis
def note(freq, len, amp=1, rate=44100):
    t = linspace(0,len,len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16) # two byte integers

# A tone, 1 second, 44100 samples per second
toneA = note(440,1,amp=10000)
toneBF= note(466,1,amp=10000)
toneB = note(494,1,amp=10000)
toneC= note(523,1,amp=10000)
toneCS= note(554,1,amp=10000)
toneD = note(587,1,amp=10000)
toneDS= note(622,1,amp=10000)
toneE= note(659,1,amp=10000)
toneF= note(698,1,amp=10000)
toneFS= note(740,1,amp=10000)
toneG = note(784,1,amp=10000)
toneAF= note(831,1,amp=10000)
toneA2= note(880,1,amp=10000)

write('Anote.wav',44100,toneA)
write('BFnote.wav',44100,toneBF)  # writing the sound to files
write('Bnote.wav',44100,toneB)
write('Cnote.wav',44100,toneC)
write('CSnote.wav',44100,toneCS)
write('Dnote.wav',44100,toneD)
write('DSnote.wav',44100,toneDS)
write('Enote.wav',44100,toneE)
write('Fnote.wav',44100,toneF)
write('FSnote.wav',44100,toneFS)
write('Gnote.wav',44100,toneG)
write('AFnote.wav',44100,toneAF)
write('A2note.wav',44100,toneA2)
