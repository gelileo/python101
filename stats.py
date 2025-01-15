import os
import json

initial_game_stats = {
    "Easy": {"win": 0, "lose": 0, "draw": 0},
    "Hard": {"win": 0, "lose": 0, "draw": 0},
    "Pro": {"win": 0, "lose": 0, "draw": 0},
}


def update_game_stats(game_stats, level, result):
    if level in game_stats and result in game_stats[level]:
        game_stats[level][result] += 1
        save_game_stats(game_stats)
    else:
        print("Invalid level or result")


def load_game_stats(file_path="game_stats.json"):
    """
    Load the game stats from a JSON file. If the file doesn't exist, create it
    with initial stats and return the initial stats.
    """
    if not os.path.exists(file_path):
        save_game_stats(initial_game_stats, file_path)
        return initial_game_stats
    else:
        with open(file_path, "r") as file:
            return json.load(file)


def save_game_stats(stats, file_path="game_stats.json"):
    """
    Save the updated game stats to a JSON file.
    """
    with open(file_path, "w") as file:
        json.dump(stats, file, indent=4)
    print(f"Game stats saved to '{file_path}'.")
