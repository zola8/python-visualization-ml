# DL

https://www.youtube.com/watch?v=Z_ikDlimN6A

https://github.com/mrdbourke/pytorch-deep-learning

https://www.learnpytorch.io/

## Neural Networks

inputs -> turn into numbers -> (input layer -> hidden layers -> output layer)

input -> manipulation -> outputs -> turn to human understandable terms

- input data: images (ramen and spagetti)
- we want the neural network to learn the representations of the images
- we turn to term: is it ramen or spagetti?

## Anatomy of Neural Networks

input layer: data goes here
hidden layer(s): learns patterns in data
output layer: representation or prediction probabilities

- supervised learning: data + labels
- unsupervised learning & self-supervised: only data itself.
    - it figures out the fundamental patterns between cat and dog image
    - but it wouldn't necessarily know the difference between the two
- transfer learning
    - takes the patterns that one model has learned and transferring it to another model
- reinforcement learning

## What is PyTorch?

- popular research deep learning framework
- write fast DL code in python
- able to access many pre-built DL models (hub/models)
- whole stack: preprocess data, model data, deploy model ...

GPU: Graphics Processing Unit (video card)
- interface: CUDA (parallel computing platform that allows software to use GPU)

TPU: Tensor Processing Unit (server)

## What is a tensor?

Numbers represented by tensors.
