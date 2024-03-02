from python.music.Tone import Tone
import threading
import time

# Source code for generating sine waves adapted from https://github.com/JamminCoder/music_maker

# sets the BPM (beats per minute) to 90
BPM = 90
pulse_length = 60 / BPM

# gives the frequency in Hz of each note in the 4th octave
note_name = {
    'C': 261.626,
    'C#': 277.183,
    'Db': 277.183,
    'D': 293.665,
    'D#': 311.127,
    'Eb': 311.127,
    'E': 329.628,
    'F': 349.228,
    'F#': 369.994,
    'Gb': 369.994,
    'G': 391.995,
    'G#': 415.305,
    'Ab': 415.305,
    'A': 440,
    'A#': 466.164,
    'Bb': 466.164,
    'B': 493.883
}

# specifies the frequency multiplier for each octave relative to 4
note_octave = {
    '0': 0.0625,
    '1': 0.125,
    '2': 0.25,
    '3': 0.5,
    '4': 1,
    '5': 2,
    '6': 4,
    '7': 8,
    '8': 16
}
# pre-defines note lengths for ease of use
note_length = {
    'eighth': pulse_length / 2,
    'eighth note triplet': pulse_length / 3,
    'quarter': pulse_length,
    'quarter note triplet': pulse_length * (2/3),
    'half': pulse_length * 2,
    'dotted half': pulse_length * 3,
    'whole': pulse_length * 4
}

# uses threading to play multiple notes at once for a chord
def play_chord(chord, chord_length, octave='3'):
    for note in chord:
        threading.Thread(target=Tone.sine, args=(
            note_name[note], chord_length, note_octave[octave])).start()

# predefines all the chords I will need in the song
C = ['C', 'E', 'G']
Am = ['A', 'C', 'E']
Em7 = ['E', 'G', 'B', 'D']
C7 = ['C', 'E', 'G', 'Bb']
F6 = ['F', 'A', 'C', 'D']
Bm7b5 = ['B', 'D', 'F', 'A']
Edim7 = ['E', 'G', 'Bb', 'Db']
Dm7 = ['D', 'F', 'A', 'C']
Dm7b5 = ['D', 'F', 'Ab', 'C']
Dbdim7 = ['C#', 'E', 'G', 'Bb']
G7sus = ['G', 'C', 'D' , 'F']
G7 = ['G', 'B', 'D' , 'F']
Dm11 = ['D', 'F', 'A', 'C', 'E', 'G']
G13 = ['G', 'B', 'D' , 'F', 'A', 'C', 'E']
C69 = ['C', 'E', 'G', 'A', 'D']

# goes through the sequence of inputs
def play_song():
        count = 0
        for i in range(2):
                play_chord(C, note_length['half'])
                Tone.sine(note_name['C'], duration=note_length['half'],
                        octave=note_octave['4'])

                play_chord(Am, note_length['half'])
                Tone.sine(note_name['C'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(Em7, note_length['dotted half'])
                Tone.sine(note_name['B'], duration=note_length['quarter'],
                        octave=note_octave['4'])
                Tone.sine(note_name['G'], duration=note_length['eighth'],
                        octave=note_octave['4'])
                Tone.sine(note_name['A'], duration=note_length['eighth'],
                        octave=note_octave['4'])
                Tone.sine(note_name['B'], duration=note_length['quarter'],
                        octave=note_octave['4'])

                play_chord(C7, note_length['quarter'])
                Tone.sine(note_name['C'], duration=note_length['quarter'],
                        octave=note_octave['5'])

                play_chord(F6, note_length['half'])
                Tone.sine(note_name['C'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(Bm7b5, note_length['half'])
                Tone.sine(note_name['A'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(Em7, note_length['half'])
                Tone.sine(note_name['G'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(Edim7, note_length['half'])
                time.sleep(note_length['half'])

                play_chord(Dm7, note_length['half'])
                Tone.sine(note_name['A'], duration=note_length['half'],
                        octave=note_octave['4'])

                play_chord(Dm7b5, note_length['half'])
                Tone.sine(note_name['F'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(C, note_length['half'])
                Tone.sine(note_name['E'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                Tone.sine(note_name['C'], duration=note_length['eighth'],
                        octave=note_octave['5'])
                Tone.sine(note_name['D'], duration=note_length['eighth'],
                        octave=note_octave['5'])

                play_chord(Dbdim7, note_length['half'])
                Tone.sine(note_name['E'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                Tone.sine(note_name['F'], duration=note_length['quarter'],
                        octave=note_octave['5'])

                play_chord(Dm7, note_length['half'])
                Tone.sine(note_name['D'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                Tone.sine(note_name['B'], duration=note_length['eighth'],
                        octave=note_octave['4'])
                Tone.sine(note_name['C'], duration=note_length['eighth'],
                        octave=note_octave['5'])

                play_chord(G7sus, note_length['quarter'])
                Tone.sine(note_name['D'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                play_chord(G7, note_length['quarter'])
                Tone.sine(note_name['E'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                
                if count > 0:
                        break

                play_chord(C, note_length['half'])
                Tone.sine(note_name['C'], duration=note_length['half'],
                        octave=note_octave['5'])

                play_chord(Dm11, note_length['quarter'])
                Tone.sine(note_name['G'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                play_chord(G13, note_length['quarter'])
                Tone.sine(note_name['E'], duration=note_length['quarter'],
                        octave=note_octave['5'])
                count += 1

        play_chord(C69, note_length['whole'])

play_song()