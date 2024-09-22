import numpy as np

def preprocess_data(data):
    processed_data = np.array(data) / np.max(data)
    return processed_data

if __name__ == "__main__":
    sample_data = [100, 150, 200]
    processed = preprocess_data(sample_data)
    print(f"Processed Data: {processed}")
