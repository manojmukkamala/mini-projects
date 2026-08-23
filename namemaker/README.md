# NameMaker
https://colab.research.google.com/drive/1WMbrZpuGxULcWp7wpN1QwJEQpaflortr

<br>
Feb 2020 – March 2020

<br><br>
Project description
<br><br>
v1:
<br>
Built a Recurrent Neural Network from scratch using Numpy and trained the model on first names of people from India and USA.
Performed data cleansing using string and NLTK libraries.
The goal of the model is to generate new names based on name patterns learnt from the training set.
Trained locally for ~18 hours over 10,000 epochs and the results are mediocre.
<br><br>

v2:
<br>
Rebuild the Recurrent Neural Network using Tensorflow and Keras and upgraded the hidden cells to LSTM/CuDNNLSTM.
Leveraged Google Collab GPU to train the model and trained for 500 epochs and attained reasonable results. Ex: arish, elina, lisha

<br><br>
v3:
<br>
Number of Hidden Units: n_a = 64
<br>
Number of Epochs: 10
<br>
Results:
<br>
ndree,
arri,
handri,
ella,
lisa,
arina,
arrit,
arleen,
shara,
anish,
arlene,
andy,
arina,
aria,
relia,
arlee,
uint,
ambir,
anda,
amina,
rjana,
inda,
andell,
amina,
ashina,
aniyah

<br><br>
Number of Hidden Units: n_a = 512
<br>
Number of Epochs: 100
<br>
Results:
<br>
lisha,
alaram,
handa,
elia,
lisa,
arhana,
ulshad,
ardes,
shant,
anelle,
aris,
akhan,
arian,
andini,
rvil,
arveen,
uint,
ambir,
antosh,
amika,
rman,
ines,
illia,
imena,
ashin,
aiden

<br><br>

## How to run

Python project (Jupyter notebook; v2/v3 use TensorFlow/Keras).
Requirements: `jupyter`, `numpy`, `pandas`, `nltk`, `tensorflow`
(e.g. `pip install jupyter numpy pandas nltk tensorflow`).

The notebook was written for Google Colab, so the data-loading cells point at
`/content/drive/My Drive/Colab Notebooks/...`. To run locally, change those two
paths to `names_us.csv` and `names.csv` in this folder (or re-run in Colab with
the files mounted).

- `names.csv` — Indian names (v1 training data)
- `names_us.csv` — US names (v2/v3 training data)
- `dinos.txt` — dinosaur names (used by the v1 experiments in `rnn_rnd.py`)
- `Namer_v1.h5` — v1 model weights (loaded by the notebook for comparison;
note: the v2 weights referenced in the notebook were never saved)
- `hand_crafted_rnn.py` / `rnn_rnd.py` / `string_utils.py` — v1 NumPy implementation

The Colab used for this work: <https://colab.research.google.com/drive/1WMbrZpuGxULcWp7wpN1QwJEQpaflortr>

---

*Original work: 2020-03 (first committed to GitHub 2020-03-04).*
