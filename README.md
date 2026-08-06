# 🎵 AI Music Generation using Deep Learning

An AI-powered Music Generation system built with **Python, TensorFlow, Keras, and Music21**. This project learns musical patterns from MIDI files using a Long Short-Term Memory (LSTM) neural network and generates new piano melodies in MIDI format. It also includes a **Streamlit web application** for generating and downloading AI-composed music.

---

## 🚀 Features

- 🎹 AI-generated piano melodies
- 🧠 LSTM-based Deep Learning model
- 🎼 MIDI dataset preprocessing using Music21
- 📊 Musical note extraction and sequence preparation
- 🎵 Automatic MIDI music generation
- 🌐 Interactive Streamlit Web Application
- 💾 Download generated MIDI files
- ⚡ TensorFlow/Keras implementation

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Music21
- NumPy
- Streamlit
- Pickle
- Git & GitHub

---

## 📂 Project Structure

```text
AI-Music-Generation/
│
├── dataset/                # MIDI dataset
├── models/                 # Trained model & extracted notes
│   ├── music_model.keras
│   └── notes.pkl
│
├── output/                 # Generated MIDI files
│   └── generated.mid
│
├── preprocess.py           # MIDI preprocessing
├── train.py                # LSTM model training
├── generate.py             # Music generation
├── app.py                  # Streamlit web app
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

### Step 1 – Data Preprocessing
- Reads MIDI files from the dataset folder.
- Extracts musical notes and chords.
- Saves processed notes into `notes.pkl`.

### Step 2 – Model Training
- Encodes note sequences.
- Trains an LSTM neural network.
- Saves the trained model as `music_model.keras`.

### Step 3 – Music Generation
- Loads the trained model.
- Predicts the next musical notes.
- Generates a new MIDI file (`generated.mid`).

### Step 4 – Streamlit Interface
- Click **Generate Music**.
- AI composes a new melody.
- Download the generated MIDI file.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/ManahilRaees46/AI-Music-Generation.git
cd AI-Music-Generation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Preprocess Dataset

```bash
python preprocess.py
```

### Train Model

```bash
python train.py
```

### Generate Music

```bash
python generate.py
```

### Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Project Workflow

```
MIDI Dataset
      │
      ▼
Preprocessing
      │
      ▼
Note Extraction
      │
      ▼
LSTM Model Training
      │
      ▼
Music Generation
      │
      ▼
Generated MIDI File
      │
      ▼
Streamlit Web App
```

---

## 🎯 Future Improvements

- 🎼 Support multiple music genres
- 🎹 Transformer-based music generation
- 🎧 In-browser audio playback
- ☁️ Deploy the application online
- 🎵 Longer and more realistic compositions

---

## 👩‍💻 Author

**Manahil Raees**

BS Computer Science Student

Interested in Artificial Intelligence, Machine Learning, and Deep Learning.

---

## ⭐ Support

If you found this project useful, don't forget to **⭐ Star** this repository.
