import os
import pickle
from music21 import converter, note, chord

DATASET_PATH = "dataset"
notes = []

print("Reading MIDI files...\n")

# Read all MIDI files
for file in os.listdir(DATASET_PATH):

    if file.lower().endswith((".mid", ".midi")):

        file_path = os.path.join(DATASET_PATH, file)

        print(f"Processing: {file}")

        try:
            midi = converter.parse(file_path)

            # Read every note from every track
            for element in midi.recurse():

                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))

                elif isinstance(element, chord.Chord):
                    notes.append(".".join(str(n) for n in element.normalOrder))

        except Exception as e:
            print(f"❌ Skipping {file} (Error: {e})")

print("\n--------------------------------")
print(f"Total Notes Extracted : {len(notes)}")
print(f"Unique Notes          : {len(set(notes))}")
print("--------------------------------")

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save notes
with open("models/notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("\n✅ Notes saved successfully!")
print("\nFirst 20 Notes:")
print(notes[:20])