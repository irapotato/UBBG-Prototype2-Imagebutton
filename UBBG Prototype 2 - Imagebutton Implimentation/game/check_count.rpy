label check_count:

    hide screen batter_needs_strike
    hide screen batter_needs_ball
    hide screen location_roll
    hide screen eye_roll

    if strike_count == 3:
        jump strikeout
    elif ball_count == 4:
        jump walk
    else:
        "The count is [ball_count] and [strike_count]."
        jump at_bat