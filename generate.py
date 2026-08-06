import pickle
import random
import numpy as np

from music21 import stream, note, chord

from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/music_model.keras")

# Load notes
with open("models/notes.pkl", "rb") as f:
    notes = pickle.load(f)

print("Model Loaded Successfully!")
print("Total Notes:", len(notes))

pitchnames = sorted(set(notes))

note_to_int = {
    note: number
    for number, note in enumerate(pitchnames)
}

int_to_note = {
    number: note
    for number, note in enumerate(pitchnames)
}

n_vocab = len(pitchnames)

sequence_length = 100

network_input = []

for i in range(len(notes) - sequence_length):

    sequence = notes[i:i + sequence_length]

    network_input.append(
        [note_to_int[n] for n in sequence]
    )

start = random.randint(0, len(network_input)-1)

pattern = network_input[start]

prediction_output = []

for note_index in range(500):

    prediction_input = np.reshape(
        pattern,
        (1, len(pattern), 1)
    )

    prediction_input = prediction_input / float(n_vocab)

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)

    pattern = pattern[1:]

    offset = 0
output_notes = []

for pattern in prediction_output:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")

        chord_notes = []

        for current_note in notes_in_chord:

            new_note = note.Note(int(current_note))

            new_note.storedInstrument = None

            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)

        new_chord.offset = offset

        output_notes.append(new_chord)

    else:

        new_note = note.Note(pattern)

        new_note.offset = offset

        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)

midi_stream.write(
    "midi",
    fp="output/generated.mid"
)

print("\n🎵 Music Generated Successfully!")
print("Saved as output/generated.mid")
