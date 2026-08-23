# Predicting-Pulsar-Stars

This repository holds the Jupyter notebook developed to identify Pulsar stars from a given dataset. Along with the Jupyter notebook other python files required to implement the Neural Network model are stored.

The repository is mainly having the following files:

### DeepNN.py

•	Includes all the necessary functions required to implment the Neural Network. 

•	ReLu activation function is choosen for the hidden layers whereas the Output layer computes sigmoid activation function.

•	Log Loss function is used to compute the Cost.

•	Backward propagation is implemented using Gradient Descent to facilitate the learning process.

•	The default learning rate is set to 0.0075 and the default number of iterations are 3000.

•	Predict function is also implemented to compute the accuracy of the model over training/test sets.


### PulsarPrediction.ipynb

•	Implemented the Neural Network model over a Pulsar stars dataset obtained from: https://www.kaggle.com/pavanraj159/predicting-a-pulsar-star.

•	Performed initial data exploration and data visualization by importing all the required packages.

•	Splitted the dataset into training and test sets and implemented the Neural Network model over the training set.

•	Using the parameters learned by the model over the training, predictions over the test set were computed and achieved the accuracy of 97.8%.

•	Working on improving the accuracy of the model through hyperparameter tuning and other techniques.


### dnn_utils.py

•	Includes the code to compute the math behind the sigmoid and relu activation functions.


### pulsar_stars.csv

•	The dataset used to implement the Neural Network.

## How to run

Python project (Jupyter notebook). Requirements: `jupyter`, `numpy`, `pandas`,
`matplotlib`, `seaborn`, `scikit-learn`, `pillow` (e.g. `pip install jupyter numpy pandas matplotlib seaborn scikit-learn pillow`).

Open the notebook from this folder so it can find `pulsar_stars.csv` and import
`dnn_utils.py` / `DeepNN.py` from disk:

```sh
jupyter notebook PulsarPrediction.ipynb
```

The notebook walks through EDA, scaling, and the hand-rolled neural network,
reporting ~97.8% test accuracy.

The dataset is public: <https://www.kaggle.com/pavanraj159/predicting-a-pulsar-star>.


---

*Original work: 2018-08 (first committed to GitHub 2018-08-06).*
