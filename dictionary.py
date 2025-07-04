available_parts = {
    "1": "computer",
    "2": "moniter",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}

computer_parts = []
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            #already in the list so remove 
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    current_choice = input("> ")