scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.gameOver(false)
})
function spawn_explorer () {
    for (let value of tiles.getTilesByType(assets.tile`myTile`)) {
        Explorer = sprites.create(img`
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
            `, SpriteKind.Player)
        tiles.placeOnTile(Explorer, value)
        scene.cameraFollowSprite(Explorer)
    }
}
function SpawnCoin3 () {
    for (let value43 of tiles.getTilesByType(assets.tile`myTile11`)) {
        coin3 = sprites.create(img`
            . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . . 
            `, SpriteKind.Food)
        tiles.placeOnTile(coin3, value43)
        animation.runImageAnimation(
        coin3,
        [img`
            9 9 b b b b 9 9 
            9 b 5 5 5 5 b 9 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            9 f d d d d f 9 
            9 9 f f f f 9 9 
            `,img`
            9 9 b b b 9 9 9 
            9 b 5 5 5 b 9 9 
            b 5 d 3 d 5 b 9 
            b 5 3 5 1 5 b 9 
            c 5 3 5 1 d c 9 
            c 5 d 1 d d c 9 
            9 f d d d f 9 9 
            9 9 f f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 d 1 5 b 9 
            9 b 5 3 1 5 b 9 
            9 c 5 3 1 d c 9 
            9 c 5 1 d d c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b 1 1 b 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b d d b 9 9 
            9 9 c d d c 9 9 
            9 9 c 3 3 c 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 1 d 5 b 9 
            9 b 5 1 3 5 b 9 
            9 c d 1 3 5 c 9 
            9 c d d 1 5 c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b b 9 9 
            9 9 b 5 5 5 b 9 
            9 b 5 d 3 d 5 b 
            9 b 5 1 5 3 5 b 
            9 c d 1 5 3 5 c 
            9 c d d 1 d 5 c 
            9 9 f d d d f 9 
            9 9 9 f f f 9 9 
            `],
        150,
        true
        )
        coin3.scale = 1.5
    }
}
function movement (character: Sprite) {
    controller.moveSprite(character, 100, 0)
    character.ay = 225
    character.setFlag(SpriteFlag.StayInScreen, true)
    controller.A.onEvent(ControllerButtonEvent.Pressed, function on_jump_pressed() {
        if (character.isHittingTile(CollisionDirection.Bottom)) {
            character.vy = -150
        }
        
    })
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile11`, function (sprite4, location4) {
    music.stopAllSounds()
    game.splash("You have made it to DAY 4!")
    game.splash("Its very high up here, but thats okay.")
    game.splash("Land on the pad below!")
    game.splash("Are you ready?")
    for (let value33 of tiles.getTilesByType(assets.tile`myTile11`)) {
        tiles.setTileAt(value33, assets.tile`Underwater`)
    }
    sprites.destroy(coin3)
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.LoopingInBackground)
})
function spawn_mermaid () {
    for (let value2 of tiles.getTilesByType(assets.tile`myTile`)) {
        Mermaid = sprites.create(img`
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
            `, SpriteKind.Player)
        tiles.placeOnTile(Mermaid, value2)
        scene.cameraFollowSprite(Mermaid)
    }
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (selectedAvatar == "Cat") {
        animation.runImageAnimation(
        Cat,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    } else if (selectedAvatar == "Mermaid") {
        animation.runImageAnimation(
        Mermaid,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    } else if (selectedAvatar == "Explorer") {
        animation.runImageAnimation(
        Explorer,
        [img`
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
            `,img`
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
            `],
        500,
        false
        )
    }
})
function spawn_cat () {
    for (let value32 of tiles.getTilesByType(assets.tile`myTile`)) {
        Cat = sprites.create(img`
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
            `, SpriteKind.Player)
        tiles.placeOnTile(Cat, value32)
        scene.cameraFollowSprite(Cat)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite23, location22) {
    game.gameOver(false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (selectedAvatar == "Cat") {
        animation.runImageAnimation(
        Cat,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    } else if (selectedAvatar == "Mermaid") {
        animation.runImageAnimation(
        Mermaid,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    } else if (selectedAvatar == "Explorer") {
        animation.runImageAnimation(
        Explorer,
        [img`
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
            `,img`
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
            `],
        500,
        false
        )
    }
})
function SpawnCoin1 () {
    for (let value4 of tiles.getTilesByType(assets.tile`myTile9`)) {
        Coin1 = sprites.create(img`
            . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . . 
            `, SpriteKind.Food)
        tiles.placeOnTile(Coin1, value4)
        animation.runImageAnimation(
        Coin1,
        [img`
            9 9 b b b b 9 9 
            9 b 5 5 5 5 b 9 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            9 f d d d d f 9 
            9 9 f f f f 9 9 
            `,img`
            9 9 b b b 9 9 9 
            9 b 5 5 5 b 9 9 
            b 5 d 3 d 5 b 9 
            b 5 3 5 1 5 b 9 
            c 5 3 5 1 d c 9 
            c 5 d 1 d d c 9 
            9 f d d d f 9 9 
            9 9 f f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 d 1 5 b 9 
            9 b 5 3 1 5 b 9 
            9 c 5 3 1 d c 9 
            9 c 5 1 d d c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b 1 1 b 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b d d b 9 9 
            9 9 c d d c 9 9 
            9 9 c 3 3 c 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 1 d 5 b 9 
            9 b 5 1 3 5 b 9 
            9 c d 1 3 5 c 9 
            9 c d d 1 5 c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b b 9 9 
            9 9 b 5 5 5 b 9 
            9 b 5 d 3 d 5 b 
            9 b 5 1 5 3 5 b 
            9 c d 1 5 3 5 c 
            9 c d d 1 d 5 c 
            9 9 f d d d f 9 
            9 9 9 f f f 9 9 
            `],
        150,
        true
        )
        Coin1.scale = 1.5
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile10`, function (sprite42, location42) {
    music.stopAllSounds()
    game.splash("DAY 3")
    game.splash("Hold tight, you are almost there!")
    game.splash("It gets a little high up here but we can handle it!")
    game.splash("Lets do it!")
    for (let value332 of tiles.getTilesByType(assets.tile`myTile10`)) {
        tiles.setTileAt(value332, assets.tile`Underwater`)
    }
    sprites.destroy(Coin2)
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.LoopingInBackground)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile12`, function (sprite2, location2) {
    music.stopAllSounds()
    for (let value42 of tiles.getTilesByType(assets.tile`myTile12`)) {
        tiles.setTileAt(value42, assets.tile`Underwater`)
    }
    animation.runImageAnimation(
    DoubleJump,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    150,
    false
    )
    sprites.destroy(DoubleJump)
    PowerUpAsk = game.askForNumber("Claim 10 seconds back! Select 1 Quick!", 1)
    if (PowerUpAsk == 1) {
        info.changeCountdownBy(10)
    } else {
        info.changeCountdownBy(-10)
    }
    music.play(music.stringPlayable("A F E F D G E F ", 120), music.PlaybackMode.LoopingInBackground)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile9`, function (sprite3, location3) {
    let PowerSelection = 0
    music.stopAllSounds()
    game.splash("You have completed DAY 1, get some rest for the next day.")
    game.splash("Its a little rocky down here, you will need to jump over obstacles!")
    ChoosePowerUp = game.askForNumber("Great " + playerName + ". Choose 1. 2x Speed, 2. 2x Jump", 1)
    sprites.destroy(Coin1)
    if (PowerSelection == 1) {
        controller.moveSprite(Explorer, 200, 0)
        controller.moveSprite(Mermaid, 200, 0)
        controller.moveSprite(Cat, 200, 0)
    } else if (PowerSelection == 2) {
        Explorer.ay = 112.5
        Mermaid.ay = 112.5
        Cat.ay = 112.5
    }
    sprites.destroy(Coin1)
    for (let value3 of tiles.getTilesByType(assets.tile`myTile9`)) {
        tiles.setTileAt(value3, assets.tile`Underwater`)
    }
    game.splash("Lets make it to DAY 3!")
    music.play(music.stringPlayable("C5 B A G A B C5 - ", 120), music.PlaybackMode.LoopingInBackground)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile15`, function (sprite23, location22) {
    game.gameOver(false)
})
function SpawnDoubleJump () {
    for (let value422 of tiles.getTilesByType(assets.tile`myTile12`)) {
        DoubleJump = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(DoubleJump, value422)
        DoubleJump.scale = 0.75
    }
}
function SpawnCoin4 () {
    for (let value432 of tiles.getTilesByType(assets.tile`myTile13`)) {
        coin4 = sprites.create(img`
            . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . . 
            `, SpriteKind.Food)
        tiles.placeOnTile(coin4, value432)
        animation.runImageAnimation(
        coin3,
        [img`
            9 9 b b b b 9 9 
            9 b 5 5 5 5 b 9 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            9 f d d d d f 9 
            9 9 f f f f 9 9 
            `,img`
            9 9 b b b 9 9 9 
            9 b 5 5 5 b 9 9 
            b 5 d 3 d 5 b 9 
            b 5 3 5 1 5 b 9 
            c 5 3 5 1 d c 9 
            c 5 d 1 d d c 9 
            9 f d d d f 9 9 
            9 9 f f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 d 1 5 b 9 
            9 b 5 3 1 5 b 9 
            9 c 5 3 1 d c 9 
            9 c 5 1 d d c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b 1 1 b 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b d d b 9 9 
            9 9 c d d c 9 9 
            9 9 c 3 3 c 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 1 d 5 b 9 
            9 b 5 1 3 5 b 9 
            9 c d 1 3 5 c 9 
            9 c d d 1 5 c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b b 9 9 
            9 9 b 5 5 5 b 9 
            9 b 5 d 3 d 5 b 
            9 b 5 1 5 3 5 b 
            9 c d 1 5 3 5 c 
            9 c d d 1 d 5 c 
            9 9 f d d d f 9 
            9 9 9 f f f 9 9 
            `],
        150,
        true
        )
        coin4.scale = 1.5
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile13`, function (sprite422, location422) {
    music.stopAllSounds()
    game.splash("DAY 5!")
    game.splash("The Last Jump!")
    game.splash("Are you ready?")
    for (let value3322 of tiles.getTilesByType(assets.tile`myTile13`)) {
        tiles.setTileAt(value3322, assets.tile`Underwater`)
    }
    sprites.destroy(coin4)
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.LoopingInBackground)
})
function SpawnCoin2 () {
    for (let value423 of tiles.getTilesByType(assets.tile`myTile10`)) {
        Coin2 = sprites.create(img`
            . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . . 
            `, SpriteKind.Food)
        tiles.placeOnTile(Coin2, value423)
        animation.runImageAnimation(
        Coin2,
        [img`
            9 9 b b b b 9 9 
            9 b 5 5 5 5 b 9 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            9 f d d d d f 9 
            9 9 f f f f 9 9 
            `,img`
            9 9 b b b 9 9 9 
            9 b 5 5 5 b 9 9 
            b 5 d 3 d 5 b 9 
            b 5 3 5 1 5 b 9 
            c 5 3 5 1 d c 9 
            c 5 d 1 d d c 9 
            9 f d d d f 9 9 
            9 9 f f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 d 1 5 b 9 
            9 b 5 3 1 5 b 9 
            9 c 5 3 1 d c 9 
            9 c 5 1 d d c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b 1 1 b 9 9 
            9 9 b 5 5 b 9 9 
            9 9 b d d b 9 9 
            9 9 c d d c 9 9 
            9 9 c 3 3 c 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b 9 9 9 
            9 9 b 5 5 b 9 9 
            9 b 5 1 d 5 b 9 
            9 b 5 1 3 5 b 9 
            9 c d 1 3 5 c 9 
            9 c d d 1 5 c 9 
            9 9 f d d f 9 9 
            9 9 9 f f 9 9 9 
            `,img`
            9 9 9 b b b 9 9 
            9 9 b 5 5 5 b 9 
            9 b 5 d 3 d 5 b 
            9 b 5 1 5 3 5 b 
            9 c d 1 5 3 5 c 
            9 c d d 1 d 5 c 
            9 9 f d d d f 9 
            9 9 9 f f f 9 9 
            `],
        150,
        true
        )
        Coin2.scale = 1.5
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile8`, function (sprite4, location4) {
    music.stopAllSounds()
    game.splash("You have made it to the end!")
    game.splash("Congratulations!")
    music.play(music.stringPlayable("C5 B A G F E D C ", 480), music.PlaybackMode.LoopingInBackground)
    game.gameOver(true)
})
let coin4: Sprite = null
let ChoosePowerUp = 0
let PowerUpAsk = 0
let DoubleJump: Sprite = null
let Coin2: Sprite = null
let Coin1: Sprite = null
let coin3: Sprite = null
let Cat: Sprite = null
let Mermaid: Sprite = null
let Explorer: Sprite = null
let musicChoice = ""
let selectedAvatar = ""
let playerName = ""
let number_of_jumps = 0
tiles.setCurrentTilemap(tilemap`MainMap`)
let LightBlue = sprites.create(img`
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
    `, SpriteKind.Player)
let SpeedBoost = sprites.create(img`
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
    `, SpriteKind.Food)
tiles.placeOnRandomTile(LightBlue, assets.tile`myTile`)
SpawnCoin1()
SpawnCoin2()
SpawnCoin3()
SpawnCoin4()
SpawnDoubleJump()
game.splash("Welcome to Underwater Trail!")
game.splash("You are stuck underwater and need to escape by getting past obstacles in the clear water to find your way out.")
playerName = game.askForString("What is your name?")
game.splash("Perfect, " + playerName + ".")
let avatarChoice = game.askForNumber("1. Explorer 2. Mermaid 3. Shark", 1)
if (avatarChoice == 1) {
    selectedAvatar = "Explorer"
    spawn_explorer()
} else if (avatarChoice == 2) {
    selectedAvatar = "Mermaid"
    spawn_mermaid()
} else {
    selectedAvatar = "Cat"
    spawn_cat()
}
let musicChoiceNum = game.askForNumber("Okay " + playerName + ". Music: 1. Sitka 2. Paris 3. Tokyo", 1)
game.splash("You have 20 seconds to reach the end.")
game.splash("Ready?")
if (musicChoiceNum == 1) {
    musicChoice = "Sitka"
    music.play(music.stringPlayable("C5 B A G A B C5 - ", 120), music.PlaybackMode.LoopingInBackground)
} else if (musicChoiceNum == 2) {
    musicChoice = "Paris"
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.LoopingInBackground)
} else {
    musicChoice = "Tokyo"
    music.play(music.stringPlayable("G A G B A G F E ", 120), music.PlaybackMode.LoopingInBackground)
}
if (selectedAvatar == "Explorer") {
    movement(Explorer)
} else if (selectedAvatar == "Mermaid") {
    movement(Mermaid)
} else if (selectedAvatar == "Cat") {
    movement(Cat)
}
info.startCountdown(20)
