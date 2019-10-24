import os, re, bpy, glob, linecache

importDir = str(os.path.dirname(os.path.realpath(__file__)))
os.chdir(importDir)

for file in glob.glob('*.qc'):
    filenoext = os.path.splitext(file)[0]
    
    if os.path.exists(filenoext + '_exported.fbx') == True:
        print('.fbx Already Exists!')
    else:
        bpy.ops.import_scene.smd(filepath=file, filter_glob=('*.qc'), doAnim=False)   
        bpy.context.object.name = 'v_weapon_root'
        bpy.context.scene.render.fps = 30
        bpy.ops.export_scene.fbx(filepath=filenoext + '_exported.fbx', bake_anim=False, global_scale=0.01, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_simplify_factor=0, add_leaf_bones=False)

qc = filenoext + '.qc'
lines_formatted = []
lines_sequence = []
animation_smd = []
animation_fps = []


with open(qc, 'rt') as searchfile:
    lines = [ i for i in enumerate(searchfile, 1) ]
    for line in lines:
        line_formatted = str(line).replace('\\\\', '\\').strip('()').replace("'","").rstrip(r'\n').replace(r'\t', r'').split(', ')
        lines_formatted.append(line_formatted)
        for l in line_formatted:
            if 'sequence' in l:
                lines_sequence.append(line[0])
            if 'animation' in l:
                animation_smd.append(line[1].split('"')[3])
                animation_fps.append(re.sub(r"\D", "", (linecache.getline(qc,line[0] + 1))))
                
    # print(lines_formatted[-1][0])
    print(animation_fps)

for smd in enumerate(animation_smd):
    importDirAnims = importDir + '\\' + smd[1].replace('"','')
    importDirAnims_noext = os.path.splitext(importDirAnims)[0]
    print(importDirAnims)
    print(smd[1])
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.smd(filepath=importDirAnims, filter_glob=('*.smd'), doAnim=True)
    bpy.context.object.name = 'v_weapon_root'
    bpy.context.scene.render.fps = int(animation_fps[smd[0]])
    bpy.ops.export_scene.fbx(filepath=importDirAnims_noext + '_exported.fbx', bake_anim=True, global_scale=0.01, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_simplify_factor=0, add_leaf_bones=False)    


line_last = int(lines_formatted[-1][0])
lines_sequence[-1] = line_last
sequence_fps = []
sequence_smd = []


######
x = -1
while x < (len(lines_sequence)-1):
    for i in range(lines_sequence[x], lines_sequence[x+1], 1):
        # print(i)
        for l in lines_formatted[i]:
            if 'fps' in l:
                sequence_fps.append(re.sub(r'\D', '', l))
                # print(sequence_fps)
            if '.smd' in l:
                sequence_smd.append(l)

    x = x + 1



# print(sequence_fps)
for smd in enumerate(sequence_smd):
    importDirSequence = importDir + '\\' + smd[1].replace('"','')
    importDirSequence_noext = os.path.splitext(importDirSequence)[0] 
    bpy.ops.wm.read_homefile(use_empty=True)
    # print(importDirSequence)
    bpy.ops.import_scene.smd(filepath=importDirSequence, filter_glob=('*.smd'), doAnim=True)
    bpy.context.object.name = 'v_weapon_root'
    bpy.context.scene.render.fps = int(sequence_fps[smd[0]])
    bpy.ops.export_scene.fbx(filepath=importDirSequence_noext + '_exported.fbx', bake_anim=True, global_scale=0.01, bake_anim_use_nla_strips=False, bake_anim_use_all_actions=False, bake_anim_simplify_factor=0, add_leaf_bones=False)