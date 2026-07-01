init python:
    
    import random

    # stat values for pitcher and batter
    
    class batter:
        def __init__(self, name, first_name, last_name, stat_eye, stat_con, stat_pow, stat_abl):
            self.name = name
            self.first_name = first_name
            self.last_name = last_name
            self.stat_eye = stat_eye
            self.stat_con = stat_con
            self.stat_pow = stat_pow
            self.stat_abl = stat_abl
    
    jd = batter("Justin Davis", "Justin", "Davis", 2, 2, 2, 1)

    class pitcher:
        def __init__(self, name, first_name, last_name, stat_loc, stat_velo, stat_acc, stat_abl):
            self.name = name
            self.first_name = first_name
            self.last_name = last_name
            self.stat_loc = stat_loc
            self.stat_velo = stat_velo
            self.stat_acc = stat_acc
            self.stat_abl = stat_abl
    wz = pitcher("Wilmary Zuniga", "Wilmary", "Zuniga", 3, 5, 3, 2)

    #stat_pitcher_location = 3
    #stat_pitcher_velo = 5
    #stat_pitcher_accuracy = 3

    #stat_batter_eye = 2
    #stat_batter_contact = 2
    #stat_batter_power = 2
    
    # function called by eye roll imagebutton screen. Only generates the random number, calculations are done locally.
    def eye_roll_function():
        global eye_roll
        eye_roll = renpy.random.randint(1,12)
    
    # function called by hit roll imagebutton screen. Only generates the random numbers used to do calculations locally.
    def hit_roll_function():
        global contact_one
        global contact_two
        global power_roll
        contact_one = renpy.random.randint(1,6)
        contact_two = renpy.random.randint(1,6)
        power_roll = renpy.random.randint(1,20)


# speaking characters
define j = Character("Justin Davis")
define w = Character("Wilmary Zuniga")
define jm = Character("Jack (Dev)")
define aa = Character("Alonso Aguilar")

label start:

    "Welcome to the Untitled Baseball Game Prototype!"

    "This is a test of implimenting the Renpy ImageButton screen to have the players roll their own dice. This is the primary planned input method for the first full prototype."

    python:
        
        pitcher_location = renpy.random.randint(1,6)
        pitcher_velocity = renpy.random.randint(1,6)
        pitcher_accuracy = renpy.random.randint(1,20)
        strike_count = 0
        ball_count = 0

        #outcome text for outs
        r_outfielder_positions = renpy.random.choice(["left fielder", "right fielder", "center fielder"])
        r_ground_out_positions = renpy.random.choice(["second baseman", "shortstop", "third baseman"])

        

    show screen player_stats

    "Today, you will be playing as Justin Davis ([jd.stat_eye] EYE, [jd.stat_con] CON, [jd.stat_pow] POW), Rookie (DH) for the Boston Beans."

    show screen pitcher_stats

    "You are practicing against Wilmary Zuniga ([wz.stat_loc] LOC, [wz.stat_acc] ACC, [wz.stat_velo] VELO), the veteran pitcher (CP) for Boston. His blistering fastball and tight mechanics have helped him lock up the closer spot for Boston for the past few seasons."

    show screen scoreboard

    "You step into the batter's box..."

    jump begin_at_bat

    label best_end:

        "Coach Aguilar draws your attention as you return to the dugout, brining you back from your momentary high off your small victory against a skilled veteran."

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
