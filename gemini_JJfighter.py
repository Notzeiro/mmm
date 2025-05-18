import random
import time

# Character data with names, HP, abilities, and descriptions
characters = {
    "Yuji Itadori": {
        "hp": 150,
        "abilities": {
            "Strong Fist": (30, "A powerful punch infused with cursed energy."),
            "Divergent Fist": (40, "A technique that releases cursed energy in two waves."),
            "Black Flash": (50, "A devastating attack that amplifies cursed energy impact."),
            "Sukuna's Curse": (60, "Unleashes a powerful attack, but has a chance to backfire. Deals damage to self if backfire", 0.5), # 0.5 is the probability of backfire
        },
        "description": "The main protagonist. High physical strength and potential for cursed energy.",
    },
    "Megumi Fushiguro": {
        "hp": 130,
        "abilities": {
            "Ten Shadows Technique: Nue": (25, "Summons Nue to attack with lightning."),
            "Ten Shadows Technique: Great Serpent": (30, "Summons a giant serpent to bind and constrict."),
            "Ten Shadows Technique: Round Deer": (35, "Summons a healing deer."),
            "Ten Shadows Technique: Mahoraga Adaptation": (70, "Summons Mahoraga. Deals massive damage, high risk."),
        },
        "description": "A skilled jujutsu sorcerer who uses the Ten Shadows Technique.",
    },
    "Nobara Kugisaki": {
        "hp": 120,
        "abilities": {
            "Hairpin": (20, "Throws a handful of nails at the enemy."),
            "Straw Doll Technique: Resonance": (35, "Links her cursed energy to a part of her target."),
            "Straw Doll Technique: Black Flash": (50, "A powerful strike with her hammer and nails."),
            "Hidden Strike": (45, "A surprise attack"),
        },
        "description": "A fierce and confident jujutsu sorcerer who uses hammer and nails.",
    },
    "Satoru Gojo": {
        "hp": 200,
        "abilities": {
            "Limitless: Neutral": (40, "Manipulates space to attack."),
            "Limitless: Blue": (50, "Attracts objects with immense force."),
            "Limitless: Red": (60, "Repels objects with immense force."),
            "Hollow Purple": (80, "A devastating attack that erases matter."),
            "Six Eyes": (0, "Passively increases accuracy and evasion.", 1.0),  # Passive ability, no direct damage.  Accuracy/evasion multiplier
        },
        "description": "The strongest jujutsu sorcerer. Possesses immense power and the Six Eyes.",
    },
    "Ryomen Sukuna": {
        "hp": 170,
        "abilities": {
            "Dismantle": (35, "Slashes the opponent with cursed energy."),
            "Cleave": (40, "A more powerful version of Dismantle."),
            "Fire Arrow": (60, "Unleashes a devastating fire attack."),
            "Malevolent Shrine": (70, "A wide-range attack that deals massive damage."),
        },
        "description": "The King of Curses. Immensely powerful and malevolent.",
    },
    "Maki Zenin": {
        "hp": 140,
        "abilities": {
            "Playful Cloud": (30, "A powerful strike with a cursed tool."),
            "Toji's Speed": (35, "Incredibly fast attack and movement."),
            "Sword Skill": (40, "Expert swordsmanship with a cursed weapon."),
            "True and Complete Power": (60, "Unleashes her full strength."),
        },
        "description": "A skilled fighter with exceptional physical abilities and cursed tools.",
    },
    "Toge Inumaki": {
        "hp": 110,
        "abilities": {
            "Cursed Speech: Stop": (20, "Freezes the opponent in place."),
            "Cursed Speech: Twist": (30, "Twists the opponent's body."),
            "Cursed Speech: Crush": (40, "Crushes the opponent with immense force."),
            "Cursed Speech: Don't Move": (50, "Stronger binding command"),
        },
        "description": "A jujutsu sorcerer who uses Cursed Speech, a powerful but dangerous ability.",
    },
    "Yuta Okkotsu": {
        "hp": 160,
        "abilities": {
            "Rika's Power: Blast": (35, "Unleashes a powerful energy blast."),
            "Rika's Power: Bind": (30, "Rika restrains the opponent."),
            "Swordplay": (45, "Expert swordsmanship with cursed energy."),
            "Copy": (50, "Copies another ability. (Random)"),
        },
        "description": "A special grade jujutsu sorcerer with immense cursed energy and the power of Rika.",
    },
     "Mahito": {
        "hp": 120,
        "abilities": {
            "Idle Transfiguration: Shape": (30, "Alters the shape of the opponent's soul, causing damage."),
            "Idle Transfiguration: Size": (35, "Changes the size of a part of the opponent's body."),
            "Soul Multiplicity": (40, "Creates clones of himself."),
            "Polymorphic Human Weapon": (50, "Transforms his arm into a deadly weapon."),
        },
        "description": "A dangerous cursed spirit who can manipulate souls.",
    },
    "Kenjaku":{
        "hp": 180,
        "abilities":{
            "Cursed Spirit Manipulation": (40, "Controls cursed spirits to attack."),
            "Body Hopping": (0, "Passively increases evasion", 1.1), # Passive ability
            "Uzamaki": (60, "Releases a massive amount of cursed energy."),
            "Barrier Technique": (50, "Traps opponent"),
        },
        "description": "An ancient sorcerer with immense knowledge and cunning.",
    }
}

def display_characters(available_characters):
    """Displays the available characters with their descriptions."""
    print("\nAvailable Characters:")
    for i, (name, data) in enumerate(available_characters.items()):
        print(f"{i + 1}. {name}: {data['description']} (HP: {data['hp']})")

def select_character(available_characters, player_num):
    """Prompts the player to select a character."""
    while True:
        display_characters(available_characters)
        try:
            choice = int(input(f"Player {player_num}, choose your character (1-{len(available_characters)}): ")) - 1
            if 0 <= choice < len(available_characters):
                character_name = list(available_characters.keys())[choice]
                return character_name, available_characters[character_name]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_abilities(character):
    """Displays the abilities of the selected character."""
    print(f"\n{character['name']}'s Abilities:")
    for i, (ability_name, (damage, description, *rest)) in enumerate(character['abilities'].items()):
        print(f"{i + 1}. {ability_name}: {description} (Damage: {damage})")

def select_ability(character):
    """Prompts the player to select an ability."""
    while True:
        display_abilities(character)
        try:
            choice = int(input(f"Choose an ability (1-{len(character['abilities'])}): ")) - 1
            if 0 <= choice < len(character['abilities']):
                return list(character['abilities'].keys())[choice]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_damage(attacker, defender, ability_name):
    """Calculates the damage dealt by an ability, considering passive abilities."""
    ability_damage, description, *rest = attacker['abilities'][ability_name]
    # Check for passive abilities that modify damage
    if ability_name == "Six Eyes" or ability_name == "Body Hopping":  # Example of a passive ability
        return 0  # Passive abilities don't deal direct damage

    # Apply damage
    damage = ability_damage

    #Check for Sukuna Backfire
    if ability_name == "Sukuna's Curse" and random.random() < attacker['abilities'][ability_name][2]:
        print("Sukuna's Curse backfired!")
        attacker['hp'] -= damage # Damage self.
        return -damage # negative damage indicates self-inflicted damage

    return damage

def apply_damage(defender, damage):
    """Applies the calculated damage to the defender."""
    if damage > 0:
        defender['hp'] -= damage
        print(f"{defender['name']} takes {damage} damage!")
    elif damage < 0:
        print(f"{defender['name']} takes {-damage} damage!") # prints the damage amount as positive
    else:
        print("No damage dealt.")

def check_game_over(player1, player2):
    """Checks if the game is over."""
    if player1['hp'] <= 0:
        print(f"{player2['name']} wins!")
        return True
    elif player2['hp'] <= 0:
        print(f"{player1['name']} wins!")
        return True
    return False

def game_turn(attacker, defender, turn_number):
    """Handles a single turn of the game."""
    print(f"\n--- Turn {turn_number} ---")
    print(f"{attacker['name']}'s turn.")

    # Apply passive effects at the start of the turn.
    if attacker['name'] == "Satoru Gojo":
        print("Satoru Gojo's Six Eyes enhances his accuracy and evasion!")
        # In a more complex game, you might track accuracy/evasion as separate stats.
    if attacker['name'] == "Kenjaku":
        print("Kenjaku's Body Hopping makes him harder to hit!")

    ability_name = select_ability(attacker)
    damage = calculate_damage(attacker, defender, ability_name)
    apply_damage(defender, damage)
    time.sleep(1)  # Add a short pause for dramatic effect

def display_hp(player1, player2):
    """Displays the current HP of both players."""
    print(f"\n{player1['name']} HP: {player1['hp']}")
    print(f"{player2['name']} HP: {player2['hp']}")

def main():
    """Main function to run the game."""
    print("Welcome to Jujutsu Kaisen Fighter!")
    available_characters = characters.copy() # Create a copy to avoid modifying the original
    # Player 1 selects character
    player1_name, player1_data = select_character(available_characters, 1)
    player1 = {"name": player1_name, "hp": player1_data["hp"], "abilities": player1_data["abilities"]}
    available_characters.pop(player1_name) # Remove selected character.

    # Player 2 selects character
    player2_name, player2_data = select_character(available_characters, 2)
    player2 = {"name": player2_name, "hp": player2_data["hp"], "abilities": player2_data["abilities"]}

    print(f"\nPlayer 1: {player1['name']} vs Player 2: {player2['name']}")
    time.sleep(1)

    turn_number = 1
    while True:
        game_turn(player1, player2, turn_number)
        display_hp(player1, player2)
        if check_game_over(player1, player2):
            break
        # Swap players for the next turn
        player1, player2 = player2, player1
        turn_number += 1

if __name__ == "__main__":
    main()
