def on_overlap_tile(sprite, location):
    sprites.destroy(mySprite)
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    info.stop_countdown()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_up_pressed():
    global spritey
    spritey += -10
    mySprite.set_position(spritex, spritey)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global mySprite2
    mySprite2 = sprites.create(assets.image("""
        myImage1
    """), SpriteKind.projectile)
    mySprite2.set_position(spritex, spritey)
    mySprite2.set_velocity(50, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_left_pressed():
    global spritex
    spritex += -10
    mySprite.set_position(spritex, spritey)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    game.reset()
info.on_countdown_end(on_countdown_end)

def on_overlap_tile2(sprite2, location2):
    game.reset()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles10,
    on_overlap_tile2)

def on_right_pressed():
    global spritex
    spritex += 10
    mySprite.set_position(spritex, spritey)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite42, otherSprite2):
    sprites.destroy(myEnemy, effects.spray, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_down_pressed():
    global spritey
    spritey += 10
    mySprite.set_position(spritex, spritey)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap2(sprite4, otherSprite):
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_overlap_tile3(sprite3, location3):
    global enemyspeed
    enemyy = 0
    enemyspeed = -1 * enemyspeed
    myEnemy.set_velocity(enemyspeed, enemyy)
scene.on_overlap_tile(SpriteKind.enemy,
    sprites.builtin.forest_tiles10,
    on_overlap_tile3)

mySprite2: Sprite = None
enemyspeed = 0
myEnemy: Sprite = None
spritey = 0
spritex = 0
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
spritex = 10
spritey = 72
mySprite.set_position(spritex, spritey)
tiles.set_current_tilemap(tilemap("""
    level8
"""))
myEnemy = sprites.create(assets.image("""
    myenemy
"""), SpriteKind.enemy)
myEnemy.set_position(141, 105)
enemyspeed = -10
myEnemy.set_velocity(enemyspeed, 0)
info.start_countdown(30)