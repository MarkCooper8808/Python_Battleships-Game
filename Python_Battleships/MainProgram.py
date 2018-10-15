from Sea import Sea
from ShipPlacer import ShipPlacer
from PositionTracker import PositionTracker
from MapConstructor import MapConstructor
from AI import AI

game_running = True


sea_battlefield_1 = Sea()
computer_battlefield = Sea()

ship_placer_player_1 = ShipPlacer()
computer_ship_placer = AI()

new_map = MapConstructor()
computer_map = MapConstructor()

#print(sea_battlefield_1.sea)
computer_sea = computer_ship_placer.placement(computer_battlefield.sea)
sea_and_map = ship_placer_player_1.prompt_placement(sea_battlefield_1.sea, new_map._battle_map)
position_tracker = PositionTracker()
position_tracker.hit_detector(sea_and_map, computer_sea)



games_played = 1

while game_running == True:
    play_again = input("\nGame finished! You've played " + str(games_played) +\
                       " consecutive games." +
                       " Enter 'y' to play again.\n")
    if play_again == "y":
        games_played+=1
        print("*" * 60)
        print("New Game\n")
        computer_battlefield = Sea()
        sea_battlefield_1 = Sea()
        

        #computer_ship_placer = AI()
        #new_map = MapConstructor()
        computer_sea = computer_ship_placer.placement(computer_battlefield.sea)
        sea_and_map = ship_placer_player_1.prompt_placement(sea_battlefield_1.sea, new_map._battle_map)
        position_tracker = PositionTracker()
        position_tracker.hit_detector(sea_and_map, computer_sea)
    else:
        game_running = False
        continue


#print(sea_battlefield_1.sea)
