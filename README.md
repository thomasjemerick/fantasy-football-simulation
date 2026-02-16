# fantasy-football-simulation

Monte Carlo Playoff Probability Engine

A probabilistic simulation engine that computes playoff probabilities using real game win probabilities and Monte Carlo methods, with interactive scenario analysis and optimal rooting guidance.

This system models thousands of possible season outcomes using actual matchup win probabilities, allowing precise estimation of playoff odds and identification of the game outcomes that most affect a team’s chances.

Designed as a general framework for sports analytics, decision analysis, and probabilistic forecasting.

Key Capabilities

Real probabilistic modeling
Uses game-level win probabilities to simulate realistic season outcomes.

Monte Carlo simulation engine
Runs thousands of simulated seasons to estimate playoff probabilities with statistical convergence.

Team-specific playoff analysis ("Fan Guide")
User selects any team, and the system computes which game outcomes most improve that team’s playoff chances, effectively generating an optimal rooting strategy.

Scenario override and counterfactual analysis
Users can force specific game outcomes and immediately recalculate playoff probabilities to measure impact.

Decision sensitivity analysis
Quantifies how each remaining game affects playoff probability, identifying high-leverage matchups.

Interactive dashboard
Streamlit interface allows real-time simulation, parameter adjustment, and scenario exploration.
