import numpy as np


def normalize_data(data):

    data = np.array(data)

    mean = np.mean(data, axis=0)

    std = np.std(data, axis=0)

    normalized_data = (data - mean) / std

    return normalized_data.tolist()
