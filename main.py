list2 = 0
def spawn_explorer():
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
def movement(character: Sprite):
    controller.move_sprite(character, 70, 0)
    character.ay = 210
    character.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    
    def on_jump_pressed():
        if character.is_hitting_tile(CollisionDirection.BOTTOM):
            character.vy = -150
    controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump_pressed)
    
def spawn_mermaid():
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

def on_overlap_tile(sprite, location):
    global ChoosePowerUp
    PowerSelection = 0
    game.splash("You have completed DAY 1, get some rest for the next day.")
    game.splash("Its a little rocky up here, you will need to jump over obstacles!")
    ChoosePowerUp = game.ask_for_number("Great " + playerName + "Choose (1. 2x Speed, 2. 2x Jump)")
    if PowerSelection == 1:
        controller.move_sprite(Explorer, 140, 0)
        controller.move_sprite(Mermaid, 140, 0)
        controller.move_sprite(Cat, 140, 0)
    elif PowerSelection == 2:
        Explorer.ay = 100
        Mermaid.ay = 100
        Cat.ay = 100
    sprites.destroy(Coin1)
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile9
        """)):
        tiles.set_tile_at(value3, assets.tile("""
            Underwater
            """))
    game.splash("Lets make it to DAY 2!")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
        """),
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    animation.run_image_animation(SpeedBoost,
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
sprites.on_overlap(SpriteKind.player, list2, on_on_overlap)

def spawn_cat():
    global Cat
    for value32 in tiles.get_tiles_by_type(assets.tile("""
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
        tiles.place_on_tile(Cat, value32)
        scene.camera_follow_sprite(Cat)

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
    for value4 in tiles.get_tiles_by_type(assets.tile("""
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
        tiles.place_on_tile(Coin1, value4)
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
Coin1: Sprite = None
ChoosePowerUp = 0
Cat: Sprite = None
Mermaid: Sprite = None
Explorer: Sprite = None
musicChoice = ""
selectedAvatar = ""
playerName = ""
SpeedBoost: Sprite = None
tiles.set_current_tilemap(tilemap("""MainMap"""))
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
tiles.place_on_random_tile(LightBlue, assets.tile("""
    myTile
    """))
for value5 in tiles.get_tiles_by_type(assets.tile("""
    myTile2
    """)):
    tiles.place_on_tile(None, value5)
SpawnCoin1()
game.splash("Welcome to Underwater Trail!")
game.splash("You are stuck underwater and need to escape by getting past obstacles in the clear water to find your way out.")
playerName = game.ask_for_string("What is your name?")
game.splash("Perfect, " + playerName)
avatarChoice = game.ask_for_number("Perfect " + playerName + """
    , select an avatar:
    1. Explorer
    2. Mermaid
    3. Shark
    """)
if avatarChoice == 1:
    selectedAvatar = "Explorer"
    spawn_explorer()
elif avatarChoice == 2:
    selectedAvatar = "Mermaid"
    spawn_mermaid()
else:
    selectedAvatar = "Cat"
    spawn_cat()
musicChoiceNum = game.ask_for_number("Okay " + playerName + """
    , choose music:
    1. Sitka
    2. Paris
    3. Tokyo
    """)
if musicChoiceNum == 1:
    musicChoice = "Sitka"
    music.play(music.string_playable("C5 B A G A B C5 - ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
elif musicChoiceNum == 2:
    musicChoice = "Paris"
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
else:
    musicChoice = "Tokyo"
    music.play(music.string_playable("G A G B A G F E ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
if selectedAvatar == "Explorer":
    movement(Explorer)
elif selectedAvatar == "Mermaid":
    movement(Mermaid)
elif selectedAvatar == "Cat":
    movement(Cat)