import random
import math

def generate_samples(mean, variance, num_samples):
    return [random.normalvariate(mean, math.sqrt(variance)) for sample in range(num_samples)]

def train_model(samples_1, samples_2):
    mean_1 = sum(samples_1) / len(samples_1)
    mean_2 = sum(samples_2) / len(samples_2)
    return mean_1, mean_2

def classify(sample, mean_1, mean_2):
    if abs(sample - mean_1) < abs(sample - mean_2):
        return 1
    else:
        return 2

def run_experiment(num_samples) :
    samples_1 = generate_samples(mean=0.5, variance=1, num_samples = num_samples)
    samples_2 = generate_samples(mean=3, variance=2, num_samples = num_samples)
    
    mean_1, mean_2 = train_model(samples_1, samples_2)

    test_samples = generate_samples(mean=2.25, variance=1.35, num_samples=100)
    classifications = [classify(sample, mean_1, mean_2) for sample in test_samples]

    print(f"Mean of distribution 1: {mean_1}")
    print(f"Mean of distribution 2: {mean_2}")
    print(f"Number of samples: {num_samples}")
    print(f"Classifications: {classifications}\n")

for num_samples in [50, 500, 5000]:
    run_experiment(num_samples)