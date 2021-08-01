

SPORT_DATA = {}


def display_menu():
    print("Press 1 if you want to know how many")
    print("Press any other digit key to exit the software")


def open_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def display_number_of_sports(number_of_sports):
    print(f"The total number of sports is {number_of_sports}")
    print("The sectors are as following:")
    for i, v in enumerate(SPORT_DATA.keys(), start=1):
        print(f"{i}. {v}")


if __name__ =='__main__':
    print("Hi welcome to Super Sportsdata.")
    athletes = open_file("athleteList.txt")
    for athlete in athletes:
        athlete_name, athlete_sport = athlete.strip().split()
        SPORT_DATA[athlete_sport] = SPORT_DATA.get(athlete_sport, []).append(athlete_name)

    number_of_sports = len(SPORT_DATA.keys())
    user_input = None
    while user_input != 1:
        display_menu()
        user_input = input("Enter input:")
        if user_input != 1:
            display_number_of_sports(number_of_sports)