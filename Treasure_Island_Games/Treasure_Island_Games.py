print("\nWelcome to the Treasure Island.")
print("Your mission is to find the treasure.")
print(r'''
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
 \_/__________________________________________________________________/''')
print("\nYou are at a crossroad. Which direction would you want to go?")

while True:
    direction = input("Enter your choice East, West or South? ").lower()

    if direction == 'east' or direction.startswith('e'):
        read_or_watch = input("\nWould you want to read or watch? ").lower()
        
        if read_or_watch == "read":
            shake_or_push = input("Would you want to shake or push? ").lower()
            
            if shake_or_push == "shake":
                swim_or_wait = input("\nWould you want to swim or wait? ").lower()
                
                if swim_or_wait == "swim":
                    fold_cut_press = input("\nWould you want to fold, cut or press? ").lower()
                    
                    if fold_cut_press == "press":
                        play_eat = input("\nWould you want to play or eat? ").lower()
                        
                        if play_eat == "eat":
                            print("Runs out of food. Good luck!")
                            break
                    
                    elif fold_cut_press == "fold":
                        print("Congratulations! You found the hidden treasure.")
                        break
                    
                    else:
                        print("Swept by tsunamis. Hunt is over!")
                        break
            
            else:
                print("You jump I jump. You are in a titanic ship.")
                break
        
        else:
            print("Sink by whirlpool. Have a spin!")
        break
    
    elif direction == 'south' or direction.startswith('s'):
        swim_or_wait = input("\nWould you want to swim or wait? ").lower()
        
        if swim_or_wait == "swim":
            fold_cut_press = input("\nWould you want to fold, cut or press? ").lower()
            
            if fold_cut_press == "press":
                play_eat = input("\nWould you want to play or eat? ").lower()
                
                if play_eat == "play":
                    print("Congratulations! You found the hidden treasure.")
                else:
                    print("Runs out of food. Good luck!")
                    break
            
            elif fold_cut_press == "fold":
                print("Congratulations! You found the hidden treasure.")
                break
                
            else:
                print("Swept by tsunamis. Hunt is over!")
                break
        else:
            print("Attacked by shark. Better luck!")
            break
    
    elif direction == 'west' or direction.startswith('w'):
        print("You have fell into a hole. Game over!")
        break
    
    else:
        print("Invalid input. Please enter East, West or South.")
