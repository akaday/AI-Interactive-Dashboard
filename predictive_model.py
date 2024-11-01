import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate some sample data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([1, 1.5, 2, 2.5, 3], dtype=float)

# Define a simple linear model
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=500)

# Make predictions
print(model.predict([10.0]))
