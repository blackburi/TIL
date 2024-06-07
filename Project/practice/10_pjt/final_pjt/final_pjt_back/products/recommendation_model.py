import pandas as pd
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from .data_processing import get_product_data

def train_model(data):
    # Prepare data
    data = data.dropna(subset=['user_id', 'fin_prdt_cd'])
    user_ids = data['user_id'].unique()
    product_ids = data['fin_prdt_cd'].unique()
    
    user_id_map = {id: idx for idx, id in enumerate(user_ids)}
    product_id_map = {id: idx for idx, id in enumerate(product_ids)}

    data['user'] = data['user_id'].map(user_id_map)
    data['product'] = data['fin_prdt_cd'].map(product_id_map)

    # Create train and test sets
    train, test = train_test_split(data, test_size=0.2)

    # Define model
    user_input = Input(shape=(1,))
    product_input = Input(shape=(1,))

    user_embedding = Embedding(input_dim=len(user_ids), output_dim=50)(user_input)
    product_embedding = Embedding(input_dim=len(product_ids), output_dim=50)(product_input)

    user_vec = Flatten()(user_embedding)
    product_vec = Flatten()(product_embedding)

    dot_product = Dot(axes=1)([user_vec, product_vec])
    output = Dense(1, activation='linear')(dot_product)

    model = Model([user_input, product_input], output)
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

    # Train model
    model.fit([train['user'], train['product']],train['rating'],  epochs=5, verbose=1)

    # Save model and mappings
    model.save('./recommendation_model.h5')
    np.save('./user_id_map.npy', user_id_map)
    np.save('./product_id_map.npy', product_id_map)

    return model
    # return data

if __name__ == '__main__':
    data = get_product_data()
    train_model(data)


def load_trained_model():
    model = load_model('./recommendation_model.h5')
    user_id_map = np.load('./user_id_map.npy', allow_pickle=True).item()
    product_id_map = np.load('./product_id_map.npy', allow_pickle=True).item()
    return model, user_id_map, product_id_map


