import pandas as pd


stats_mapper = {
    "player_id": {"dtype": "string", "name": "gsis_id_id"},
    "season": {"dtype": pd.Int16Dtype()},
    "week": {"dtype": pd.Int8Dtype()},
    "recent_team": {"dtype": "string", "name": "team_id"},
    "opponent_team": {"dtype": "string", "name": "opponent_team_id"},
    "completions": {"dtype": pd.Int8Dtype()},
    "attempts": {"dtype": pd.Int8Dtype()},
    "passing_yards": {"dtype": pd.Int16Dtype()},
    "passing_tds": {"dtype": pd.Int8Dtype()},
    "interceptions": {"dtype": pd.Int8Dtype()},
    "sacks": {"dtype": pd.Int8Dtype()},
    "sack_yards": {"dtype": pd.Int8Dtype()},
    "sack_fumbles": {"dtype": pd.Int8Dtype()},
    "sack_fumbles_lost": {"dtype": pd.Int8Dtype()},
    "passing_air_yards": {"dtype": pd.Int16Dtype()},
    "passing_yards_after_catch": {"dtype": pd.Int16Dtype()},
    "passing_first_downs": {"dtype": pd.Int8Dtype()},
    "passing_2pt_conversions": {"dtype": pd.Int8Dtype()},
    "carries": {"dtype": pd.Int8Dtype()},
    "rushing_yards": {"dtype": pd.Int16Dtype()},
    "rushing_tds": {"dtype": pd.Int8Dtype()},
    "rushing_fumbles": {"dtype": pd.Int8Dtype()},
    "rushing_fumbles_lost": {"dtype": pd.Int8Dtype()},
    "rushing_2pt_conversions": {"dtype": pd.Int8Dtype()},
    "rushing_first_downs": {"dtype": pd.Int8Dtype()},
    "receptions": {"dtype": pd.Int8Dtype()},
    "targets": {"dtype": pd.Int8Dtype()},
    "receiving_yards": {"dtype": pd.Int16Dtype()},
    "receiving_tds": {"dtype": pd.Int8Dtype()},
    "receiving_fumbles": {"dtype": pd.Int8Dtype()},
    "receiving_fumbles_lost": {"dtype": pd.Int8Dtype()},
    "receiving_yards_after_catch": {"dtype": pd.Int16Dtype()},
    "receiving_first_downs": {"dtype": pd.Int8Dtype()},
    "receiving_2pt_conversions": {"dtype": pd.Int8Dtype()},
    "target_share": {"dtype": pd.Float32Dtype(), "name": "receiving_target_share"},
    "special_teams_tds": {"dtype": pd.Int8Dtype()},
}