"""Synthetic Poisson scoreline example; not trained on client or NHL data."""
from math import exp, factorial


def poisson_pmf(rate: float, goals: int) -> float:
    return exp(-rate) * rate**goals / factorial(goals)


def outcome_probabilities(home_xg: float, away_xg: float, max_goals: int = 12):
    home = draw = away = 0.0
    for home_goals in range(max_goals + 1):
        p_home = poisson_pmf(home_xg, home_goals)
        for away_goals in range(max_goals + 1):
            probability = p_home * poisson_pmf(away_xg, away_goals)
            if home_goals > away_goals:
                home += probability
            elif home_goals == away_goals:
                draw += probability
            else:
                away += probability
    return {"home_win": home, "draw": draw, "away_win": away}


if __name__ == "__main__":
    # Made-up expected-goal rates for demonstration only.
    for outcome, probability in outcome_probabilities(3.1, 2.7).items():
        print(f"{outcome}: {probability:.1%}")
