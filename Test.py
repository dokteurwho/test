# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:40:03 2016

@author: rom
"""

import numpy as np


#a new Test
#bye

class Test(object):

    def __init__(self, sizes):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def returnWeights(self):
        """Return the output of the network if ``a`` is input."""
        return self.weights

    def returnBiases(self):
        return self.biases


print("hello")

m = [5,4,3,12]

print(m[1:2])

classTest = Test(m)

print("Weights")
print(classTest.returnWeights()[0][0,0])
#print(np.sum(classTest.returnWeights,axis=0))
print("biases")
print(classTest.returnBiases())

for a,b in zip([5,4,9],[3,5]):
    print(a," ",b)
