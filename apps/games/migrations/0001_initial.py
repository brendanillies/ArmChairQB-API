# Generated by Django 4.2.5 on 2023-10-17 18:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('stadium_id', models.CharField(editable=False, max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70, verbose_name='name')),
            ],
            options={
                'db_table': 'Stadiums',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('game_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('season', models.IntegerField(editable=False)),
                ('game_type', models.CharField(editable=False, max_length=4)),
                ('week', models.IntegerField(editable=False)),
                ('gameday', models.DateField(editable=False)),
                ('weekday', models.CharField(editable=False, max_length=9)),
                ('gametime', models.TimeField(editable=False)),
                ('location', models.CharField(editable=False, max_length=4)),
                ('overtime', models.IntegerField(default=0, editable=False)),
                ('espn_game_id', models.IntegerField(db_column='espn_game_id', editable=False, verbose_name='espn_game_id')),
                ('divisional_game', models.IntegerField(db_column='divisional_game', editable=False, verbose_name='divisional_game')),
                ('away_team', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, related_name='schedule_away', to='teams.teams')),
                ('home_team', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, related_name='schedule_home', to='teams.teams')),
                ('stadium_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='games.stadium')),
                ('roof', models.CharField(default='', max_length=8)),
                ('surface', models.CharField(default='', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Schedule',
                'db_table': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='PlayByPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_team', models.ForeignKey(db_column='away_team_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_away_team', to='teams.teams')),
                ('away_team_score', models.IntegerField(default=0)),
                ('away_timeouts_remaining', models.IntegerField(default=0)),
                ('defenders_in_box', models.IntegerField(default=0, null=True)),
                ('defense_num_of_rushers', models.IntegerField(default=0, null=True)),
                ('defense_personnel', models.CharField(default='', max_length=15, null=True)),
                ('defense_player_gsis_ids', models.CharField(default='', max_length=175, null=True)),
                ('down', models.IntegerField(default=0, null=True)),
                ('drive_end_transition', models.CharField(default='', max_length=30, null=True)),
                ('drive_ended_with_score', models.IntegerField(default=0, null=True)),
                ('drive_first_downs', models.IntegerField(default=0, null=True)),
                ('drive_inside_twenty', models.IntegerField(default=0, null=True)),
                ('drive_net_yards', models.IntegerField(default=0, null=True)),
                ('drive_num', models.IntegerField(default=0, null=True)),
                ('drive_play_count', models.IntegerField(default=0, null=True)),
                ('drive_quarter_end', models.IntegerField(default=0, null=True)),
                ('drive_quarter_start', models.IntegerField(default=0, null=True)),
                ('drive_result', models.CharField(default='', max_length=25, null=True)),
                ('drive_start_transition', models.CharField(default='', max_length=30, null=True)),
                ('drive_time_of_possession', models.TimeField(default=datetime.time(0, 0))),
                ('drive_yards_penalized', models.IntegerField(default=0, null=True)),
                ('extra_point_attempt', models.IntegerField(default=0, null=True)),
                ('extra_point_result', models.CharField(default='', max_length=6, null=True)),
                ('field_goal_attempt', models.IntegerField(default=0, null=True)),
                ('field_goal_kick_distance', models.IntegerField(default=0, null=True)),
                ('field_goal_result', models.CharField(default='', max_length=7, null=True)),
                ('fourth_down_converted', models.IntegerField(default=0, null=True)),
                ('fourth_down_failed', models.IntegerField(default=0, null=True)),
                ('fumble', models.IntegerField(default=0, null=True)),
                ('fumble_forced', models.IntegerField(default=0, null=True)),
                ('fumble_lost', models.IntegerField(default=0, null=True)),
                ('fumble_not_forced', models.IntegerField(default=0, null=True)),
                ('fumble_out_of_bounds', models.IntegerField(default=0, null=True)),
                ('game_seconds_remaining', models.IntegerField(default=0)),
                ('half', models.CharField(default='', max_length=8)),
                ('half_seconds_remaining', models.IntegerField(default=0)),
                ('home_team', models.ForeignKey(db_column='home_team_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_home_team', to='teams.teams')),
                ('home_team_score', models.IntegerField(default=0)),
                ('home_timeouts_remaining', models.IntegerField(default=0)),
                ('kickoff_attempt', models.IntegerField(default=0, null=True)),
                ('kickoff_downed', models.IntegerField(default=0, null=True)),
                ('kickoff_fair_catch', models.IntegerField(default=0, null=True)),
                ('kickoff_in_endzone', models.IntegerField(default=0, null=True)),
                ('kickoff_inside_twenty', models.IntegerField(default=0, null=True)),
                ('kickoff_out_of_bounds', models.IntegerField(default=0, null=True)),
                ('kickoff_touchback', models.IntegerField(default=0, null=True)),
                ('no_huddle', models.IntegerField(default=0, null=True)),
                ('offense_formation', models.CharField(default='', max_length=15, null=True)),
                ('offense_personnel', models.CharField(default='', max_length=15, null=True)),
                ('offense_player_gsis_ids', models.CharField(default='', max_length=175, null=True)),
                ('own_kickoff_recovery', models.IntegerField(default=0, null=True)),
                ('own_kickoff_recovery_touchdown', models.IntegerField(default=0, null=True)),
                ('pass_air_yards', models.IntegerField(default=0, null=True)),
                ('pass_attempt', models.IntegerField(default=0, null=True)),
                ('pass_complete', models.IntegerField(default=0, null=True)),
                ('pass_first_down', models.IntegerField(default=0, null=True)),
                ('pass_incomplete', models.IntegerField(default=0, null=True)),
                ('pass_interception', models.IntegerField(default=0, null=True)),
                ('pass_length', models.CharField(default='', max_length=7, null=True)),
                ('pass_location', models.CharField(default='', max_length=7, null=True)),
                ('pass_touchdown', models.IntegerField(default=0, null=True)),
                ('pass_yards', models.IntegerField(default=0, null=True)),
                ('pass_yards_after_catch', models.IntegerField(default=0, null=True)),
                ('penalty', models.IntegerField(default=0, null=True)),
                ('penalty_team', models.ForeignKey(blank=True, db_column='penalty_team_id', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_penalty_team', to='teams.teams')),
                ('penalty_type', models.CharField(default='', max_length=75, null=True)),
                ('penalty_yards', models.IntegerField(default=0, null=True)),
                ('play_description', models.CharField(db_column='play_description', default='', max_length=750)),
                ('play_type', models.CharField(default='', max_length=20, null=True)),
                ('punt_attempt', models.IntegerField(default=0, null=True)),
                ('punt_blocked', models.IntegerField(default=0, null=True)),
                ('punt_downed', models.IntegerField(default=0, null=True)),
                ('punt_fair_catch', models.IntegerField(default=0, null=True)),
                ('punt_in_endzone', models.IntegerField(default=0, null=True)),
                ('punt_inside_twenty', models.IntegerField(default=0, null=True)),
                ('punt_out_of_bounds', models.IntegerField(default=0, null=True)),
                ('qb_dropback', models.IntegerField(default=0, null=True)),
                ('qb_hit', models.IntegerField(default=0, null=True)),
                ('qb_kneel', models.IntegerField(default=0, null=True)),
                ('qb_scramble', models.IntegerField(default=0, null=True)),
                ('qb_spike', models.IntegerField(default=0, null=True)),
                ('quarter', models.IntegerField(default=0)),
                ('quarter_end', models.IntegerField(default=0)),
                ('quarter_seconds_remaining', models.IntegerField(default=0)),
                ('return_touchdown', models.IntegerField(default=0, null=True)),
                ('rush_gap', models.CharField(default='', max_length=7, null=True)),
                ('rush_location', models.CharField(default='', max_length=7, null=True)),
                ('rush_touchdown', models.IntegerField(default=0, null=True)),
                ('rush_attempt', models.IntegerField(default=0, null=True)),
                ('rush_first_down', models.IntegerField(default=0, null=True)),
                ('rush_yards', models.IntegerField(default=0, null=True)),
                ('sack', models.IntegerField(default=0, null=True)),
                ('safety', models.IntegerField(default=0, null=True)),
                ('shotgun', models.IntegerField(default=0, null=True)),
                ('side_of_field', models.CharField(default='', max_length=4, null=True)),
                ('tackle_assist', models.IntegerField(default=0, null=True)),
                ('tackle_solo', models.IntegerField(default=0, null=True)),
                ('tackled_for_loss', models.IntegerField(default=0, null=True)),
                ('team_with_possession', models.ForeignKey(blank=True, db_column='team_with_possession_id', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_team_with_possession', to='teams.teams')),
                ('third_down_converted', models.IntegerField(default=0, null=True)),
                ('third_down_failed', models.IntegerField(default=0, null=True)),
                ('timeout_taken', models.IntegerField(default=0, null=True)),
                ('timeout_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_timeout_team', to='teams.teams')),
                ('touchdown', models.IntegerField(default=0, null=True)),
                ('touchdown_team', models.ForeignKey(blank=True, db_column='touchdown_team_id', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_touchdown_team', to='teams.teams')),
                ('two_point_attempt', models.IntegerField(default=0, null=True)),
                ('two_point_conv_result', models.CharField(default='', max_length=7, null=True)),
                ('week', models.IntegerField(default=0, null=True)),
                ('yardline_100', models.IntegerField(default=0, null=True)),
                ('yards_gained', models.IntegerField(default=0, null=True)),
                ('yards_to_go', models.IntegerField(default=0)),
                ('fumbled_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_fumbler', to='players.playeridentifier')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_game_ids', to='games.schedule')),
                ('kicker_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_kicking_player', to='players.playeridentifier')),
                ('passer_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_passing_player', to='players.playeridentifier')),
                ('penalty_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_penalty_player', to='players.playeridentifier')),
                ('receiver_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_receiving_player', to='players.playeridentifier')),
                ('rusher_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_rushing_player', to='players.playeridentifier')),
                ('touchdown_gsis_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pbp_touchdown_player', to='players.playeridentifier')),
                ('season', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Play By Play',
                'db_table': 'PlayByPlay',
            },
        ),
    ]
