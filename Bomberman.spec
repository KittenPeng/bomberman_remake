# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['grid_game.py'],
    pathex=[],
    binaries=[],
    datas=[('Bomb Bounce.wav', '.'), ('Bomb Explodes.wav', '.'), ('Hurry Up 1.wav', '.'), ('Hurry Up 2.wav', '.'), ('Item Bounce.wav', '.'), ('Item Get.wav', '.'), ('Kick Voice.wav', '.'), ('Kick.wav', '.'), ('Pause Jingle.wav', '.'), ('Place Bomb.wav', '.'), ('Pressure Block.wav', '.'), ('Skull.wav', '.'), ('Throw.wav', '.'), ('debug_tile_raw.png', '.'), ('pause.png', '.'), ('Screenshot 2026-01-05 102131.png', '.'), ('SNES - Super Bomberman 2 - Battle Stages - Battle Stage 01.png', '.'), ('SNES - Super Bomberman 2 - Miscellaneous - Bombs.png', '.'), ('SNES - Super Bomberman 2 - Miscellaneous - Items.png', '.'), ('SNES - Super Bomberman 2 - Playable Characters - Bomberman.png', '.'), ('SNES - Super Bomberman 2 - Tilesets - Battle Game Tiles.png', '.'), ('test_block1.png', '.'), ('test_block2.png', '.'), ('test_block4.png', '.'), ('test_extract1.png', '.'), ('test_extract2.png', '.'), ('test_extract4.png', '.'), ('test_scaled.png', '.'), ('Super Bomberman 2 - Battle 1 (SNES OST).mp3', '.')],
    hiddenimports=['pygame', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Bomberman',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
