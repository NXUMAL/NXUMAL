def main():
    # Room types and their details
    room_types = {
        "Double": {"Cost Per Night": 600, "Number of Sleeper": 2},
        "Triple": {"Cost Per Night": 750, "Number of Sleeper": 3},
        "Quad": {"Cost Per Night": 1100, "Number of Sleeper": 4},
        "Queen": {"Cost Per Night": 1500, "Number of Sleeper": 2}
    }

    # Get guest information
    name = input("Enter guest's name: ")
    surname = input("Enter guest's surname: ")
    email = input("Enter guest's email address: ")

    # Get room type and number of guests
    print("Room Types:")
    for room_type, details in room_types.items():
        print(f"Type of Room: {room_type}, Cost Per Night: R{details['Cost Per Night']}, Number of Sleeper: {details['Number of Sleeper']} sleeper")

    required_room_type = input("Enter the type of room required: ")
    num_guests = int(input("Enter the number of guests: "))

    # Calculate number of rooms required
    num_rooms = (num_guests + room_types[required_room_type]["Number of Sleeper"] - 1) // room_types[required_room_type]["Number of Sleeper"]

    # Get number of days staying
    num_days = int(input("Enter the number of days the guest/s will be staying: "))

    # Calculate total cost
    total_cost = num_rooms * room_types[required_room_type]["Cost Per Night"] * num_days

    # Display total cost
    print(f"Total cost of the booking: R{total_cost:.2f}")


if __name__ == "__main__":
    main()

