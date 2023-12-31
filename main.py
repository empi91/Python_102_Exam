import text
from Classes.player import Player
from Classes.room import Room
from Classes.location import locations_dict
from Classes.interface import MainMenu
import functions as f

while True:
    player_name = input("Enter name of your character: ")
    backpack = []

    player = Player(player_name, backpack)
    main_room = Room("Main room")
    main_menu = MainMenu()

    main_room.__str__(player_name)
    print(text.interface_help)

    while True:
        choice = main_menu.print_options()
        match choice:
            case "/sprawdź":
                f.inspect(main_room.current_position, main_room, locations_dict)
            case "/lewo":
                main_room.current_position = f.move_left(main_room.current_position)
                print(f"Stoisz teraz przed: {main_room.locations[main_room.current_position]}")
            case "/prawo":
                main_room.current_position = f.move_right(main_room.current_position)
                print(f"Stoisz teraz przed: {main_room.locations[main_room.current_position]}")
            case "/weź":
                f.take_item(
                    main_room.current_position,
                    locations_dict,
                    backpack
                )
            case "/użyj":
                f.use_item(
                    main_room.current_position,
                    locations_dict,
                    backpack
                )
            case "/odłóż":
                f.throw_item(
                    main_room.current_position,
                    locations_dict,
                    backpack
                )
            case "/plecak":
                f.check_backpack(backpack)
            case "/zakończ":
                exit()
            case "/pomoc":
                print(text.interface_help)
            case _:
                print("Błędna komenda")
