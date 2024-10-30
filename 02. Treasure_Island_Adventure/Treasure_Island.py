#Game Introduction
print("\nWelcome to the Treasure Island.")
print("Your mission is to find the treasure.")
print(r"""
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
 """)
print("\nYou are beginning to set sail to hunt for treasure. Which direction would you want to go?")

#Get user input
while True:
    direction = input("Enter your choice East, West or South? ").lower()

    if direction == 'east' or direction.startswith('e'):
        read_or_watch = input("\nOn your eastward journey, would you rather delve into a book or be entertained by a movie? Enter read or watch:").lower()
        
        if read_or_watch == "read":
            shake_or_push = input("\nA mysterious box catches your eye on the bookshelf. Would you rather give the box a shake or press the button to unlock its secrets? Enter shake or press:").lower()
            
            if shake_or_push == "shake":
                swim_or_wait = input("\nAfter a long voyage, you discover a secluded island. A peaceful lake lies at the island's core, would take the plunge and swim across, or bide your time and wait for a boat? Enter swim or wait:").lower()
                
                if swim_or_wait == "swim":
                    fold_cut_press = input("\nHaving successfully navigated the lake, darkness falls upon you. To prepare for rest, would you prefer to adapt your shirt into a tent, nourish yourself with the fruits, or signal for help by pressing the button? Enter fold or cut or press:").lower()
                    
                    if fold_cut_press == "press":
                        play_eat = input("\nA key lies at the foot of your tent, but your stomach growls. Would you rather soothe your soul with music or satisfy your hunger with food? Enter play or eat:").lower()
                        
                        if play_eat == "eat":
                            print("\nRuns out of food. Good luck!")
                            break
                    
                    elif fold_cut_press == "fold":
                        print("\nCongratulations! You found the hidden treasure.")
                        break
                    
                    else:
                        print("\nSwept by tsunamis. Hunt is over!")
                        break
            
            else:
                print("\nYou jump I jump. You are in a titanic ship.")
                break
        
        else:
            print("\nSink by whirlpool. Have a spin!")
        break
    
    elif direction == 'south' or direction.startswith('s'):
        swim_or_wait = input("\nOn your southward journey, you discover an island. A peaceful lake lies at the island's core, would take the plunge and swim across, or bide your time and wait for a boat? Enter swim or wait:").lower()
        
        if swim_or_wait == "swim":
            fold_cut_press = input("\nHaving successfully navigated the lake, darkness falls upon you. To prepare for rest, would you prefer to adapt your shirt into a tent, nourish yourself with the fruits, or signal for help by pressing the button? Enter fold or cut or press:").lower()
            
            if fold_cut_press == "press":
                play_eat = input("\nA key lies at the foot of your tent, but your stomach growls. Would you rather soothe your soul with music or satisfy your hunger with food? Enter play or eat:").lower()
                
                if play_eat == "play":
                    print("\nCongratulations! You found the hidden treasure.")
                else:
                    print("\nRuns out of food. Good luck!")
                    break
            
            elif fold_cut_press == "fold":
                print("\nCongratulations! You found the hidden treasure.")
                break
                
            else:
                print("\nSwept by tsunamis. Hunt is over!")
                break
        else:
            print("\nAttacked by shark. Better luck!")
            break
    
    elif direction == 'west' or direction.startswith('w'):
        print("\nYou have fell into a hole. Game over!")
        break
    
    else:
        print("Invalid input. Please enter East, West or South.")
