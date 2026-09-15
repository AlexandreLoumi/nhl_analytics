
select
    game_id::NUMBER as game_id,
    data:season::NUMBER as season ,
    data:gameType::NUMBER as game_type,
    data:startTimeUTC::TIMESTAMP as game_datetime_utc,
    data:homeTeam:id::NUMBER as home_team_id,
    data:homeTeam:commonName:default::VARCHAR as home_team_name,
    data:homeTeam:abbrev::VARCHAR as home_team_abbrev,
    data:homeTeam:score::NUMBER as home_score,
    data:awayTeam:id::NUMBER as away_team_id,
    data:awayTeam:commonName:default::VARCHAR as away_team_name,
    data:awayTeam:abbrev::VARCHAR as away_team_abbrev,
    data:awayTeam:score::NUMBER as away_score,
    data:gameOutcome:lastPeriodType::VARCHAR as game_end_type
from {{ source('nhl', 'raw_games') }}