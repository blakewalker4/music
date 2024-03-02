import math
import numpy
import time
import pygame
import threading

beats_per_measure = 1
num_measures = 2
bpm = 120
pulse_length = 60 / bpm

# gives the frequency in Hz of each note in the 4th octave
note_name = {
'A' : 440,
'Bb' :466.164,
'B' : 493.883,
'C' : 523.251,
'Db' : 554.365,
'D' : 587.33,
'Eb' : 622.254,
'E' : 659.255,
'F' : 698.456,
'Gb' : 739.989,
'G' : 783.991,
'Ab' : 830.609
}
pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

class Tone:
    def sine(frequency, duration=1, speaker=None):
        """
        Play tone code taken and modified from https://stackoverflow.com/a/16268034
        """

        num_samples = int(round(duration * sample_rate))

        #setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
        buf = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        # amplitude = 2 ** (bits - 1) - 1
        amplitude = 500

        for s in range(num_samples):
            t = float(s) / sample_rate    # time in seconds

            sine = sine_x(amplitude, frequency, t)

            # Control which speaker to play the sound from
            if speaker == 'r':
                buf[s][1] = sine # right
            elif speaker == 'l':
                buf[s][0] = sine # left

            else:
                buf[s][0] = sine # left
                buf[s][1] = sine # right
                

        sound = pygame.sndarray.make_sound(buf)
        one_sec = 1000 # Milliseconds
        sound.play(loops = 1, maxtime=int(duration * one_sec))
        time.sleep(duration)
    
    @staticmethod
    def create_tone_from_list(frequency_array, duration=1):
        tone_threads = []
        
        for freq in frequency_array:
            thread = threading.Thread(target=Tone.sine, args=[freq, duration])
            tone_threads.append(thread)
        
        for thread in tone_threads:
            thread.start()
        
        for thread in tone_threads:
            thread.join()


for repeat in range(2):
    for measure in range(2):
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(2 * note_name['D'], duration=pulse_length)
        Tone.sine(2 * note_name['A'], duration=pulse_length * 1.5)
        Tone.sine(note_name['Ab'], duration=pulse_length)
        Tone.sine(note_name['G'], duration=pulse_length)
        Tone.sine(note_name['F'], duration=pulse_length)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['F'], duration=pulse_length / 2)
        Tone.sine(note_name['G'], duration=pulse_length / 2)

    for measure in range(2):
        Tone.sine(note_name['C'], duration=pulse_length / 2)
        Tone.sine(note_name['C'], duration=pulse_length / 2)
        Tone.sine(2 * note_name['D'], duration=pulse_length)
        Tone.sine(2 * note_name['A'], duration=pulse_length * 1.5)
        Tone.sine(note_name['Ab'], duration=pulse_length)
        Tone.sine(note_name['G'], duration=pulse_length)
        Tone.sine(note_name['F'], duration=pulse_length)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['F'], duration=pulse_length / 2)
        Tone.sine(note_name['G'], duration=pulse_length / 2)

    for measure in range(2):
        Tone.sine(note_name['B'], duration=pulse_length / 2)
        Tone.sine(note_name['B'], duration=pulse_length / 2)
        Tone.sine(2 * note_name['D'], duration=pulse_length)
        Tone.sine(2 * note_name['A'], duration=pulse_length * 1.5)
        Tone.sine(note_name['Ab'], duration=pulse_length)
        Tone.sine(note_name['G'], duration=pulse_length)
        Tone.sine(note_name['F'], duration=pulse_length)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['F'], duration=pulse_length / 2)
        Tone.sine(note_name['G'], duration=pulse_length / 2)

    for measure in range(1):
        Tone.sine(note_name['Bb'], duration=pulse_length / 2)
        Tone.sine(note_name['Bb'], duration=pulse_length / 2)
        Tone.sine(2 * note_name['D'], duration=pulse_length)
        Tone.sine(2 * note_name['A'], duration=pulse_length * 1.5)
        Tone.sine(note_name['Ab'], duration=pulse_length)
        Tone.sine(note_name['G'], duration=pulse_length)
        Tone.sine(note_name['F'], duration=pulse_length)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['F'], duration=pulse_length / 2)
        Tone.sine(note_name['G'], duration=pulse_length / 2)

    for measure in range(1):
        Tone.sine(note_name['Bb'], duration=pulse_length / 2)
        Tone.sine(note_name['Bb'], duration=pulse_length / 2)
        Tone.sine(2 * note_name['D'], duration=pulse_length)
        Tone.sine(2 * note_name['A'], duration=pulse_length * 1.5)
        Tone.sine(note_name['Ab'], duration=pulse_length)
        Tone.sine(note_name['G'], duration=pulse_length)
        Tone.sine(note_name['F'], duration=pulse_length)
        Tone.sine(note_name['D'], duration=pulse_length / 2)
        Tone.sine(note_name['F'], duration=pulse_length / 2)
        Tone.sine(note_name['D'], duration=pulse_length / 2)


