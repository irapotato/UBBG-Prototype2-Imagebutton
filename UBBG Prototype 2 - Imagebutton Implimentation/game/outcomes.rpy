label outcome_text:

    show screen outcome_screen

    "The result is an Outcome Score of [outcome_score]."

    hide screen scoreboard
    hide screen pitcher_stats
    hide screen player_stats
    hide screen batter_roll_contact 
    hide screen batter_roll_power
    hide screen pitcher_roll_velocity
    hide screen pitcher_roll_accuracy
    hide screen hit_score_screen
    hide screen pitch_score_screen
    hide screen outcome_screen

    if 50 <= outcome_score:     
        jump homerun
                
    elif 31 <= outcome_score <= 49:
        jump hit_triple

    elif 14 <= outcome_score <= 30:
        jump hit_double

    elif 7 <= outcome_score <= 13:
        jump hit_single

    elif -6 <= outcome_score <= 6:
        "You just barely miss contacting the ball the way you'd like, and you pop it out of play behind you. Foul Ball!"

        if strike_count == 0 or 1:

            $ strike_count += 1

            jump check_count

        else:
            "You foul off a 3rd strike for a foul ball. Phew! That was close."
            jump at_bat

    elif -19 <= outcome_score <= -7:
        jump fly_out

    elif -44 <= outcome_score <= -20:
        jump ground_out

    elif outcome_score <= -45:
        jump double_play

    label walk:
       
        hide screen scoreboard
        hide screen pitcher_stats
        hide screen player_stats
        hide screen batter_roll_contact 
        hide screen batter_roll_power
        hide screen pitcher_roll_velocity
        hide screen pitcher_roll_accuracy
        hide screen hit_score_screen
        hide screen pitch_score_screen
        hide screen outcome_screen
        
        "You manage to draw a walk. Not much you could do better there, I guess."

        w "Ahh, you got lucky! I'm barely even warmed up. Next time, it's 3 strikes and a K!"

        j "He couldn't even keep the ball in the zone, and somehow it still feels like he won. Next time, I'm swinging for the fences."

        jump neutral_end

    label strikeout:

        hide screen scoreboard
        hide screen pitcher_stats
        hide screen player_stats
        hide screen batter_roll_contact 
        hide screen batter_roll_power
        hide screen pitcher_roll_velocity
        hide screen pitcher_roll_accuracy
        hide screen hit_score_screen
        hide screen pitch_score_screen
        hide screen outcome_screen

        "Strikeout! You feel a bit embarassed as you walk back to the dugout for some reason, despite knowing even MVPs strike out sometimes."

        w "That's right, rook! You best know your stuff before you come at a vet again!"

        "You strike out to Wilmary. He strikes you as a bit insecure under his brash comments, like someone who knows they've been let off the hook once too many times."

        j "He's got good stuff today, I could barely keep up. I was fighting to even make contact, Major League pitching really is another level."

        jump bad_end

    label fly_out:

        "You get under the pitch, but not cleanly enough to hit the ball into a gap. You fly out to the [r_outfielder_positions]."

        w "Ah, that's what I'm talking about! They don't pay me all this to be lettin' up easy hits!"

        "Veteran contract money {i}does{/i} sound pretty nice to someone making Rookie minimum salary..."

        j "I'm never gonna be a vet if I don't get my swing tighter. I'll work on my grip for the rest of practice and see if I can't work a few things out."

        jump bad_end

    label ground_out:

        "You ground the ball sharply to the [r_ground_out_positions], who makes a soft throw to first to make the out."

        w "Nice play! Major League fielders ain't no chumps, haha! At least you can tell all your friends you made contact!"
        
        "You let Wilmary have his jokes for now, as you know you weren't far from making clean contact. You'll take your lumps and come back stronger."

        j "Better here than once the season starts, I guess. I'll be riding the bench for the rest of my life if I don't get my swing cleaned up."

        jump bad_end


    label double_play:

        "You ground the ball weakly to the shortstop, who scoops it up and steps lightly on second base before rifling the ball to the First Baseman. Double Play!"

        w "Haha, nice try rook. Keep working and next time maybe you'll just get one out instead of two next time! Hahaha!"

        "Wilmary laughs just a {i}little{/i} too hard at his own jokes. I'm not sure if he thinks he's funny or if he's too macho to say how he really feels."

        j "Either way, that sucked. I'll hit the tee tomorrow and see if I can't figure out a thing or two."

        jump bad_end


    label hit_single:

        "You hit the ball into the shallow outfield, as the [r_outfielder_positions] runs in to grab it and prevent you from getting past first. A well struck single!"

        w "Damn! I missed my spot, I should have had your ass!"

        "You know he's trying to call you lucky, but a hit is a hit. If you can do this consistently, you can build something special."

        j "There's always next time. Plenty of pre-season left, I'm looking forward to it."

        jump good_end

    label hit_double:

        show crack1 at truecenter

        "You pull the bat through the zone as hard as you can, and the ball CRACK!s cleanly off as it sails into a gap in the outfield. The [r_outfielder_positions] runs to grab it as you clear first at full speed and continue running until you're standing safely at second base. Double!!"

        w "C'MON, CATCH THE BALLLLL!!!"

        "Wilmary says something you can't quite hear as the second baseman chuckles quietly. It seems like this is normal behavior for him, based on the reactions."

        j "Nah, that's all barrel. We can run it again if you want!"

        hide crack1

        jump good_end

    label hit_triple:

        show crack2 at truecenter

        "The ball explodes off the bat with a huge CRACK!! as you make {i}almost{/i} perfect contact, sending the ball bouncing off the wall. The [r_outfielder_positions] comes running up quickly, but you slide into third base as the ball makes its' way to the cutoff man. Safe for a Triple!!!"

        w "Damn, the kid has a bat!! Next time, I gotta take this serious."

        "You chuckle, knowing that there was no way he was holding back. He's just trying to save face, and it doesn't seem to be working."

        j "Ha, me too I guess. A bit more power and that ball was a souvenir."

        hide crack2

        jump good_end

    label homerun:

        show crack3 at truecenter

        "You unload on the pitch with a raucous CRACK!!!, sending it ripping into the stands over the [r_outfielder_positions]'s head as they watch it clear the fence. HOME RUN!!!!"

        w "SHIT!!! well... uh..."

        "Wilmary looks back at you after you cross home plate, a mix of shaken and flustered that's visible even from 90 feet away. He seems to have nothing to say at the moment."

        hide crack3

        j "Good AB. I'm still working on my swing, but every little bit of practice helps. Thanks, man."

        w "Yeah, sure. I'm sure everyone at {i}Cheap Seats{/i} will have heard all about this by the end of the night!"

        "He seems more concerned with how people will think of him at the bar than he is about actually improving..."

        

        jump best_end