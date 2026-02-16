# fantasy-football-simulation

# Monte Carlo Playoff Probability Engine

> A probabilistic simulation engine that computes playoff odds using real matchup win probabilities and large-scale Monte Carlo simulation.

**What it does:** simulates thousands of possible season outcomes to estimate playoff probabilities, quantify game-by-game leverage, and generate an **optimal rooting guide** for any selected team.

---

## ✨ Highlights

- **Real win probabilities → realistic simulations** (not coin flips)
- **Monte Carlo playoff odds** with configurable simulation count + tiebreak rules
- **“Fan Guide” / Rooting Guide**: pick a team and get **who to root for** in every remaining game
- **Counterfactual scenarios**: force winners and instantly recalculate playoff odds
- **Interactive dashboard** built with **Streamlit**

---

## 🧠 What this answers

- **What is each team’s probability of making the playoffs?**
- **Which remaining games matter most for Team X?**
- **Who should Team X’s fans root for?**
- **How much does one game swing playoff probability?**
- **What’s the best-case path to the playoffs?**

---

## 🔬 Methodology (Monte Carlo)

For each simulation:

1. Initialize current standings  
2. Simulate remaining games using win probabilities  
3. Compute final standings  
4. Select playoff teams based on league settings  

After **N** simulations, playoff probability is estimated empirically:

**Playoff Probability(team) = (# simulations team makes playoffs) / N**

This is the same core approach used in **sports forecasting**, **risk modeling**, and **quantitative Monte Carlo systems**.
