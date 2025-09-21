"""

whoseTurn = 0

"""
"""

playerDicedNumber = 0

"""
"""

def on_button_multiplayer_a_pressed(player2):

"""
"""

global playerDicedNumber

"""
"""

if whoseTurn != 0 and mp.get_player_property(player2, mp.PlayerProperty.NUMBER) == whoseTurn:

"""
"""

playerDicedNumber = randint(1, 6)

"""
"""

game.splash("Rolled " + ("" + str(playerDicedNumber)))

"""
"""

mp.on_button_event(mp.MultiplayerButton.A,

"""
"""

ControllerButtonEvent.PRESSED,

"""
"""

on_button_multiplayer_a_pressed)

"""
"""

def on_update_interval():

"""
"""

global whoseTurn, playerDicedNumber

"""
"""

if playerDicedNumber != 0:

"""
"""

if playerDicedNumber == 6:

"""
"""

mp.game_over_player_win(mp.get_player_by_number(whoseTurn))

"""
"""

game.set_game_over_effect(True, effects.confetti)

"""
"""

whoseTurn = 0

"""
"""

playerDicedNumber = 0

"""
"""

if whoseTurn == 0:

"""
"""

whoseTurn = randint(1, 2)

"""
"""

game.splash("Player " + ("" + str(whoseTurn)))

"""
"""

game.on_update_interval(100, on_update_interval)

"""
# hand over turn

def on_button_multiplayer_a_pressed(player2):
    global playerDicedNumber
    # only accept the current player's press
    if whoseTurn != 0 and mp.get_player_property(player2, mp.PlayerProperty.NUMBER) == whoseTurn:
        playerDicedNumber = randint(1, 6)
        game.splash("Rolled " + ("" + str(playerDicedNumber)))
        if playerDicedNumber == 6:
            mp.game_over_player_win(player2)
            game.set_game_over_effect(True, effects.confetti)
        else:
            next_turn()
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def next_turn():
    global whoseTurn, playerDicedNumber
    whoseTurn = randint(1, 2)
    playerDicedNumber = 0
    game.splash("Player " + ("" + str(whoseTurn)) + """
        's turn
        Press A to roll
        """)
playerDicedNumber = 0
whoseTurn = 0
next_turn()