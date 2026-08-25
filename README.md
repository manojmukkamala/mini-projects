# mini-projects

A collection of small personal projects and experiments — one folder per
project. Mostly Python (notebooks or scripts), with some MATLAB, R, and SQL.
Bigger standalone projects live in their own repositories; coursework lives
in the sibling [e-learning](https://github.com/manojmukkamala/e-learning)
repo.

## Projects

| Project | What it is | Stack |
|---|---|---|
| `MNIST` | MNIST digit classification with PyTorch (Sentdex tutorial follow-along) | Python, PyTorch |
| `breast_cancer` | Logistic-regression classifier on the UCI Wisconsin breast-cancer dataset (coursework) | MATLAB |
| `cats_and_dogs` | Cat-vs-dog CNN on the Oxford-IIIT Pet dataset (dataset re-downloadable; regeneration documented) | Python, notebook |
| `computer_vision` | OpenCV experiments: lane detection and practice notebooks (video demos) | Python, OpenCV |
| `death_rates` | Multivariate linear regression on US state death rates (coursework) | MATLAB |
| `diabetic_patients_readmission` | Predicting hospital readmission for diabetic patients from patient attributes | Python, notebook |
| `esp32_examples` | Small ESP32 hardware experiments: 12 V fan toggle and HC-SR04 ultrasonic distance reads | MicroPython, runs on the ESP32 |
| `esp32_mqtt` | MQTT smoke-test tools: PC-side paho scripts + ESP32 umqtt script, TLS via Traefik | Python, MicroPython |
| `esp32_whistle_counter` | KY-037 whistle counter that publishes the running total to an MQTT broker over the LAN | MicroPython, runs on the ESP32 |
| `excel_cell_name_finder` | Convert an Excel cell number to its column letter (e.g. 16384 → XFD) | Python, stdlib |
| `h1b_salary_analysis` | Salary survey for data-engineer roles from the DOL's public H-1B LCA disclosures | Python, notebook |
| `hhgtg` | NLP pipeline (tokenize → POS → frequency → TF-IDF → KMeans) over the five-book *Hitchhiker's Guide* series (corpus kept locally, copyrighted) | Python, notebook |
| `inko_random_wikipedia_article` | Tiny CLI that fetches a random English Wikipedia article's title + summary | Python, uv package + tests |
| `ionosphere` | Classification study on the UCI Johns Hopkins Ionosphere radar dataset | Python, notebook |
| `melbourne_housing` | Intro-ML tutorial: decision-tree house-price prediction on Kaggle's Melbourne Housing data | Python, notebook |
| `namemaker` | Random baby-name generator from name-word fragments | Python |
| `neural_networks` | 2024–25 ML coursework notebooks, from intro to Kaggle-intermediate (sklearn + basic neural nets) | Python, notebook |
| `predicting_pulsar_stars` | Identifying pulsar stars with a neural network on radio-telescope data | Python, notebook |
| `prime_number_finder` | Finding prime numbers up to N in T-SQL | SQL |
| `raspberrypi_examples` | Small Raspberry Pi hardware experiments (GPIO, camera) + a Pi provisioning script | Python/shell, runs on the Pi |
| `raspberrypi_spark_cluster` | Multi-node Spark 4.1.2 cluster on Raspberry Pis via Docker Compose (master/workers, Unity Catalog, RustFS) + a test job | Python, Docker |
| `second_most_word` | Find the second-most-repeated word in a paragraph (ties included) | Python, stdlib |
| `sqlparse` | Extract table names referenced in a SQL query (a tokenizing sketch) | Python, stdlib |
| `smart_kettle` | ESP32 kettle: MLX90614 temperature + HX711 load-cell level to an OLED and Home Assistant over MQTT | MicroPython, runs on the ESP32 |
| `stock_market_analysis` | Two market-analysis notebooks + a VFINX ROI-simulation subproject with a Streamlit dashboard | Python, notebook, Streamlit |
| `text_analytics` | Spam/ham SMS classification and a topic-modelling look (coursework) | R |
| `time_series_analysis` | Practice notebook on the classic Airline Passengers time series (1949–1960) | Python, notebook |

Original creation dates for the projects folded in from standalone repos
are noted in each project's README.

## Conventions

See [AGENTS.md](AGENTS.md) for the full rules. Short version:

- One folder per project, `snake_case` names.
- One `.venv` per project, created on demand (`uv sync` where a
  `pyproject.toml` exists) and never committed.
- Python dependencies via committed `pyproject.toml` + `uv.lock`.
- Notebook outputs are not committed.
- No videos, datasets, weights, or other bulky artifacts in git — excluded
  data is documented as re-downloadable in the project README.
