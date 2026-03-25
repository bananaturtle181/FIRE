# Personal activity tracker
import sys

def main():
  
    daily_activity_goal , tracking_days  = get_args()
    days_hitting_target, total_step, daily_step = collect_steps(daily_activity_goal,tracking_days)
    highest_step, lowest_step, best_day, worst_day = compute_stats(total_step,tracking_days, daily_step)
    ave_step = total_step / tracking_days

    results = {"Daily steps":daily_step,
              "Total steps over tracking days":total_step,
              "Average steps":ave_step,
              "Best day = day": best_day,
              "Highest steps":highest_step,
              "Worst day= day": worst_day,
              "Lowest steps":lowest_step,
              "Days hitting goal":days_hitting_target
    }
    
    return results

def get_args():
    arg = sys.argv
    
    if len(arg) == 3:
        try:
            daily_activity_goal = int(arg[1])
            tracking_days = int(arg[2])
            
        except ValueError:
            sys.exit("Both daily goal and tracking days need to be integers")

    else: sys.exit("Incorrect number of arugments provided. Please enter an activity goal and the number of days to track only")
    return daily_activity_goal, tracking_days

def collect_steps(daily_activity_goal,tracking_days):
    daily_step = []
    total_step = 0
    hit_results = []

    if tracking_days <= 0:
        sys.exit("Invalid tracking days. Please enter an appropriate number of days to track")

    while len(daily_step) < tracking_days:    
            
        try:
            daily_step_count = int(input("What was your step count today?"))
        except ValueError:
            print("Step count is not an integer")
            continue

        if daily_step_count <= 0:
            print("Invalid step count. Step count must be positive and more than zero")
        else:
            daily_step.append(daily_step_count)
            total_step += daily_step_count
            hit_results.append(hit_miss(daily_step_count,daily_activity_goal))
            goal_hit = sum(hit_results)

    return goal_hit,total_step,daily_step

def compute_stats(total_step,tracking_days,daily_step):
    #Computing average number of steps per day
        ave_step = round(total_step / tracking_days)

        #Computing highest and lowest step count and best/worst day
        highest_step = max(daily_step)
        lowest_step = min(daily_step)

        try:
            best_day = daily_step.index(highest_step) + 1
            worst_day = daily_step.index(lowest_step) + 1
        except ValueError:
            sys.exit("Highest or lowest step count not found")
        return highest_step, lowest_step, best_day, worst_day

# def activity_tracker():

#     # Getting input from user for daily steps and how many days they want to track
#     arg = sys.argv
#     daily_step = []
#     total_step = 0
#     hit_results = []

#     # Validating user has input enough arguments
#     if len(arg) == 3:

#         # Try/except for values that may not be integers
#         try:
#             daily_activity_goal = int(arg[1])
#             tracking_days = int(arg[2])
            
#         except ValueError:
#             sys.exit("Both daily goal and tracking days need to be integers")

#     else: sys.exit("Incorrect number of arugments provided. Please enter an activity goal and the number of days to track only")

#     if tracking_days <= 0:
#         sys.exit("Invalid tracking days. Please enter an appropriate number of days to track")

#     while len(daily_step) < tracking_days:    
            
#         try:
#             daily_step_count = int(input("What was your step count today?"))
#         except (ValueError , UnboundLocalError):
#             print("Step count is not an integer")
#             continue

#         if daily_step_count <= 0:
#             print("Invalid step count. Step count must be positive and more than zero")
#         else:
#             daily_step.append(daily_step_count)
#             total_step += daily_step_count
#             hit_results.append(hit_miss(daily_step_count,daily_activity_goal))
    
#     #Computing how many days the step goal was hit
#     goal_hit = sum(hit_results)
        
#     #Computing average number of steps per day
#     ave_step = round(total_step / tracking_days)

#     #Computing highest and lowest step count and best/worst day
#     highest_step = max(daily_step)
#     lowest_step = min(daily_step)

#     try:
#         best_day = daily_step.index(highest_step) + 1
#         worst_day = daily_step.index(lowest_step) + 1
#     except ValueError:
#         sys.exit("Highest or lowest step count not found")

#     result = {"Daily steps":daily_step,
#               "Total steps over tracking days":total_step,
#               "Average steps":ave_step,
#               "Best day": best_day,
#               "Highest steps":highest_step,
#               "Worst day": worst_day,
#               "Lowest steps":lowest_step,
#               "Days hitting goal":goal_hit
#     }

#     return result


def hit_miss(step,goal):
    return step >= goal


if __name__ == "__main__":
    print(main())