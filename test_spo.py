import random
from spo import generate_spo_levels

def generate_random_binary_sequence(length=7):
    return [random.randint(0, 1) for _ in range(length)]

def test_all_levels_on_input(x):
    spo_levels = generate_spo_levels()
    results = []
    for i, level_fn in enumerate(spo_levels, start=1):
        try:
            output = level_fn(x)
        except Exception as e:
            output = f"Error: {e}"
        results.append((i, output))
    return results

def print_results(results, x):
    print(f"Input sequence: {x}")
    for level, result in results:
        print(f"Level {level:03d} → Output: {result}")

def evaluate_multiple_runs(num_runs=5, seq_length=7):
    spo_levels = generate_spo_levels()
    scores = [0] * len(spo_levels)

    for _ in range(num_runs):
        x = generate_random_binary_sequence(seq_length)
        for i, level_fn in enumerate(spo_levels):
            try:
                output = level_fn(x)
                if output in (0, 1):
                    scores[i] += 1
            except:
                continue

    for i, score in enumerate(scores, start=1):
        print(f"Level {i:03d} → Passed {score}/{num_runs} runs")

if __name__ == "__main__":
    # Example: single input test
    sample_input = generate_random_binary_sequence()
    results = test_all_levels_on_input(sample_input)
    print_results(results, sample_input)

    # Uncomment to run multiple evaluations
    # evaluate_multiple_runs(num_runs=10)
