function SpawnExplorer() {
    
    for (let value of tiles.getTilesByType(assets.tile`
        PlayerSpawn
        `)) {
        Explorer = sprites.create(img`
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
        tiles.placeOnTile(Explorer, value)
        scene.cameraFollowSprite(Explorer)
    }
}

function BoostFunction() {
    
    Boost = sprites.create(img`
            . . . . . . . . . . . . . . . .
            . . . . . . 6 6 6 6 . . . . . .
            . . . . 6 6 6 5 5 6 6 6 . . . .
            . . . 7 7 7 7 6 6 6 6 6 6 . . .
            . . 6 7 7 7 7 8 8 8 1 1 6 6 . .
            . . 7 7 7 7 7 8 8 8 1 1 5 6 . .
            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 .
            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 .
            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 .
            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 .
            . . 6 8 7 7 8 6 6 6 6 6 8 6 . .
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . .
            . . . 6 8 8 8 8 8 8 8 8 6 . . .
            . . . . 6 6 8 8 8 8 6 6 . . . .
            . . . . . . 6 6 6 6 . . . . . .
            . . . . . . . . . . . . . . . .
            `, SpriteKind.Player)
}

let Boost : Sprite = null
let Explorer : Sprite = null
tiles.setCurrentTilemap(tilemap`MainMap`)
SpawnExplorer()
BoostFunction()
