def get_int():

    step_goal = int(input("What is your step goal? "))
    # daily_class = "Miss"
    daily_result = {}
    weekly_steps = 0
    hit_count = 0
    steps = []

    for day in range (1,8):
            while True:
                try:
                    daily_step = int(input("How many steps did you hit today? "))
                    break
                except ValueError:
                     print("Step count is not an integer.")

            if daily_step >= step_goal:
                daily_class = "Hit"
                hit_count += 1
            else:
                daily_class = "Miss"

            daily_result[day] = {"Hit or miss": daily_class,
                         "Step count": daily_step,
            }
            weekly_steps += daily_step
            steps.append(daily_step)

    max_step = max(steps)
    max_index = steps.index(max_step) + 1

    return [daily_result,
            f"Total steps for the week is {weekly_steps}",
            f"Average steps for the week is {round(weekly_steps/7)}",
            f"You hit your step goal {hit_count} day(s)",
            f"Highest step count is {max_step} which occured on day {max_index}"
            ]


test = get_int()
print(test)