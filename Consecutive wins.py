def win_counter(results):

    win_count = 0
    current_streak = 0
    streak_detected = False

    for games in results: 
        #Counting total wins

        if games == 1:
            win_count += 1
            current_streak +=1
        
        elif games == 0:
            current_streak = 0

        if current_streak >= 2:
            streak_detected = True

    return { "win_count": win_count, 
            "streak?": streak_detected
            }

results = [1, 0, 1, 1, 0, 1, 1, 1]
print(win_counter(results))