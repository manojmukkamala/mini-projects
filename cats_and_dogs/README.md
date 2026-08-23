# cats_and_dogs

Cat-vs-dog CNN exercise (2020) on the **Oxford-IIIT Pet Dataset**
(Parkhi et al., CVPR 2012, "Cats and Dogs" — 37 breeds, ~200 images per
class; here only the `Cat/` and `Dog/` folders are used, resized to
100×100 grayscale). Four entry points, all training a small
2-convolution keras model (binary cross-entropy, sigmoid head):

- `test.py` — the plain script. Loads `X.pickle`/`y.pickle`, trains on
  the first 2048 samples, batch 32, 3 epochs. The image-scanning /
  pickle-writing half is present but **commented out** (the pickles
  already existed when this was run).
- `catsdogs.py` — the same script with the image-scanning /
  pickle-writing block **enabled**: rebuilds `X.pickle`/`y.pickle`
  from the images and trains on the full set (the "regeneration" half
  that is commented out in `test.py`). Its `DATADIR` points at an
  older machine's checkout — repoint it before running.
- `CatsAndDogs.ipynb` — two sections: a **PyTorch** attempt (data
  builder class, tensor setup, one sample visualized) and the
  **TensorFlow** version of the same CNN, trained 10 epochs.
- `VGG16.ipynb` — a 224px data-builder variant (`REBUILD_DATA = True`),
  a small custom convnet, and a **VGG16 transfer-learning** experiment
  (imagenet weights, early layers frozen, custom final layer). Note:
  its last cell references `vgg_modified_input`, which no cell
  defines — the experiment was left mid-work; cells run top-to-bottom
  as-is except where noted.

## How to run

```sh
pip install tensorflow opencv-python numpy matplotlib tqdm
# and torch, only for the PyTorch section of CatsAndDogs.ipynb
```

1. Get the Pet Images (see Data) and extract so you have a
   `PetImages/Cat` and `PetImages/Dog` directory.
2. Point `DATADIR` at it (`test.py`, `CatsAndDogs.ipynb` TF section;
   the notebook builders use the same layout under their `CATS`/`DOGS`
   paths).
3. Regenerate the pickles (below), then run `test.py` or the
   notebooks.

## Data

**No data files are committed** — by design. `X.pickle` (239 MB, the
100×100 grayscale arrays) and `y.pickle` (labels) live only in the
local working copy; `*.pickle` is gitignored repo-wide, and
`X.pickle` is the only copy of the processed arrays (regenerating it
needs the original images). `y.pickle` is trivially regenerable.

Oxford-IIIT Pet dataset (CC BY-SA 4.0), ~800 MB, re-downloadable —
index page <https://www.robots.ox.ac.uk/~vgg/data/pets/>:

- BitTorrent (recommended): <https://academictorrents.com/details/b18bbd9ba03d50b0f7f479acc9f4228a408cecc1>
- HTTP fallback (verified live 2026-08-23, redirects to a live file):
  <https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz>
  (dataset) and
  <https://thor.robots.ox.ac.uk/~vgg/data/pets/annotations.tar.gz>
  (ground truth).

The simplest is `catsdogs.py` with its `DATADIR` pointed at your
`PetImages` folder (the block is already enabled). Alternatively,
run the image-scanning block with `DATADIR` set: it's the
`##`-commented section at the top of `test.py`, a standalone cell in
the TF section of `CatsAndDogs.ipynb`, or the `DogsVSCats` builder
class in `VGG16.ipynb` (224px variant).

## Notes

- **Stale paths (documented, not fixed):** the notebooks point at old
  Colab mounts (`/content/drive/My Drive/CatsAndDogs/PetImages/…`),
  `test.py` at a previous local checkout
  (`/Users/Manoj/Downloads/CatsAndDogs/PetImages`), and `catsdogs.py`
  at an even older machine's checkout
  (`/Users/shz204/Downloads/CatsAndDogs/PetImages`). Nothing in the
  repo depends on any of these — point them at your extracted
  `PetImages` directory.
