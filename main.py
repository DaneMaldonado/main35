def SpawnExplorer():
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
def spawn_mermaid():
    global mySprite
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        transparency16
        """)):
        mySprite = sprites.create(img("""
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
        tiles.place_on_tile(Explorer, value2)
        scene.camera_follow_sprite(Explorer)
def spawn_shark():
    global mySprite
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        transparency16
        """)):
        mySprite = sprites.create(img("""
                .............ccfff..............
                ...........ccddbcf..............
                ..........ccddbbf...............
                ..........fccbbcf...............
                .....fffffccccccff.........ccc..
                ...ffbbbbbbbcbbbbcfff....ccbbc..
                ..fbbbbbbbbcbcbbbbcccff.cdbbc...
                ffbbbbbbffbbcbcbbbcccccfcdbbf...
                fbcbbb11ff1bcbbbbbcccccffbbf....
                fbbb11111111bbbbbcccccccbbcf....
                .fb11133cc11bbbbcccccccccccf....
                ..fccc31c111bbbcccccbdbffbbcf...
                ...fc13c111cbbbfcddddcc..fbbf...
                ....fccc111fbdbbccdcc.....fbbf..
                ........ccccfcdbbcc........fff..
                .............fffff..............
                """),
            SpriteKind.player)
        tiles.place_on_tile(Explorer, value3)
        scene.camera_follow_sprite(Explorer)
mySprite: Sprite = None
Explorer: Sprite = None
musicChoice = ""
selectedAvatar = ""
tiles.set_current_tilemap(tilemap("""
    MainMap
    """))
# Declare globally
# Level 0 - Introduction
game.splash("Welcome to Underwater Trail!")
playerName = game.ask_for_string("What is your name?")
game.splash("Perfect, " + playerName)
# Avatar Selection
avatarChoice = game.ask_for_number("Perfect " + playerName + """
    , select an avatar:
    1. Explorer
    2. Mermaid
    3. Shark
    """)
# Spawn selected avatar
if avatarChoice == 1:
    selectedAvatar = "Explorer"
    SpawnExplorer()
elif avatarChoice == 2:
    selectedAvatar = "Mermaid"
    spawn_mermaid()
else:
    selectedAvatar = "Shark"
    spawn_shark()
# Music Selection
musicChoiceNum = game.ask_for_number("Okay " + playerName + """
    , choose music:
    1. Sitka
    2. Paris
    3. Tokyo
    """)
if musicChoiceNum == 1:
    musicChoice = "Sitka"
    music.play_melody("C5 B A G A B C5 - ", 120)
elif musicChoiceNum == 2:
    musicChoice = "Paris"
    music.play_melody("E B C5 A B G A F ", 120)
else:
    musicChoice = "Tokyo"
    music.play_melody("G A G B A G F E ", 120)

def enable_movement_and_physics(character: Sprite):
    controller.move_sprite(character, 100, 0)  # Only allow horizontal movement
    character.ay = 300  # Gravity strength
    character.set_flag(SpriteFlag.STAY_IN_SCREEN, True)  # Prevent falling off screen

    def on_jump_pressed():
        if character.is_hitting_tile(CollisionDirection.BOTTOM):
            character.vy = -150  # Jump velocity (negative goes up)

    controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump_pressed)

# Apply to selected avatar
if selectedAvatar == "Explorer":
    enable_movement_and_physics(Explorer)
elif selectedAvatar == "Mermaid":
    enable_movement_and_physics(mySprite)
elif selectedAvatar == "Shark":
    enable_movement_and_physics(mySprite)