def get_result(final_score): # param is dict

    home = final_score['home_score']
    away = final_score['away_score']
    if home > away:
        return 'Home win'
    elif home < away:
        return 'Away win'
    elif home == away:
        return 'Draw'

def get_results(final_scores):
    total = get_result(final_scores)
    return total



# (You could try and use a list comprehension for this)