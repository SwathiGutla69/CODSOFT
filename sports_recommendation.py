print("=== Sports Recommendation System ===")

sports = {
    "cricket": ["IPL", "World Cup", "Champions Trophy"],
    "football": ["Premier League", "La Liga", "UEFA Champions League"],
    "kabaddi": ["Pro Kabaddi League", "National Kabaddi Championship"],
    "tennis": ["Wimbledon", "US Open", "Australian Open"],
    "badminton": ["BWF World Tour", "All England Open", "Thomas Cup"]
}

sport = input("Enter your favorite sport: ").lower()

if sport in sports:
    print("\nRecommended Events:")
    for event in sports[sport]:
        print("-", event)
else:
    print("Sorry! Sport not found.")