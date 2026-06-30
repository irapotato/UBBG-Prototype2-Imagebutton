init python:
    
    stat_pitcher_location = 2
    stat_pitcher_velo = 5
    stat_pitcher_accuracy = 3

    stat_batter_eye = 2
    stat_batter_contact = 3
    stat_batter_power = 5
    
    import random
    def eye_roll():
        global eye_roll_total
        eye_roll_total = random.randint(1,12) + (stat_batter_eye * 0.5)

    def contact



define j = Character("Justin Davis")
define w = Character("Wilmary Zuniga")
define jm = Character("Jack (Dev)")
define aa = Character("Alonso Aguilar")




label start:

    "Welcome to the Untitled Baseball Game Prototype #2!"

    "This is a test of Renpy where we will be running batting practice using multiple .rpy files to allow implimentation and make it easier to develop the game in steps."

    python:
        

        pitcher_location = renpy.random.randint(1,6)

        #replacing the commented python code with imagebutton commands and python functions above
        # batter_eye = renpy.random.randint(1,12)

        #contact_one = renpy.random.randint(1,6)
        #contact_two = renpy.random.randint(1,6)
        #powerd20 = renpy.random.randint(1,20)
        #contact_roll = 0
        pitcher_velocity = renpy.random.randint(1,6)
        pitcher_accuracy = renpy.random.randint(1,20)
        strike_count = 0
        ball_count = 0

        #outcome text for outs
        r_outfielder_positions = renpy.random.choice(["Left Fielder", "Right Fielder", "Center Fielder"])
        r_ground_out_positions = renpy.random.choice(["Second Baseman", "Shortstop", "Third Baseman"])

        

    show screen player_stats

    "Today, you will be playing as Justin Davis (+[stat_batter_eye] EYE, +[stat_batter_contact] CON, [stat_batter_power] POW), Rookie (DH) for the Boston Beans."

    show screen pitcher_stats

    "You are practicing against Wilmary Zuniga (+[stat_pitcher_location] LOC, +[stat_pitcher_accuracy] ACC, +[stat_pitcher_velo] VELO), the veteran pitcher (CP) for Boston."

    show screen scoreboard

    "You step into the batter's box..."

    jump begin_at_bat

    label best_end:

        "Coach Aguilar draws your attention as you return to the dugout, high on your small victory against a skilled veteran."

        aa "Nice one, Davis!!! That ball was gone from the moment it left his hand. Good eye, good swing, good {i}everything{/i}!!!"

        "Coach lays it on thick, perhaps to try and buoy your confidence for the season. It's early, but it's never {i}too{/i} early to get on your coach's good side."

        "You sit back on the bench, a bit numb from satisfaction. Not only did you show what you can do, but you shut up a veteran closer with your bat and determination."

        "But even still, this is just one at bat. If you're going to carve out a career, you'll need to win these battles over and over, and against different opponents. This isn't the end, its only the beginning."
        show bestending at truecenter

        menu:
            
            "Congratulations! You have beaten the Prototype 2 Scenario and achieved the BEST ENDING! Would you like to play again?"

            "Play again!":
                hide bestending

                jump start
                    
            
            "Quit?":
                "Bye and thanks for playing!"
                return
                jump gameend



    return

    label good_end:
    
        "Coach Aguilar draws your attention as you return to the dugout, high on your small victory against a skilled veteran."

        aa "That's it, Davis!! Show these old vets the new kid on the block is here to play!"

        "Coach's encouragement seems to slightly annoy some of the veterans, but they greet you warmly as you get back to the bench."

        "You take a seat, and reflect for a second. You just held your own against a pitcher you've seen on TV, something you dreamed about playing baseball in college."

        "But even still, this is just one at bat. If you're going to carve out a career, you'll need to win these battles over and over, and against different opponents. This isn't the end, its only the beginning."

        show goodending at truecenter


        menu:
            

            "Congratulations! You have beaten the Prototype 2 Scenario, and achieved the GOOD ENDING! Would you like to play again?"

            "Play again!":
                hide goodending
                jump start
            
            "Quit?":
                hide goodending
                "Bye and thanks for playing!"
                jump gameend
    

    return

            
    
    label neutral_end:
    
    "Coach Aguilar talks to you as you head back to the dugout to watch the next hitter."

    aa "Good eye Davis, that's a win in my book. Any time you can get on base as a DH, you're helping the team. I just hope you've got some legs, otherwise you may be double play bait!"

    "Coach gives you an encouraging pat on the back, and you take a seat and watch the next few hitters as you try to get Wilmary's release timing down."
    show neutralending at truecenter


    menu:
        "You have completed the Untitled Baseball Game Prototype 2 and achieved the NEUTRAL ENDING! Would you like to try again?"

        "Try again?":
            hide neutralending
            jump start
            
        "Quit?":
            hide neutralending
            "Bye and thanks for playing!"
            jump gameend

    
    return

    label bad_end:
    
    "Coach Aguilar pulls you over as you get back to the dugout. He doesn't look angry, but he definitely doesn't look happy."

    aa "Davis, you've got to keep focused. Once you're in the box, it's you {i}vs{/i} the pitcher. Nothing else matters but you hitting that ball and getting on base by whatever means necessary."

    "His tone makes you think deeply as you sit back down on the bench and watch the other hitters. You realize that once you're in the Majors, results are all that matter."

    "You focus sharply on the next at bat, trying to pick up anything you can for your next chance to show what you can do..."

    show badending at truecenter

    menu:
        "You have just completed the Untitled Baseball Game Prototype 2, and unfortunately achieved the BAD ENDING! Would you like to try again?"

        "Try again?":
            hide badending

            jump start
        
        "Quit?":
            hide badending
            "Bye and thanks for playing!"
            return
            jump gameend
         
    
label gameend:

return
