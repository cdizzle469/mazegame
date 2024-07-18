scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    sprites.destroy(mySprite)
    tiles.setCurrentTilemap(tilemap`level4`)
    info.stopCountdown()
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    spritey += -10
    mySprite.setPosition(spritex, spritey)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite2 = sprites.create(assets.image`myImage1`, SpriteKind.Projectile)
    mySprite2.setPosition(spritex, spritey)
    mySprite2.setVelocity(50, 0)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    spritex += -10
    mySprite.setPosition(spritex, spritey)
})
info.onCountdownEnd(function () {
    game.reset()
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles10, function (sprite2, location2) {
    game.reset()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    spritex += 10
    mySprite.setPosition(spritex, spritey)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite42, otherSprite2) {
    sprites.destroy(myEnemy, effects.spray, 500)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    spritey += 10
    mySprite.setPosition(spritex, spritey)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite4, otherSprite) {
    game.reset()
})
scene.onOverlapTile(SpriteKind.Enemy, sprites.builtin.forestTiles10, function (sprite3, location3) {
    let enemyy = 0
    enemyspeed = -1 * enemyspeed
    myEnemy.setVelocity(enemyspeed, enemyy)
})
let mySprite2: Sprite = null
let enemyspeed = 0
let myEnemy: Sprite = null
let spritey = 0
let spritex = 0
let mySprite: Sprite = null
mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
spritex = 10
spritey = 72
mySprite.setPosition(spritex, spritey)
tiles.setCurrentTilemap(tilemap`level8`)
myEnemy = sprites.create(assets.image`myenemy`, SpriteKind.Enemy)
myEnemy.setPosition(141, 105)
enemyspeed = -10
myEnemy.setVelocity(enemyspeed, 0)
info.startCountdown(30)
