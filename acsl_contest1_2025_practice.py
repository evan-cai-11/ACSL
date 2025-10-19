def calculate_score(player_data):
    scores = {"A": 1, "R": 1, "O": 3, "G": 3, "B": 6, "AO": 5, "OB": 10, "BG": 10, "GR": 5}

    player_score = 0
    for i in range(len(player_data)):
        player_score += scores[player_data[i]]

    return player_score

def ordered_scores(p1, p2, p3):
    p1_data = p1.split()
    p2_data = p2.split()
    p3_data = p3.split()

    p1_score = calculate_score(p1_data)
    p2_score = calculate_score(p2_data)
    p3_score = calculate_score(p3_data)

    return p1_score, p2_score, p3_score

def setup():
    p1 = input()
    p2 = input()
    p3 = input()
    scores = ordered_scores(p1, p2, p3)
    sorted_scores = sorted(scores, reverse = True)
    print(sorted_scores)

setup()