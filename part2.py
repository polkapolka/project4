
SPORT_DATA = {}


def display_menu(sports_list):
    print("Now you can see athletes belonging to a particular sport with just a press of a button")
    print("Which sport would you want to select?")
    for i, v in enumerate(sports_list):
        print(f"{i}. {v}")


def open_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def display_athletes_in_sport(sport):
    print(f"You have chosen {sport}")
    print("Athletes in sport")
    for athlete in SPORT_DATA.get(sport,[]):
        print(f"{athlete}\t {sport}")


if __name__ =='__main__':
    print("Hi welcome to Super Sportsdata.")
    athletes = open_file("athleteList.txt")
    for athlete in athletes:
        athlete_name, athlete_sport = athlete.strip().split()
        SPORT_DATA[athlete_sport] = SPORT_DATA.get(athlete_sport, []).append(athlete_name)
    print("We have updated our software")

    number_of_sports = len(SPORT_DATA.keys())
    user_input = 0
    while user_input < number_of_sports:
        display_menu()
        user_input = int(input("Select choice:")) - 1
        if user_input in list(range(number_of_sports)):
            chosen_sport = list(SPORT_DATA.keys())[user_input]
            display_athletes_in_sport(chosen_sport)