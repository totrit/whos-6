def on_button_multiplayer_a_pressed(player2):
    global playerDicedNumber
    if whoseTurn != 0 and player2 == mp.get_player_by_number(whoseTurn):
        playerDicedNumber = randint(1, 6)
        game.splash("Rolled " + ("" + str(playerDicedNumber)))
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

playerDicedNumber = 0
whoseTurn = 0
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . .
        . . . . f 5 4 5 5 4 5 f . . . .
        . . . f e 4 5 5 5 5 4 e f . . .
        . . f b 3 e 4 4 4 4 e 3 b f . .
        . . f 3 3 3 3 3 3 3 3 3 3 f . .
        . f 3 3 e b 3 e e 3 b e 3 3 f .
        . f 3 3 f f e e e e f f 3 3 f .
        . f b b f b f e e f b f b b f .
        . f b b e 1 f 4 4 f 1 e b b f .
        f f b b f 4 4 4 4 4 4 f b b f f
        f b b f f f e e e e f f f b b f
        . f e e f b d d d d b f e e f .
        . . e 4 c d d d d d d c 4 e . .
        . . e f b d b d b d b b f e . .
        . . . f f 1 d 1 d 1 d f f . . .
        . . . . . f f b b f f . . . . .
        """),
    SpriteKind.player)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE), mySprite)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO), mySprite2)
mySprite.set_position(6, 108)
mySprite2.set_position(145, 104)
mp.set_player_indicators_visible(True)

def on_update_interval():
    global whoseTurn, playerDicedNumber
    if playerDicedNumber != 0:
        if playerDicedNumber == 6:
            mp.game_over_player_win(mp.get_player_by_number(whoseTurn))
            game.set_game_over_effect(True, effects.confetti)
        whoseTurn = 0
        playerDicedNumber = 0
        if whoseTurn == 0:
            whoseTurn = randint(1, 2)
            mp.get_player_sprite(mp.get_player_by_number(whoseTurn)).say_text(":)", 1200)
game.on_update_interval(100, on_update_interval)
