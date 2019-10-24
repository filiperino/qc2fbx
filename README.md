# qc2fbx

features:
- scales down to 0.01
- as of now changes root bone name to 'v_weapon_root'
- exports all animations without leaf bones and the proper framerate
- mesh export settings adjusted to have no warnings about smoothing groups later

prerequisites:

blender 2.8 (https://www.blender.org/download/)

python 3.7.0 32-bit (https://www.python.org/downloads/release/python-370/)

usage:
1. clone repo or download as .zip
2. copy s.py and run.bat wherever you have the .qc files and _anims 
3. run "run.bat" and wait for it to finish, press enter to quit the cmd

if your blender .exe isn't on C: then change the path accordingly in the run.bat file.


to-do:
- run tests on different source engine games to make it game-independent
- make it recursive and more user-friendly
- fix tec-9 and ssg08 skeleton to make it compatible with other v_weapons

this wasn't supposed to be public but hey
