

def get_user_input():
    """Prompt user for season and plant type."""
    season = input(
        "Enter the season (summer, winter, spring, autumn): "
    ).strip().lower()
    plant_type = input(
        "Enter the plant type (flower, vegetable, herb): "
    ).strip().lower()
    return season, plant_type



# Determine advice based on the season


def get_advice(season, plant_type):
    """Return gardening advice based on season and plant type."""
    advice_dict = {
        "summer": {
            "flower": "Water your flowers regularly and provide some shade.",
            "vegetable": (
                "Water vegetables often and mulch to retain moisture."
            ),
            "herb": "Harvest herbs frequently to encourage growth."
        },
        "winter": {
            "flower": "Protect flowers from frost with covers.",
            "vegetable": "Grow hardy vegetables and use cloches.",
            "herb": "Move herbs indoors or cover them."
        },
        "spring": {
            "flower": "Plant bulbs and fertilise for early blooms.",
            "vegetable": (
                "Start seeds indoors and transplant after frost."
            ),
            "herb": "Plant new herbs and prune old growth."
        },
        "autumn": {
            "flower": "Deadhead spent blooms and prepare for winter.",
            "vegetable": (
                "Harvest late crops and prepare soil for next year."
            ),
            "herb": "Dry herbs for winter use."
        }
    }
    season_advice = advice_dict.get(season, {})
    return season_advice.get(plant_type, "No advice for this combination.")

# Determine advice based on the plant type


def recommend_plants(season):
    """Recommend plants based on the season."""
    recommendations = {
        "summer": ["Sunflower", "Tomato", "Basil"],
        "winter": ["Pansy", "Kale", "Rosemary"],
        "spring": ["Daffodil", "Lettuce", "Mint"],
        "autumn": ["Chrysanthemum", "Broccoli", "Sage"]
    }
    return recommendations.get(season, [])

# Print the generated advice


def main():
    """Main workflow for the gardening advice app."""
    season, plant_type = get_user_input()
    advice = get_advice(season, plant_type)
    print("\nGardening Advice:")
    print(advice)

    plants = recommend_plants(season)
    if plants:
        print(
            "\nRecommended plants for {}: {}".format(
                season.capitalize(), ", ".join(plants)
            )
        )
    else:
        print("\nNo plant recommendations for this season.")


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
