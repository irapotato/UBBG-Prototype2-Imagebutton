label begin_at_bat:
    "The count is [ball_count] and [strike_count]."

label at_bat:
    "Zuniga winds up..."

    $ pitcher_location = renpy.random.randint(1,6)
    
    # attempting to replace the batter rolls with imagebutton screens for input.
    # $ batter_eye = renpy.random.randint(1,12)

    show screen location_roll

    "He rolls for Location (1d6)... [pitcher_location]."
    
    if pitcher_location == 1 or pitcher_location == 6:

        #modal imagebutton to have player roll for eye.

        show screen roll_for_eye
        "The pitch is outside! Roll to try and take the pitch..."

        $ needed_roll_ball = int((stat_pitcher_location * 0.5) + 5)
        # $ eye_roll_total = (stat_batter_eye * 0.5) + batter_eye

        show screen batter_needs_ball

        "Pitcher's Location stat is [stat_pitcher_location], hitter needs to roll a [needed_roll_ball]."

        if eye_roll_total >= needed_roll_ball:
            $ ball_count += 1

            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye], giving you a [eye_roll_total] Eye total. You manage to not swing, Ball [ball_count]!"

            $ is_hit = False

            if ball_count == 4:
                jump check_count

        else:
            $ strike_count += 1

            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye], giving you a [eye_roll_total] Eye total. You awkwardly swing at nothing, Strike [strike_count]!"

            $ is_hit = False

            jump check_count
            
            
    elif pitcher_location == 2:
        "The pitch is high and outside, not too hard to hit. You try to make contact..."
        $ needed_roll_strike =int(2 * ((0.5 * stat_pitcher_location) + pitcher_location))
        $ eye_roll_total = (stat_batter_eye * 0.5) + batter_eye
        show screen batter_needs_strike
        "Pitcher's Location stat is [stat_pitcher_location], hitter needs to roll a [needed_roll_strike]."

        if eye_roll_total >= needed_roll_strike:
            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye], totaling [eye_roll_total]. You make contact!"
            $ is_hit = True
        else:
            $ strike_count +=1
            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye], totaling [eye_roll_total]. You swing and miss, Strike [strike_count]!"
            $ is_hit = False
            jump check_count


    elif pitcher_location == 3:
        
        "The pitch is low and outside, pulling away from you. You try to make contact..."
        $ needed_roll_strike = 2 * ((0.5 * stat_pitcher_location) + pitcher_location)
        $ eye_roll_total = (stat_batter_eye * 0.5) + batter_eye
        show screen batter_needs_strike
        "Pitcher's Location stat is [stat_pitcher_location], hitter needs to roll a [needed_roll_strike]."

        if eye_roll_total >= needed_roll_strike:
            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye], totaling [eye_roll_total]. You make contact!"
            $ is_hit = True
        else:
            show screen eye_roll

            $ strike_count +=1
            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye], totaling [eye_roll_total]. You swing and miss, Strike [strike_count]!"
            $ is_hit = False
            jump check_count

    elif pitcher_location == 4:
        "The pitch is high and inside, approaching the edge of the zone. You try to make contact..."
        $ needed_roll_strike = 2 * ((0.5 * stat_pitcher_location) + pitcher_location)
        $ eye_roll_total = (stat_batter_eye * 0.5) + batter_eye
        show screen batter_needs_strike
        "Pitcher's Location stat is [stat_pitcher_location], hitter needs to roll a [needed_roll_strike]."

        if eye_roll_total >= needed_roll_strike:
            show screen eye_roll

            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye]. You make contact!"
            $ is_hit = True
        else:
            $ strike_count +=1
            show screen eye_roll
            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye]. You swing and miss, Strike [strike_count]!"
            $ is_hit = False
            jump check_count
            
    elif pitcher_location == 5:
        "The pitch is low and inside, dotted on the corner of the zone. You'll need a good eye to catch this one. You try to make contact..."
        $ needed_roll_strike = 2 * ((0.5 * stat_pitcher_location) + pitcher_location)
        $ eye_roll_total = (stat_batter_eye * 0.5) + batter_eye
        show screen batter_needs_strike
        "Pitcher's Location stat is [stat_pitcher_location], hitter needs to roll a [needed_roll_strike]."

        if eye_roll_total >= needed_roll_strike:
            show screen eye_roll
            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye]. You make contact!"
            $ is_hit = True
        else:
            show screen eye_roll                
            $ strike_count +=1
            "Your Eye roll (1d12) is [batter_eye] + [0.5 * stat_batter_eye]. You swing and miss, Strike [strike_count]!"
            $ is_hit = False
            jump check_count



    if is_hit == False:
        jump check_count
        
    else:
        hide screen batter_needs_strike
        hide screen batter_needs_ball
        hide screen location_roll
        hide screen eye_roll           

        $ contact_one = renpy.random.randint(1,6)
        $ contact_two = renpy.random.randint(1,6)

        if contact_one >= contact_two:
            $ contact_total = stat_batter_contact + contact_one
        else:
            $ contact_total = stat_batter_contact + contact_two

        show screen batter_roll_contact
        "Your Contact rolls (>2d6 + [stat_batter_contact]) were [contact_one] and [contact_two], meaning your Contact total is [contact_total]."

        $ powerd20 = renpy.random.randint(1,20)
        $ power_total = powerd20 + stat_batter_power

        show screen batter_roll_power
        "Your Power roll (1d20 + [stat_batter_power]) was [powerd20], giving you a Power total of [power_total]."

        python:
            hit_score = power_total * contact_total

            pitcher_velocity = renpy.random.randint(1,6)
            pitcher_accuracy = renpy.random.randint(1,20)

            pitch_score = (stat_pitcher_accuracy + pitcher_accuracy) * (stat_pitcher_velo + pitcher_velocity)
            outcome_score = hit_score - pitch_score

        show screen hit_score_screen
        "Your hit score is [power_total] X [contact_total], totaling [hit_score]!"

        show screen pitcher_roll_accuracy
        show screen pitcher_roll_velocity

        "Zuniga rolls for Velocity (1d6 + [stat_pitcher_velo]) and Accuracy (1d20 + [stat_pitcher_accuracy])."

        show screen pitch_score_screen
        "He rolls [pitcher_velocity] (+[stat_pitcher_velo]) and [pitcher_accuracy] (+[stat_pitcher_accuracy]), giving him a Pitch Effectiveness of [pitch_score]"

        jump outcome_text