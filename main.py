def SpawnEnemy():
    global Guard
    Guard = sprites.create(img("""
        ........................
        ......ffff..............
        ....fff22fff............
        ...fff2222fff...........
        ..fffeeeeeefff..........
        ..ffe222222eef..........
        ..fe2ffffff2ef..........
        ..ffffeeeeffff..........
        .ffefbf44fbfeff.........
        .fee41fddf14eef.........
        fdfeeddddd4eff..........
        fbffee444edd4e..........
        fbf4f2222edde...........
        fcf.f22cccee............
        .ff.f44cdc4f............
        ....fffddcff............
        .....fddcff.............
        ....cddc................
        ....cdc.................
        ....cc..................
        ........................
        ........................
        ........................
        ........................
    """), SpriteKind.player)
    
    for value13 in tiles.get_tiles_by_type(assets.tile("""
        myTile16
    """)):
        tiles.place_on_tile(Guard, value13)
        tiles.set_tile_at(value13, assets.tile("""
            Underwater
        """))
    
    def moveguard():
        while True:
            Guard.vx = -20
            pause(1500)
            Guard.vx = 20
            pause(1500)
    
    control.run_in_parallel(moveguard)
    
def spawnexplorer():
    global Explorer
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        Explorer = sprites.create(img("""
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
        tiles.place_on_tile(Explorer, value)
        scene.camera_follow_sprite(Explorer)
def SpawnCoin3():
    global coin3
    for value12 in tiles.get_tiles_by_type(assets.tile("""
        myTile11
        """)):
        coin3 = sprites.create(img("""
                . . b b b b . .
                . b 5 5 5 5 b .
                b 5 d 3 3 d 5 b
                b 5 3 5 5 1 5 b
                c 5 3 5 5 1 d c
                c d d 1 1 d d c
                . f d d d d f .
                . . f f f f . .
                """),
            SpriteKind.food)
        tiles.place_on_tile(coin3, value12)
        animation.run_image_animation(coin3,
            [img("""
                    9 9 b b b b 9 9
                    9 b 5 5 5 5 b 9
                    b 5 d 3 3 d 5 b
                    b 5 3 5 5 1 5 b
                    c 5 3 5 5 1 d c
                    c d d 1 1 d d c
                    9 f d d d d f 9
                    9 9 f f f f 9 9
                    """),
                img("""
                    9 9 b b b 9 9 9
                    9 b 5 5 5 b 9 9
                    b 5 d 3 d 5 b 9
                    b 5 3 5 1 5 b 9
                    c 5 3 5 1 d c 9
                    c 5 d 1 d d c 9
                    9 f d d d f 9 9
                    9 9 f f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 d 1 5 b 9
                    9 b 5 3 1 5 b 9
                    9 c 5 3 1 d c 9
                    9 c 5 1 d d c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b 1 1 b 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b d d b 9 9
                    9 9 c d d c 9 9
                    9 9 c 3 3 c 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 1 d 5 b 9
                    9 b 5 1 3 5 b 9
                    9 c d 1 3 5 c 9
                    9 c d d 1 5 c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b b 9 9
                    9 9 b 5 5 5 b 9
                    9 b 5 d 3 d 5 b
                    9 b 5 1 5 3 5 b
                    9 c d 1 5 3 5 c
                    9 c d d 1 d 5 c
                    9 9 f d d d f 9
                    9 9 9 f f f 9 9
                    """)],
            150,
            True)
        coin3.scale = 1.5
def movement(character: Sprite):
    controller.move_sprite(character, 100, 0)
    character.ay = 225
    character.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    
    def on_jump_pressed():
        if character.is_hitting_tile(CollisionDirection.BOTTOM):
            character.vy = -150
    controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump_pressed)
    
def SpawnVariables():
    global numberofjumps, LightBlue, SpeedBoost
    numberofjumps = 0
    LightBlue = sprites.create(img("""
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
            """),
        SpriteKind.player)
    SpeedBoost = sprites.create(img("""
            9 9 9 9 9 b b b b b b 9 9 9 9 9
            9 9 9 b b 9 9 9 9 9 9 b b 9 9 9
            9 9 b b 9 9 9 9 9 9 9 9 b b 9 9
            9 b b 9 d 9 9 9 9 9 9 9 9 b b 9
            9 b 9 d 9 9 9 9 9 1 1 1 9 9 b 9
            b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
            b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
            b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
            b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
            b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
            b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
            9 b 5 3 3 3 d 9 9 9 9 d d 5 b 9
            9 b d 5 3 3 3 3 3 3 3 d 5 b b 9
            9 9 b d 5 d 3 3 3 3 5 5 b b 9 9
            9 9 9 b b 5 5 5 5 5 5 b b 9 9 9
            9 9 9 9 9 b b b b b b 9 9 9 9 9
            """),
        SpriteKind.food)
def spawnmermaid():
    global Mermaid
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        Mermaid = sprites.create(img("""
                . . . . . . 5 . 5 . . . . . . .
                . . . . . f 5 5 5 f f . . . . .
                . . . . f 1 5 2 5 1 6 f . . . .
                . . . f 1 6 6 6 6 6 1 6 f . . .
                . . . f 6 6 f f f f 6 1 f . . .
                . . . f 6 f f d d f f 6 f . . .
                . . f 6 f d f d d f d f 6 f . .
                . . f 6 f d 3 d d 3 d f 6 f . .
                . . f 6 6 f d d d d f 6 6 f . .
                . f 6 6 f 3 f f f f 3 f 6 6 f .
                . . f f d 3 5 3 3 5 3 d f f . .
                . . f d d f 3 5 5 3 f d d f . .
                . . . f f 3 3 3 3 3 3 f f . . .
                . . . f 3 3 5 3 3 5 3 3 f . . .
                . . . f f f f f f f f f f . . .
                . . . . . f f . . f f . . . . .
                """),
            SpriteKind.player)
        tiles.place_on_tile(Mermaid, value2)
        scene.camera_follow_sprite(Mermaid)
def characterMovement():
    if selectedAvatar == "Explorer":
        movement(Explorer)
    elif selectedAvatar == "Mermaid":
        movement(Mermaid)
    elif selectedAvatar == "Cat":
        movement(Cat)

def on_overlap_tile(sprite4, location4):
    music.stop_all_sounds()
    game.splash("You have made it to DAY 4!")
    game.splash("Its very high up here, but thats okay.")
    game.splash("Land on the pad below!")
    game.splash("Are you ready?")
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile11
        """)):
        tiles.set_tile_at(value4, assets.tile("""
            Underwater
            """))
    sprites.destroy(coin3)
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile11
        """),
    on_overlap_tile)

def on_left_pressed():
    if selectedAvatar == "Cat":
        animation.run_image_animation(Cat,
            [img("""
                    e e e . . . . e e e . . . .
                    c d d c . . c d d c . . . .
                    c b d d f f d d b c . . . .
                    c 3 b d d b d b 3 c . . . .
                    f b 3 d d d d 3 b f . . . .
                    e d d d d d d d d e . . . .
                    e d f d d d d f d e . b f b
                    f d d f d d f d d f . f d f
                    f b d d b b d d 2 f . f d f
                    . f 2 2 2 2 2 2 b b f f d f
                    . f b d d d d d d b b d b f
                    . f d d d d d b d d f f f .
                    . f d f f f d f f d f . . .
                    . f f . . f f . . f f . . .
                    """),
                img("""
                    . . . . . . . . . . . . . .
                    e e e . . . . e e e . . . .
                    c d d c . . c d d c . . . .
                    c b d d f f d d b c . . . .
                    c 3 b d d b d b 3 c . . . .
                    f b 3 d d d d 3 b f . . . .
                    e d d d d d d d d e . . . .
                    e d f d d d d f d e b f b .
                    f d d f d d f d d f f d f .
                    f b d d b b d d 2 b f d f .
                    . f 2 2 2 2 2 2 d b d b f .
                    . f d d d d d d d f f f . .
                    . f d b d f f f d f . . . .
                    . . f f f f . . f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . .
                    e e e . . . . e e e . . . .
                    c d d c . . c d d c . . . .
                    c b d d f f d d b c . . . .
                    c 3 b d d b d b 3 c . . . .
                    f b 3 d d d d 3 b f . . . .
                    e d d d d d d d d e . . . .
                    e d f d d d d f d e . b f b
                    f d d f d d f d d f . f d f
                    f b d d b b d d 2 b f f d f
                    . f 2 2 2 2 2 2 d b b d b f
                    . f d d d d d d d f f f f .
                    . . f d b d f d f . . . . .
                    . . . f f f f f f . . . . .
                    """)],
            500,
            False)
    elif selectedAvatar == "Mermaid":
        animation.run_image_animation(Mermaid,
            [img("""
                    . . . . . . 5 . 5 . . . . . . .
                    . . . . . f 5 5 5 f . . . . . .
                    . . . . f 6 2 5 5 6 f . . . . .
                    . . . f 6 6 6 6 1 6 6 f . . . .
                    . . . f 6 6 6 6 6 1 6 f . . . .
                    . . . f d f d 6 6 6 1 f . . . .
                    . . . f d f d 6 6 6 6 f f . . .
                    . . . f d 3 d d 6 6 6 f 6 f . .
                    . . . . f d d d f f 6 f f . . .
                    . . . . . f f 5 3 f 6 6 6 f . .
                    . . . . f 5 3 3 f f f f f . . .
                    . . . . f 3 3 f d f . . . . . .
                    . . . . . f 3 f d f . . . . . .
                    . . . . f 3 5 3 f d f . . . . .
                    . . . . f f 3 3 f f . . . . . .
                    . . . . . . f f f . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . 5 . 5 . . . . . .
                    . . . . . . f 5 5 5 f . . . . .
                    . . . . . f 6 2 5 5 6 f . . . .
                    . . . . f 6 6 6 6 1 6 6 f . . .
                    . . . . f 6 6 6 6 6 1 6 f . . .
                    . . . . f d f d 6 6 6 1 f . . .
                    . . . . f d f d 6 6 6 6 f f . .
                    . . . . f d 3 d d 6 6 6 f 6 f .
                    . . . . . f d d d f f 6 f f . .
                    . . . . . . f f 3 3 f f 6 6 f .
                    . . . . . f d d d d f f f f . .
                    . . . . . f d d d f 3 f . . . .
                    . . . . . . f f f d 5 3 f . . .
                    . . . . . f f f 3 3 f f . . . .
                    . . . . . f f f f f f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . 5 . 5 . . . . . .
                    . . . . . . f 5 5 5 f . . . . .
                    . . . . . f 6 2 5 5 6 f . . . .
                    . . . . f 6 6 6 6 1 6 6 f . . .
                    . . . . f 6 6 6 6 6 1 6 f . . .
                    . . . . f d f d 6 6 6 1 f . . .
                    . . . . f d f d 6 6 6 6 f f . .
                    . . . . f d 3 d d 6 6 6 f 6 f .
                    . . . . . f d d d f f 6 f f . .
                    . . . . . . f f 3 3 f f 6 6 f .
                    . . . . . f 5 3 3 d d f f f . .
                    . . . . . f 3 3 3 f d d f . . .
                    . . . . . . f 3 5 f f f . . . .
                    . . . . . f 3 3 3 3 f . . . . .
                    . . . . . . f f f f f . . . . .
                    """)],
            500,
            False)
    elif selectedAvatar == "Explorer":
        animation.run_image_animation(Explorer,
            [img("""
                    . . . f 4 4 f f f f . . . . . .
                    . . f 4 5 5 4 5 f b f f . . . .
                    . . f 5 5 5 5 4 e 3 3 b f . . .
                    . . f e 4 4 4 e 3 3 3 3 b f . .
                    . . f 3 3 3 3 3 3 3 3 3 3 f . .
                    . f 3 3 e e 3 b e 3 3 3 3 f . .
                    . f 3 3 e e e f f 3 3 3 3 f . .
                    . f 3 e e e f b f b b b b f . .
                    . . f e 4 4 f 1 e b b b b f . .
                    . . . f 4 4 4 4 f b b b b f f .
                    . . . f e e e f f f b b b b f .
                    . . . f d d d e 4 4 f b b f . .
                    . . . f d d d e 4 4 e f f . . .
                    . . f b d b d b e e b f . . . .
                    . . f f 1 d 1 d 1 d f f . . . .
                    . . . . f f b b f f . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . f 4 4 f f f f . . . . . .
                    . . f 4 5 5 4 5 f b f f . . . .
                    . . f 5 5 5 5 4 e 3 3 b f . . .
                    . . f e 4 4 4 e 3 3 3 3 b f . .
                    . f 3 3 3 3 3 3 3 3 3 3 3 f . .
                    . f 3 3 e e 3 b e 3 3 3 3 f . .
                    . f 3 3 e e e f f 3 3 3 3 f . .
                    . . f e e e f b f b b b b f f .
                    . . . e 4 4 f 1 e b b b b b f .
                    . . . f 4 4 4 4 f b b b b b f .
                    . . . f d d d e 4 4 b b b f . .
                    . . . f d d d e 4 4 f f f . . .
                    . . f d d d b b e e b b f . . .
                    . . f b d 1 d 1 d d b f . . . .
                    . . . f f f b b f f f . . . . .
                    """)],
            500,
            False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def selectMusic():
    global musicChoice
    if musicChoiceNumber == 1:
        musicChoice = "Sitka"
        music.play(music.string_playable("C5 B A G A B C5 - ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif musicChoiceNumber == 2:
        musicChoice = "Paris"
        music.play(music.string_playable("E B C5 A B G A F ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    else:
        musicChoice = "Tokyo"
        music.play(music.string_playable("G A G B A G F E ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
def spawncat():
    global Cat
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        Cat = sprites.create(img("""
                e e e . . . . e e e . . . .
                c d d c . . c d d c . . . .
                c b d d f f d d b c . . . .
                c 3 b d d b d b 3 c . . . .
                f b 3 d d d d 3 b f . . . .
                e d d d d d d d d e . . . .
                e d f d d d d f d e . b f b
                f d d f d d f d d f . f d f
                f b d d b b d d 2 f . f d f
                . f 2 2 2 2 2 2 b b f f d f
                . f b d d d d d d b b d b f
                . f d d d d d b d d f f f .
                . f d f f f d f f d f . . .
                . f f . . f f . . f f . . .
                """),
            SpriteKind.player)
        tiles.place_on_tile(Cat, value6)
        scene.camera_follow_sprite(Cat)

def on_overlap_tile2(sprite43, location43):
    music.stop_all_sounds()
    game.splash("You have made it to the end!")
    game.splash("Congratulations!")
    music.play(music.string_playable("C5 B A G F E D C ", 480),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite23, location22):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile3)

def on_right_pressed():
    if selectedAvatar == "Cat":
        animation.run_image_animation(Cat,
            [img("""
                    . . . . e e e . . . . e e e
                    . . . . c d d c . . c d d c
                    . . . . c b d d f f d d b c
                    . . . . c 3 b d b d d b 3 c
                    . . . . f b 3 d d d d 3 b f
                    . . . . e d d d d d d d d e
                    b f b . e d f d d d d f d e
                    f d f . f d d f d d f d d f
                    f d f . f 2 d d b b d d b f
                    f d f f b b 2 2 2 2 2 2 f .
                    f b d b b d d d d d d b f .
                    . f f f d d b d d d d d f .
                    . . . f d f f d f f f d f .
                    . . . f f . . f f . . f f .
                    """),
                img("""
                    . . . . . . . . . . . . . .
                    . . . . e e e . . . . e e e
                    . . . . c d d c . . c d d c
                    . . . . c b d d f f d d b c
                    . . . . c 3 b d b d d b 3 c
                    . . . . f b 3 d d d d 3 b f
                    . . . . e d d d d d d d d e
                    . b f b e d f d d d d f d e
                    . f d f f d d f d d f d d f
                    . f d f b 2 d d b b d d b f
                    . f b d b d 2 2 2 2 2 2 f .
                    . . f f f d d d d d d d f .
                    . . . . f d f f f d b d f .
                    . . . . f f . . f f f f . .
                    """),
                img("""
                    . . . . . . . . . . . . . .
                    . . . . e e e . . . . e e e
                    . . . . c d d c . . c d d c
                    . . . . c b d d f f d d b c
                    . . . . c 3 b d b d d b 3 c
                    . . . . f b 3 d d d d 3 b f
                    . . . . e d d d d d d d d e
                    b f b . e d f d d d d f d e
                    f d f . f d d f d d f d d f
                    f d f f b 2 d d b b d d b f
                    f b d b b d 2 2 2 2 2 2 f .
                    . f f f f d d d d d d d f .
                    . . . . . f d f d b d f . .
                    . . . . . f f f f f f . . .
                    """)],
            500,
            False)
    elif selectedAvatar == "Mermaid":
        animation.run_image_animation(Mermaid,
            [img("""
                    . . . . . . . 5 . 5 . . . . . .
                    . . . . . . f 5 5 5 f . . . . .
                    . . . . . f 6 5 5 2 6 f . . . .
                    . . . . f 6 6 1 6 6 6 6 f . . .
                    . . . . f 6 1 6 6 6 6 6 f . . .
                    . . . . f 1 6 6 6 d f d f . . .
                    . . . f f 6 6 6 6 d f d f . . .
                    . . f 6 f 6 6 6 d d 3 d f . . .
                    . . . f f 6 f f d d d f . . . .
                    . . f 6 6 6 f 3 5 f f . . . . .
                    . . . f f f f f 3 3 5 f . . . .
                    . . . . . . f d f 3 3 f . . . .
                    . . . . . . f d f 3 f . . . . .
                    . . . . . f d f 3 5 3 f . . . .
                    . . . . . . f f 3 3 f f . . . .
                    . . . . . . . f f f . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 5 . 5 . . . . . . .
                    . . . . . f 5 5 5 f . . . . . .
                    . . . . f 6 5 5 2 6 f . . . . .
                    . . . f 6 6 1 6 6 6 6 f . . . .
                    . . . f 6 1 6 6 6 6 6 f . . . .
                    . . . f 1 6 6 6 d f d f . . . .
                    . . f f 6 6 6 6 d f d f . . . .
                    . f 6 f 6 6 6 d d 3 d f . . . .
                    . . f f 6 f f d d d f . . . . .
                    . f 6 6 f f 3 3 f f . . . . . .
                    . . f f f f d d d d f . . . . .
                    . . . . f 3 f d d d f . . . . .
                    . . . f 3 5 d f f f . . . . . .
                    . . . . f f 3 3 f f f . . . . .
                    . . . . f f f f f f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 5 . 5 . . . . . . .
                    . . . . . f 5 5 5 f . . . . . .
                    . . . . f 6 5 5 2 6 f . . . . .
                    . . . f 6 6 1 6 6 6 6 f . . . .
                    . . . f 6 1 6 6 6 6 6 f . . . .
                    . . . f 1 6 6 6 d f d f . . . .
                    . . f f 6 6 6 6 d f d f . . . .
                    . f 6 f 6 6 6 d d 3 d f . . . .
                    . . f f 6 f f d d d f . . . . .
                    . f 6 6 f f 3 3 f f . . . . . .
                    . . f f f d d 3 3 5 f . . . . .
                    . . . f d d f 3 3 3 f . . . . .
                    . . . . f f f 5 3 f . . . . . .
                    . . . . . f 3 3 3 3 f . . . . .
                    . . . . . f f f f f . . . . . .
                    """)],
            500,
            False)
    elif selectedAvatar == "Explorer":
        animation.run_image_animation(Explorer,
            [img("""
                    . . . . . . f f f f 4 4 f . . .
                    . . . . f f b f 5 4 5 5 4 f . .
                    . . . f b 3 3 e 4 5 5 5 5 f . .
                    . . f b 3 3 3 3 e 4 4 4 e f . .
                    . . f 3 3 3 3 3 3 3 3 3 3 f . .
                    . . f 3 3 3 3 e b 3 e e 3 3 f .
                    . . f 3 3 3 3 f f e e e 3 3 f .
                    . . f b b b b f b f e e e 3 f .
                    . . f b b b b e 1 f 4 4 e f . .
                    . f f b b b b f 4 4 4 4 f . . .
                    . f b b b b f f f e e e f . . .
                    . . f b b f 4 4 e d d d f . . .
                    . . . f f e 4 4 e d d d f . . .
                    . . . . f b e e b d b d b f . .
                    . . . . f f d 1 d 1 d 1 f f . .
                    . . . . . . f f b b f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f 4 4 f . . .
                    . . . . f f b f 5 4 5 5 4 f . .
                    . . . f b 3 3 e 4 5 5 5 5 f . .
                    . . f b 3 3 3 3 e 4 4 4 e f . .
                    . . f 3 3 3 3 3 3 3 3 3 3 3 f .
                    . . f 3 3 3 3 e b 3 e e 3 3 f .
                    . . f 3 3 3 3 f f e e e 3 3 f .
                    . f f b b b b f b f e e e f . .
                    . f b b b b b e 1 f 4 4 e . . .
                    . f b b b b b f 4 4 4 4 f . . .
                    . . f b b b 4 4 e d d d f . . .
                    . . . f f f 4 4 e d d d f . . .
                    . . . f b b e e b b d d d f . .
                    . . . . f b d d 1 d 1 d b f . .
                    . . . . . f f f b b f f f . . .
                    """)],
            500,
            False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def SpawnCoin1():
    global Coin1
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        myTile9
        """)):
        Coin1 = sprites.create(img("""
                . . b b b b . .
                . b 5 5 5 5 b .
                b 5 d 3 3 d 5 b
                b 5 3 5 5 1 5 b
                c 5 3 5 5 1 d c
                c d d 1 1 d d c
                . f d d d d f .
                . . f f f f . .
                """),
            SpriteKind.food)
        tiles.place_on_tile(Coin1, value7)
        animation.run_image_animation(Coin1,
            [img("""
                    9 9 b b b b 9 9
                    9 b 5 5 5 5 b 9
                    b 5 d 3 3 d 5 b
                    b 5 3 5 5 1 5 b
                    c 5 3 5 5 1 d c
                    c d d 1 1 d d c
                    9 f d d d d f 9
                    9 9 f f f f 9 9
                    """),
                img("""
                    9 9 b b b 9 9 9
                    9 b 5 5 5 b 9 9
                    b 5 d 3 d 5 b 9
                    b 5 3 5 1 5 b 9
                    c 5 3 5 1 d c 9
                    c 5 d 1 d d c 9
                    9 f d d d f 9 9
                    9 9 f f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 d 1 5 b 9
                    9 b 5 3 1 5 b 9
                    9 c 5 3 1 d c 9
                    9 c 5 1 d d c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b 1 1 b 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b d d b 9 9
                    9 9 c d d c 9 9
                    9 9 c 3 3 c 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 1 d 5 b 9
                    9 b 5 1 3 5 b 9
                    9 c d 1 3 5 c 9
                    9 c d d 1 5 c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b b 9 9
                    9 9 b 5 5 5 b 9
                    9 b 5 d 3 d 5 b
                    9 b 5 1 5 3 5 b
                    9 c d 1 5 3 5 c
                    9 c d d 1 d 5 c
                    9 9 f d d d f 9
                    9 9 9 f f f 9 9
                    """)],
            150,
            True)
        Coin1.scale = 1.5

def on_overlap_tile4(sprite42, location42):
    music.stop_all_sounds()
    game.splash("DAY 3")
    game.splash("Hold tight, you are almost there!")
    game.splash("It gets a little high up here but we can handle it!")
    game.splash("Lets do it!")
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile10
        """)):
        tiles.set_tile_at(value5, assets.tile("""
            Underwater
            """))
    sprites.destroy(Coin2)
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile10
        """),
    on_overlap_tile4)

def on_overlap_tile5(sprite2, location2):
    global PowerUpAsk
    music.stop_all_sounds()
    for value11 in tiles.get_tiles_by_type(assets.tile("""
        myTile12
        """)):
        tiles.set_tile_at(value11, assets.tile("""
            Underwater
            """))
    animation.run_image_animation(DoubleJump,
        [img("""
                9 9 9 9 9 b b b b b b 9 9 9 9 9
                9 9 9 b b 9 9 9 9 9 9 b b 9 9 9
                9 9 b b 9 9 9 9 9 9 9 9 b b 9 9
                9 b b 9 d 9 9 9 9 9 9 9 9 b b 9
                9 b 9 d 9 9 9 9 9 1 1 1 9 9 b 9
                b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                9 b 5 3 3 3 d 9 9 9 9 d d 5 b 9
                9 b d 5 3 3 3 3 3 3 3 d 5 b b 9
                9 9 b d 5 d 3 3 3 3 5 5 b b 9 9
                9 9 9 b b 5 5 5 5 5 5 b b 9 9 9
                9 9 9 9 9 b b b b b b 9 9 9 9 9
                """),
            img("""
                9 9 9 9 9 9 9 9 b b 9 9 9 9 9 9
                9 9 9 9 9 9 9 b 9 1 b 9 9 9 9 9
                9 9 b b 9 9 9 b 9 9 b 9 9 9 9 9
                9 b 9 1 b 9 9 b b b 9 9 b b b 9
                9 b 3 9 b 9 b b b b 9 b 9 9 1 b
                9 b b b b b 9 9 1 1 b b 3 9 9 b
                9 9 9 9 b 9 d 9 1 1 b b b b b 9
                9 9 9 9 b 5 3 9 9 9 b 9 9 9 9 9
                9 9 b b b 5 3 3 d 9 b 9 9 9 9 9
                9 b 5 1 b b 5 5 9 b b b b 9 9 9
                9 b 5 5 b b b b b b 3 9 9 3 9 9
                9 b b b b b b b 9 b 9 1 1 9 b 9
                9 9 9 b 5 5 1 b 9 b 9 1 1 9 b 9
                9 9 9 b 5 5 5 b 9 b 3 9 9 3 b 9
                9 9 9 9 b b b 9 9 9 b b b b 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                """),
            img("""
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 b b 9 9 9 9 9
                9 9 9 9 9 9 9 9 b 9 1 b 9 9 9 9
                9 9 9 b b b b b b 9 9 b 9 9 9 9
                9 9 b 9 9 d 9 9 1 1 d b b b b 9
                9 9 9 b d 9 9 9 1 1 9 9 d 9 1 b
                9 9 b 9 d 9 9 9 9 9 9 9 d 9 9 b
                9 9 b 9 3 3 9 9 9 9 9 d b b b 9
                9 b 5 d 9 3 3 3 d d b b b b 9 9
                b 5 5 5 b b b b b b b 9 9 1 b 9
                b 5 5 b 9 9 9 9 9 9 b 3 9 9 b 9
                9 b b 9 9 9 9 9 9 9 9 b b b 9 9
                """),
            img("""
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 1 1 1 9 9 9
                9 9 9 1 1 9 9 9 9 9 1 1 1 9 9 9
                9 9 9 1 1 9 9 1 1 9 1 1 1 9 9 9
                9 9 9 9 9 9 9 1 1 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 1 9 9 9 9
                9 9 9 9 1 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
                """)],
        150,
        False)
    sprites.destroy(DoubleJump)
    PowerUpAsk = game.ask_for_number("Claim 10 seconds back! Select 1!", 1)
    if PowerUpAsk == 1:
        info.change_countdown_by(10)
    else:
        info.change_countdown_by(-10)
    music.play(music.string_playable("A F E F D G E F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
        """),
    on_overlap_tile5)

def on_overlap_tile6(sprite3, location3):
    global ChoosePowerUp
    PowerSelection = 0
    music.stop_all_sounds()
    game.splash("You have completed DAY 1, get some rest for the next day.")
    game.splash("Its a little rocky down here, you will need to jump over obstacles!")
    ChoosePowerUp = game.ask_for_number("Great " + playerName + ". Choose 1. 2x Speed, 2. 2x Jump",
        1)
    if PowerSelection == 1:
        controller.move_sprite(Explorer, 200, 0)
        controller.move_sprite(Mermaid, 200, 0)
        controller.move_sprite(Cat, 200, 0)
    elif PowerSelection == 2:
        Explorer.ay = 112.5
        Mermaid.ay = 112.5
        Cat.ay = 112.5
    sprites.destroy(Coin1)
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile9
        """)):
        tiles.set_tile_at(value3, assets.tile("""
            Underwater
            """))
    game.splash("Lets make it to DAY 3!")
    music.play(music.string_playable("C5 B A G A B C5 - ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
        """),
    on_overlap_tile6)

def SelectAvatar():
    global selectedAvatar
    if avatarChoice == 1:
        selectedAvatar = "Explorer"
        spawnexplorer()
    elif avatarChoice == 2:
        selectedAvatar = "Mermaid"
        spawnmermaid()
    else:
        selectedAvatar = "Cat"
        spawncat()
def SpawnDoubleJump():
    global DoubleJump
    for value9 in tiles.get_tiles_by_type(assets.tile("""
        myTile12
        """)):
        DoubleJump = sprites.create(img("""
                . . . . . b b b b b b . . . . .
                . . . b b 9 9 9 9 9 9 b b . . .
                . . b b 9 9 9 9 9 9 9 9 b b . .
                . b b 9 d 9 9 9 9 9 9 9 9 b b .
                . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                . b d 5 3 3 3 3 3 3 3 d 5 b b .
                . . b d 5 d 3 3 3 3 5 5 b b . .
                . . . b b 5 5 5 5 5 5 b b . . .
                . . . . . b b b b b b . . . . .
                """),
            SpriteKind.food)
        tiles.place_on_tile(DoubleJump, value9)
        DoubleJump.scale = 0.75
def SpawnCoin4():
    global coin4
    for value10 in tiles.get_tiles_by_type(assets.tile("""
        myTile13
        """)):
        coin4 = sprites.create(img("""
                . . b b b b . .
                . b 5 5 5 5 b .
                b 5 d 3 3 d 5 b
                b 5 3 5 5 1 5 b
                c 5 3 5 5 1 d c
                c d d 1 1 d d c
                . f d d d d f .
                . . f f f f . .
                """),
            SpriteKind.food)
        tiles.place_on_tile(coin4, value10)
        animation.run_image_animation(coin3,
            [img("""
                    9 9 b b b b 9 9
                    9 b 5 5 5 5 b 9
                    b 5 d 3 3 d 5 b
                    b 5 3 5 5 1 5 b
                    c 5 3 5 5 1 d c
                    c d d 1 1 d d c
                    9 f d d d d f 9
                    9 9 f f f f 9 9
                    """),
                img("""
                    9 9 b b b 9 9 9
                    9 b 5 5 5 b 9 9
                    b 5 d 3 d 5 b 9
                    b 5 3 5 1 5 b 9
                    c 5 3 5 1 d c 9
                    c 5 d 1 d d c 9
                    9 f d d d f 9 9
                    9 9 f f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 d 1 5 b 9
                    9 b 5 3 1 5 b 9
                    9 c 5 3 1 d c 9
                    9 c 5 1 d d c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b 1 1 b 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b d d b 9 9
                    9 9 c d d c 9 9
                    9 9 c 3 3 c 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 1 d 5 b 9
                    9 b 5 1 3 5 b 9
                    9 c d 1 3 5 c 9
                    9 c d d 1 5 c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b b 9 9
                    9 9 b 5 5 5 b 9
                    9 b 5 d 3 d 5 b
                    9 b 5 1 5 3 5 b
                    9 c d 1 5 3 5 c
                    9 c d d 1 d 5 c
                    9 9 f d d d f 9
                    9 9 9 f f f 9 9
                    """)],
            150,
            True)
        coin4.scale = 1.5

def on_overlap_tile7(sprite422, location422):
    music.stop_all_sounds()
    game.splash("DAY 5!")
    game.splash("The Last Jump!")
    game.splash("Are you ready?")
    for value52 in tiles.get_tiles_by_type(assets.tile("""
        myTile13
        """)):
        tiles.set_tile_at(value52, assets.tile("""
            Underwater
            """))
    sprites.destroy(coin4)
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile13
        """),
    on_overlap_tile7)

def SpawnCoin2():
    global Coin2
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        myTile10
        """)):
        Coin2 = sprites.create(img("""
                . . b b b b . .
                . b 5 5 5 5 b .
                b 5 d 3 3 d 5 b
                b 5 3 5 5 1 5 b
                c 5 3 5 5 1 d c
                c d d 1 1 d d c
                . f d d d d f .
                . . f f f f . .
                """),
            SpriteKind.food)
        tiles.place_on_tile(Coin2, value8)
        animation.run_image_animation(Coin2,
            [img("""
                    9 9 b b b b 9 9
                    9 b 5 5 5 5 b 9
                    b 5 d 3 3 d 5 b
                    b 5 3 5 5 1 5 b
                    c 5 3 5 5 1 d c
                    c d d 1 1 d d c
                    9 f d d d d f 9
                    9 9 f f f f 9 9
                    """),
                img("""
                    9 9 b b b 9 9 9
                    9 b 5 5 5 b 9 9
                    b 5 d 3 d 5 b 9
                    b 5 3 5 1 5 b 9
                    c 5 3 5 1 d c 9
                    c 5 d 1 d d c 9
                    9 f d d d f 9 9
                    9 9 f f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 d 1 5 b 9
                    9 b 5 3 1 5 b 9
                    9 c 5 3 1 d c 9
                    9 c 5 1 d d c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b 1 1 b 9 9
                    9 9 b 5 5 b 9 9
                    9 9 b d d b 9 9
                    9 9 c d d c 9 9
                    9 9 c 3 3 c 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b 9 9 9
                    9 9 b 5 5 b 9 9
                    9 b 5 1 d 5 b 9
                    9 b 5 1 3 5 b 9
                    9 c d 1 3 5 c 9
                    9 c d d 1 5 c 9
                    9 9 f d d f 9 9
                    9 9 9 f f 9 9 9
                    """),
                img("""
                    9 9 9 b b b 9 9
                    9 9 b 5 5 5 b 9
                    9 b 5 d 3 d 5 b
                    9 b 5 1 5 3 5 b
                    9 c d 1 5 3 5 c
                    9 c d d 1 d 5 c
                    9 9 f d d d f 9
                    9 9 9 f f f 9 9
                    """)],
            150,
            True)
        Coin2.scale = 1.5

def on_overlap_tile8(sprite232, location222):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile8)

coin4: Sprite = None
ChoosePowerUp = 0
PowerUpAsk = 0
DoubleJump: Sprite = None
Coin2: Sprite = None
Coin1: Sprite = None
musicChoice = ""
Cat: Sprite = None
selectedAvatar = ""
Mermaid: Sprite = None
SpeedBoost: Sprite = None
numberofjumps = 0
coin3: Sprite = None
Explorer: Sprite = None
musicChoiceNumber = 0
avatarChoice = 0
playerName = ""
LightBlue: Sprite = None
Guard: Sprite = None
Guard = None
tiles.set_current_tilemap(tilemap("""
    MainMap
    """))
SpawnVariables()
tiles.place_on_random_tile(LightBlue, assets.tile("""
    myTile
    """))
SpawnCoin1()
SpawnCoin2()
SpawnCoin3()
SpawnCoin4()
SpawnDoubleJump()
game.splash("Welcome to Underwater Trail!")
game.splash("You are stuck underwater and need to escape by getting past obstacles in the clear water to find your way out.")
playerName = game.ask_for_string("What is your name?")
game.splash("Perfect, " + playerName + ".")
avatarChoice = game.ask_for_number("1. Explorer 2. Mermaid 3. Shark", 1)
SelectAvatar()
musicChoiceNumber = game.ask_for_number("Okay " + playerName + ". Music: 1. Sitka 2. Paris 3. Tokyo",
    1)
game.splash("You have 20 seconds to reach the end.")
game.splash("Ready?")
selectMusic()
characterMovement()
SpawnEnemy()
info.start_countdown(20)