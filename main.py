import streamlit as st
import numpy as np
import pandas as pd

# -------------------------
# LEAGUE DATA
# -------------------------

# League 1: your main 10-team league (4-team playoff)
league1_teams_data = [
    {"team": "Team 01",      "wins": 8, "pf": 1808.9},
    {"team": "Team 02",             "wins": 7, "pf": 1662.47},
    {"team": "Team 03",    "wins": 7, "pf": 1689.74},
    {"team": "Team 04", "wins": 8, "pf": 1672.35},
    {"team": "Team 05",    "wins": 6, "pf": 1840.97},
    {"team": "Team 06","wins": 6, "pf": 1757.76},
    {"team": "Team 07",     "wins": 6, "pf": 1642.12},
    {"team": "Team 08",              "wins": 6, "pf": 1580.12},
    {"team": "Team 09",           "wins": 4, "pf": 1498.64},
    {"team": "Team 10",                   "wins": 2, "pf": 1277.85},
]

league1_games_data = [
    # Week, GameID, TeamA, TeamB, ProbA
    (13, 11, "Team 10",                 "Team 04",0.25),
    (13, 12, "Team 03",  "Team 02",               0.5000),
    (13, 13, "Team 01",    "Team 07",       0.52),
    (13, 14, "Team 05",  "Team 08",                0.54),
    (13, 15, "Team 06","Team 09",          0.52),
]

# League 2: 8-team league (6-team playoff)
league2_teams_data = [
    {"team": "Team 11",         "wins": 8, "pf": 1589.85},
    {"team": "Team 12",  "wins": 7, "pf": 1432.90},
    {"team": "Team 13",           "wins": 6, "pf": 1268.85},
    {"team": "Team 14",      "wins": 5, "pf": 1394.00},
    {"team": "Team 15",             "wins": 4, "pf": 1437.95},
    {"team": "Team 16",         "wins": 4, "pf": 1272.90},
    {"team": "Team 17",            "wins": 4, "pf": 1238.80},
    {"team": "Team 18",           "wins": 2, "pf": 1096.75},
]

league2_games_data = [
    # Week, GameID, TeamA, TeamB, ProbA
    (11, 1,  "Team 18",           "Team 16",         0.92),
    (11, 2,  "Team 12", "Team 13",           0.1),
    (11, 3,  "Team 15",             "Team 17",            0.86),
    (11, 4,  "Team 11",        "Team 14",      0.36),
    (12, 5,  "Team 12", "Team 18",           0.56644),
    (12, 6,  "Team 16",         "Team 15",             0.46956),
    (12, 7,  "Team 13",           "Team 11",        0.44386),
    (12, 8,  "Team 17",            "Team 14",      0.47053),
    (13, 9,  "Team 18",           "Team 15",             0.43269),
    (13, 10, "Team 11",        "Team 12", 0.52596),
    (13, 11, "Team 14",      "Team 16",         0.52270),
    (13, 12, "Team 17",            "Team 13",           0.49401),
    (14, 13, "Team 18",           "Team 15",             0.43269),
    (14, 14, "Team 11",        "Team 17",            0.56205),
    (14, 15, "Team 14",      "Team 18",           0.55967),
    (14, 16, "Team 17",            "Team 11",        0.43795),
    (15, 17, "Team 13",           "Team 17",            0.50599),
    (15, 18, "Team 16",         "Team 13",           0.50080),
    (15, 19, "Team 12", "Team 16",         0.52957),
    (15, 20, "Team 14",      "Team 12", 0.49312),
]

# League 3: [REDACTED] – 12-team league (6-team playoff)
league3_teams_data = [
    {"team": "Team 19", "wins": 8, "pf": 1272.38},
    {"team": "Team 20",                 "wins": 7, "pf": 1276.40},
    {"team": "Team 21",             "wins": 7, "pf": 1219.92},
    {"team": "Team 22",   "wins": 6, "pf": 1178.70},
    {"team": "Team 23",                 "wins": 6, "pf": 1167.50},
    {"team": "Team 24", "wins": 6, "pf": 1107.36},
    {"team": "Team 25",            "wins": 5, "pf": 1206.22},
    {"team": "Team 26",           "wins": 5, "pf": 1062.48},
    {"team": "Team 27",        "wins": 3, "pf": 1149.64},
    {"team": "Team 28",             "wins": 3, "pf": 1114.34},
    {"team": "Team 29",                    "wins": 2, "pf": 1148.04},
    {"team": "Team 30",              "wins": 2, "pf": 1083.52},
]

league3_games_data = [
    # Week, GameID, TeamA, TeamB, ProbA
    (11, 1,  "Team 22",   "Team 20",              0.74),
    (11, 2,  "Team 26",          "Team 30",           0.04),
    (11, 3,  "Team 19","Team 27",     0.65),
    (11, 4,  "Team 24","Team 29",                 0.9999999999),
    (11, 5,  "Team 21",            "Team 28",          0.84),
    (11, 6,  "Team 23",                "Team 25",         0.0),
    (12, 7,  "Team 26",          "Team 22",0.4740716944),
    (12, 8,  "Team 20",                "Team 19", 0.5007886126),
    (12, 9,  "Team 30",             "Team 24", 0.4945592639),
    (12, 10, "Team 27",       "Team 21",          0.4851702426),
    (12, 11, "Team 29",                   "Team 23",              0.4957979564),
    (12, 12, "Team 28",            "Team 25",         0.4802030544),
    (13, 13, "Team 22",  "Team 19", 0.4808900566),
    (13, 14, "Team 24","Team 26",        0.5103417764),
    (13, 15, "Team 21",            "Team 20",              0.4886873478),
    (13, 16, "Team 23",                "Team 30",           0.5186537658),
    (13, 17, "Team 25",           "Team 27",     0.5120083536),
    (13, 18, "Team 28",            "Team 29",                 0.4925520912),
    (14, 19, "Team 24","Team 22",0.484396735),
    (14, 20, "Team 19","Team 21",          0.5105244152),
    (14, 21, "Team 26",          "Team 23",              0.4764527036),
    (14, 22, "Team 20",                "Team 25",         0.5141342614),
    (14, 23, "Team 30",             "Team 28",          0.4929886344),
    (14, 24, "Team 27",       "Team 29",                 0.5003481773),
]

LEAGUES = {
    "League A": {
        "teams_data": league1_teams_data,
        "games_data": league1_games_data,
        "num_playoff_teams": 4,
        "default_focus_team": "Team 05",
    },
    "League B": {
        "teams_data": league2_teams_data,
        "games_data": league2_games_data,
        "num_playoff_teams": 6,
        "default_focus_team": "Team 11",  # can change if you want
    },
    "League C": {
        "teams_data": league3_teams_data,
        "games_data": league3_games_data,
        "num_playoff_teams": 6,
        "default_focus_team": "Team 26",   # assuming this is you
    },
}

# -------------------------
# STREAMLIT UI – LEAGUE SELECT
# -------------------------

st.title("Fantasy Playoff Odds Simulator")

league_choice = st.sidebar.selectbox(
    "Select league",
    list(LEAGUES.keys()),
    index=0
)

league_cfg = LEAGUES[league_choice]

teams_df = pd.DataFrame(league_cfg["teams_data"])
games_df = pd.DataFrame(
    league_cfg["games_data"],
    columns=["week", "game_id", "team_a", "team_b", "prob_a"]
)
num_playoff_teams = league_cfg["num_playoff_teams"]
default_focus_team = league_cfg["default_focus_team"]

st.markdown(
    f"### {league_choice} "
)
st.markdown(
    "This sim runs many random seasons using your remaining schedule and odds. "
    "You can **force specific matchups** and see how that changes playoff chances, "
    "then get a **rooting guide** for a chosen team."
)

# -------------------------
# GLOBAL SETTINGS
# -------------------------

st.sidebar.header("Simulation Settings")
n_sims = st.sidebar.slider("Number of simulations", 1_000, 50_000, 10_000, step=1_000)
seed = st.sidebar.number_input("Random seed (0 = none)", min_value=0, value=0)
use_pf_tiebreaker = st.sidebar.checkbox("Use PF as tiebreaker", value=True)

if seed != 0:
    np.random.seed(seed)

st.sidebar.markdown("------")
st.sidebar.subheader("Forced Outcomes")

st.sidebar.caption(
    "For any matchup, choose Random (use ProbA) or force Team A / Team B to win."
)

override_options = ["Random", "Force Team A", "Force Team B"]
# overrides_sidebar: (week, game_id) -> 'R' | 'A' | 'B'
overrides_sidebar: dict[tuple[int, int], str] = {}

for _, row in games_df.iterrows():
    label = f"Week {row['week']} – {row['team_a']} vs {row['team_b']}"
    key = f"{league_choice}_override_{row['week']}_{row['game_id']}"
    choice = st.sidebar.selectbox(label, override_options, index=0, key=key)
    if choice == "Random":
        overrides_sidebar[(int(row["week"]), int(row["game_id"]))] = "R"
    elif choice == "Force Team A":
        overrides_sidebar[(int(row["week"]), int(row["game_id"]))] = "A"
    else:
        overrides_sidebar[(int(row["week"]), int(row["game_id"]))] = "B"

# -------------------------
# SIMULATION LOGIC
# -------------------------

def run_simulation(
    n_sims: int,
    overrides: dict[tuple[int, int], str],
    num_playoff_teams: int
) -> pd.DataFrame:
    """Run n_sims seasons with given overrides; return playoff odds table."""
    teams = teams_df["team"].tolist()
    pf_map = teams_df.set_index("team")["pf"].to_dict()

    playoff_counts = {t: 0 for t in teams}
    total_wins = {t: 0.0 for t in teams}

    for _ in range(n_sims):
        # start from current wins
        wins = teams_df.set_index("team")["wins"].astype(float).to_dict()

        # play out all remaining games
        for _, g in games_df.iterrows():
            w_game = int(g["week"])
            gid = int(g["game_id"])
            a = g["team_a"]
            b = g["team_b"]
            p_a = float(g["prob_a"])

            override = overrides.get((w_game, gid), "R")

            if override == "A":
                winner, loser = a, b
            elif override == "B":
                winner, loser = b, a
            else:
                # random outcome based on prob_a
                if np.random.rand() <= p_a:
                    winner, loser = a, b
                else:
                    winner, loser = b, a

            wins[winner] += 1  # PF/PA stay fixed; only wins change

        # build final table
        sim_df = pd.DataFrame({
            "team": teams,
            "wins": [wins[t] for t in teams],
            "pf":   [pf_map[t] for t in teams],
        })

        if use_pf_tiebreaker:
            sim_df = sim_df.sort_values(["wins", "pf"], ascending=[False, False])
        else:
            sim_df = sim_df.sort_values(["wins", "team"], ascending=[False, True])

        sim_df = sim_df.reset_index(drop=True)

        # top N make playoffs
        playoff_teams = sim_df.head(num_playoff_teams)["team"].tolist()

        for t in teams:
            total_wins[t] += wins[t]
            if t in playoff_teams:
                playoff_counts[t] += 1

    # aggregate
    results = pd.DataFrame({
        "Team": teams,
        "BaseWins": teams_df["wins"].astype(float),
        "AvgFinalWins": [total_wins[t] / n_sims for t in teams],
        "PlayoffProb":  [playoff_counts[t] / n_sims for t in teams],
    })

    results = results.sort_values("PlayoffProb", ascending=False).reset_index(drop=True)
    return results


def compute_effects_for_team(
    my_team: str,
    base_overrides: dict[tuple[int, int], str],
    n_sims_effect: int,
    num_playoff_teams: int
):
    """
    For each *undecided* game, compute how forcing A or B affects my_team's playoff prob.
    Respects existing overrides (forced results) as part of the baseline.
    Returns:
      effects_df, baseline_prob, optimal_prob, optimal_overrides
    """

    # 1. BASELINE — uses current sidebar overrides
    baseline_results = run_simulation(n_sims_effect, base_overrides, num_playoff_teams)
    baseline_prob = float(
        baseline_results.loc[baseline_results["Team"] == my_team, "PlayoffProb"]
    )

    records = []

    # 2. For each game: Compare forcing A vs B, unless already decided
    for _, g in games_df.iterrows():
        wk = int(g["week"])
        gid = int(g["game_id"])
        key = (wk, gid)

        # If this game is ALREADY DECIDED in overrides, skip it
        if base_overrides.get(key, "R") in ["A", "B"]:
            continue

        a = g["team_a"]
        b = g["team_b"]

        # Force A wins
        overA = base_overrides.copy()
        overA[key] = "A"
        resA = run_simulation(n_sims_effect, overA, num_playoff_teams)
        probA = float(resA.loc[resA["Team"] == my_team, "PlayoffProb"])

        # Force B wins
        overB = base_overrides.copy()
        overB[key] = "B"
        resB = run_simulation(n_sims_effect, overB, num_playoff_teams)
        probB = float(resB.loc[resB["Team"] == my_team, "PlayoffProb"])

        records.append({
            "Week": wk,
            "GameID": gid,
            "Matchup": f"{a} vs {b}",
            "Outcome_A": f"{a} wins",
            "Outcome_B": f"{b} wins",
            a + " win prob": probA,
            b + " win prob": probB,
            "Delta_A": probA - baseline_prob,
            "Delta_B": probB - baseline_prob,
        })

    effects_df = pd.DataFrame(records)

    # If everything is already forced, nothing left to optimize
    if effects_df.empty:
        effects_df["BestOutcomeForTeam"] = pd.Series(dtype=str)
        effects_df["BestDelta"] = pd.Series(dtype=float)
        optimal_overrides = base_overrides.copy()
        optimal_prob = baseline_prob
        return effects_df, baseline_prob, optimal_prob, optimal_overrides

    # 3. Optimal choices ONLY for undecided games
    optimal_overrides = base_overrides.copy()
    best_outcomes = []
    best_deltas = []

    for _, row in effects_df.iterrows():
        wk = row["Week"]
        gid = row["GameID"]
        key = (wk, gid)

        a_name, b_name = row["Matchup"].split(" vs ")

        if row["Delta_A"] >= row["Delta_B"]:
            optimal_overrides[key] = "A"
            best_outcomes.append(f"{a_name} beats {b_name}")
            best_deltas.append(row["Delta_A"])
        else:
            optimal_overrides[key] = "B"
            best_outcomes.append(f"{b_name} beats {a_name}")
            best_deltas.append(row["Delta_B"])

    effects_df["BestOutcomeForTeam"] = best_outcomes
    effects_df["BestDelta"] = best_deltas

    # 4. Recompute best possible playoff odds under the optimal path
    optimal_results = run_simulation(n_sims_effect, optimal_overrides, num_playoff_teams)
    optimal_prob = float(
        optimal_results.loc[optimal_results["Team"] == my_team, "PlayoffProb"]
    )

    return effects_df, baseline_prob, optimal_prob, optimal_overrides


# -------------------------
# RUN SIM & DISPLAY RESULTS
# -------------------------

results = run_simulation(n_sims, overrides_sidebar, num_playoff_teams)

st.subheader(f"Playoff Odds – {league_choice}")
st.caption(f"Top {num_playoff_teams} teams make the playoffs in this league.")
st.dataframe(
    results.style.format({"AvgFinalWins": "{:.2f}", "PlayoffProb": "{:.1%}"})
)

# -------------------------
# OPTIMAL PATH / ROOTING GUIDE
# -------------------------

st.markdown("---")
st.subheader("Optimal Path / Rooting Guide")

team_options = teams_df["team"].tolist()
default_index = team_options.index(default_focus_team) if default_focus_team in team_options else 0
my_team = st.selectbox("Focus team", team_options, index=default_index)

st.caption(
    "We treat the current overrides as the baseline scenario, "
    "then for each *undecided* game we ask: "
    f"‘If this side is forced to win, how does that change {my_team}'s playoff chances?’"
)

with st.spinner("Computing game-by-game impact..."):
    effects_df, baseline_prob, optimal_prob, optimal_overrides = compute_effects_for_team(
        my_team,
        overrides_sidebar,
        n_sims_effect=n_sims,
        num_playoff_teams=num_playoff_teams
    )

st.markdown(
    f"**Baseline playoff probability for `{my_team}`:** "
    f"**{baseline_prob:.1%}**"
)
st.markdown(
    f"**If every remaining undecided game broke the best possible way for `{my_team}`,** "
    f"their playoff probability would be about **{optimal_prob:.1%}**."
)

st.markdown("#### Game-by-game impact on your playoff odds")

effects_display = effects_df.copy()

if not effects_display.empty:
    effects_display["Delta_A"] = effects_display["Delta_A"].map(lambda x: f"{x:+.1%}")
    effects_display["Delta_B"] = effects_display["Delta_B"].map(lambda x: f"{x:+.1%}")
    effects_display["BestDelta"] = effects_display["BestDelta"].map(lambda x: f"{x:+.1%}")
    effects_display = effects_display.sort_values("BestDelta", ascending=False)

    st.dataframe(effects_display[
        ["Week", "GameID", "Matchup", "Outcome_A", "Delta_A",
         "Outcome_B", "Delta_B", "BestOutcomeForTeam", "BestDelta"]
    ])
else:
    st.info("All remaining games are already forced in the sidebar; no undecided games to analyze.")

# -------------------------
# RAW INPUTS
# -------------------------

st.subheader("Raw Inputs")
with st.expander("Current Standings"):
    st.dataframe(teams_df)
with st.expander("Remaining Schedule & Probabilities"):
    st.dataframe(games_df)
