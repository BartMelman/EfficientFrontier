import numpy as np
import pandas as pd


def PCA(Sigma, numComponents):
    eigenValues, eigenVectors = np.linalg.eigh(Sigma)
    eigenValues = np.flip(eigenValues)
    eigenValues[numComponents:] = 0
    Q = np.flip(eigenVectors, 1)
    D = np.diag(eigenValues)
    ReducedSigma = np.matmul(np.matmul(Q, D), Q.T)
    np.fill_diagonal(ReducedSigma, np.diag(Sigma))
    return ReducedSigma


class GMV():
    def __init__(self, method, numComponents=None):
        self.w = None
        self.numCompanies = None
        self.method = method
        self.numComponents = numComponents

    def train(self, df):
        if self.method == 'IID':
            ### assume that the stocks are uncorrelated
            inverseVariance = 1/df.var()
            self.w = inverseVariance/sum(inverseVariance)
        elif self.method in ['general', 'PCA']:
            ### stocks can be correlated
            self.numCompanies = df.shape[1]
            Sigma = df.cov()
            if self.method == 'PCA':
                reducedSigma = PCA(Sigma, self.numComponents)
                Sigma = reducedSigma
            inverseSigma = np.linalg.inv(Sigma)
            iota = np.ones((self.numCompanies, 1))
            self.w = np.matmul(inverseSigma, iota) / (np.matmul(iota.T, np.matmul(inverseSigma, iota)))
            self.w = pd.DataFrame(self.w.T, columns=df.columns).iloc[0]
        else:
            raise ValueError('method not in options', self.method)


    def predict(self, df):
        return (self.w*df).sum(axis='columns')
