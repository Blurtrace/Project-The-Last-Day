import random


def calculate_remaining_days(current_day, goal_days=10):
    return goal_days - current_day


def calculate_remaining_damage(daily_damage, days_left):
    return daily_damage * days_left


def check_health_viability(current_health, future_total_damage):
    return current_health > future_total_damage


def issue_defeat_alert(health, remaining_days):
    print("\n--- FORECAST ALERT ---")
    print(
        f"With {health} health it is not possible to survive {remaining_days} more days.")
    print("GAME OVER: Inevitable exhaustion before day 10.")


def is_dead(health):
    return health <= 0


def end_game(cause):
    print("\n-------------------------------------------")
    print("GAME OVER: The game has ended.")
    print(f"Cause of death: {cause}.")
    print("-------------------------------------------")


def check_vital_status(current_health):
    if is_dead(current_health):
        end_game("Health depleted (Accumulated damage)")
        return True
    return False


def run_defeat_check(health, water, food, days_without_water, current_day):
    remaining_days = calculate_remaining_days(current_day)

    # Check death by dehydration
    if water <= 0:
        days_without_water += 1
        if days_without_water >= 3:
            end_game("Dehydration (3 days without water)")
            return True, days_without_water
    else:
        days_without_water = 0

    # Check damage due to hunger
    daily_damage = 10 if food <= 0 else 0
    future_total_damage = calculate_remaining_damage(
        daily_damage, remaining_days)

    if not check_health_viability(health, future_total_damage):
        issue_defeat_alert(health, remaining_days)
        return True, days_without_water

    return False, days_without_water


# -------------------------
# Test Run
# -------------------------
finished, days_without_water = run_defeat_check
(health, water, food, days_without_water, current_day)

if not finished:
    print("The player can continue.")
