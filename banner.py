def banner_text(text: str = " ", screen_width: int = 70) -> None:
    """
    print the `text` centered to the width of the screen,
    with the ** printed at the left and right border

    Args:
        text (str, optional): The `text` that needs to be printed.
        An asterick (*) will result in printing the row of astericks.
        The default would print blank line with ** at left and right ends.
        Defaults to " ".
        screen_width (int, optional):The width of the screen to print within.
        (including the 4 places for ** at both the ends)
        Defaults to 70.

    Raises:
        ValueError: If the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String is larger than specified width {}".format(screen_width))
        
    elif text == "*":
        print("*" * screen_width)
    else:
        centered_string = text.center(screen_width - 4)
        print("**{}**".format(centered_string))
        
        
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")