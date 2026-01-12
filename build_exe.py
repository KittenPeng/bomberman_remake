"""
Build script to create an executable from grid_game.py
"""
import PyInstaller.__main__
import os

# Get all data files that need to be included
data_files = []

# Add all .wav files
wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]
for wav in wav_files:
    data_files.append(f'{wav};.')

# Add all .png files
png_files = [f for f in os.listdir('.') if f.endswith('.png')]
for png in png_files:
    data_files.append(f'{png};.')

# Add .mp3 file if it exists
mp3_file = 'Super Bomberman 2 - Battle 1 (SNES OST).mp3'
if os.path.exists(mp3_file):
    data_files.append(f'{mp3_file};.')

# Build PyInstaller arguments
args = [
    'grid_game.py',
    '--onefile',  # Create a single executable file
    '--name=Bomberman',  # Name of the executable
    '--console',  # Keep console window for debugging (change to --noconsole if you want no console)
]

# Add all data files
for data_file in data_files:
    args.extend(['--add-data', data_file])

# Add hidden imports if needed
args.extend(['--hidden-import', 'pygame'])
args.extend(['--hidden-import', 'numpy'])

print("Building executable...")
print("This may take a few minutes...")
print(f"Including {len(data_files)} data files...")
PyInstaller.__main__.run(args)
print("\nBuild complete! Check the 'dist' folder for Bomberman.exe")
