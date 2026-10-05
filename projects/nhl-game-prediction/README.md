# NHL Game Outcome Modeling (Synthetic Example)

## Problem

Estimate home-win, draw, and away-win probabilities from pre-game expected-goal rates. The freelance project work covered NHL prediction workflows; this repository contains a separately authored educational example and does not include client code, odds, schedules, player data, or predictions.

## Method

A Poisson goal-count model assigns a distribution to each team's goals from two expected-goal inputs. The joint independent score distribution is summed into home-win, draw, and away-win probabilities. Inputs are illustrative and must be estimated from historical data before this method can be evaluated.

## Reproduce

Run `python example.py`. The script prints probabilities for a synthetic matchup. Change the two explicit expected-goal inputs to explore the model's behavior.

## Limitations

The independence assumption is simplistic; the inputs are not trained or calibrated; there is no backtest, betting edge, or performance claim. A real evaluation needs time-aware splits, calibration analysis, baselines, documented data provenance, and leakage checks. This example is not betting advice.
