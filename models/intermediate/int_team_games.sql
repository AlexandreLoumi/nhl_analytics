
select
    game_id,
    season,
    game_type,
    game_datetime_utc,

    home_team_id as team_id,
    home_team_name as team_name,
    home_team_abbrev as team_abbrev,
    home_score as goals_for,

    away_team_id as opponent_id,
    away_team_name as opponent_name,
    away_team_abbrev as opponent_abbrev,
    away_score as goals_against,
    'H' as home_away,

    case
        when home_score > away_score then 'Win'
        when home_score < away_score then 'Loss'
    end as result,

    game_end_type
from {{ref('stg_games')}}

union all

select
    game_id,
    season,
    game_type,
    game_datetime_utc,

    away_team_id as team_id,
    away_team_name as team_name,
    away_team_abbrev as team_abbrev,
    away_score as goals_for,

    home_team_id as opponent_id,
    home_team_name as opponent_name,
    home_team_abbrev as opponent_abbrev,
    home_score as goals_against,
    'A' as home_away,

    case
        when home_score < away_score then 'Win'
        when home_score > away_score then 'Loss'
    end as result,
    game_end_type
    from {{ref('stg_games')}}

