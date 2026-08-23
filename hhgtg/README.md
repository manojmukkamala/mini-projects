# hhgtg

NLP exercise notebook over the complete five-book *Hitchhiker's Guide to
the Galaxy* series (Douglas Adams): tokenization → POS tagging → word
frequency → dictionary definitions → TF / TF-IDF matrices → KMeans
clustering of sentences. Built as a Colab notebook (2024).

## What's here

- `HHGTG.ipynb` — the notebook (outputs cleared)

## The corpus is NOT in this repo (by design)

The notebook's data — the full text of all five books — is copyrighted
and intentionally **not committed**. Locally, the corpus lives as
per-chapter PDFs under `~/Nextcloud/Shared/Books/HHGTG/`:

| Folder | Book |
|---|---|
| `1. hhgtg` | The Hitch Hiker's Guide to the Galaxy |
| `2. rateou` | The Restaurant at the End of the Universe |
| `luae` | Life, the Universe and Everything |
| `slatfat` | So Long, and Thanks for All the Fish |
| `mh` | Mostly Harmless |

The notebook consumes `dont_panic.pickle`: a list
`[hhgtg, rateou, luae, slatfat, mh]` where each element is a list of
chapter strings. Regenerate it from the PDFs (`pdftotext` from poppler; text verified
identical to the 2024 extracts up to whitespace, which the notebook's
cleaning cells normalize anyway):

```python
import os, pickle, subprocess

BASE = os.path.expanduser("~/Nextcloud/Shared/Books/HHGTG")
BOOKS = ["1. hhgtg", "2. rateou", "luae", "slatfat", "mh"]

def chapters(folder):
    d = os.path.join(BASE, folder)
    files = sorted((f for f in os.listdir(d) if f.startswith("ch")),
                   key=lambda f: int(f[2:-4]))
    return [subprocess.check_output(["pdftotext", "-q", os.path.join(d, f), "-"]).decode()
            for f in files]

dont_panic = [chapters(b) for b in BOOKS]
with open("dont_panic.pickle", "wb") as f:
    pickle.dump(dont_panic, f)
```

## Running the notebook

It was authored in Colab, so before running:

- Re-point the `/content/drive/...HHGTG/...` paths at local equivalents.
- The original `get_book()` fetch source (an angelfire mirror) is dead —
  load the pickle instead of scraping.
- Runtime deps: `nltk` (stopwords, punkt, averaged_perceptron_tagger,
  wordnet), `PyDictionary`, `fpdf`, plus the usual pandas / numpy /
  scipy / sklearn / seaborn stack. No manifest — notebook-only project
  (repo convention: lazy manifests).
