import random
from statistics import mean as ave

def run_quiz():
    random_results = []
    num_questions = random.randint(5,10)
    total_correct = 0
    final_results = {}

    for _ in range(num_questions):

        r_w = random.randint(0,1)
        random_results.append(r_w)

        total_correct += r_w

    average_score = ave(random_results)

    final_results = {"Questions attempted": num_questions,
                     "Correct answers": total_correct,
                     "Average score": average_score
    }

    return final_results

quiz_results = run_quiz()
print(quiz_results)