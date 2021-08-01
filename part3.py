
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


def get_user_input():
    first_input = input("Type Yes if so else type No:")
    if first_input == "No":
        second_input = None
    elif first_input == "Yes":
        print("Is sport closed?")
        second_input = input("Type Yes if so else type No:")
    return (first_input, second_input)


def showReport(data):
    for k, v in data.items():
        if v[0] is "Yes":
            if v[1] is "No":
                return f"{k} is affected and open"
            elif v[1] is "Yes":
                return f"{k} is affected and closed"
        elif v[0] is "No":
            return f"{k} is not affected and open"


if __name__ =='__main__':
    print("Hi welcome to Super Sportsdata.")
    athletes = open_file("athleteList.txt")
    for athlete in athletes:
        athlete_name, athlete_sport = athlete.strip().split()
        SPORT_DATA[athlete_sport] = SPORT_DATA.get(athlete_sport, []).append(athlete_name)
    print("We have updated our software")

    sports = list(SPORT_DATA.keys())
    number_of_sports = len(SPORT_DATA.keys())
    secList = {}
    for i, sport in enumerate(sports):
        print(f"Is sport {sport} affected?")
        secList[sport] = get_user_input()
    showReport(secList)
