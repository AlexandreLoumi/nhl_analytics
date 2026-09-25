select

    player_id::NUMBER as player_id,

    data:first_name::VARCHAR as first_name,
    data:last_name::VARCHAR as last_name,
    data:number::NUMBER as sweater_number,
    data:position::VARCHAR as position,
    data:shoots_catches::VARCHAR as shoots_catches,

    data:height::NUMBER as height_cm,
    data:weight::NUMBER as weight_kg,

    data:birth_date::DATE as birth_date,
    data:birth_city::VARCHAR as birth_city,
    data:birth_country::VARCHAR as birth_country,

    data:team::VARCHAR as team_abbrev

from {{ source('nhl', 'raw_players')}}