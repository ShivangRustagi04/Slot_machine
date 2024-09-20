import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Symbols for slot machine
symbols = ['A', 'B', 'C', 'D', 'Jackpot']

# Generate synthetic spin data
def generate_spin_data(num_samples=10000):
    data = []
    for _ in range(num_samples):
        reel1 = np.random.choice(symbols)
        reel2 = np.random.choice(symbols)
        reel3 = np.random.choice(symbols)
        
        # Define win condition (win if all symbols in the middle row match)
        win = int(reel1 == reel2 == reel3)
        
        # Feature vector includes reel1, reel2, reel3 (encoded as one-hot)
        data.append([reel1, reel2, reel3, win])
    
    return pd.DataFrame(data, columns=['reel1', 'reel2', 'reel3', 'win'])

# Encode symbols into one-hot for ML model
def encode_data(df):
    return pd.get_dummies(df[['reel1', 'reel2', 'reel3']], drop_first=True)

# Train the model
def train_model():
    # Generate and encode data
    df = generate_spin_data()
    X = encode_data(df)
    y = df['win']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Test the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy:.2f}')
    
    # Save the model
    with open('model/slot_model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    train_model()
