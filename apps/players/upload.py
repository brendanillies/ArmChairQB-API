import pandas as pd


players_mapper = {
    "gsis_id": {"dtype": "string"},
    "espn_id": {"dtype": pd.Int32Dtype()},
    "yahoo_id": {"dtype": pd.Int32Dtype()},
    "name": {"dtype": "string", "name": "player_name"},
    "db_season": {"dtype": pd.Int16Dtype()},
    "college": {"dtype": "string"},
}

depth_charts_mapper = {
    "season": {"dtype": pd.Int16Dtype()},
    "club_code": {"dtype": "string", "name": "team_id"},
    "week": {"dtype": pd.Int8Dtype()},
    "depth_team": {"dtype": "string", "name": "depth"},
    "formation": {"dtype": "string"},
    "gsis_id": {"dtype": "string", "name": "gsis_id_id"},
    "position": {"dtype": "string"},
    "depth_position": {"dtype": "string"},
    "full_name": {"dtype": "string", "name": "player_name"},
}

rosters_mapper = {
    "season": {"dtype": pd.Int16Dtype()},
    "team": {"dtype": "string", "name": "team_id"},
    "position": {"dtype": "string"},
    "status": {"dtype": "string"},
    "week": {"dtype": pd.Int8Dtype()},
    "player_id": {"dtype": "string", "name": "gsis_id_id"},
    "espn_id": {"dtype": pd.Int32Dtype()},
    "yahoo_id": {"dtype": pd.Int32Dtype()},
    "player_name": {"dtype": "string"},
    "headshot_url": {"dtype": "string"},
}
