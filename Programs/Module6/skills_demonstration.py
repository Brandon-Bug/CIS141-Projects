game_library_1 = [["Minecraft", "Creative"], ["Among Us", "Horror"], ["Team Fortress 2", "FPS"], ["Phasmophobia", "Horror"]]

game_library_2 = [["Lethal Company", "Horror"], ["Overwatch","FPS"], ["Fortnite", "FPS"], ["Slime Rancher", "Creative"], ["Halo Infinite", "FPS"], ["Little Big Planet", "Creative"]]

game_library_3 = [["Lethal Company", "Horror"], ["Overwatch","FPS"], ["Fortnite", "FPS"], ["Slime Rancher", "Creative"], ["Halo Infinite", "FPS"], ["Little Big Planet", "Creative"], ["Minecraft", "Creative"], ["Among Us", "Horror"], ["Team Fortress 2", "FPS"], ["Phasmophobia", "Horror"]]


horror_games = 0
creative_games = 0
fps_games = 0

for video_game in game_library_3:
    
    if video_game[1] == "Horror":
        horror_games += 1
    
    elif video_game[1] == "Creative":
        creative_games += 1
    
    else:
        fps_games += 1

print(f"This game library has {creative_games} creative games, {horror_games} horror games, and {fps_games} FPS games!")
