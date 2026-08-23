# neural_networks

Repository to hold the Neural Networks built by me.

Machine-learning coursework notebooks: sklearn models plus a few
neural networks built from scratch with numpy. The companion MNIST
project lives in the top-level `MNIST/` folder.

## Notebooks

| Notebook | Contents |
|---|---|
| Basic Neural Network.ipynb | Building a neural network from scratch (numpy) |
| NN.ipynb | From-scratch net, shorter variant of the above |
| IRIS.ipynb | Iris: data loading, scaling, built-in model, then from-scratch forward/backprop |
| BreastCancer.ipynb | Breast-cancer data: logistic regression and a neural network |
| LinearRegression.ipynb | Linear regression walkthrough (train/test split, scaling) |
| DataAndAnalysis.ipynb | Linear + logistic regression on breast-cancer data. Kaggle-era: imports the Kaggle-only `MLmodels` module and has a stale `C:/Users/...` data path, so it will not run as-is |
| IntroToMachineLearning.ipynb | Basic data exploration, model validation, under/overfitting |
| Kaggle-IntermediateMachineLearning.ipynb | Kaggle course: missing values, categorical variables, feature engineering (needs `xgboost`) |
| NeuralNetwork.ipynb | AND gate with a neural network; pulsar classification (stale `C:/Users/.../pulsar_stars.csv` data path) |
| ScratchPad.ipynb | Scratch experiments (CLT, distributions, misc); references local `/Users/Manoj/Downloads/...` files |

## How to run

```bash
python -m venv .venv
.venv/bin/pip install numpy pandas scikit-learn matplotlib xgboost
.venv/bin/jupyter notebook
```

Notebook outputs are cleared; rerun cells to regenerate them.

## Reference

The code for Michael Nielsen's *Neural Networks and Deep Learning*
book, which this coursework was done alongside, is kept in the local
Nextcloud copy (`neural-networks-and-deep-learning-master/`) and is
not in this repo. Its MNIST dataset re-downloads from
<http://neuralnetworksanddeeplearning.com> (`data/mnist.pkl.gz`).
