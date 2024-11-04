# Task: Write a Python function called track_scores
# Create a function that can take an arbitrary number of game scores as arguments.
# The function should print:
#
# The highest score.
# The lowest score.
# The total number of scores provided.
# If no scores are provided, it should print: "No scores to track."
# Call the function with the scores 45, 67,and 89.

def track_scores(*scores):
    if not scores:
        print("no scores to track.")
    else:
        highest_score = max(scores)
        lowest_score = min(scores)
        total_scores = len(scores)

        print(f"highest score: {highest_score}")
        print(f"lowest score: {lowest_score}")
        print(f"total number of scores: {total_scores}")


track_scores(45,67,89)
