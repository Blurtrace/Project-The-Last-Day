# -------------------------------
# GENERAL CALCULATIONS
# -------------------------------

def calculate_remaining_days(current_turn, goal_turns=10):
    """Calculates how many days are left to finish."""
    return goal_turns - current_turn


def calculate_remaining_damage(damage_per_day, remaining_turns):
    """Calculates the total damage the player will receive until day 10."""
    return damage_per_day * remaining_turns


# -------------------------------
# PREDICTIONS
# -------------------------------

def predict_death_by_thirst(days_without_water, remaining_turns):
    """Predicts if the player will die due to lack of water."""
    return (days_without_water + remaining_turns) >= 3


def predict_death_by_hunger(player_health, damage_per_day, remaining_turns):
    """Predicts if health will reach 0 before day 10."""
    total_expected_damage = damage_per_day * remaining_turns
    return player_health <= total_expected_damage


# -------------------------------
# HEALTH VERIFICATION
# -------------------------------

def check_health_viability(player_health, future_total_damage):
    """Checks if health is enough to survive."""
    return player_health > future_total_damage


def emit_defeat_alert(player_health, remaining_turns):
    """Displays a future defeat alert."""
    print("\n--- PREDICTION ALERT ---")
    print(f"With {player_health} health it is not possible to survive {remaining_turns} more days.")
    print("GAME OVER: Exhaustion will be inevitable before day 10.")


# -------------------------------
# DEATH CONDITION
# -------------------------------

def is_dead(player_health):
    """Evaluates if health has reached 0."""
    return player_health <= 0


def end_game(death_cause):
    """Displays the end of the game."""
    print("\n-------------------------------------------")
    print("GAME OVER: The game has ended.")
    print(f"Cause of death: {death_cause}")
    print("-------------------------------------------")


def check_vital_status(player_health):
    """Coordinates if the game should end."""
    if is_dead(player_health):
        end_game("Health depleted (Accumulated damage)")
        return True


# -------------------------------
# MAIN VERIFICATION SYSTEM
# -------------------------------

def run_defeat_verification(player_health, water_supply, food_supply, days_without_water, current_turn, damage_per_day):
    """Coordinates all system predictions."""

    remaining_turns = calculate_remaining_days(current_turn)

    # Prediction due to thirst
    if predict_death_by_thirst(days_without_water, remaining_turns):
        end_game("Death by dehydration")
        return True

    # Prediction due to hunger
    if predict_death_by_hunger(player_health, damage_per_day, remaining_turns):
        end_game("Death by starvation")
        return True

    # Future damage evaluation
    future_damage = calculate_remaining_damage(damage_per_day, remaining_turns)

    if not check_health_viability(player_health, future_damage):
        emit_defeat_alert(player_health, remaining_turns)
        return True