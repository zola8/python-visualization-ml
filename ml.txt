https://www.youtube.com/watch?v=BUTjcAjfMgY


intelligence:
    - understand how the world works
    - world = complex thing, we use model

model:
    - something that lets you make prediction
    - input data -> (mental) model -> prediction        , black clouds -> mind -> it's going to rain
    - 3 ways computers can learn:
        - machine learning (ML)
        - deep learning (DL)
        - reinforcement learning (RL)

1. Machine Learning (ML)
    - allows computer to learn tasks directly from data
    - training (phase 1):
            training data -> learning algorithm -> ML model
    - inference (phase 2):
            new data -> ML model -> prediction

    - inference: (prediction) y = mx+b
    - training phase:
        L (loss function) = actual values - predicted values
        goal: find parameter values with smallest loss      --> gradient loss
    - computers can fit models to reality using data and maths
    - different ways to learn parameters from data:
            - linear regression             (regression)
            - logistic regression           (classification)
            - decision tree                 (both)
            - random forest                 (both)
            - support vector machine        (both)
            - XGBoost                       (both)


2. Deep Learning (DL)
    - neural networks that learn optimal features (on their own)
    - cat image -> pixel -> contour -> shape -> parts of objects -> high level concepts -> output layer, prediction  == layers
    - Neural Networks (NN): a series of operations that can approximate any function
    - neuron = fundamental building block of NN
        x (it takes a set of inputs) * multiplies by weights, sums together, adds a scalar value (bias), then passes through a nonlinear function
        z = g(∑(w*x + b))
        z = output, g = activation
    - neurons -> layers -> network
    - different type of
        - neurons: vanilla, LSTM
        - activations: ReLU, sigmoid, tanh, softmax
        - layers: fully connected, recurrent, convolutional, attention, pooling, normalization, dropout
        - networks: feedforward (FFNN), RNN, CNN, transformer
    - training neural nets:
        - searching for the parameters with the smallest loss
        - gradient descent = algorith for updating parameters to minimize loss
            new params = old params - learning rate * gradient loss
        - more optimizers: (variation of gradient descent used in practice)
            - gradient descent, SGD, mini batch GD, adaptive moment estimation
        - hyperparameters: values that guide the training process
            - epoch: number of times the entire dataset is passed through the model during training
            - learning rate: how much to adjust weights
            - batch size: number of samples used to compute each update to the model's weights
            - dropout: fraction of neurons randomly set to 0 during training to prevent overfitting


3. Reinforcement learning (RL)
    - computer learns trough trial and error
    - (supervised learning: human curates examples -> model learns from examples, from high quality data)
    - RL: model interacts with reality and get reward for good actions
    - models are not bound by human labelling or expertise
    - example: alpha go, SL (supervised learning) cannot surpass the grandmaster level
    - how does it work?
        - update parameters to maximize rewards
        - J (objective, reward) = SUM( model output * reward at time )
        - the model isn't producing prediction,
        - rather it's generating probability distribution of different actions it might take (given the current state of the environment)
        - we want to update the parameters that our model gives a high probability to actions, which results in high reward
    - more RL techniques


data:
    - what makes good data?
        quantity: more is better > than less (prone to overfitting = memorizing and doesn't generalize)
        quality: garbage in -> garbage out, should represent reality
            accuracy: correctness
            diversity: representativeness of your data, contain all the different scenarios you want to use
