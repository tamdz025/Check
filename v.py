
import os; import re; import getopt; import random; import pyzstd; from xml.dom import minidom; from colorama import Fore, Style; import sys; import shutil; import zipfile; import uuid; from collections import Counter; import xml.etree.ElementTree as ET; from collections import defaultdict; import os as O, binascii as X; from pathlib import Path; from random import randint; import datetime; import time; import struct; import hashlib; import json

AutoMod = __file__

TimeUpdate = os.path.getmtime(AutoMod)
TimeLine = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(TimeUpdate))

# Đọc version từ file
try:
    folders = os.listdir("Resources")
    Ver = next((f for f in folders if os.path.isdir(os.path.join("Resources", f))), "Unknown")
except:
    Ver = "Unknown"
width = shutil.get_terminal_size(fallback=(80, 20)).columns

def print_centered(line):
    text_only = line.encode('ascii', 'ignore').decode() 
    spaces = max((width - len(text_only)) // 2, 0)
    print(" " * spaces + line)

# In banner
print("╭" + "─" * (width - 2) + "╮")
print_centered("  Ytb Tâm Mod AOV")
print_centered("  Tool: Mod Skin Engine")
print_centered(f"  Version : {Ver}")
print("╰" + "─" * (width - 2) + "╯")
print()

# In thêm info
print_centered(f" {TimeLine}")
print_centered(f" Python {os.sys.version.split()[0]}")

with open("ZSTD_DICT.xml", 'rb') as f:
    ZSTD_DICT = f.read()
ZSTD_LEVEL = 1

def giai(a):
    if os.path.isdir(a):
        for root, dirs, files in os.walk(a):
            if 'imprint' in root.lower():
                continue
            for file in files:
                file_path = os.path.join(root, file)
                _giaima_file(file_path)
    else:
        if 'imprint' not in a.lower():
            _giaima_file(a)

def _giaima_file(filepath):
    try:
        if not os.path.isfile(filepath):
            return

        with open(filepath, "rb") as f:
            input_blob = f.read()

        if b'"Jg' in input_blob or b"<?xml" in input_blob:
            return
        pos = input_blob.find(b"\x28\xb5\x2f\xfd")
        if pos != -1:
            anti_pos = input_blob.rfind(b'ANTI_DECOMP__')
            if anti_pos != -1:
                input_blob = input_blob[:anti_pos]

            if input_blob.startswith(b"\x22\x4a\x00\xef"):
                input_blob = input_blob[8:]

            input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]
            output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            with open(filepath, "wb") as f:
                f.write(output_blob)
        else:
            pass

    except Exception as e:
        pass

def enc(path1=None):
    if path1 is None: path1 = input("Nhập đường dẫn: ")
    for path in path1.split():
        files = []
        if os.path.isdir(path):
            for f1, _, f2 in os.walk(path):
                if 'imprint' not in f1.lower():
                    files += [os.path.join(f1, f) for f in f2 if f.endswith(('.xml','.bytes','.txt'))]
        elif os.path.isfile(path): files = [path]
        for file in files:
            try:
                with open(file, 'rb') as f: b = f.read()
                c = pyzstd.compress(b, 1, pyzstd.ZstdDict(ZSTD_DICT))
                if file.endswith('.xml'): c += b"ModByYtbTamPro"
                c += c[len(c)//2:len(c)//2+randint(3,4)]
                c = b'"J\x00\xef' + len(b).to_bytes(4,'little') + c
                with open(file, 'wb') as f: f.write(c)
            except Exception as e:
                pass
#print("\033[36m[III]. Chọn Chức Năng Fix Lag\n   [1].Fix Lag AssetRefs\n   [2].Fix Lag Born\n   [3].Không Fix Lag")
fixlag = '1'#input("\n>>> ")

def process_input_numbers(numbers):
    return numbers

if len(sys.argv) < 2:
    print("Vui lòng nhập user_id làm tham số dòng lệnh")
    sys.exit()

user_id = sys.argv[1]

# Tạo thư mục data/user_id nếu chưa có
base_path = f"./{user_id}"
os.makedirs(base_path, exist_ok=True)

# Đường dẫn file selected_skin_id.txt riêng theo user
selected_skin_path = os.path.join(base_path, "selected_skin_id.txt")

if not os.path.exists(selected_skin_path):
    print(f"File {selected_skin_path} không tồn tại")
    sys.exit()

with open(selected_skin_path, "r", encoding="utf-8") as f:
    numbers = [int(line.strip()) for line in f if line.strip().isdigit()]

results = process_input_numbers(numbers)
if results is None:
    sys.exit()
result_str = ' '.join(map(str, results))
IDD = result_str
IDMODSKIN = IDD.split()
IDMODSKIN1 = IDD.split()

if len(IDMODSKIN1) == 1:
    pass
    #sys.exit()

DANHSACH = IDD.split()

with open(f'Resources/{Ver}/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
    a = f.read()
if b'"J\x00' in a:
    giai(f'Resources/{Ver}/Databin/Client/Actor/heroSkin.bytes')

FILES_MAP = [
    f'Resources/{Ver}/Languages/VN_Garena_VN/languageMap.txt',
    f'Resources/{Ver}/Languages/VN_Garena_VN/languageMap_Newbie.txt',
    f'Resources/{Ver}/Languages/VN_Garena_VN/languageMap_WorldConcept.txt',
    f'Resources/{Ver}/Languages/VN_Garena_VN/languageMap_Xls.txt',
    f'Resources/{Ver}/Languages/VN_Garena_VN/lanMapIncremental.txt'
]

for mapp in FILES_MAP:
    with open(mapp, 'rb') as f:
        a = f.read()
    if b'"J\x00' in a:
        giai(mapp)

TENSKIN = []
for mapp in FILES_MAP:
    for i in DANHSACH:
        with open(mapp, 'rb') as f:
            rpl = f.read()
        with open(f'Resources/{Ver}/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
            RPL = f.read()

        i = int(i)
        IDFIND = RPL.find(i.to_bytes(4, 'little') + int(str(i)[:3]).to_bytes(4, 'little'))
        if IDFIND != -1:
            try:
                VT = RPL[IDFIND + 12:IDFIND + 31]
                VT1 = rpl.find(VT)
                VT2 = rpl.find(b'\r', VT1)
                VTR = rpl[VT1:VT2]

                VT = RPL[IDFIND + 40:IDFIND + 59]
                VT1 = rpl.find(VT)
                VT2 = rpl.find(b'\r', VT1)
                VTR_SKIN = rpl[VT1:VT2]

                A = VTR[22:]
                B = VTR_SKIN[22:]
                FolderMod = ((A + b' ' + B).decode(errors='ignore'))
                FolderMod = ''.join(char for char in FolderMod if char not in ['/', '\\', ':', '*', '?', '"', '<', '>', '|'])

                if FolderMod.strip() != '' and '[ex]' not in FolderMod:
                    TENSKIN.append(FolderMod)
            except:
                continue 
aaabbbcccnnn = ''
for FolderMod in TENSKIN:
    aaabbbcccnnn = FolderMod
    ten_final = FolderMod

FolderMod = f"{base_path}/FOLDERMOD/Pack {len(DANHSACH)} Skin"
if not os.path.exists(FolderMod):
    os.makedirs(FolderMod)
with open(os.path.join(FolderMod, 'SkinListMod.txt'), 'w', encoding='utf-8') as f:
    f.writelines(f'{i+1}. {name}\n' for i, name in enumerate(TENSKIN))
directorie = f'{FolderMod}/Resources/{Ver}/AssetRefs/Hero'
os.makedirs(directorie, exist_ok=True)
base_path = f"{FolderMod}/Resources/{Ver}/Databin/Client/"
directories = ["Actor", "Shop", "Sound", "Skill", "Character", "Motion", "Global", "Huanhua"]
for directory in directories:
    os.makedirs(os.path.join(base_path, directory), exist_ok=True)
#-----------------------------------------------
file_actor = f"Resources/{Ver}/Databin/Client/Actor/heroSkin.bytes"
file_actor_mod = f"{FolderMod}/Resources/{Ver}/Databin/Client/Actor/heroSkin.bytes"
shutil.copy(file_actor, file_actor_mod)
#giai(file_actor_mod)

file_shop = f"Resources/{Ver}/Databin/Client/Shop/HeroSkinShop.bytes"
file_shop_mod = f"{FolderMod}/Resources/{Ver}/Databin/Client/Shop/HeroSkinShop.bytes"
shutil.copy(file_shop, file_shop_mod)
giai(file_shop_mod)

file_sound1 = f"Resources/{Ver}/Databin/Client/Sound/BattleBank.bytes"
file_sound_mod1 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound/BattleBank.bytes"
shutil.copy(file_sound1, file_sound_mod1)
giai(file_sound_mod1)

file_sound2 = f"Resources/{Ver}/Databin/Client/Sound/ChatSound.bytes"
file_sound_mod2 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound/ChatSound.bytes"
shutil.copy(file_sound2, file_sound_mod2)
giai(file_sound_mod2)

file_sound3 = f"Resources/{Ver}/Databin/Client/Sound/HeroSound.bytes"
file_sound_mod3 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound/HeroSound.bytes"
shutil.copy(file_sound3, file_sound_mod3)
giai(file_sound_mod3)

file_sound4 = f"Resources/{Ver}/Databin/Client/Sound/LobbyBank.bytes"
file_sound_mod4 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound/LobbyBank.bytes"
shutil.copy(file_sound4, file_sound_mod4)
giai(file_sound_mod4)

file_sound5 = f"Resources/{Ver}/Databin/Client/Sound/LobbySound.bytes"
file_sound_mod5 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound/LobbySound.bytes"
shutil.copy(file_sound5, file_sound_mod5)
giai(file_sound_mod5)

Sound_Files = f"{FolderMod}/Resources/{Ver}/Databin/Client/Sound"

file_skill1 = f"Resources/{Ver}/Databin/Client/Skill/liteBulletCfg.bytes"
file_mod_skill1 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Skill/liteBulletCfg.bytes"
shutil.copy(file_skill1, file_mod_skill1)
giai(file_mod_skill1)

file_skill2 = f"Resources/{Ver}/Databin/Client/Skill/skillmark.bytes"
file_mod_skill2 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Skill/skillmark.bytes"
shutil.copy(file_skill2, file_mod_skill2)
giai(file_mod_skill2)

Huanhua = f"{FolderMod}/Resources/{Ver}/Databin/Client/Huanhua/ResSkinExclusiveBattleEffectCfg.bytes"
Huanhua1 = f"Resources/{Ver}/Databin/Client/Huanhua/ResSkinExclusiveBattleEffectCfg.bytes"
shutil.copy(Huanhua1, Huanhua)
giai(Huanhua)

file_Character = f"Resources/{Ver}/Databin/Client/Character/ResCharacterComponent.bytes"
file_mod_Character = f"{FolderMod}/Resources/{Ver}/Databin/Client/Character/ResCharacterComponent.bytes"
shutil.copy(file_Character, file_mod_Character)
giai(file_mod_Character)

file_Modtion = f"Resources/{Ver}/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
file_mod_Modtion = f"{FolderMod}/Resources/{Ver}/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
shutil.copy(file_Modtion, file_mod_Modtion)
giai(file_mod_Modtion)

file_vien = f"Resources/{Ver}/Databin/Client/Global/HeadImage.bytes"
file_mod_vien = f"{FolderMod}/Resources/{Ver}/Databin/Client/Global/HeadImage.bytes"
shutil.copy(file_vien, file_mod_vien)
giai(file_mod_vien)

with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes') as zipf:
    zipf.extractall(f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/')
    giai(f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml')
#-----------------------------------------------
ngoaihinhkhieov=b'B\x10\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xea\x0f\x00\x00\x0e\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa2\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Cam\x04\x00\x00\x00\x04\x00\x00\x00\xa3\x00\x00\x00\x19\x00\x00\x00ArtSkinLobbyShowMovie~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Movie\x04\x00\x00\x00\x04\x00\x00\x00Y\x00\x00\x00\x11\x00\x00\x00useNewMecanim<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x0f\x00\x00\x00bUnityLight<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00a\x00\x00\x00\x19\x00\x00\x00bUseCodeAnimComponent<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00f\x00\x00\x00\x08\x00\x00\x00MSAAR\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.EAntiAliasing\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x03\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xd2\x02\x00\x00\x05\x00\x00\x00\x8e\x00\x00\x00\x0b\x00\x00\x00Elementw\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Idle\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Loop\x04\x00\x00\x00\x04\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Run\x04\x00\x00\x00\x04\x00\x00\x00\x84\x00\x00\x00\x0b\x00\x00\x00Elementm\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/Dance_Effects/167/dance_03_texiao\x04\x00\x00\x00\x04\x00\x00\x00\x86\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00.\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.05998039\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.389713\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-2.490662\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xf9\x00\x00\x00\x03\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00xC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V1.831149E-07\x04\x00\x00\x00\x04\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00yC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V-8.35189E-09\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00z8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
bacvalheinevo1 = b'\r\x01\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x00D898FD6DC80FD88F_##\x00\x0b\x00\x00\x00\x14\x00\x00\x0062C20D284D202339_##\x00\x14\x00\x00\x00105E41477A829A72_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x0013311.png\x00\x00\x00\x01\x00\x00\x00\x00\x00\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc4\x0b=\x00\x00\xf7\x07\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020220902000000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdd\x83\x01\x00\x01\x01\x00\x00\x06,\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
#-----------------------------------------------
bacvalheinevo5 = b'\x15\x01\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x0b\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_6.png\x00\x01\x00\x01\x00\x00\x00\x00\x01\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x8a\t=\x00\x00\x9f\x8c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020210318060000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x86\x01\x00\x01\x01\x00\x00\x06:\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
#-----------------------------------------------
#-----------------------------------------------
bgbuterbac1 = b' \x01\x00\x00d-\x00\x00t\x00\x00\x00\x14\x00\x00\x0059AFBB630F219764_##\x00\x14\x00\x00\x00\x14\x00\x00\x00A07C714FC9B4B897_##\x00\x14\x00\x00\x004E514D7070D9574D_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x0011620.png\x00\x00\x00\x14\x00\x00\x001236D7EB468A4620_##'
#-----------------------------------------------
bgbuterbac5= b'(\x01\x00\x00d-\x00\x00t\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x00\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_6.png\x00\x00\x00\x14\x00\x00\x001236D7EB468A4620_##' # BG Toi Thuong
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
bacngokhongevo1 = b'\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x07\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_1.png'    
#-----------------------------------------------
bacngokhongevo5 = b'\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x07\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_6.png'
#-----------------------------------------------
ngoaihinhdoveres = b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhxanhveres= b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'

#-----------------------------------------------
def Track_Guid_Skill(directory_path):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        with open(file_path, "rb") as r0:
            context = r0.read()
            Tracks = re.findall(rb'<Track trackName="(.*?)</Track>', context, re.DOTALL)
            if Tracks:
                for i in range(len(Tracks)):
                    trackName = Tracks[i]
                    guid_track = (re.findall(rb'guid="(.+?)" enabled', trackName)[0]).decode()
                    guid_true = str.encode(f'id="{i}" guid="{guid_track}"')
                    IdGuidFalse = re.findall(str.encode(rf'id="(.+?)" guid="{guid_track}"'), context)
                    if IdGuidFalse:
                        for j in range(len(IdGuidFalse)):
                            j = IdGuidFalse[j].decode()
                            guid_false = str.encode(f'id="{j}" guid="{guid_track}"')
                            context = context.replace(guid_false, guid_true)
                            
        with open(file_path, "wb") as w0:
            w0.write(context)
#-----------------------------------------------
def Function_Track_Guid_AddGetHoliday(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, "rb") as r0:
            context = r0.read()
            Tracks = re.findall(rb'<Track trackName="(.*?)</Track>', context, re.DOTALL)
            if Tracks:
                for i in range(len(Tracks)):
                    trackName = Tracks[i]
                    guid_track = (re.findall(rb'guid="(.+?)" enabled', trackName)[0]).decode()
                    guid_true = str.encode(f'id="{i}" guid="{guid_track}"')
                    IdGuidFalse = re.findall(str.encode(rf'id="(.+?)" guid="{guid_track}"'), context)
                    if IdGuidFalse:
                        for j in range(len(IdGuidFalse)):
                            j = IdGuidFalse[j].decode()
                            guid_false = str.encode(f'id="{j}" guid="{guid_track}"')
                            context = context.replace(guid_false, guid_true)
        with open(file_path, "wb") as w0:
            w0.write(context)
#-----------------------------------------------
class StringBytes:
    def __init__(self,String):
        self.String=String
        self.OldString=String
    def tell(self):
        return len(self.OldString)-len(self.String)
    def seek(self,I,O=0):
        if O==0:
            self.String=self.OldString[I:]
        elif O==1:
            self.String=self.String[I:]
    def read(self,Int=None):
        if Int==None:
            if type(self.String)==str:
                return ""
            else:
                return b""
        R=self.String[:Int]
        self.String=self.String[Int:]
        return R
class Bytes_XML:
    def decode(String):
        def get_int(A):
            return int.from_bytes(A.read(4), 'little')        
        def get_str(A, pos=None):
            if pos is not None:
                A.seek(pos, 0)
            ofs = get_int(A)
            stri = A.read(ofs-4)
            return stri.decode()        
        def get_node(A, fid=None, sta=None):
            global i
            ofs = get_int(A)
            stri = get_str(A)
            stri1 = stri
            myid = i
            i += 1
            A.seek(4, 1)
            aidx = get_int(A)
            ite = False
            attr = {}
            for j in range(0, aidx):
                attr1 = get_attr(A)
                if type(attr1) == str:
                    text1 = attr1
                    ite = True
                else:
                    attr.update(attr1)
            if fid is None:
                nod[myid] = ET.SubElement(root, stri1, attrib=attr)
            else:
                nod[myid] = ET.SubElement(nod[fid], stri1, attrib=attr)
            if ite:
                if text1 == '':
                    nod[myid].set("value",' ')
                else:
                    nod[myid].set("value",text1)
            check_four(A)
            chk = sta + ofs - A.tell()
            if chk > 12:
                A.seek(4, 1)
                sidx = get_int(A)
                for h in range(0, sidx):
                    get_node(A, myid, A.tell())
            A.seek(sta + ofs, 0)        
        def get_attr(A, pos=None):
            if pos is None:
                pos = A.tell()
            ofs = get_int(A)
            type = get_int(A)
            if type == 5:
                stri = A.read(ofs - 8).decode()[1:]
                check_four(A)
                A.seek(pos + ofs, 0)
                return stri
            else:
                if type == 6:
                    stri = A.read(ofs - 8).decode()
                    if stri[0:2] == 'JT':
                        if stri == 'JTArr':
                            stri = 'Array'
                        elif stri == 'JTPri':
                            stri = 'String'
                        else:
                            stri = stri[2:]
                        name = 'var'
                    else:
                        name = 'var_Raw'
                elif type == 8:
                    stri2 = A.read(ofs - 8).decode()
                    if stri2[0:4] == 'Type':
                        stri = stri2[4:]
                        name = 'type'
                    else:
                        stri = stri2
                        name = 'type_Raw'
                else:
                    stri = A.read(ofs - 8).decode()
                    name = str(type)
                    A.seek(pos + ofs, 0)
                return {name:stri}
        def check_four(A):
            if get_int(A) != 4:
                A.seek(-4, 1)
        A=StringBytes(String)
        global i, nod, root
        i = 0
        nod = {}
        ofs = get_int(A)
        stri = get_str(A)
        stri1 = stri
        A.seek(4, 1)
        aidx = get_int(A)
        ite = False
        attr = {}
        for j in range(0, aidx):
            attr1 = get_attr(A)
            if type(attr1) == str:
                text1 = attr1
                ite = True
            else:
                attr.update(attr1)
        root = ET.Element(stri1, attrib=attr)
        if ite:
            nod[myid].set("value",text1)
        check_four(A)
        chk = ofs - A.tell()
        if chk > 12:
            A.seek(4, 1)
            sidx = get_int(A)
            for h in range(0, sidx):
                get_node(A, None, A.tell())
        try:return minidom.parseString(ET.tostring(root,"utf-8").decode()).toprettyxml(indent="  ",newl="\r\n").encode()
        except: return ET.tostring(root,"utf-8").decode()
    def encode(xmlfile):
        def byteint(num):
            return num.to_bytes(4, byteorder='little')
        def bytestr(stri):
            outbyte = byteint(len(stri) + 4)
            outbyte = outbyte + stri.encode()
            return outbyte
        def byteattr(key, attr):
            if key == 'var':
                if attr[key] == 'Array':
                    stri = 'JTArr'
                elif attr[key] == 'String':
                    stri = 'JTPri'
                else:
                    stri = 'JT' + attr[key]
                aid = 6
            elif key == 'var_Raw':
                stri = attr[key]
                aid = 6
            elif key == 'type':
                stri = 'Type' + attr[key]
                aid = 8
            elif key == 'type_Raw':
                stri = attr[key]
                aid = 8
            elif key == "value": return b""
            else:
                import unicodedata
                if unicodedata.numeric(key):
                    stri = attr[key]
                    aid = int(key)
            stripro = stri.encode()
            outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
            return outbyte
        def bytenode(node):
            iftex = False
            name1 = node.tag
            name = bytestr(name1)
            attr1 = b''
            aindex = len(node.attrib)
            plus = 8
            for key in node.attrib:
                if key=="value":aindex-=1
                attr1 = attr1 + byteattr(key, node.attrib)
            if (node.get("value") != None) and (node.get("value")[0:1] != '\n'):
                if node.get("value") == ' ':
                    stri1 = ''
                else:
                    stri1 = node.get("value")
                iftex = True
                stripro = ('V' + stri1).encode()
                attr1 = attr1 + byteint(len(stripro) + 8) + byteint(5) + stripro + byteint(4)
                aindex += 1
                plus = 4
            attr1 = byteint(len(attr1) + plus) + byteint(aindex) + attr1 + byteint(4)
            alchild = b''
            if len(node):
                cindex = 0
                for child in node:
                    alchild = alchild + bytenode(child)
                    cindex += 1
                alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
            else:
                if iftex == False:
                    alchild = byteint(4)
            bnode = name + attr1 + alchild
            bnode = byteint(len(bnode) + 4) + bnode
            return bnode
        tree = ET.fromstring(xmlfile)
        byt = bytenode(tree)
        return byt
                          
def process_file(file_path_FL, LC):
    with open(file_path_FL, "rb") as f:
        G = f.read()
        with open(file_path_FL, "wb") as f1:
            try:
                if LC == "1":
                    f1.write(Bytes_XML.decode(G))
                elif LC == "2":
                    f1.write(Bytes_XML.encode(G.decode()))
            except Exception as e:
                pass
        
def process_directory(directory_path, LC):
    file_path_FL = directory_path
    process_file(file_path_FL, LC) 
#-----------------------------------------------
ngoaihinhvaneov=b'/\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xd7\x0b\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x1c\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xcd\x01\x00\x00\x03\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhvaneovvang=b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
ngoaihinhvaneovdo= b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
#-----------------------------------------------
def hex_to_dec(a):
    len(a)
    a=a[::-1]
    a=a.hex()
    a=int(a,16)
    return a
def dec_to_hex(a):
    a=hex(a)[2:]
    if len(a)%2==1:
        a='0'+a
    return (bytes.fromhex(a))[::-1]
#-----------------------------------------------
for IDMODSKIN in IDMODSKIN1:
    index = DANHSACH.index(IDMODSKIN)
    TENSKIN_NOW = TENSKIN[index]
    fileasset = f'Resources/{Ver}/AssetRefs/Hero/{IDMODSKIN[:3]}_AssetRef.bytes'
    fileasset_mod2 = f'{FolderMod}/Resources/{Ver}/AssetRefs/Hero/{IDMODSKIN[:3]}_AssetRef.bytes'
    shutil.copy(fileasset, fileasset_mod2)
    print('-' * 53)
    print(f"{TENSKIN_NOW:^53}")
    print('-' * 53)
    SKINEOV = ''
    if IDMODSKIN == '13311':
        SKINEOV = "r"
    if IDMODSKIN == '16707':
        SKINEOV = "b"
    if IDMODSKIN == '15412':
        SKINEOV = "y"
    if IDMODSKIN == '51015':
        SKINEOV = "l"
    
    nhap_id = IDMODSKIN
    IDCHECK = IDMODSKIN
    skinid = IDMODSKIN.encode()
    IDSOUND_S = IDMODSKIN
    phukien = ''
    phukienb = ''
    phukienv = ''
    IDINFO=int(IDMODSKIN)+1
    IDINFO=str(IDINFO)
    if str(IDINFO)[3:4] == '0':
        IDINFO=IDINFO[:3]+IDINFO[4:]
    IDINFO=str(IDINFO)

    if IDCHECK == '52007':
        phukien1 = input(
            '\033[1;97m[\033[1;91m?\033[1;97m] Mod Component:\n'
            '\033[1;97m [1] \033[1;92mBlue\n'
            '\033[1;97m [2] \033[1;92mRed\n'
            '\033[1;97m [3] \033[1;92mNo Mod Component\n'
            '\033[1;97m[•] INPUT: '
        )
        if phukien1 == "1":
            phukien = 'xanh'
        if phukien1 == "2":
            phukien = 'do'
    if IDCHECK == '13311':
        phukien1v = input(
            '\033[1;97m[\033[1;91m?\033[1;97m] Mod Component:\n'
            '\033[1;97m [1] \033[1;92mGreen\n'
            '\033[1;97m [2] \033[1;92mRed\n'
            '\033[1;97m [3] \033[1;92mNo Mod Component\n'
            '\033[1;97m[•] INPUT: '
        )
        if phukien1v == "1":
            phukienv = 'vangv'
        if phukien1v == "2":
            phukienv = 'dov'
    if IDCHECK == '11620':
        phukien12 = input(
            '\033[1;97m[\033[1;91m?\033[1;97m] Mod Component:\n'
            '\033[1;97m [1] \033[1;92mPurple\n'
            '\033[1;97m [2] \033[1;92mRed\n'
            '\033[1;97m [3] \033[1;92mNo Mod Component\n'
            '\033[1;97m[•] INPUT: '
        )
        if phukien12 == "1":
            phukienb = 'tim'
        if phukien12 == "2":
            phukienb = 'do'
    if IDMODSKIN == '11620':
        try:
            with open(file_shop_mod, 'rb') as f:
                codenew = f.read()
            codenew = codenew.replace(bgbuterbac1, bgbuterbac5)
            with open(file_shop_mod, 'wb') as f:
                f.write(codenew)
            print('Awaken_Label_1 --> Awaken_Label_5')
        except:
            print("⚠ Không thể thay background Shop. Bỏ qua...")
    if IDMODSKIN == '13311':
        try:
            with open(file_shop_mod, 'rb') as f:
                codenew = f.read()
            codenew = codenew.replace(bacvalheinevo1, bacvalheinevo5)
            with open(file_shop_mod, 'wb') as f:
                f.write(codenew)
            print('Awaken_Label_1 --> Awaken_Label_5')
        except:
            print("⚠ Không thể thay background Shop. Bỏ qua...")
    if IDMODSKIN == '16707':
        try:
            with open(file_shop_mod, 'rb') as f:
                codenew = f.read()
            codenew = codenew.replace(bacngokhongevo1, bacngokhongevo5)
            with open(file_shop_mod, 'wb') as f:
                f.write(codenew)
            print('Awaken_Label_1 --> Awaken_Label_5')
        except:
            print("⚠ Không thể thay background Shop. Bỏ qua...")
    try:
        id_mod = dec_to_hex(int(skinid.decode()))
        id_0 = dec_to_hex(int(skinid[:3].decode() + '00'))
        hero_actor = dec_to_hex(int(skinid[:3].decode()))
        
        with open(file_actor_mod, 'rb') as f:
            strin = f.read()
        pos_mod = strin.find(id_mod + b'\x00\x00' + hero_actor)
        pos_base = strin.find(id_0 + b'\x00\x00' + hero_actor)
        
        if pos_mod != -1 and pos_base != -1:
            actor_mod = strin[pos_mod - 4:pos_mod + hex_to_dec(strin[pos_mod - 4:pos_mod - 2])]
            actor_0 = strin[pos_base - 4:pos_base + hex_to_dec(strin[pos_base - 4:pos_base - 2])]
    
            if skinid == b'16707':
                actor_mod = actor_mod[:4] + actor_0[4:10] + actor_mod[10:36] + b'\x00' + actor_mod[37:]
                actor_mod=actor_mod.replace(b'\x07\x00\x00\x00301677',b'\x07\x00\x00\x00301670',1)
                actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_16707\x2ejpg',b'\x12\x00\x00\x00Share_16707_2\x2ejpg').replace(b'\x0a\x00\x00\x0016707\x2ejpg',b'\x0c\x00\x00\x0016707_2\x2ejpg').replace(b'\x0b\x00\x00\x00301677\x2ejpg',b'\x0d\x00\x00\x00301677_2\x2ejpg').replace(b'\x0f\x00\x00\x00301677head\x2ejpg',b'\x11\x00\x00\x00301677_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x2d\x00\x00\x00\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x2f\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d')
            elif skinid == b'10620':
                actor_mod = actor_mod[:4] + actor_0[4:10] + actor_mod[10:36] + b'\x00' + actor_mod[37:]
                actor_mod = actor_mod.replace(b'\x08\x00\x00\x003010620', b'\x07\x00\x00\x00301060', 1)
            elif skinid == b'13311':
                actor_mod = actor_mod[:4] + actor_0[4:10] + actor_mod[10:36] + b'\x00' + actor_mod[37:]
                actor_mod=actor_mod.replace(b'\x08\x00\x00\x003013311',b'\x07\x00\x00\x00301330',1)
                actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_13311\x2ejpg',b'\x12\x00\x00\x00Share_13311_2\x2ejpg').replace(b'\x0a\x00\x00\x0013311\x2ejpg',b'\x0c\x00\x00\x0013311_2\x2ejpg').replace(b'\x0c\x00\x00\x003013311\x2ejpg',b'\x0e\x00\x00\x003013311_2\x2ejpg').replace(b'\x10\x00\x00\x003013311head\x2ejpg',b'\x12\x00\x00\x003013311_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x33\x00\x00\x00\x42\x47\x5f\x44\x69\x52\x65\x6e\x4a\x69\x65\x5f\x31\x33\x33\x31\x32\x5f\x54\x33\x2f\x42\x47\x5f\x79\x69\x6e\x79\x69\x6e\x67\x7a\x68\x69\x73\x68\x6f\x75\x5f\x30\x31\x5f\x70\x6c\x61\x74\x66\x6f\x72\x6d')
            elif skinid == b'11620':
                actor_mod = actor_mod[:4] + actor_0[4:10] + actor_mod[10:36] + b'\x00' + actor_mod[37:]
                actor_mod=actor_mod.replace(b'\x08\x00\x00\x003011620',b'\x07\x00\x00\x00301160',1)
                actor_mod=actor_mod.replace(
                b'\x25\x00\x00\x00\x42\x47\x5F\x43\x6F\x6D\x6D\x6F\x6E\x73\x5F\x30\x31\x2F\x42\x47\x5F\x43\x6F\x6D\x6D\x6F\x6E\x73\x5F\x30\x31\x5F\x50\x6C\x61\x74\x66\x6F\x72\x6D\x00',
                b'\x36\x00\x00\x00\x42\x47\x5F\x44\x61\x6F\x46\x65\x6E\x67\x4A\x69\x4E\x69\x61\x6E\x67\x5F\x31\x31\x36\x32\x31\x2F\x42\x47\x5F\x79\x69\x6E\x79\x69\x6E\x67\x7A\x68\x69\x73\x68\x6F\x75\x5F\x30\x31\x5F\x70\x6C\x61\x74\x66\x6F\x72\x6D\x00').replace(
                b'\x10\x00\x00\x00Share_11620\x2ejpg',
                b'\x12\x00\x00\x00Share_11620_2\x2ejpg').replace(
b'\x0a\x00\x00\x0011620\x2ejpg',
                b'\x0c\x00\x00\x0011620_2\x2ejpg').replace(
                b'\x0c\x00\x00\x003011620\x2ejpg',
                b'\x0e\x00\x00\x003011620_2\x2ejpg').replace(
                b'\x10\x00\x00\x003011620head\x2ejpg',
                b'\x12\x00\x00\x003011620_2head\x2ejpg')
            elif skinid == b'15412':
                actor_mod = actor_mod[:4] + actor_0[4:10] + actor_mod[10:36] + b'\x00' + actor_mod[37:]
                actor_mod = actor_mod.replace(
                    b'\x08\x00\x00\x003015412', b'\x07\x00\x00\x00301540', 1
                ).replace(
                    b'\x12\x00\x00\x003015412_B43_1', b'\x0c\x00\x00\x003015412', 1
                )
            else:
                nhanDangId_0 = actor_0[64:]
                nhanDangId_0 = nhanDangId_0[:hex_to_dec(nhanDangId_0[:2]) + 4]
    
                actor_mod = (
                    actor_mod[:64] + nhanDangId_0 +
                    actor_mod[64 + hex_to_dec(actor_mod[64:66]) + 4:]
                )
                actor_mod = actor_mod.replace(id_mod + b'\x00\x00' + hero_actor, id_0 + b'\x00\x00' + hero_actor)
                actor_mod = actor_mod[:36] + b'\x00' + actor_mod[37:]
            actor_mod = dec_to_hex(len(actor_mod) - 4) + actor_mod[2:]
            dieukienmod=actor_mod
            #print(dieukienmod)
            strin = strin.replace(actor_0, actor_mod, 1)
        with open(file_actor_mod, 'wb') as f:
            f.write(strin)
    
    except Exception as bug:
        print(bug)
        print('\n\t\033[0m          [   \033[1;31mKhông Mod Heroskin Mặc Định\033[0m    ]')
#-----------------------------------------------
    print('Mod Skin Phụ')
    try:
        for nnn in range(1,30):
            #nnn=int(nnn.decode()[3:])-1
            with open(file_actor_mod,'rb') as f:
                strin = f.read()
                hero_actor=dec_to_hex(int(skinid[:3].decode()))
                id_mod=dec_to_hex(int(skinid.decode()))
                pos = strin.find(id_mod+b'\x00\x00'+hero_actor)
                if pos!=-1:
                    actor_mod = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                    if skinid==b'16707':
                        actor_mod=actor_mod.replace(b'\x07\x00\x00\x00301677',b'\x09\x00\x00\x00301677_2',1)
                        actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_16707\x2ejpg',b'\x12\x00\x00\x00Share_16707_2\x2ejpg').replace(b'\x0a\x00\x00\x0016707\x2ejpg',b'\x0c\x00\x00\x0016707_2\x2ejpg').replace(b'\x0b\x00\x00\x00301677\x2ejpg',b'\x0d\x00\x00\x00301677_2\x2ejpg').replace(b'\x0f\x00\x00\x00301677head\x2ejpg',b'\x11\x00\x00\x00301677_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x2d\x00\x00\x00\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x2f\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d')
                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                    if skinid==b'13311':
                        actor_mod=actor_mod.replace(b'\x08\x00\x00\x003013311',b'\x0a\x00\x00\x003013311_2',1)
                        actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_13311\x2ejpg',b'\x12\x00\x00\x00Share_13311_2\x2ejpg').replace(b'\x0a\x00\x00\x0013311\x2ejpg',b'\x0c\x00\x00\x0013311_2\x2ejpg').replace(b'\x0c\x00\x00\x003013311\x2ejpg',b'\x0e\x00\x00\x003013311_2\x2ejpg').replace(b'\x10\x00\x00\x003013311head\x2ejpg',b'\x12\x00\x00\x003013311_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x33\x00\x00\x00\x42\x47\x5f\x44\x69\x52\x65\x6e\x4a\x69\x65\x5f\x31\x33\x33\x31\x32\x5f\x54\x33\x2f\x42\x47\x5f\x79\x69\x6e\x79\x69\x6e\x67\x7a\x68\x69\x73\x68\x6f\x75\x5f\x30\x31\x5f\x70\x6c\x61\x74\x66\x6f\x72\x6d')
                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                    if skinid==b'11620':
                        actor_mod=actor_mod.replace(b'\x08\x00\x00\x003011620',b'\x0a\x00\x00\x003011620_1',1)
                        actor_mod=actor_mod.replace(b'\x25\x00\x00\x00\x42\x47\x5F\x43\x6F\x6D\x6D\x6F\x6E\x73\x5F\x30\x31\x2F\x42\x47\x5F\x43\x6F\x6D\x6D\x6F\x6E\x73\x5F\x30\x31\x5F\x50\x6C\x61\x74\x66\x6F\x72\x6D\x00',b'\x36\x00\x00\x00\x42\x47\x5F\x44\x61\x6F\x46\x65\x6E\x67\x4A\x69\x4E\x69\x61\x6E\x67\x5F\x31\x31\x36\x32\x31\x2F\x42\x47\x5F\x79\x69\x6E\x79\x69\x6E\x67\x7A\x68\x69\x73\x68\x6F\x75\x5F\x30\x31\x5F\x70\x6C\x61\x74\x66\x6F\x72\x6D\x00').replace(b'\x10\x00\x00\x00Share_11620\x2ejpg',b'\x12\x00\x00\x00Share_11620_2\x2ejpg').replace(b'\x0a\x00\x00\x0011620\x2ejpg',b'\x0c\x00\x00\x0011620_2\x2ejpg').replace(b'\x0c\x00\x00\x003011620\x2ejpg',b'\x0e\x00\x00\x003011620_2\x2ejpg').replace(b'\x10\x00\x00\x003011620head\x2ejpg',b'\x12\x00\x00\x003011620_2head\x2ejpg')
                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                    id_2=dec_to_hex(int(skinid[:3].decode())*100+nnn)
                    pos = strin.find(id_2+b'\x00\x00'+hero_actor)
                    if pos !=-1:
                        actor_2 = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                        re_2 = actor_mod[:4]+id_2+actor_mod[6:][:30]+dec_to_hex(nnn)+actor_mod[37:]
                        if re_2!=b'' and actor_2!=b'' and nnn!=int(skinid[3:].decode()):
                            strin=strin.replace(actor_2,re_2)
                            with open(file_actor_mod,'wb') as f1:
                                f1.write(strin)
    except Exception as bug:
        print(bug)
    
    try:
        with open(file_shop_mod, 'rb') as f: d = f.read()
    except:
        pass
    i1 = int(IDMODSKIN).to_bytes(4, 'little')
    i2 = int(IDMODSKIN[:3] + '00').to_bytes(4, 'little')
    
    try: d = bytearray(open(file_actor_mod,'rb').read())
    except: print(" File lỗi"); exit()
    
    p1 = d.find(i1)
    p2 = d.find(i2)
    if p1 == -1 or p2 == -1: pass
    
    b1 = bytearray(d[p1:p1+33])
    b2 = bytearray(d[p2:p2+33])
    print(b1)
    print(b2)
    
    b1[-1], b2[-1] = b2[-1], b1[-1]
    d[p1:p1+33] = b1
    d[p2:p2+33] = b2
    
    open(file_actor_mod,'wb').write(d)

    ID = IDMODSKIN
    Show = 'y'  # input("\n \033[1;36mShow Name? (y/n): ")
    IDB = int(ID).to_bytes(4, byteorder="little")
    IDH = int(ID[0:3]).to_bytes(4, byteorder="little")
    Files = [file_shop_mod]
    
    for File in Files:
        All = []
        Skin = ""
        file = open(File, "rb")
        Code = file.read()
        Find = -10
        while True:
            Find = Code.find(b"\x00\x00" + IDH, Find + 10)
            if Find == -1:
                break
            elif str(int.from_bytes(Code[Find - 2:Find], byteorder="little"))[0:3] == ID[0:3]:
                VT2 = int.from_bytes(Code[Find - 6:Find - 4], byteorder="little")
                Code2 = Code[Find - 6:Find - 6 + VT2]
                All.append(Code2)
                if Code2.find(IDB) != -1:
                    Skin = Code2
    
        if Skin == "":
            print("\n \033[1;31m The id couldn't be found in " + File + " file!")
            if "HeroSkinShop.bytes" in File:
                continue 
            IDNew = input("\n\033[1;36m  Enter an alternate skin ID: ")
            IDK = int(IDNew).to_bytes(4, byteorder="little")
            Find = -1
            while True:
                Find = Code.find(b"\x00\x00" + IDK, Find + 1)
                if str(int.from_bytes(Code[Find - 6:Find - 8], byteorder="little")) == IDNew[0:3]:
                    Sum = int.from_bytes(Code[Find - 2:Find], byteorder="little")
                    Skin = Code[Find - 2:Find - 2 + Sum]
                    break
    
        for Id in All:
            Cache = Skin.replace(Skin[4:6], Id[4:6], 1)
            Cache = Cache.replace(Cache[35:44], Id[35:40] + Cache[40:44], 1)
            if Show == "y":
                if Id == Skin:
                    Cache = Cache.replace(Skin[35:44], b"\x00" * 5 + b"\x14" + b"\x00" * 3, 1)
                if Id == All[0]:
                    Cache = Cache.replace(Id[35:44], Skin[35:44], 1)
    
            Hero = hex(int(ID[0:3]))[2:]
            if len(Hero) == 3:
                Hero = Hero[1:3] + "0" + Hero[0]
            else:
                Hero += "00"
            Hero += "0000"
            Hero = bytes.fromhex(Hero)
            Cache = Cache.replace(Cache[8:12], Hero, 1)
    
            if File == Files[0]:
                if Id == All[0]:
                    ID30 = b"\x07\x00\x00\x0030" + bytes(ID[0:3] + "0", "utf8") + b"\x00"
                    XYZ = Cache[64]
                    ID0 = Cache[64: 68 + XYZ]
                    Cache = Cache.replace(ID0, ID30, 1)
                    VT = Id.find(b"Hero_")
                    NumHero = Id[VT - 4]
                    Hero = Id[VT - 4: VT + NumHero]
                    Cache = Cache.replace(b"jpg\x00\x01\x00\x00\x00\x00", b"jpg\x00" + Hero)
                    Full = Cache.count(Hero)
                    if Full > 1:
                        Cache = Cache.replace(b"jpg\x00" + Hero, b"jpg\x00\x01\x00\x00\x00\x00", Full - 1)
                    EndTheCode = hex(len(Cache))
                    if len(EndTheCode) == 5:
                        EndTheCode = EndTheCode[3:5] + "0" + EndTheCode[2:3]
                    else:
                        EndTheCode = EndTheCode[4:6] + EndTheCode[2:4]
                    EndTheCode = bytes.fromhex(EndTheCode)
                    Cache = Cache.replace(Cache[0:2], EndTheCode, 1)
    
            Code = Code.replace(Id, Cache, 1)
        file = open(File, "wb")
        file.write(Code)
        file.close()
#----------------------------------------------
    if len(IDMODSKIN1) == 1:
        if b'Skin_Icon_HeadFrame' in dieukienmod:
            chedovien='1'
            if chedovien == '1':
                data = dieukienmod
                target = b'\x00\x00\x10\x00\x00\x00Share_'+IDCHECK.encode()+b'.jpg'
                index = data.find(target) - 2
                two_bytes_before = data[index:index+2]
                print(two_bytes_before)
            if chedovien == '2':
                idvien=input('viền cần mod : ')
                two_bytes_before=bytes.fromhex(str(idvien))
            if two_bytes_before != b'\x00\x00':
                if chedovien in ['1', '2']:

                    inp=file_mod_vien
                    with open(inp,'rb') as f:
                        ab=f.read()
                    a=two_bytes_before
                    i=ab.find(a)-4
                    vt=ab[i:i+4]
                    vtr=int.from_bytes(vt,byteorder='little')
                    vt1=ab[i:i+vtr]
                    id2='6500'
                    a1=bytes.fromhex(str(id2))
                    f.close()
                    i1=ab.find(a1)-4
                    vt11=ab[i1:i1+4]
                    vtr1=int.from_bytes(vt11,byteorder='little')
                    vt2=ab[i1:i1+vtr1]
                    vt1=vt1.replace(a,a1)
                    vt11=ab.replace(vt2,vt1)
                    with open(inp,'wb') as go:
                        go.write(vt11)
            else:
                print('không tìm thấy viền (vui lòng nhập thủ công)')
#----------------------------------------------
    if fixlag == '1':
        if b"Skin_Icon_Skill" in dieukienmod or IDCHECK == "53702":
            fileasset_mod = f'{FolderMod}/Resources/{Ver}/AssetRefs/Hero/{IDMODSKIN[:3]}_AssetRef.bytes'
            giai(fileasset_mod)
            id=IDCHECK
            if IDCHECK == "13311":
                with open(fileasset_mod,'rb') as f:rpl=f.read()
                CODETONG = rpl.replace(b"prefab_skill_effects/hero_skill_effects/133_direnjie/", b"prefab_skill_effects/component_effects/13311/13311_5/")
                with open(fileasset_mod,'wb') as f:f.write(CODETONG)
                print(f'  [✓] Fix Lag  {os.path.basename(fileasset_mod)}')
                
            elif IDCHECK == "16707":
                with open(fileasset_mod,'rb') as f:rpl=f.read();f.close()
                CACHE=[]
                VTR=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'particlesInFirstLayer')-4];VTC=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'animationsw')-8]
                DAU1=rpl[:rpl.find(b'particlesInFirstLayer')-8]
                VTF=b''
                if rpl.find(b'skinSubset') != -1:
                    VTF=rpl[rpl.find(b'skinSubset')-8:]
                    CUOI1=rpl[rpl.find(b'animationsw')-8:rpl.find(b'skinSubset')-8]
                else:
                    CUOI1=rpl[rpl.find(b'animationsw')-8:]
                while True:
                    if VTC == b'': break
                    CACHE.append(VTC[:int.from_bytes((VTC[:4]),'little')])
                    VTC=VTC[int.from_bytes((VTC[:4]),'little'):]
                CODETONG=b''
                for i in CACHE:
                    VT=i.find(b'Element')-8
                    VTDAU=i[VT-8:VT]
                    DAU=i[:VT-8]
                    VTD=i[VT:]
                    CODE=b''
                    for ig in range(i.count(b'Element')):
                        VTC=VTD[:int.from_bytes((VTD[:4]),'little')]
                        VT=VTC[103:111]
                        VT1=VTC[111:121]
                        VT2=VTC[121:167]
                        Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                        VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                        if VTT.find(id[:3].encode())!= -1:
                            IDEOV = "16707_5"
                            RPL=VTT[4:].replace(b"hero_skill_effects/167_wukong/",b"component_effects/16707/16707_5/").replace(b"Hero_Skill_Effects/167_wukong/",b"component_effects/16707/16707_5/");RPL=RPL.replace(IDEOV.encode()+b'/'+IDEOV.encode(),IDEOV.encode())
                        else:RPL=VTT[4:]
                        RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                        CODE+=RPL
                        VTD=VTD[int.from_bytes((VTD[:4]),'little'):]
                    CODE=len(DAU+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE).to_bytes(4,'little')+DAU[4:]+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE;CODETONG+=CODE
                if id in('15704','11107'):
                    VTP=CUOI1[:149]
                    CUOI=CUOI1[149:]
                    ELEMENT=[]
                    while True:
                        VT=CUOI[:4]
                        if CUOI==b'': break
                        ELEMENT.append(CUOI[:int.from_bytes(VT,'little')])
                        CUOI=CUOI[int.from_bytes(VT,'little'):]
                    CUOI1=b''
                    for VTC in ELEMENT:
                        VT=VTC[103:111]
                        VT1=VTC[111:121]
                        VT2=VTC[121:167]
                        Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                        VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                        RPL=VTT[4:]
                        RPL=RPL[:5]+id.encode()+b'/'+RPL[5:]
                        RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                        CUOI1+=RPL
                    CUOI1=VTP[:141]+(len(CUOI1)+8).to_bytes(4,'little')+VTP[145:]+CUOI1
                CODETONG=len(DAU1[:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF).to_bytes(4,'little')+DAU1[4:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF
                #with open('kb1.bytes','wb') as f:f.write(CODETONG)
                with open(fileasset_mod,'wb') as f:f.write(CODETONG)
                
                print(f'  [✓] Fix Lag  {os.path.basename(fileasset_mod)}')
#----------------------------------------------
            else:
                with open(fileasset_mod,'rb') as f:rpl=f.read();f.close()
                CACHE=[]
                VTR=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'particlesInFirstLayer')-4];VTC=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'animationsw')-8]
                DAU1=rpl[:rpl.find(b'particlesInFirstLayer')-8]
                VTF=b''
                if rpl.find(b'skinSubset') != -1:
                    VTF=rpl[rpl.find(b'skinSubset')-8:]
                    CUOI1=rpl[rpl.find(b'animationsw')-8:rpl.find(b'skinSubset')-8]
                else:
                    CUOI1=rpl[rpl.find(b'animationsw')-8:]
                while True:
                    if VTC == b'': break
                    CACHE.append(VTC[:int.from_bytes((VTC[:4]),'little')])
                    VTC=VTC[int.from_bytes((VTC[:4]),'little'):]
                CODETONG=b''
                for i in CACHE:
                    VT=i.find(b'Element')-8
                    VTDAU=i[VT-8:VT]
                    DAU=i[:VT-8]
                    VTD=i[VT:]
                    CODE=b''
                    for ig in range(i.count(b'Element')):
                        VTC=VTD[:int.from_bytes((VTD[:4]),'little')]
                        VT=VTC[103:111]
                        VT1=VTC[111:121]
                        VT2=VTC[121:167]
                        Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                        VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                        if VTT.find(id[:3].encode())!= -1:
                            RPL=VTT[4:].replace(b"hero_skill_effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))]),b"hero_skill_effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))])+b'/'+id.encode()).replace(b"Hero_Skill_Effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))]),b"Hero_Skill_Effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))])+b'/'+id.encode());RPL=RPL.replace(id.encode()+b'/'+id.encode(),id.encode())
                        else:RPL=VTT[4:]
                        RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                        CODE+=RPL
                        VTD=VTD[int.from_bytes((VTD[:4]),'little'):]
                    CODE=len(DAU+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE).to_bytes(4,'little')+DAU[4:]+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE;CODETONG+=CODE
                if id in('15704','11107'):
                    VTP=CUOI1[:149]
                    CUOI=CUOI1[149:]
                    ELEMENT=[]
                    while True:
                        VT=CUOI[:4]
                        if CUOI==b'': break
                        ELEMENT.append(CUOI[:int.from_bytes(VT,'little')])
                        CUOI=CUOI[int.from_bytes(VT,'little'):]
                    CUOI1=b''
                    for VTC in ELEMENT:
                        VT=VTC[103:111]
                        VT1=VTC[111:121]
                        VT2=VTC[121:167]#MODLQ
                        Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                        VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                        RPL=VTT[4:]
                        RPL=RPL[:5]+id.encode()+b'/'+RPL[5:]
                        RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                        CUOI1+=RPL
                    CUOI1=VTP[:141]+(len(CUOI1)+8).to_bytes(4,'little')+VTP[145:]+CUOI1
                CODETONG=len(DAU1[:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF).to_bytes(4,'little')+DAU1[4:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF
                #with open('kb1.bytes','wb') as f:f.write(CODETONG)
                with open(fileasset_mod,'wb') as f:f.write(CODETONG)
                print(f'{os.path.basename(fileasset_mod)}')
                print("-"*53)
        if IDCHECK == '52007':
            if phukien in ["do", "xanh"]:
                process_directory(fileasset_mod, '1')
                with open(fileasset_mod, 'rb') as f:
                    strin = f.read()
                if phukien == "do":
                    strin = strin.replace(
                        b'hero_skill_effects/520_Veres/52007/',
                        b'component_effects/520_Veres/52007/5200402/'
                    )
                if phukien == "xanh":
                    strin = strin.replace(
                        b'hero_skill_effects/520_Veres/52007/',
                        b'component_effects/52007/5200401/'
                    )
                with open(fileasset_mod, 'wb') as f:
                    f.write(strin)
                process_directory(fileasset_mod, '2')
    
    print('[✓] Âm Thanh Databin')
    if IDCHECK == "53002" or b"Skin_Icon_SoundEffect" in dieukienmod or b"Skin_Icon_Dialogue" in dieukienmod:
        skin_id_input = IDMODSKIN
        sound_directory = Sound_Files
        sound_files = os.listdir(sound_directory)

        all_skin_ids = []
        for i in range(21):
            i_str = f"{i:02d}"  # 00 -> 20
            all_skin_ids.append(b"\x00" + int(skin_id_input[:3] + i_str).to_bytes(4, "little"))

        initial_skin_id = all_skin_ids[0]
        selected_skin_id = all_skin_ids[int(skin_id_input[3:])]

        all_skin_ids.remove(selected_skin_id)
        all_skin_ids.remove(initial_skin_id)

        for sound_file_name in sound_files:
            with open(os.path.join(sound_directory, sound_file_name), "rb") as sound_file:
                sound_data = sound_file.read()

            if skin_id_input == "13311":
                if sound_file_name == 'BattleBank.bytes':
                    sound_data = sound_data.replace(b'\x9dO\x14', b'\xff3\x00').replace(b'\x9eO\x14', b'\xff3\x00').replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
                if sound_file_name == 'ChatSound.bytes':
                    sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00')
                if sound_file_name == 'HeroSound.bytes':
                    sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
                if sound_file_name == 'LobbyBank.bytes':
                    sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')
                if sound_file_name == 'LobbySound.bytes':
                    sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')
            if skin_id_input == "11620" and sound_file_name in ['BattleBank.bytes', 'HeroSound.bytes', 'LobbyBank.bytes', 'LobbySound.bytes', 'ChatSound.bytes']:
                sound_data = sound_data.replace(b'\x50\x2d', b'\x30\x30')
                sound_data = sound_data.replace(b'\x64\x2d', b'\x30\x30')
                sound_data = sound_data.replace(b'\x15\xbb\x11', b'\x50\x2d\x00').replace(b'\x16\xbb\x11', b'\x50\x2d\x00')

            if skin_id_input == "16707":
                if sound_file_name == 'BattleBank.bytes':
                    sound_data = sound_data.replace(b'/~\x19', b'CA\x00').replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
                if sound_file_name == 'ChatSound.bytes':
                    sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
                if sound_file_name == 'HeroSound.bytes':
                    sound_data = sound_data.replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
                if sound_file_name == 'LobbyBank.bytes':
                    sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
                if sound_file_name == 'LobbySound.bytes':
                    sound_data = sound_data.replace(b'0~\x19', b'CA\x00')

            if sound_file_name != "CoupleSound.bytes":
                for skin_id in all_skin_ids:
                    skin_id += b"\x00" * 8
                    sound_data = sound_data.replace(skin_id, b"\x0000" + b"\x00" * 10)
            else:
                for skin_id in all_skin_ids:
                    skin_id += b"\x02\x00\x00\x00\x01"
                    sound_data = sound_data.replace(skin_id, b"\x0000\x00\x00\x02\x00\x00\x00\x01")

            if selected_skin_id in sound_data:
                if sound_file_name != "CoupleSound.bytes":
                    sound_data = sound_data.replace(initial_skin_id + b"\x00" * 8, b"\x0000" + b"\x00" * 10)
                    sound_data = sound_data.replace(selected_skin_id + b"\x00" * 8, initial_skin_id + b"\x00" * 8)
                else:
                    sound_data = sound_data.replace(initial_skin_id + b"\x02\x00\x00\x00\x01", b"\x0000\x00\x00\x02\x00\x00\x00\x01")
                    sound_data = sound_data.replace(selected_skin_id + b"\x02\x00\x00\x00\x01", initial_skin_id + b"\x02\x00\x00\x00\x01")

            with open(os.path.join(sound_directory, sound_file_name), "wb") as sound_file:
                sound_file.write(sound_data)
            print(f"     Sound: {sound_file_name}  Done")
    print(f"{'+ Trạng Thái Mod':<25}")
#----------------------------------------------
    FixNgoaiHinh = 'y'#input('Fix Yes Or No :').lower()
    if FixNgoaiHinh in ['yes', 'y']:
        if IDCHECK not in ["13008", "52007"]:
            with open(file_mod_Character, 'rb') as f:
                Code = f.read()
    
            user_prefix = IDMODSKIN[:3]
            relevant_patterns = []
    
            for i in range(10500, 20000):
                if str(i).startswith(user_prefix):
                    bcode = i.to_bytes(4, 'little')
                    if bcode in Code:
                        relevant_patterns.append(bcode)
    
            for i in range(50100, 60000):
                if str(i).startswith(user_prefix):
                    bcode = i.to_bytes(4, 'little')
                    if bcode in Code:
                        relevant_patterns.append(bcode)
    
            if relevant_patterns:
                first_pattern = relevant_patterns[0]
                pos = Code.find(first_pattern)
                if pos == -1:
                    print(f"[!] Không tìm thấy pattern đầu.")
                else:
                    start = pos - 155
                    full_code = b''
                    temp_code = Code[start:]
                    cursor = 0
    
                    while cursor + 4 < len(temp_code):
                        len_block = int.from_bytes(temp_code[cursor:cursor+4], 'little')
                        block = temp_code[cursor:cursor+len_block+4]
    
                        if all(pat not in block for pat in relevant_patterns):
                            break
    
                        full_code += block
                        cursor += len_block + 4
    
                    if full_code:
                        new_code = Code.replace(full_code, b'')
                        with open(file_mod_Character, 'wb') as f:
                            f.write(new_code)
                        print(f'    Fix Mất Ngoại Hình - {IDMODSKIN}')
#----------------------------------------------
    if IDCHECK == "53002" or b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod:
        def B2Js(blocks_data):
            offset = 140
            blocks = []
            
            def S():
                nonlocal offset
                value = struct.unpack_from("<I", blocks_data, offset)[0]
                offset += 4
                return value
        
            def S2():
                nonlocal offset
                value = struct.unpack_from("<H", blocks_data, offset)[0]
                offset += 2
                return value
        
            def S8():
                nonlocal offset
                value = struct.unpack_from("<Q", blocks_data, offset)[0]
                offset += 8
                return value
                
            def B1():
                nonlocal offset
                value = struct.unpack_from("<B", blocks_data, offset)[0]
                offset += 1
                return value
            def B2():
                return B1() == 1
        
        
            def Str():
                nonlocal offset
                length = struct.unpack_from("<I", blocks_data, offset)[0]
                offset += 4
                raw_bytes = blocks_data[offset:offset + length]
                offset += length
                try:
                    value = raw_bytes.decode("utf-8").strip("\x00")
                except UnicodeDecodeError:
                    value = raw_bytes.decode("utf-8", errors="replace").strip("\x00")
                return value
        
            while offset < len(blocks_data):
                block = {}
                try:
                    blockinfo = S()
                    block['CfgID'] = int(S())
                    block['DependCfgID'] = int(S())
                    
                    block['MarkName'] = Str()
                    block['MarkDesc'] = Str()
                    block['ActionName'] = Str()
                    
                    block['MarkOverlapRule'] = int(S())
                    
                    block['bLayerEffect'] = B1()
                    
                    block['MaxLayer'] = int(S())
                    block['OnlyTriggerLayer'] = int(S())
                    block['CostLayer'] = int(S())
                    block['TriggerLayer'] = int(S())
                    block['ImmuneTime'] = int(S())
                    block['LastMaxTime'] = int(S())
                    block['CDTime'] = int(S())
                    block['AddMarkImmuneTime'] = int(S())
        
                    block['bAutoTrigger'] = B2()
                    block['EffectMask'] = S()
                    block['LayerEffectName'] = []
                    for i in range(1, 11):
                        efx = Str()
                        if efx:
                            block['LayerEffectName'].append(efx)
        
                    block['bAgeImmeExcute'] = B2()
                    block['bUseHUDInd'] = B2()
                    block['bHUDIndDir'] = B2()
                    block['bHUDIndProSlot'] = B1()
        
                    block['HUDIndColor'] = S()
                    block['HUDIndProColor'] = S()
                    block['IndPriority'] = int(S())
                    
                    block['bAutoTriggerOnDead'] = B2()
        
                    block['RotateFollowParent'] = int(S())
        
                    block['bSpecialBuffEffect'] = B2()
                    block['bInvisibleSelf'] = B2()
                    block['bInvisibleEnemy'] = B2()
                    block['bInvisibleTeamNotSelf'] = B2()
                    block['bDeadPreserve'] = B2()
                    blocks.append(block)
                except ValueError as e:
                    print(f"Error reading block at offset {offset}: {e}")
                    break
        
            return json.dumps(blocks, ensure_ascii=False, indent=4)
        
        
        def pack_string(value):
            encoded = value.encode('utf-8') + b'\x00'
            length = len(encoded)
            return struct.pack("<I", length) + encoded
        
        
        def JstoB(json_data, binary_file):
            blocks = json.loads(json_data)
            binary_data = bytearray()
            header = bytearray()
            header.extend(b'MSES\x07\x00\x00\x00')
            Blast = 0
            total_blocks = len(blocks)
            header.extend(struct.pack("<I", Blast))
            header.extend(struct.pack("<I", total_blocks))
            header.extend(b'\x61' * 32)
            header.extend(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            header.extend(b'\x00' * (140 - len(header)))
            binary_data.extend(header)
        
            def U(fmt, value):
                nonlocal block_data
                block_data.extend(struct.pack(fmt, value))
        
            def S1(value):
                nonlocal block_data
                block_data.extend(pack_string(value))
        
            for block in blocks:
                block_data = bytearray()
        
                U("<I", block.get('CfgID', 0))
                U("<I", block.get('DependCfgID', 0))
                
                S1(block.get('MarkName', ""))
                S1(block.get('MarkDesc', ""))
                S1(block.get('ActionName', ""))
                
                U("<I", block.get('MarkOverlapRule', 0))
        
                block_data.append(1 if block.get('bLayerEffect', False) else 0)
        
                U("<I", block.get('MaxLayer', 0))
                U("<I", block.get('OnlyTriggerLayer', 0))
                U("<I", block.get('CostLayer', 0))
                U("<I", block.get('TriggerLayer', 0))
                U("<I", block.get('ImmuneTime', 0))
                U("<I", block.get('LastMaxTime', 0))
                U("<I", block.get('CDTime', 0))
                U("<I", block.get('AddMarkImmuneTime', 0))
                
                block_data.append(1 if block.get('bAutoTrigger', False) else 0)
                
                U("<I", block.get('EffectMask', 0))
                
                layerefx = block.get("LayerEffectName", [])
                for i in range(10):
                    if i < len(layerefx):
                        S1(layerefx[i])
                    else:
                        S1("")
                block_data.append(1 if block.get('bAgeImmeExcute', False) else 0)
                block_data.append(1 if block.get('bUseHUDInd', False) else 0)
                block_data.append(1 if block.get('bHUDIndDir', False) else 0)
                block_data.append(block.get('bHUDIndProSlot', 0))
                
                U("<I", block.get('HUDIndColor', 0))
                U("<I", block.get('HUDIndProColor', 0))
                U("<I", block.get('IndPriority', 0))
                
                block_data.append(1 if block.get('bAutoTriggerOnDead', False) else 0)
        
                U("<I", block.get('RotateFollowParent', 0))
                
                block_data.append(1 if block.get('bSpecialBuffEffect', False) else 0)
                block_data.append(1 if block.get('bInvisibleSelf', False) else 0)
                block_data.append(1 if block.get('bInvisibleEnemy', False) else 0)
                block_data.append(1 if block.get('bInvisibleTeamNotSelf', False) else 0)
                block_data.append(1 if block.get('bDeadPreserve', False) else 0)
        
                Blen = len(block_data)
                final_block = struct.pack("<I", Blen) + block_data
                binary_data.extend(final_block)
                Bflast = Blen
         
        
            Blast = Bflast + 4
            binary_data[8:12] = struct.pack("<I", Blast)
            md5_hash = hashlib.md5(binary_data[140:]).hexdigest().encode('utf-8')
            binary_data[96:96 + len(md5_hash)] = md5_hash
            binary_data[140 - 12:140] = b'\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00'
        
            with open(binary_file, "wb") as bf:
                bf.write(binary_data)
        
        
        def process_file_skillmark(filename, mode):
            directory = os.path.dirname(filename)
            basename = os.path.basename(filename)
        
            if mode == 1:
                # bytes -> json
                with open(filename, "rb") as f:
                    json_data = B2Js(f.read())
                output_path = os.path.join(directory, "skillmark.bytes")
                with open(output_path, "w", encoding="utf-8") as json_file:
                    json_file.write(json_data)
        
            elif mode == 2:
                # json -> bytes
                with open(filename, "r", encoding="utf-8") as json_file:
                    json_data = json_file.read()
                output_path = os.path.join(directory, "skillmark.bytes")
                JstoB(json_data, output_path)
            else:
                print("Mode không hợp lệ! Chỉ dùng 1 (bytes->json) hoặc 2 (json->bytes).")

        HEADER_BYTES = bytes.fromhex('4D5345530700000082000000940000006161616161616161616161616161616161616161616161616161616161616161000000000000000000000000000000005554462D380000000000000000000000000000000000000000000000000000003838653064656464636165663833333762656433363464343937343436626561000000008C00000000000000')
        
        def bytes_to_xml(byte_data):
            xml_elements = []
            i = 0
            while i < len(byte_data):
                try:
                    total_length, track_id = struct.unpack_from('<I4s', byte_data, i)
                    track_id = int.from_bytes(track_id, byteorder='little')
        
                    action_name_length = struct.unpack_from('<I', byte_data, i + 9)[0]
                    action_name_end = i + 13 + action_name_length
                    action_name = byte_data[i + 13:action_name_end].decode('utf-8', errors='ignore').rstrip('\x00')
        
                    rong_start = action_name_end
                    rong = byte_data[rong_start:rong_start + 41]
                    resource_length = struct.unpack_from('<I', byte_data, rong_start + 41)[0]
                    resource_end = rong_start + 45 + resource_length
                    resource = byte_data[rong_start + 45:resource_end].decode('utf-8', errors='ignore').rstrip('\x00')
        
                    track = ET.Element('Track', ConfigID=str(track_id), BulletName=action_name, resource=resource, none=rong.hex())
                    xml_elements.append(ET.tostring(track, encoding='unicode'))
        
                    i = resource_end
                except struct.error:
                    break
        
            return '\n\n'.join(xml_elements)
        
        def save_xml_from_bytes(file_path):
            with open(file_path, 'rb') as file:
                byte_content = file.read()
        
            xml_content = bytes_to_xml(byte_content[140:])
            new_file_path = file_path.replace('.bytes', '.xml')
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(xml_content)
            os.remove(file_path)
        
        def xml_to_bytes(xml_str):
            byte_data = bytearray()
            root = ET.ElementTree(ET.fromstring(f'<root>{xml_str}</root>')).getroot()
        
            for track in root:
                track_id = int(track.attrib['ConfigID'])
                action_name = track.attrib['BulletName']
                rong = bytes.fromhex(track.attrib['none'])
                resource = track.attrib['resource']
                
                action_name_encoded = action_name.encode('utf-8')
                resource_encoded = resource.encode('utf-8')
                
                resource_length = len(resource_encoded) + 1
                action_name_length = len(action_name_encoded) + 1
                total_length = 13 + action_name_length + 41 + resource_length
        
                byte_data.extend(int_to_bytes(total_length, 4))
                byte_data.extend(int_to_bytes(track_id, 4))
                byte_data.append(0)
                byte_data.extend(int_to_bytes(action_name_length, 4))
                byte_data.extend(action_name_encoded)
                byte_data.append(0)
                byte_data.extend(rong)
                byte_data.extend(int_to_bytes(resource_length, 4))
                byte_data.extend(resource_encoded)
                byte_data.append(0)
        
            return bytes(byte_data)
        
        def int_to_bytes(value, length):
            return value.to_bytes(length, byteorder='little')
        
        def is_utf8(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file.read()
                return True
            except UnicodeDecodeError:
                return False
        
        def process_file_litebullet(file_path, option):
            filename = os.path.basename(file_path)
            if option == 1 and "liteBulletCfg" in filename and filename.endswith('.bytes'):
                save_xml_from_bytes(file_path)
            elif option == 2 and "liteBulletCfg" in filename and filename.endswith('.xml'):
                if is_utf8(file_path):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        xml_content = file.read()
                    byte_content = xml_to_bytes(xml_content)
                    new_file_path = file_path.replace('.xml', '.bytes')
                    with open(new_file_path, 'wb') as file:
                        file.write(HEADER_BYTES + byte_content)
                    os.remove(file_path)

        process_file_litebullet(file_mod_skill1, 1)
        file_mod_skill11 = f"{FolderMod}/Resources/{Ver}/Databin/Client/Skill/liteBulletCfg.xml"
        ID_SKIN = IDMODSKIN
        ID_SKIN = ID_SKIN.encode('utf-8')
        
        with open(file_mod_skill11, 'rb') as f:
            strin = f.read()
        
        try:
            heroname = re.compile(rb'hero_skill_effects/(' + ID_SKIN[:3] + rb'[^/]+)/')
            heroname = heroname.search(strin)
            hero_name = heroname.group(1)
        except AttributeError:
            print('   [-] Không Mod LiteBulletCfg Trên Mặc Định')
        else:
            print(hero_name)
            strin = strin.replace(
                b"Prefab_Skill_Effects/Hero_Skill_Effects",
                b"prefab_skill_effects/hero_skill_effects"
            ).replace(
                b"hero_skill_effects/" + hero_name + b"/",
                b"hero_skill_effects/" + hero_name + b"/" + ID_SKIN + b"/"
            )
        
            if ID_SKIN == b'11215':
                strin = strin.replace(b'<Track ConfigID="11200"',b'<Track ConfigID="11215235" BulletName="112s1b1" resource="prefab_skill_effects/hero_skill_effects/112_gongshuban/11215/gongshuban_attack01_spell01" none="983a0000000000000100003200000001000100010000000000000000000000000000007e04e803e803" />\n<Track ConfigID="11200"')
            
            if ID_SKIN == b'13311':
                strin = strin.replace(b"prefab_skill_effects/hero_skill_effects/133_direnjie/13311/",b"prefab_skill_effects/component_effects/13311/13311_5/")
            with open(file_mod_skill11, "wb") as f:
                f.write(strin)
    
            print('    [-] ' + os.path.basename(file_mod_skill1) + '    Done')
        process_file_litebullet(file_mod_skill11, 2)
        process_file_skillmark(file_mod_skill2,1)
        with open(file_mod_skill2, 'rb') as f:
            strin = f.read()
        
        try:
            namehero = re.compile(rb'hero_skill_effects/(' + ID_SKIN[:3] + rb'[^/]+)/')
            namehero = namehero.search(strin)
            name_hero = namehero.group(1)
        except AttributeError:
            print('   [-] Không Mod SkillMark Trên Mặc Định')
        else:
            print(name_hero)
            strin = strin.replace(
                b"Prefab_Skill_Effects/Hero_Skill_Effects",
                b"prefab_skill_effects/hero_skill_effects"
            ).replace(
                b"hero_skill_effects/" + name_hero + b"/",
                b"hero_skill_effects/" + name_hero + b"/" + ID_SKIN + b"/"
            )
            with open(file_mod_skill2, "wb") as f:
                f.write(strin)

            print('    [-] ' + os.path.basename(file_mod_skill2) + '    Done')
        process_file_skillmark(file_mod_skill2,2)
#-----------------------------------------------
    AllID=[]
    for i in range(21):
        if i<10: AllID.append(ID[0:3]+"0"+str(i))
        else: AllID.append(ID[0:3]+str(i))
    All_S=[]
    for i in AllID:
        i=hex(int(i))[2:]
        All_S.append(bytes.fromhex(f"{i[2:4]}{i[0:2]}0000"))
    with open(file_mod_Modtion,"rb") as f:
        begin=f.read(140)
        All_Code=[]
        while True:
            SL=f.read(2)
            if SL==b"": 
                f.close()
                break
            SL0=SL[0]+SL[1]*256+2
            Code=SL+f.read(SL0)
            if All_S[AllID.index(ID)] in Code: All_Code.append(Code)
            elif All_S[0] in Code: All_Code.append(Code)
    CodeDB=[]
    CodeMD=[]
    CodeMD2=[]
    for code in All_Code:
        if code[0:2] in b"6\x00S\x00": CodeDB.append(code)
        else:
            CodeMD.append(code)
            CodeMD2.append(code)
    aw=0
    if len(CodeDB)>1:
        print(f"Choose One Or {len(CodeDB)}: ",end="")
        aw=int(input())-1
    if len(CodeDB)>0:
        CodeR=CodeDB[aw]
        idmod=CodeR[21:25]
        for code in CodeMD:
            vtf=CodeMD.index(code)
            for id in All_S:
                vt=code.find(id)
                if vt!=-1:
                    codet=code[vt+4:vt+8]
                    code=code.replace(codet,idmod,1)
                else: break
            CodeMD[vtf]=code
    else:
        for code in CodeMD:
            vtr=CodeMD.index(code)
            vt=code.find(All_S[AllID.index(ID)])
            idmod=code[vt+4:vt+8]
            for id in All_S:
                vt=code.find(id)
                if vt!=-1:
                    codet=code[vt+4:vt+8]
                    code=code.replace(codet,idmod,1)
                else: break
            CodeMD[vtr]=code
    with open(file_mod_Modtion,"rb") as f:
        y=f.read()
        f.close()
    for i in range(len(CodeMD)): y=y.replace(CodeMD2[i],CodeMD[i],1)
    if len(CodeMD)+len(CodeDB)==0:
        for id in All_S: y=y.replace(id,b"00\x00\x00",1)
    with open(file_mod_Modtion,"wb") as f: f.write(y)
    #print("—" * 53)
    print(f"    Mod Motion ID: {IDMODSKIN}")
#-----------------------------------------------
    Files_Directory_Path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod4/'
    with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDMODSKIN[:3]}'+'_Actions.pkg.bytes') as File_Zip:
        File_Zip.extractall(Files_Directory_Path)
        File_Zip.close()
    HERO_NAME_LIST = os.listdir(Files_Directory_Path)
    for HERO_NAME_ITEM in HERO_NAME_LIST:
        NAME_HERO = HERO_NAME_ITEM
    if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod or IDCHECK == "53702":

        new_folder_path = Files_Directory_Path
        new_files_list = os.listdir(new_folder_path)
        NAME_HERO = new_files_list
        effect_name = NAME_HERO
        for new_file_item in new_files_list:
            effect_name = new_file_item
        for name1 in NAME_HERO:
            NAME_HERO = name1
        directory_path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'

    Id_Skin = IDMODSKIN.encode()
    Name_Hero = NAME_HERO.encode()
    HD = b'y'
    Skins = b'n'

    FILES_XML = []
    for root, dirs, files in os.walk(Files_Directory_Path):
        for file in files:
            if file.endswith('.xml'):
                FILES_XML.append(os.path.join(root, file))

    for file_path in FILES_XML:
        giai(file_path)

        with open(file_path, 'rb') as f:
            All = f.read()

        if b'"Jg\x00' not in All:
            ListAll = All.split(b'\r\n')
            CODE_EFF = [x for x in ListAll if b'prefab_skill_effects/hero_skill_effects/' in x.lower()]
            if len(CODE_EFF) == 0:
                continue

            for text in CODE_EFF:
                if b'<String name="prefabName"' in text:
                    continue
                if Id_Skin not in [b'13311', b'16707']:
                    text1 = re.sub(
                        re.escape(b"prefab_skill_effects/hero_skill_effects/" + Name_Hero + b'/'),
                        b"prefab_skill_effects/hero_skill_effects/" + Name_Hero + b'/' + Id_Skin + b'/',
                        text,
                        flags=re.IGNORECASE
                    )
                    text1 = text1.replace(b'/' + Id_Skin + b'/' + Id_Skin + b'/', b'/' + Id_Skin + b'/')
                else:
                    ID_EOV = Id_Skin + b'_5/'
                    text1 = re.sub(
                        re.escape(b"prefab_skill_effects/hero_skill_effects/" + Name_Hero + b'/'),
                        b"prefab_skill_effects/component_effects/" + Id_Skin + b'/' + ID_EOV,
                        text,
                        flags=re.IGNORECASE
                    )

                if HD == b'y':
                    text1 = text1.replace(b'" refParamName=""', b'.prefab" refParamName=""')
                    text1 = text1.replace(b'_E.prefab"', b'_E"').replace(b'_e.prefab"', b'_e"')
                    text1 = text1.replace(b'.prefab.prefab" refParamName=""', b'.prefab" refParamName=""')

                All = All.replace(text, text1)
            if Skins == b'y' and b'bUseTargetSkinEffect' not in All:
                new_lines = []
                for line in All.split(b'\r\n'):
                    new_lines.append(line)
                    if b'<String name="resourceName"' in line:
                        new_lines.append(b'        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>')
                All = b'\r\n'.join(new_lines)
            All = All.replace(b'bAllowEmptyEffect" value="true"', b'bAllowEmptyEffect" value="false"')
            with open(file_path, 'wb') as f:
                f.write(All)
            AABBCC = 'YtbTâmModAOV'
#---------------—------------———----------------
            if IDMODSKIN == '10611' and 'U1B1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = re.sub(
                        br'<Condition id="[^"]+" guid="2e5f463f-105d-4143-b786-e59ea8b34fa2" status="true" />',
                        b'<!-- ' + AABBCC.encode('utf-8') + b' -->', rpl)
                    rpl=rpl.replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/106_xiaoqiao/xiaoqiao_skill03_cutin" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/106_xiaoqiao/10611/xiaoqiao_skill03_cutin" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '10611' and 'A3.xml' in file_path: 
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="clipName" value="Atk3"', b'<String name="clipName" value="Atk1"')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '11215':
                with open(file_path, "rb") as f:
                    All = f.read()
                
                All = re.sub(
                    rb'(<Track trackName=".*?</Track>)',
                    lambda m: m.group(1) if (
                        b"random" in m.group(1).lower() or b"spawnobjectduration" in m.group(1).lower()
                    ) else b'\n'.join(
                        line for line in m.group(1).splitlines() if b"SkinOrAvatar" not in line
                    ),
                    All,
                    flags=re.DOTALL
                )
                
                with open(file_path, "wb") as f:
                    f.write(All)
#---------------—------------———----------------
            if IDMODSKIN == '13213' and 'S1B1.xml' in file_path:
                with open(file_path, "rb") as f:
                    All = f.read()
                
                All = re.sub(
                    rb'(<Track trackName=".*?</Track>)',
                    lambda m: m.group(1) if b"random" in m.group(1).lower() else b'\n'.join(
                        line for line in m.group(1).splitlines() if b"SkinOrAvatar" not in line
                    ),
                    All,
                    flags=re.DOTALL
                )
                
                with open(file_path, "wb") as f:
                    f.write(All)
                
#---------------—------------———----------------
            if IDMODSKIN == '59901' and 'S1E60.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/599_LvMeng/5991_LvMeng_Shak_Mid" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/599_LvMeng/59901/5991_LvMeng_Shak_Mid" refParamName="" useRefParam="false" />').replace(b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/599_LvMeng/5991_LvMeng_Shak" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/599_LvMeng/59901/5991_LvMeng_Shak" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '59901' and 'S1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'</Action>',b'    <Track trackName="SetAnimationParamsTick0" eventType="SetAnimationParamsTick" guid="c2e40485-fa44-4c14-a09b-1d2e010bce50" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\r\n      <Event eventName="SetAnimationParamsTick" time="0.000" isDuration="false" guid="d376c3bc-4c1d-4c28-8198-cfe33a7f29d2">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <Array name="boolNames" refParamName="" useRefParam="false" type="String">\r\n          <String value="Spell1_1_Start" />\r\n        </Array>\r\n        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">\r\n          <bool value="true" />\r\n        </Array>\r\n      </Event>\r\n      <SkinOrAvatarList id="59998" />\r\n    </Track>\r\n    <Track trackName="SetAnimationParamsTick0" eventType="SetAnimationParamsTick" guid="1f2d81a7-47bc-4ba1-8ea4-3f8d6631872c" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\r\n      <Event eventName="SetAnimationParamsTick" time="0.066" isDuration="false" guid="67735e55-debf-43ab-9854-0f65154bf4f8">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <Array name="boolNames" refParamName="" useRefParam="false" type="String">\r\n          <String value="Spell1_1_Start" />\r\n        </Array>\r\n        <Array name="boolValues" refParamName="" useRefParam="false" type="bool">\r\n          <bool value="false" />\r\n        </Array>\r\n      </Event>\r\n      <SkinOrAvatarList id="59998" />\r\n    </Track>\r\n    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="f367f53c-2614-4451-8662-1d6c9abf8d19" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" OrConditions="true" SkinAvatarFilterType="11">\r\n      <Event eventName="PlayAnimDuration" time="0.000" length="1.000" isDuration="true" guid="96b1fc43-7446-4e66-ac22-d6617f0c1dde">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="clipName" value="Spell1_11" refParamName="" useRefParam="false" />\r\n        <int name="layer" value="3" refParamName="" useRefParam="false" />\r\n        <float name="endTime" value="999999.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="59998" />\r\n    </Track>\r\n  </Action>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] == '111':
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/sunshangxiang',
                    b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/'+IDMODSKIN+b'/sunshangxiang'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '11107' and 'death.xml' not in file_path.lower():
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="clipName" value="',
                    b'<String name="clipName" value="11107/'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '51504' and 'death.xml' not in file_path.lower():
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="clipName" value="',
                    b'<String name="clipName" value="51504/'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '12304' and 'death.xml' not in file_path.lower():
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="clipName" value="',
                    b'<String name="clipName" value="12304/'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '15704' and 'death.xml' not in file_path.lower():
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="clipName" value="',
                    b'<String name="clipName" value="15704/'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] == '173':
                with open(file_path, 'rb') as f:
                    rpl = f.read()

                    rpl = re.sub(
                    b'prefab_skill_effects/hero_skill_effects/173_liyuanfang/' + re.escape(IDMODSKIN.encode()) + b'/Liyuanfang_buff01_spell03', b'prefab_skill_effects/hero_skill_effects/173_liyuanfang/Liyuanfang_buff01_spell03', rpl)

                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '53802':
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'prefab_skill_effects/hero_skill_effects/538_Iggy/53802/Iggy_Spell3_Circle_01_E',
                    b'prefab_skill_effects/hero_skill_effects/538_Iggy/Iggy_Spell3_Circle_01_E')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '50108' and 'U1E2.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/501_TelAnnas/501_Teer_spellC',b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/501_TelAnnas/50108/501_Teer_spellC').replace(b'        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '54402' and 'U1B1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/544_Painter/Painter_spell03_cutin" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_spell03_cutin" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '54402' and 'U1E0.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/544_Painter/Painter_spell03_camera" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_spell03_camera" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '11620' and 'S3.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<SkinOrAvatarList id="11620" />',b'')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '11620' or IDMODSKIN == b'11620':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
            
                if phukienb == 'tim':
                    rpl = re.sub(
                        br'prefab_skill_effects/hero_skill_effects/116_Jingke/11620/',
                        b'prefab_skill_effects/Component_Effects/11620/1162001/',
                        rpl, flags=re.IGNORECASE
                    )
                    rpl = re.sub(br'11620/11620_3/', b'11620/1162001/', rpl, flags=re.IGNORECASE)
                    rpl = re.sub(br'11620/1162001/11607/11607_huijidi_01', b'11607/11607_huijidi_01', rpl, flags=re.IGNORECASE)
            
                elif phukienb == 'do':
                    rpl = re.sub(
                        br'prefab_skill_effects/hero_skill_effects/116_Jingke/11620/',
                        b'Prefab_Skill_Effects/Component_Effects/11620/1162002/',
                        rpl, flags=re.IGNORECASE
                    )
                    rpl = re.sub(br'11620/11620_3/', b'11620/1162002/', rpl, flags=re.IGNORECASE)
                    rpl = re.sub(br'11620/1162002/11607/11607_huijidi_01', b'11607/11607_huijidi_01', rpl, flags=re.IGNORECASE)
            
                else:
                    rpl = re.sub(br'prefab_skill_effects/hero_skill_effects/116_Jingke/11620/', 
                                 b'prefab_skill_effects/component_effects/11620/11620_5/', rpl, flags=re.IGNORECASE)
            
                    rpl = re.sub(br'prefab_skill_effects/hero_skill_effects/116_JingKe/11620/11620_5/11607', 
                                 b'prefab_skill_effects/component_effects/11620/11620_5/', rpl, flags=re.IGNORECASE)
            
                    rpl = re.sub(br'11620/11620_3/', b'11620/11620_5/', rpl, flags=re.IGNORECASE)
            
                    rpl = re.sub(br'11620/11620_5/11607/11607_huijidi_01', b'11607/11607_huijidi_01', rpl, flags=re.IGNORECASE)
            
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='13613' and 'S1E1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'</Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'</Event>\r\n    </Track>\r\n    <Track trackName="Youtuber_You_Mod_Skin" eventType="TriggerParticleTick" guid="daa65ca6-798c-4280-84b3-171fc3a73a82" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="5f30bc82-d28a-4b25-b3a6-92fc32eac064">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13613/WuZeTian_hurt02" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="0.600" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='13613' and 'S1E2.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'</Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'</Event>\r\n    </Track>\r\n    <Track trackName="Youtuber_You_Mod_Skin" eventType="TriggerParticleTick" guid="daa65ca6-798c-4280-84b3-171fc3a73a82" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="5f30bc82-d28a-4b25-b3a6-92fc32eac064">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13613/WuZeTian_hurt02" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="0.600" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='13613' and 'S1E3.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'</Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'</Event>\r\n    </Track>\r\n    <Track trackName="Youtuber_You_Mod_Skin" eventType="TriggerParticleTick" guid="daa65ca6-798c-4280-84b3-171fc3a73a82" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="5f30bc82-d28a-4b25-b3a6-92fc32eac064">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13613/WuZeTian_hurt02" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="0.600" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')

                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13613' and 'S1B1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Vector3 name="scaling" x="1.300" y="1.000" z="1.000" refParamName="" useRefParam="false" />', b'<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false" />')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '51015' or IDMODSKIN == b'51015':
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                        b'SkinAvatarFilterType="9">', b'SkinAvatarFilterType="8">'
                    ).replace(
                        b'SkinAvatarFilterType="11">', b'SkinAvatarFilterType="9">'
                    ).replace(
                        b'SkinAvatarFilterType="8">', b'SkinAvatarFilterType="11">'
                    ).replace(
                        b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/510_Liliana/5101_Fox" refParamName="" useRefParam="false" />',
                        b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/510_Liliana/' +
                        IDMODSKIN.encode() + 
                        b'/5101_Fox" refParamName="" useRefParam="false" />'
                    )
            
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] =='510' and 'U11.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Track trackName="ChangeActorMeshTick0" eventType="ChangeActorMeshTick" guid="3b065f40-1044-4f90-a2d5-1be4f1a968ee" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">', b'<Track trackName="ChangeActorMeshTick0" eventType="ChangeActorMeshTick" guid="3b065f40-1044-4f90-a2d5-1be4f1a968ee" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] =='537' and 'S12.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S',b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDCHECK =='53702' and "S13B1.xml" in file_path and "S14B1.xml" in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/537_Trip/53702/Trip_attack_spell01_Indicator',b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_Indicator')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13314':
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<SkinOrAvatarList id="13314" />',b'')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN == '13314' and 'skin14E3.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'      </Event>\r\n',b'      </Event>\r\n      <SkinOrAvatarList id="23714" />').replace(b'SkinAvatarFilterType="9">', b'SkinAvatarFilterType="11">')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN == '13314' and 'U1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'      </Event>\r\n      \r\n    </Track>\r\n  </Action>\r\n</Project>',b'      </Event>\r\n      <SkinOrAvatarList id="13314" />\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '59802' and 'P0E1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/598_DaSiKong/59800_DaSiKong_BianShen" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/598_DaSiKong/59802/59800_DaSiKong_BianShen" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)

#---------------—------------———----------------
            if IDMODSKIN[:3] =='537' and 'Change.xml' in file_path and 'ChangeB.xml' in file_path :
                with open(file_path, 'rb') as f:
                                rpl = f.read().replace(b'537_Trip/',b'537_Trip/53702/')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='59702' and 'P1E01.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'e40d96061260" enabled="true"',b'e40d96061260" enabled="false"')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='59702' and 'P2.xml'in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/KuangTie_attack02_spell02A_1',b'prefab_skill_effects/hero_skill_effects/597_kuangtie/59702/KuangTie_attack02_spell02A_1')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='59702' and 'U1.xml'in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/KuangTie_attack_spell03_1" refParamName="" useRefParam="false" />', b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/597_kuangtie/59702/KuangTie_attack_spell03_1" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='59702' and 'U11.xml'in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/KuangTie_attack02_spell03_1" refParamName="" useRefParam="false" />', b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/597_kuangtie/59702/KuangTie_attack02_spell03_1" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] == '521':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                if IDMODSKIN != '52108' and any(x in file_path for x in ['S1B3', 'S1B4']):
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_2"', b'Florentino_spell01_bullet03"')
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_fade_2"', b'Florentino_spell01_bullet03_fade"')
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_2_e"', b'Florentino_spell01_bullet03_e"')
                    rpl = rpl.replace(b'Florentino_spell01_buff01_2"', b'Florentino_spell01_buff01"')
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_3"', b'Florentino_spell01_bullet03"')
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_fade_3"', b'Florentino_spell01_bullet03_fade"')
                    rpl = rpl.replace(b'Florentino_spell01_bullet03_3_e"', b'Florentino_spell01_bullet03_e"')
                    rpl = rpl.replace(b'Florentino_spell01_buff01_3"', b'Florentino_spell01_buff01"')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '11120' and 'A1B1.xml' in file_path:
                with open(file_path, 'rb') as f: sec = f.read().replace(b'</Action>', b'  <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="5.000" isDuration="true" guid="6d868a6f-8ee5-477f-b215-8168ab03ce28">\n        <String name="OutputLiteBulletName" value="111a4b1" refParamName="" useRefParam="false"/>\n        <uint name="ConfigID" value="11102" refParamName="" useRefParam="false"/>\n        <TemplateObject name="ReferenceID" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\n        <TemplateObject name="TargetID" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Condition id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" status="true"/>\n      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="c0253b7e-2e8c-461d-919a-e5617c64555b">\n        <TrackObject name="trackId" id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n  </Action>')
                with open(file_path,'wb') as f: f.write(sec)
            if IDMODSKIN == '11120' and 'A2B1.xml' in file_path:
                with open(file_path, 'rb') as f: sec = f.read().replace(b'</Action>', b'  <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="5.000" isDuration="true" guid="6d868a6f-8ee5-477f-b215-8168ab03ce28">\n        <String name="OutputLiteBulletName" value="111a2b1" refParamName="" useRefParam="false"/>\n        <uint name="ConfigID" value="11101" refParamName="" useRefParam="false"/>\n        <TemplateObject name="ReferenceID" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\n        <TemplateObject name="TargetID" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Condition id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" status="true"/>\n      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="c0253b7e-2e8c-461d-919a-e5617c64555b">\n        <TrackObject name="trackId" id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n  </Action>')
                with open(file_path,'wb') as f: f.write(sec)
            if IDMODSKIN == '11120' and 'A4B1.xml' in file_path:
                with open(file_path, 'rb') as f: sec = f.read().replace(b'</Action>', b'  <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="5.000" isDuration="true" guid="6d868a6f-8ee5-477f-b215-8168ab03ce28">\n        <String name="OutputLiteBulletName" value="111a4b1" refParamName="" useRefParam="false"/>\n        <uint name="ConfigID" value="11102" refParamName="" useRefParam="false"/>\n        <TemplateObject name="ReferenceID" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\n        <TemplateObject name="TargetID" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" SkinAvatarFilterType="11">\n      <Condition id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" status="true"/>\n      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="c0253b7e-2e8c-461d-919a-e5617c64555b">\n        <TrackObject name="trackId" id="10" guid="\xe9\x83\x91\xe5\x87\xaf\xe6\x98\x8e" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="11119"/>\n      <SkinOrAvatarList id="11120"/>\n    </Track>\n  </Action>')
                with open(file_path,'wb') as f: f.write(sec)
#---------------—------------———----------------
            if IDMODSKIN == '10603' and 'death.xml' not in file_path.lower():
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<String name="clipName" value="',
                    b'<String name="clipName" value="10603/'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] == '540' and 'U1B1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/540_Bright/5401_Bright_God" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/540_Bright/'+ IDMODSKIN.encode() + b'/5401_Bright_God" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '54402' and 'A4B1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_Atk4_blue',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_blue').replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_Atk4_red',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_red')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '15412' and 'P12E2.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/15413_HuaMuLan_Red', b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15413_HuaMuLan_Red')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN == '15412' and 'U1B0.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/huamulan_Skill_pingmu" refParamName="" useRefParam="false" />', b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huamulan_Skill_pingmu" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN == '15412' and 'T1B0.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/huamulan_Skill_pingmu" refParamName="" useRefParam="false" />', b'<String name="prefab" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huamulan_Skill_pingmu" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '19015' and 'U1B0.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />',b'').replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/190_ZhuGeLiang/19015/19009/Zhugeliang_attack01_spell03_UI" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/190_ZhuGeLiang/19015/Zhugeliang_attack01_spell03_UI" refParamName="" useRefParam="false" />').replace(b'<Track trackName="19015" eventType="CheckSkinIdVirtualTick" guid="b66d59b2-b5f0-4365-870a-a57357f5df93" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">',b'<Track trackName="19015" eventType="CheckSkinIdTick" guid="b66d59b2-b5f0-4365-870a-a57357f5df93" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'<Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="17c9207c-19af-4061-9d63-109437868f7d">',b'<Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="17c9207c-19af-4061-9d63-109437868f7d">')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN  == '19015':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                rpl = rpl.replace(b'SkinAvatarFilterType="9">',b'SkinAvatarFilterType="8">').replace(b'SkinAvatarFilterType="11">',b'SkinAvatarFilterType="9">').replace(b'SkinAvatarFilterType="8">',b'SkinAvatarFilterType="11">')
                rpl = re.sub(
                    br'<int name="skinId" value="19015" refParamName="" useRefParam="false"\s*/?>',
                    b'<int name="skinId" value="19000" refParamName="" useRefParam="false" />',
                    rpl
                )
                rpl = re.sub(
                    br'<SkinOrAvatarList\s+id="19015"\s*/?>',
                    b'<SkinOrAvatarList id="99999" />',
                    rpl
                )
                with open(file_path, 'wb') as f:
                    f.write(rpl)

#---------------—------------———----------------
            if IDMODSKIN =='52007':
                if phukien == "do":
                    with open(file_path, 'rb') as f:
                        rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',b'prefab_skill_effects/component_effects/52007/5200402/')
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
                elif phukien == "xanh":
                    with open(file_path, 'rb') as f:
                        rpl = f.read().replace(
                b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',
                b'prefab_skill_effects/component_effects/52007/5200401/'
            )
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='13015' and 'A4.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<bool name="useNegateValue" value="true"', b'<bool name="useNegateValue" value="false"')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '15013' and'A1.xml'in file_path and 'A2.xml' in file_path and 'A3.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true"',b'guid="9d243092-f160-4189-a9da-f132595032c9" enabled="false"')
                with open(file_path, 'wb') as f:
                    f.write(rpl)          
            if IDMODSKIN == '15013' and'S2.xml'in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl=rpl.replace(b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'<int name="skinId" value="15013" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'<Track trackName="StopTrack0" eventType="StopTrack" guid="89e9fe10-5e42-48ab-9645-51638a7d13dd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="14" guid="b73050c0-0afc-4e3b-98e2-6ffe12d3d489" status="true" />\r\n      <Condition id="15" guid="84b2cbba-51cc-4673-adab-a3624a854953" status="false" />',b'<Track trackName="StopTrack0" eventType="StopTrack" guid="89e9fe10-5e42-48ab-9645-51638a7d13dd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="15" guid="84b2cbba-51cc-4673-adab-a3624a854953" status="false" />').replace(b'eventType="CheckActorPositionDuration" guid="173653f1-8aaf-47ee-84a3-92cf343f6711" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="14" guid="b73050c0-0afc-4e3b-98e2-6ffe12d3d489" status="true" />',b'eventType="CheckActorPositionDuration" guid="173653f1-8aaf-47ee-84a3-92cf343f6711" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'eventType="HitTriggerTick" guid="20bc71d4-b49e-44a2-a23e-a44e663ba943" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="14" guid="b73050c0-0afc-4e3b-98e2-6ffe12d3d489" status="true" />',b'eventType="HitTriggerTick" guid="20bc71d4-b49e-44a2-a23e-a44e663ba943" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'<Track trackName="SetAnimationParamsTick0" eventType="SetAnimationParamsTick" guid="5006012f-c7cf-484b-943b-4b0350bbd0b0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="37" guid="173653f1-8aaf-47ee-84a3-92cf343f6711" status="false" />\r\n      <Condition id="14" guid="b73050c0-0afc-4e3b-98e2-6ffe12d3d489" status="true" />',b'<Track trackName="SetAnimationParamsTick0" eventType="SetAnimationParamsTick" guid="5006012f-c7cf-484b-943b-4b0350bbd0b0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="37" guid="173653f1-8aaf-47ee-84a3-92cf343f6711" status="false" />').replace(b'</Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'</Event>\r\n    </Track>\r\n    <Track trackName="SetAnimationParamsTick0" eventType="SetAnimationParamsTick" guid="ecc440c2-8021-4dc0-958a-b812278d2407" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="37" guid="173653f1-8aaf-47ee-84a3-92cf343f6711" status="true" />\r\n      <Condition id="-1" guid="" status="true" />\r\n      <Condition id="14" guid="b73050c0-0afc-4e3b-98e2-6ffe12d3d489" status="false" />\r\n      <Event eventName="SetAnimationParamsTick" time="0.000" isDuration="false" guid="f2d3828f-602b-4092-9a2c-7c139d7be8c4">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <Array name="floatNames" refParamName="" useRefParam="false" type="String">\r\n          <String value="RandomSpell2" />\r\n        </Array>\r\n        <Array name="floatValues" refParamName="" useRefParam="false" type="float">\r\n          <float value="0.500" />\r\n        </Array>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13706':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'<SkinOrAvatarList id="13706" />',b'<SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />\n      <SkinOrAvatarList id="13706" />').replace(b'        <bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />',b'        <bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false" />\r\n      </Event>').replace(
b'        <int name="changeSkillID" value="13705" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />',b'        <int name="changeSkillID" value="13705" refParamName="" useRefParam="false" />\r\n      </Event>').replace(
b'        <int name="changeSkillID" value="13702" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />',b'        <int name="changeSkillID" value="13702" refParamName="" useRefParam="false" />\r\n      </Event>').replace(
b'        <int name="changeSkillID" value="13703" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />',b'        <int name="changeSkillID" value="13703" refParamName="" useRefParam="false" />\r\n      </Event>').replace(
b'        <int name="changeSkillID" value="13700" refParamName="" useRefParam="false" />\r\n      </Event>\r\n      <SkinOrAvatarList id="13700" />\n      <SkinOrAvatarList id="13701" />\n      <SkinOrAvatarList id="13702" />\n      <SkinOrAvatarList id="13703" />\n      <SkinOrAvatarList id="13704" />\n      <SkinOrAvatarList id="13705" />\n      <SkinOrAvatarList id="13707" />\n      <SkinOrAvatarList id="13708" />\n      <SkinOrAvatarList id="13709" />',b'        <int name="changeSkillID" value="13700" refParamName="" useRefParam="false" />\r\n      </Event>')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN == '13706' and 'S4.xml':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = rpl.replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/137_simayi/SiMaYi_SkillHud" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/137_simayi/13706/SiMaYi_SkillHud" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13011' and 'S2.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckSkinIdTick" guid="1d2453a9-f234-4489-90f4-dde12f642d17" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="77eedf3b-88d2-466f-b13c-d8e44504dc8d">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckHeroIdTick" guid="1d2453a9-f234-4489-90f4-dde12f642d17" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="77eedf3b-88d2-466f-b13c-d8e44504dc8d">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="130" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN == '13011' and 'S21.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read() 
                    rpl = rpl.replace(b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckSkinIdTick" guid="753f3471-d461-40e5-b0d9-9305c2d4615d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="d302841f-faf8-4336-9895-50109a87ca31">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckHeroIdTick" guid="753f3471-d461-40e5-b0d9-9305c2d4615d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="d302841f-faf8-4336-9895-50109a87ca31">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="130" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>').replace(b"""<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">""",b"""<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">""").replace(b"GongBenWuZang_attack01_spell01_2",b"GongBenWuZang_attack01_spell01_1")
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN == '13011' and 'S22.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckSkinIdTick" guid="cea185dc-6db5-47e8-9a5f-fbf0f2aabacb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="df5f721f-659b-4ce7-8ae0-a869b902e35e">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'    <Track trackName="T2skin\xe7\xbe\x8e\xe6\x9c\xaftrue" eventType="CheckHeroIdTick" guid="cea185dc-6db5-47e8-9a5f-fbf0f2aabacb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="df5f721f-659b-4ce7-8ae0-a869b902e35e">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="130" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>').replace(b"""<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">""",b"""<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="a07302eb-cb3b-4146-9996-d018f92247aa" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">""").replace(b"GongBenWuZang_attack01_spell01_3",b"GongBenWuZang_attack01_spell01_2")
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN == '13011' and 'S2.xml' not in file_path and 'S21.xml' not in file_path and 'S22.xml' not in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />>\r\n        <<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />>\r\n        <<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='13015' and 'A4.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />',b'')
                with open(file_path, 'wb') as f:
                    f.write(rpl)

#---------------—------------———----------------
            if IDMODSKIN[:3] =='524' and 'A1E9.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/524_Capheny/'+IDMODSKIN.encode()+b'/Atk1_FireRange',b'prefab_skill_effects/hero_skill_effects/524_Capheny/Atk1_FireRange')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13112'and'P1E5.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN == '13111'and'P1E5.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bone_Weapon01').replace(b'Bip001 Prop1',b'Bone_Weapon01')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN == '13116'and'P1E5.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN[:3] =='537' and 'S12.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S',b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='11119' and 'A1B1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />', b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="750" z="0" refParamName="" useRefParam="false" />')
                with open(file_path,'wb') as f: 
                    f.write(rpl)
#---------------—------------———----------------
                if IDMODSKIN =='11119' and 'A2B1.xml' in file_path:
                    with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="700" z="0" refParamName="" useRefParam="false" />')
                    with open(file_path,'wb') as f: 
                        f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13112' and 'P1E5.xml'in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13111' and 'P1E5.xml'in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bone_Weapon01').replace(b'Bip001 Prop1',b'Bone_Weapon01')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13116' and 'P1E5.xml'in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                with open(file_path,'wb') as f: f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN =='14111' and 'S1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Event eventName="PlayAnimDuration" time="0.000" length="1.167" isDuration="true" guid="8c3310a3-4c0c-44ce-9f4e-6273c7d05d98">',b'<Event eventName="PlayAnimDuration" time="0.000" length="1.700" isDuration="true" guid="8c3310a3-4c0c-44ce-9f4e-6273c7d05d98">').replace(b'      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="1" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="TriggerParticle" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.700" isDuration="true" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/14111_spell01_A.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.500" z="1.200" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="TriggerParticle" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.700" isDuration="true" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/14111_spell01_B.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.500" z="1.200" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN =='14111' and 'S1B1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="CheckSkinIdVirtualTick0" eventType="CheckSkinIdVirtualTick" guid="8f286ccb-5124-446a-a1b1-b72f7a82dd09" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdVirtualTick" time="0.000" isDuration="false" guid="3a8b83a4-4375-4c7f-9ba1-e9a1459303c3">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="14118" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="f4847356-eaf3-4669-b9ad-ba78401b4c5b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.600" isDuration="true" guid="554fdc14-4ac7-4685-8160-9950a8be03f1">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_Diaochan/14111/diaochan_attack_spell01.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.500" z="1.200" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="CheckSkillCombineConditionTick0" eventType="CheckSkillCombineConditionTick" guid="5ccf0732-2aa3-4f64-b2f9-bd6de2e6afd9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="8f286ccb-5124-446a-a1b1-b72f7a82dd09" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="66fc6cfc-7779-4faa-8a7d-d761e49984ed">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141921" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="18\xe7\x9a\xae\xe8\x82\xa4\xe5\xbc\x80\xe5\xa4\xa7\xe4\xbb\xa5\xe5\x90\x8e\xe5\x8f\x91\xe6\x8b\x9b" eventType="TriggerParticle" guid="32288ab6-074b-4d86-820d-8ce3dc813663" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="5ccf0732-2aa3-4f64-b2f9-bd6de2e6afd9" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.600" isDuration="true" guid="905c16af-30f5-43da-88dd-0d98ae56640c">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_Diaochan/14111/14118_spell01_B.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
,b'    <Track trackName="CheckHeroIdTick0" eventType="CheckHeroIdTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="3a8b83a4-4375-4c7f-9ba1-e9a1459303c3">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="141" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="1" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />    \t\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n        <bool name="bCopyActorUseSrcActor" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="TriggerParticle" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />    \t\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.600" isDuration="true" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/diaochan_attack_spell01.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.500" z="1.200" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="TriggerParticle" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />    \t\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.600" isDuration="true" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/diaochan_attack_spell01_S.prefab" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.500" z="1.200" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN =='14111' and 'S1B2.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="14118\xe6\xa3\x80\xe6\xb5\x8b" eventType="CheckSkinIdTick" guid="4cd2db1b-e00b-4b71-916f-e9c0b1b21d07" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="03d1e9c3-a23a-4ead-aaf8-7cd333b318b4">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="14118" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c6a98de8-8f76-4f6b-8f80-1bcd17efbc2c" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="4" guid="4cd2db1b-e00b-4b71-916f-e9c0b1b21d07" status="false" />\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="a4c68b42-3e79-4aa1-8af2-451b9e077923">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_Diaochan/14111/diaochan_attack_spell01_1.prefab" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="CheckSkillCombineConditionTick" guid="b37bdadd-b8c9-440e-9ea0-2705476cc057" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="4" guid="4cd2db1b-e00b-4b71-916f-e9c0b1b21d07" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="a88e4c5e-b65e-4bbf-851d-1bd898e9f7d0">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="685ff200-95ad-4b43-8471-83a9572b039b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="b37bdadd-b8c9-440e-9ea0-2705476cc057" status="false" />\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="9d4c8390-89f0-4ed4-96f3-18dc7af1d978">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_Diaochan/14111/diaochan_attack_spell01_1.prefab" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="90043ce2-7a80-4e53-b87d-944fe49f7924" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="b37bdadd-b8c9-440e-9ea0-2705476cc057" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="96d74687-1dc4-4407-ab36-663b1eb619b2">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/141_Diaochan/14111/diaochan_attack_spell01_1_S.prefab" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>', b'    <Track trackName="CheckHeroIdTick0" eventType="CheckHeroIdTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="03d1e9c3-a23a-4ead-aaf8-7cd333b318b4">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="141" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="1" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n     <Track trackName="BUFF" eventType="CheckSkillCombineConditionTick" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />     \t\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="141920" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="NOBUFF" eventType="TriggerParticleTick" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-NOBUFF" status="true"/>\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/diaochan_attack_spell01_1.prefab" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="BUFF" eventType="TriggerParticleTick" guid="MOD-BY-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111" status="true" />    \t\r\n      <Condition id="0" guid="MOD-BY-Tran_Thi_Nhung-FIX-14111-BUFF" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="Tran_Thi_Nhung">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/diaochan_attack_spell01_1_S.prefab" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="Prefab_Skill_Effects/Hero_Skill_Effects/141_DiaoChan/14111/diaochan_attack_spell01_1_S_B.prefab" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN == '15015' and 'U1.xml' not in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(
                    b'<int name="skinId" value="15015" refParamName="" useRefParam="false" />',
                    b'<int name="skinId" value="15015" refParamName="" useRefParam="false" />\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />'
        )
                with open(file_path, 'wb') as f:
                    f.write(rpl)
            if IDMODSKIN =='15015'and'U1.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl=re.sub(b'"resourceName" value="(.*?)"', b'"resourceName" value="Mod_By_Tran_Thi_Nhung_Mod_15015"', rpl).replace(b'  </Action>',b'    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="57036c14-d685-4131-9f93-9a4c65ac9929" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="28" guid="c0b9dcbe-c83f-4a57-b203-70a202308416" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.067" isDuration="false" guid="ca1ffb7f-b6a8-4320-b14a-f4f2b6e5084d">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n       <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="5d4a923f-56f2-4670-ac7e-1c6692324f59" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="0.367" isDuration="false" guid="b596efb1-714d-4626-bfed-5d53a538b7e1">\r\n       <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell02" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="aaf02147-7a99-4c02-99d8-89b6e16fc5a3" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="28" guid="c0b9dcbe-c83f-4a57-b203-70a202308416" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.967" isDuration="false" guid="7fdcb80c-b70e-4561-994b-eaf31b8f27d0">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell03" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="888f2edc-d3a7-4a18-bb56-647f9678cf07" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="0.466" isDuration="false" guid="b6eb7044-1230-47fe-92c3-e017d0694f3e">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell04" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle1" eventType="TriggerParticle" guid="4ba448f3-97b2-4763-b956-63a0dcecf458" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="39" guid="6e38b810-2c03-4c25-9331-fd09a03cb2e2" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.100" length="2.000" isDuration="true" guid="0c29a8c5-d7cd-4b8e-b7c8-02ad44aeb5c3">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n       <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell01a" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="128c3dc2-2ceb-4c50-845d-540db4c2ea24" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="39" guid="6e38b810-2c03-4c25-9331-fd09a03cb2e2" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.967" isDuration="false" guid="f863d83d-0a9f-4e86-b389-3403a9eef30e">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15015/hanxin_attack03_spell03a" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SetAnimationParamsDuration0" eventType="SetAnimationParamsDuration" guid="ec1e4f35-2611-4b30-872c-da1c818e2c29" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n     <Condition id="28" guid="e89a739d-ad18-433f-83c7-ed477652dd8f" status="true" />\r\n      <Event eventName="SetAnimationParamsDuration" time="0.000" length="2.330" isDuration="true" guid="6fb1f212-a88d-4671-8904-8b3def9cda85">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <Array name="floatNames" refParamName="" useRefParam="false" type="String">\r\n          <String value="spell3pa" />\r\n        </Array>\r\n        <Array name="floatValues" refParamName="" useRefParam="false" type="float">\r\n          <float value="1.000" />\r\n        </Array>\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='15012' and 'U1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/150_Hanxin_spellC_01"',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15012/150_Hanxin_spellC_01"')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='15216':
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'SkinAvatarFilterType="9">',b'SkinAvatarFilterType="8">').replace(b'SkinAvatarFilterType="11">',b'SkinAvatarFilterType="9">').replace(b'SkinAvatarFilterType="8">',b'SkinAvatarFilterType="11">')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13311':
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/133_direnjie/13311/',b'prefab_skill_effects/component_effects/13311/13311_5/').replace(b'"Play_DiRenJie_Attack_1"', b'"Play_DiRenJie_Attack_1_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Short"', b'"Play_DiRenJie_Voice_Short_Skin11_AW3"').replace(b'"Play_DiRenJie_Attack_Hit_1"', b'"Play_DiRenJie_Attack_Hit_1_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_A"', b'"Play_DiRenJie_Skill_A_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Anger"', b'"Play_DiRenJie_Voice_Anger_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_A_Hit"', b'"Play_DiRenJie_Skill_A_Hit_Skin11_AW2"').replace(b'"Play_DiRenJie_Attack_Hit_2"', b'"Play_DiRenJie_Attack_Hit_2_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_B"', b'"Play_DiRenJie_Skill_B_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_B_Hit"', b'"Play_DiRenJie_Skill_B_Hit_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Red"', b'"Play_DiRenJie_Card_Red_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Blue"', b'"Play_DiRenJie_Card_Blue_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Yellow"', b'"Play_DiRenJie_Card_Yellow_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Dead"', b'"Play_DiRenJie_Voice_Dead_Skin11_AW3"').replace(b'"Play_DiRenJie_Voice_Skill_B"', b'"Play_DiRenJie_Voice_Skill_B_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_C"', b'"Play_DiRenJie_Skill_C_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Skill_C"', b'"Play_DiRenJie_Voice_Skill_C_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_C_Hit"', b'"Play_DiRenJie_Skill_C_Hit_Skin11_AW2"')
                with open(file_path,'wb') as f: 
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '13311' and 'U1' in file_path:
                if phukienv == "dov":
                    with open(file_path, 'rb') as f:
                        rpl = f.read().replace(b'prefab_skill_effects/component_effects/13311/13311_5/',b'prefab_skill_effects/component_effects/13311/1331102/')
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '16707':
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/167_wukong/16707/',b'prefab_skill_effects/component_effects/16707/16707_5/').replace(b'"Play_Back_WuKong"', b'"Play_Back_WuKong_Skin7_AW3"').replace(b'"Play_WuKong_Attack_1"', b'"Play_WuKong_Attack_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Short"', b'"Play_WuKong_VO_Short_Skin7_AW4"').replace(b'"Play_WuKong_Attack_Hit_1"', b'"Play_WuKong_Attack_Hit_1_Skin7_AW3"').replace(b'"Play_WuKong_Attack_2"', b'"Play_WuKong_Attack_2_Skin7_AW3"').replace(b'"Play_WuKong_VO_Anger"', b'"Play_WuKong_VO_Anger_Skin7_AW4"').replace(b'"Play_WuKong_Skill_Passive_Hit1"', b'"Play_WuKong_Skill_Passive_Hit1_Skin7_AW3"').replace(b'"Play_WuKong_Skill_Passive_Hit2"', b'"Play_WuKong_Skill_Passive_Hit2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_Passive_Hit3"', b'"Play_WuKong_Skill_Passive_Hit3_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_2"', b'"Play_WuKong_Skill_B_2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_Hit"', b'"Play_WuKong_Skill_B_Hit_Skin7_AW3"').replace(b'"Play_WuKong_VO_Dead"', b'"Play_WuKong_VO_Dead_Skin7_AW4"').replace(b'"Play_WuKong_Skill_A_2"', b'"Play_WuKong_Skill_A_2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_A_Hit"', b'"Play_WuKong_Skill_A_Hit_Skin7_AW3"').replace(b'"Play_WuKong_Skill_A_1"', b'"Play_WuKong_Skill_A_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_A"', b'"Play_WuKong_VO_Skill_A_Skin7_AW4"').replace(b'"Play_WuKong_Skill_A_Run"', b'"Play_WuKong_Skill_A_Run_Skin7_AW3"').replace(b'"Stop_WuKong_Skill_A_Run"', b'"Stop_WuKong_Skill_A_Run_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_1"', b'"Play_WuKong_Skill_B_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_B"', b'"Play_WuKong_VO_Skill_B_Skin7_AW4"').replace(b'"Play_WuKong_Skill_C"', b'"Play_WuKong_Skill_C_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_C"', b'"Play_WuKong_VO_Skill_C_Skin7_AW4"').replace(b'"Play_WuKong_Skill_C_01"', b'"Play_WuKong_Skill_C_01_Skin7_AW3"').replace(b'"Play_WuKong_Skill_C_02"', b'"Play_WuKong_Skill_C_02_Skin7_AW3"').replace(b'"Play_WuKong_Skill_C_Hit"', b'"Play_WuKong_Skill_C_Hit_Skin7_AW3"')
                with open(file_path,'wb') as f: f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '16707' and 'U1B0.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="\xe5\xa4\xa7\xe9\x83\xa8\xe5\x88\x86\xe7\x89\xb9\xe6\x95\x88" eventType="TriggerParticleTick" guid="f6e33881-833c-448c-9490-fe53bcc022dc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false" />\r\n      <Condition id="13" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false" />\r\n      <Event eventName="TriggerParticleTick" time="0.133" isDuration="false" guid="e75b172d-2997-4a8f-a8dd-ee0368971d7f">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.100" z="0.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>', b'    <Track trackName="CreateRandomTick0" eventType="SpawnBulletTick" guid="SpawnBulletTick-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Event eventName="SpawnBulletTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <String name="SpecialActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <int name="bulletUpperLimit" value="1" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="CheckRandomRangeTick0" eventType="CheckSkillCombineConditionTick" guid="cac41341-211d-4291-8c37-b7586af7e586" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineId" value="130912" refParamName="" useRefParam="false"/>\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a0659289-d2c5-47f7-8206-e6a3fecb4ec9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Condition id="18" guid="cac41341-211d-4291-8c37-b7586af7e586" status="true"/>\r\n      <Event eventName="TriggerParticleTick" time="0.133" isDuration="false">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="60" refParamName="" useRefParam="false"/>\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.100" z="0.000" refParamName="" useRefParam="false"/>\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false"/>\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="PlayHeroSoundTick0" eventType="PlayHeroSoundTick" guid="96204c97-a0cc-4a3f-825c-37ad1d56e6cf" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Condition id="18" guid="cac41341-211d-4291-8c37-b7586af7e586" status="true"/>\r\n      <Event eventName="PlayHeroSoundTick" time="0.133" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="eventName" value="Play_WuKong_Skill_C_01_Skin7_AW3" refParamName="" useRefParam="false"/>\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9a09802-b37d-4562-9963-f566adbddfa5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Condition id="18" guid="cac41341-211d-4291-8c37-b7586af7e586" status="false"/>\r\n      <Event eventName="TriggerParticleTick" time="0.133" isDuration="false">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03_1" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="2.000" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.100" z="0.000" refParamName="" useRefParam="false"/>\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false"/>\r\n        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="PlayHeroSoundTick0" eventType="PlayHeroSoundTick" guid="06e07caf-383b-484f-af7c-5ab073ba3256" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="817e473d-e7ad-4d3c-98e3-208f37995506" status="false"/>\r\n      <Condition id="15" guid="5d13ff64-966b-4903-9530-d53ad6faeaa7" status="false"/>\r\n      <Condition id="18" guid="cac41341-211d-4291-8c37-b7586af7e586" status="false"/>\r\n      <Event eventName="PlayHeroSoundTick" time="0.133" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="eventName" value="Play_WuKong_Skill_C_02_Skin7_AW3" refParamName="" useRefParam="false"/>\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN == '16707' and '16707_Back.xml' in file_path:
                with open(file_path,'rb') as f:
                    rpl=f.read()
                    rpl=rpl.replace(rpl, b'<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n    <TemplateObjectList>\r\n    <TemplateObject id="0" objectName="self" isTemp="false"/>\r\n    <TemplateObject id="1" objectName="target" isTemp="false"/>\r\n    </TemplateObjectList>\r\n    <RefParamList>\r\n    <Vector3i name="_TargetDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\r\n    <Vector3i name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\r\n    </RefParamList>\r\n    <Action tag="" length="0.100" loop="false">\r\n    <Track trackName="Check Buff 2 False" eventType="CheckSkillCombineConditionTick" guid="Check-Buff-2-False-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\r\n       <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineId" value="130912" refParamName="" useRefParam="false"/>\r\n        <Enum name="checkOPType" value="1" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="Buff 2 Trigger" eventType="HitTriggerTick" guid="4cbe0c17-34e7-4f93-a2dd-7125490ccdda" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="0" guid="Check-Buff-2-False-Tran_Thi_Nhung" status="true"/>\r\n       <Event eventName="HitTriggerTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="SelfSkillCombineID_3" value="130912" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <bool name="bIngnoreDeadState" value="true" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="StopTracks" eventType="StopTracks" guid="38239ecc-c096-4ed7-b84b-1473a2ee8bca" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n       <Condition id="0" guid="Check-Buff-2-False-Tran_Thi_Nhung" status="true"/>\r\n       <Event eventName="StopTracks" time="0.000" isDuration="false">\r\n        <Array name="trackIds" refParamName="" useRefParam="false" type="TrackObject">\r\n            <TrackObject id="4" guid="Check-Buff-2-True-Tran_Thi_Nhung"/>\r\n            <TrackObject id="9" guid="1363e6df-dddd-4b69-bf83-d6c13aeeda84"/>\r\n        </Array>\r\n        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="Repeat" eventType="SpawnBulletTick" guid="f1c1b16d-4604-45bd-bf48-d349f75e48d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n       <Condition id="0" guid="Check-Buff-2-False-Tran_Thi_Nhung" status="true"/>\r\n       <Event eventName="SpawnBulletTick" time="0.100" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <String name="SpecialActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <int name="bulletUpperLimit" value="1" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="Check Buff 2 True" eventType="CheckSkillCombineConditionTick" guid="Check-Buff-2-True-Tran_Thi_Nhung" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n       <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineId" value="130912" refParamName="" useRefParam="false"/>\r\n        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false"/>\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="Remove Buff 2" eventType="RemoveBuffTick" guid="4206358d-b971-4030-99d1-8e13dd866c3f" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n       <Condition id="4" guid="Check-Buff-2-True-Tran_Thi_Nhung" status="true"/>\r\n       <Event eventName="RemoveBuffTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="buffId" value="130912" refParamName="" useRefParam="false"/>\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="Repeat" eventType="SpawnBulletTick" guid="a65615b9-d5b3-4e6a-8ed3-11f6cf3de6fe" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n       <Condition id="4" guid="Check-Buff-2-True-Tran_Thi_Nhung" status="true"/>\r\n       <Event eventName="SpawnBulletTick" time="0.100" isDuration="false">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <String name="SpecialActionName" value="prefab_characters/prefab_hero/167_wukong/skill/16707_back" refParamName="" useRefParam="false"/>\r\n        <int name="bulletUpperLimit" value="1" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path,'wb') as f: 
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN =='11113' and 'S1E2.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Condition id="13" guid="ca3dd627-8d6d-4661-b08f-c2fe67130b12" status="true" />',b'<!--'+AABBCC.encode('utf-8') +b'-->')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN =='11113' and 'S2.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Condition id="4" guid="d4d3787f-4aca-405b-a25e-3a83e5b3e8bb" status="true" />',b'<!--'+AABBCC.encode('utf-8') +b'-->')
                with open(file_path,'wb') as f: f.write(rpl)
            if IDMODSKIN =='11113' and 'U1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Condition id="7" guid="92b36a35-ec2d-4a50-88e9-73f085da65d8" status="true" />',b'<!--'+AABBCC.encode('utf-8') +b'-->').replace(b'<Condition id="6" guid="f6bb4dff-ef39-4636-9b11-fdf89e1e0461" status="true" />',b'<!--'+AABBCC.encode('utf-8') +b'-->').replace(b'eventType="SpawnBulletTick" guid="cbe5ad61-6542-40fe-9317-c881f4618927" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <!--'+AABBCC.encode('utf-8') +b'-->',b'eventType="SpawnBulletTick" guid="cbe5ad61-6542-40fe-9317-c881f4618927" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="f6bb4dff-ef39-4636-9b11-fdf89e1e0461" status="true" />').replace(b'<TrackObject id="17" guid="036b40ff-08d6-415a-9d97-97e0942d2aee" />\r\n          <TrackObject id="33" guid="f33baa3c-2b9e-4fbb-8650-dacb612888ba" />\r\n          <TrackObject id="18" guid="2d8e1f0d-7f4a-41d6-bef4-aa762513d4fa" />\r\n          <TrackObject id="23" guid="1414bd9d-4a3e-4263-81d9-d5b75fd19390" />',b'<TrackObject id="17" guid="036b40ff-08d6-415a-9d97-97e0942d2aee" />\r\n          <TrackObject id="33" guid="f33baa3c-2b9e-4fbb-8650-dacb612888ba" />\r\n          <TrackObject id="23" guid="1414bd9d-4a3e-4263-81d9-d5b75fd19390" />').replace(b'</Event>\r\n    </Track>\r\n  </Action>\r\n</Project>',b'</Event>\r\n    </Track>\r\n    <Track trackName="StopTracks0" eventType="StopTracks" guid="abfc4701-c38e-4969-925e-fc3ef0f64b78" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="f6bb4dff-ef39-4636-9b11-fdf89e1e0461" status="true" />\r\n      <Condition id="8" guid="fd62cea3-5d27-43e5-950d-d3fb75ed09fc" status="true" />\r\n      <Event eventName="StopTracks" time="0.000" isDuration="false" guid="b889ae65-11d9-4724-aa75-6b874d4d7e48">\r\n        <Array name="trackIds" refParamName="" useRefParam="false" type="TrackObject">\r\n          <TrackObject id="17" guid="036b40ff-08d6-415a-9d97-97e0942d2aee" />\r\n          <TrackObject id="33" guid="f33baa3c-2b9e-4fbb-8650-dacb612888ba" />\r\n          <TrackObject id="18" guid="2d8e1f0d-7f4a-41d6-bef4-aa762513d4fa" />\r\n          <TrackObject id="23" guid="1414bd9d-4a3e-4263-81d9-d5b75fd19390" />\r\n        </Array>\r\n        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                with open(file_path,'wb') as f: f.write(rpl)

#---------------—------------———----------------
            if IDMODSKIN =='15012' and 'U1.xml' in file_path:
                with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/150_Hanxin_spellC_01"',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/150_hanxin/15012/150_Hanxin_spellC_01"')
                with open(file_path, 'wb') as f: f.write(rpl)
            
#---------------—------------———----------------
            if IDMODSKIN == '17106' and 'P1E5.xml' in file_path:
                with open(file_path, 'rb') as f:
                    rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/171_zhangfei/17106/1719_zhangfei', b'prefab_skill_effects/hero_skill_effects/171_zhangfei/1719_zhangfei')
                with open(file_path, 'wb') as f: f.write(rpl)
#-----------------------------------------------
            if IDMODSKIN == '13210':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                if 'A1.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = rpl.replace(b'\r\n  </Action>',b'\n    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132113" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132112" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                if 'A2.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132112" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132111" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132113" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>    ')
                if 'A3.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132113" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132111" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132112" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                if 'S1B1.xml' in file_path:
                    with open(file_path,'rb') as f:
                        rpl = f.read()
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="c83eb09d-73c4-461b-938f-f73070abc892" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="8593531d-6223-4e88-8100-271908335727" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="0509e695-f257-4517-aca1-44a7fcea5df8" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="e9ad175b-19a2-4349-bbe2-9943b68b27d2">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132112" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="HitTriggerTick" guid="1d752369-b04e-4751-9c2e-bf07c90d34dd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="76baa7d0-5675-46c1-989a-9ddaf2867faa" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="5f9271af-ec05-4d4f-af1e-70941661041c">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132113" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle6" eventType="TriggerParticle" guid="536a47d0-fdc5-441e-b382-53866c442844" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="c83eb09d-73c4-461b-938f-f73070abc892" status="false" />\r\n      <Condition id="5" guid="0509e695-f257-4517-aca1-44a7fcea5df8" status="false" />\r\n      <Condition id="7" guid="76baa7d0-5675-46c1-989a-9ddaf2867faa" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="0.700" isDuration="true" guid="38ee198d-1e31-45e7-857a-06c00d811da8">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_bullet_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>').replace(b'<bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />',b'')
                if 'S12B0.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = re.sub(b'"resourceName" value="(.*?)"', b'"resourceName" value="Tran_Thi_Nhung"', rpl)
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="1" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="b0dbc04b-5f6d-4610-a37b-b5240f304825">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132111" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="2" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fb9ffe1e-fc80-463c-aa04-7e4749711ab8">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132112" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="3" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_132113" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="6786a65e-f11b-484a-a0ae-613c7521f69e">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132113" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba2 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="c7107416-30e0-4ee8-83fa-5f97bb948faf" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="4a8d55af-a3b6-4c1a-b7b9-830ea761ccf9">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_01" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba3 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="bca0dd8d-b83a-49da-982c-6cadaef3966a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="129a0664-39ba-43af-9d93-43c6b7d64878">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_02" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                if 'S11B0.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = re.sub(b'"resourceName" value="(.*?)"', b'"resourceName" value="Tran_Thi_Nhung"', rpl)
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="1" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="b0dbc04b-5f6d-4610-a37b-b5240f304825">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132111" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="2" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fb9ffe1e-fc80-463c-aa04-7e4749711ab8">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132112" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="3" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_132113" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="6786a65e-f11b-484a-a0ae-613c7521f69e">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132113" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba2 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="c7107416-30e0-4ee8-83fa-5f97bb948faf" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="4a8d55af-a3b6-4c1a-b7b9-830ea761ccf9">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_01" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba3 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="bca0dd8d-b83a-49da-982c-6cadaef3966a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="129a0664-39ba-43af-9d93-43c6b7d64878">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_02" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                if 'S1B0.xml' in file_path:
                    with open(file_path, 'rb') as f:
                        rpl = f.read()
                        rpl = re.sub(b'"resourceName" value="(.*?)"', b'"resourceName" value="Tran_Thi_Nhung"', rpl)
                        rpl = rpl.replace(b'  </Action>',b'    <Track trackName="1" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="b0dbc04b-5f6d-4610-a37b-b5240f304825">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132111" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="2" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fb9ffe1e-fc80-463c-aa04-7e4749711ab8">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132112" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="3" eventType="CheckSkillCombineConditionTick" guid="Mod_By_Tran_Thi_Nhung_132113" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="6786a65e-f11b-484a-a0ae-613c7521f69e">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132113" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="44" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_02_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="45" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_03_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13210/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba2 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="c7107416-30e0-4ee8-83fa-5f97bb948faf" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="4a8d55af-a3b6-4c1a-b7b9-830ea761ccf9">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_01" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba3 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="bca0dd8d-b83a-49da-982c-6cadaef3966a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="129a0664-39ba-43af-9d93-43c6b7d64878">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_02" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132111" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_Mod_132112" status="false" />\r\n      <Condition id="Tran_Thi_Nhung" guid="Mod_By_Tran_Thi_Nhung_132113" status="false" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                with open(file_path, 'wb') as f:
                    f.write(rpl)
#---------------—------------———----------------
            if IDMODSKIN == '52113':
                with open(file_path, 'rb') as f:
                    rpl = f.read()
                    rpl = re.sub(rb'SkinAvatarFilterType="9"', b'SkinAvatarFilterType="__TMP__"', rpl, flags=re.IGNORECASE)
                    rpl = re.sub(rb'SkinAvatarFilterType="11"', b'SkinAvatarFilterType="9"', rpl, flags=re.IGNORECASE)
                    rpl = re.sub(rb'SkinAvatarFilterType="__TMP__"', b'SkinAvatarFilterType="11"', rpl, flags=re.IGNORECASE)
                    rpl = re.sub(b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/521_Florentino/52113_Florentino_BianShen" refParamName="" useRefParam="false" />', b'<String name="prefabName" value="Prefab_Skill_Effects/Hero_Skill_Effects/521_Florentino/52113/52113_Florentino_BianShen" refParamName="" useRefParam="false" />', rpl, flags=re.IGNORECASE)
                    rpl=rpl.replace(b'<SkinOrAvatarList id="52113" />',b'')
                text = rpl.decode('utf-8')
                lines = text.splitlines()
                new_lines = []
                for line in lines:
                    if '<String name="clipName"' in line:
                        new_lines.append(
                        '        <int name="frameRate" value="10800" refParamName="" useRefParam="false" />')
                    new_lines.append(line)
            
                new_text = '\n'.join(new_lines)
                rpl = new_text.encode('utf-8')
            
                with open(file_path, 'wb') as f:
                    f.write(rpl)
                    
#-----------------------------------------------
    IDNODMODCHECK = ['13210', '13011', '52414', '15015', '15013', '13314', '13706','59901','13213','11215','59802','10915','15412','10611','10620','11120', '15710','54804']
    
    if IDCHECK not in IDNODMODCHECK:
        directorypath = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'
        files_list = os.listdir(directorypath)
        for filename in files_list:
            filecheck = os.path.join(directorypath, filename)
            with open(filecheck, 'rb') as f:
                All = f.read()
            # --- Xử lý đặc biệt cho các ID trong list này ---
            if IDMODSKIN in ['14111'] and filename not in ['S1.xml', 'S1B1.xml', 'S1B2.xml', 'S1B11.xml', 'S1B12.xml', 'S1B21.xml', 'S1B22.xml']:

                rpl = All.replace(
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <<<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
                    ).replace(
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
                    ).replace(
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <<<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',
                        b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />'
                    )
                with open(filecheck, 'wb') as f:
                    f.write(rpl)
                continue  # Skip file này, KHÔNG xử lý CheckSkinIdTick & FixSkinAvatar
    
            # --- Xử lý CheckSkinIdTick ---
            CheckSkinIdTick = (
                '<int name="skinId" value="' + IDMODSKIN + '" refParamName="" useRefParam="false" />'
            ).encode()
            CheckSkinIdTick0 = (
                '<int name="skinId" value="' + IDMODSKIN[:3] + '00" refParamName="" useRefParam="false" />'
            ).encode()
            if CheckSkinIdTick in All:
                All = All.replace(CheckSkinIdTick, CheckSkinIdTick0)
                print(f'CheckSkinIdTick : {filename}')
    
            # --- Xử lý FixSkinAvatar ---
            FixSkinAvatar = ('<SkinOrAvatarList id="' + IDMODSKIN + '" />').encode()
            FixSkinAvatar1 = ('<SkinOrAvatarList id="' + IDMODSKIN[:3] + '00" />').encode()
            if FixSkinAvatar in All:
                All = All.replace(FixSkinAvatar, FixSkinAvatar1)
    
            # --- Xử lý đặc biệt cho IDMODSKIN == '54805' ---
            if IDMODSKIN == '54805':
                xoa = b'<SkinOrAvatarList id="54800" />'
                if xoa in All:
                    All = All.replace(xoa, b'')  # Xóa dòng
    
            # --- Ghi lại file ---
            with open(filecheck, 'wb') as f:
                f.write(All)
            
#-----------------------------------------------
    if IDCHECK in ['53002'] or b"Skin_Icon_SoundEffect" in dieukienmod or b"Skin_Icon_Dialogue" in dieukienmod:
        if IDCHECK not in ["13311", "16707"]:
            directory_path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'
            
            for file in os.listdir(directory_path):
                filepath = os.path.join(directory_path, file)
                with open(filepath, 'rb') as f:
                    data = f.read()
                IDMS = IDMODSKIN.encode()
                if IDMS.decode()[3] == '0':
                    IDSOUND1 = IDMS.decode()[4]
                else:
                    IDSOUND1 = IDMS.decode()[-2:]
                ID_S = b"_Skin" + IDSOUND1.encode()
                ListAll = data.split(b'\r\n')
                eventname = b'<String name="eventName" value="'
                
                CODE_SOUND = [x for x in ListAll if eventname.lower() in x.lower()]
            
                if len(CODE_SOUND) != 0:
                    for text in CODE_SOUND:
                        text1 = text.replace(
                            b'" refParamName="" useRefParam="false" />',
                            ID_S + b'" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />'
                        ).replace(ID_S * 2, ID_S)
            
                        data = data.replace(text, text1)
                
                if IDMODSKIN == "11620":
                    if b"_Skin20" in data:
                        data = data.replace(b"_Skin20", b"_Skin20_AW5")
                with open(filepath, 'wb') as f:
                    f.write(data)
            print('    Mod Sound : Done')
                
            def remove_extra_skin_array(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                except UnicodeDecodeError:
                    return
    
                lines = text.splitlines()
                processed_lines = []
                inside_event = False
                in_extraskin_block = False
    
                for line in lines:
                    stripped = line.strip()
    
                    if '<Event eventName="PlayHeroSoundTick"' in stripped:
                        inside_event = True
                    if '</Event>' in stripped and inside_event:
                        inside_event = False
    
                    if inside_event and '<Array name="extraSkinId"' in stripped and '/>' in stripped:
                        continue
                    if inside_event and '<Array name="extraSkinId"' in stripped and '/>' not in stripped:
                        in_extraskin_block = True
                        continue
                    if in_extraskin_block:
                        if '</Array>' in stripped:
                            in_extraskin_block = False
                        continue
    
                    processed_lines.append(line)
    
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(processed_lines))
    
            def remove_extra_skin_array_in_folder(directory_path):
                for filename in os.listdir(directory_path):
                    if filename.endswith('.xml'):
                        file_path = os.path.join(directory_path, filename)
                        remove_extra_skin_array(file_path)
    
            if os.path.isdir(directory_path):
                remove_extra_skin_array_in_folder(directory_path)

    # fix ef pro
    VMODCHECK = '2'
    MODCHECK = '1'
    if MODCHECK == '1':
        IDNODMODCHECK = ['14111', '13210', '16707', '13011','13213','10620']
        #IDCHECK = IDCHECK[:3]+'00'
        if IDCHECK not in IDNODMODCHECK:
            ABCD=[]
            files_list = os.listdir(directory_path)
            for filename in files_list:
                if filename in ['A1B1.xml', 'A2B1.xml', 'A1b2.xml', 'A2b2.xml'] and IDCHECK == "11119":
                    continue
                elif filename == 'P1E5.xml' and IDCHECK[:3] == '131':
                    continue
                elif filename != 'S1B1.xml' and IDCHECK == '13609':
                    continue
                elif filename != 'u1b1.xml' and IDCHECK == '59901':
                    continue
                elif filename != ["A1B1.xml", "A1b2.xml", "A2B1.xml", "A2b2.xml"] and IDCHECK == '11120':
                    continue
                elif filename != 'U1E1.xml' and IDCHECK == '10611':
                    continue
                if filename in ['S1E2.xml', 'S2.xml', 'U1.xml'] and IDCHECK == "11113":
                    continue
                elif filename == 'U1.xml' and IDCHECK == '15015':
                    continue
                file_path = os.path.join(directory_path, filename)
                if VMODCHECK == "1":
                    with open(file_path, 'rb') as file:
                        xml_bytes = file.read()#.decode('utf-8')
                        start_phrase = b'<Track trackName="'
                        end_phrase = b'</Track>' 
                        start_index = xml_bytes.find(start_phrase)
                        end_index = xml_bytes.find(end_phrase, start_index)
                        while start_index != -1 and end_index != -1:
                            track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                            start_index = xml_bytes.find(start_phrase, end_index)
                            end_index = xml_bytes.find(end_phrase, start_index)
                            if b'"skinId" value="' + IDCHECK.encode() + b'"' in track_text:
                                ABCD.append(track_text)
                                    #print(track_text)
                                    #track_text = track_text.encode()
                    for track_text in ABCD:
                        with open(file_path, 'rb') as file:
                            xml_bytes = file.read()
                        modified_data = (
                                track_text
                                .replace(b"CheckSkinIdTick", b"CheckHeroIdTick")
                                .replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick")
                                .replace(
                                    b'"skinId" value="' + IDCHECK.encode() + b'"',
                                    b'"heroId" value="' + IDCHECK[:3].encode() + b'"'
                                )
                            )                                        
                        modified_data1 = xml_bytes.replace(track_text, modified_data)
                        with open(file_path, 'wb') as file:
                            file.write(modified_data1)
                if VMODCHECK == "2":
                    with open(file_path, 'rb') as file:
                        xml_bytes = file.read()#.decode('utf-8')
                        start_phrase = b'<Track trackName="'
                        end_phrase = b'</Track>' 
                        start_index = xml_bytes.find(start_phrase)
                        end_index = xml_bytes.find(end_phrase,start_index)
                        while start_index != -1 and end_index != -1:
                            track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                            start_index = xml_bytes.find(start_phrase, end_index)
                            end_index = xml_bytes.find(end_phrase, start_index)
                            if b'"skinId" value="' + IDCHECK.encode() + b'"' in track_text:
                                ABCD.append(track_text)
                                print(track_text)
                                    #track_text = track_text.encode()
                    for track_text in ABCD:
                        if b'<bool name="bEqual" value="false" refParamName="" useRefParam="false" />' in track_text:
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()
                            modified_data = (
                                    track_text
                                    .replace(
b'<int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />',
b'        <int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />')
                                    .replace(b"CheckSkinIdVirtualTick", b"CheckSkinIdTick")
                                )                                        
                            modified_data1 = xml_bytes.replace(track_text, modified_data)
                            with open(file_path, 'wb') as file:
                                file.write(modified_data1)
                        if b'<bool name="bEqual" value="false" refParamName="" useRefParam="false" />' not in track_text:
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()
                            modified_data = (
                                    track_text
                                    .replace(
b'        <int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />', 
b'        <int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />')
                                    .replace(b"CheckSkinIdVirtualTick", b"CheckSkinIdTick")
                                )                                        
                            modified_data1 = xml_bytes.replace(track_text, modified_data)
                            with open(file_path, 'wb') as file:
                                file.write(modified_data1)
    Kiem_Tra_Code = os.path.join(Files_Directory_Path, f'{NAME_HERO}', 'skill')
    for file in os.listdir(Kiem_Tra_Code):
        File_Check_Code = os.path.join(Kiem_Tra_Code, file)
        if IDCHECK == '11120' and file not in ["A1B1.xml", "A1b2.xml", "A2B1.xml", "A2b2.xml", "A4B1.xml", "A4b2.xml", "S2.xml"]:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
                All = All.replace(b'<SkinOrAvatarList id="11120" />',b'<SkinOrAvatarList id="23720" />')
            with open(File_Check_Code, "wb") as f:
                f.write(All)
        if IDCHECK == '10915' and 'U1E1.xml' not in file:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
            
            pattern = rb'(<Track trackName=".*?</Track>)'
            matches = re.findall(pattern, All, re.DOTALL)
            
            for track_content in matches:
                if (
                    b'<int name="changeSkillID" value="10902"' in track_content
                    or b'<int name="changeSkillID" value="10900"' in track_content
                    or b'<bool name="bImmeStop" value="true"' in track_content
                ):
                    continue 
    
                if b'<SkinOrAvatarList id="10915" />' in track_content:
                    new_track = track_content.replace(b'<SkinOrAvatarList id="10915" />', b'')
                    All = All.replace(track_content, new_track)
            
            with open(File_Check_Code, "wb") as f:
                f.write(All)
            
        if IDMODSKIN == '10915' and 'S1B2.xml' in file:
            with open(File_Check_Code, "rb") as f: rpl = f.read().replace(b'<Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="fb822b25-5916-4075-8d1e-e570f8432650" enabled="true"',b'<Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="fb822b25-5916-4075-8d1e-e570f8432650" enabled="false"')
            with open(File_Check_Code, "wb") as f:
                f.write(rpl)
        if IDMODSKIN == '10915' and 'S2.xml' in file:
            with open(File_Check_Code, "rb") as f: rpl = f.read().replace(b'<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="8e6fab3b-8028-4e01-a59f-a9288f6446a1" enabled="true"',b'<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="8e6fab3b-8028-4e01-a59f-a9288f6446a1" enabled="false"')
            with open(File_Check_Code, "wb") as f:
                f.write(rpl)
        if IDMODSKIN == '10915' and 'S2E9.xml' in file:
            with open(File_Check_Code, "rb") as f: rpl = f.read().replace(b'<Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="2bebbe12-947f-4e1a-b72f-283c29f43837" enabled="true',b'<Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="2bebbe12-947f-4e1a-b72f-283c29f43837" enabled="false')
            with open(File_Check_Code, "wb") as f:
                f.write(rpl)
        if IDMODSKIN == '10915' and 'U1B0.xml' in file:
            with open(File_Check_Code, "rb") as f: rpl = f.read().replace(b'<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="8b472108-87cf-4dbb-a6bd-cabbd0fbf6ae" enabled="true',b'<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="8b472108-87cf-4dbb-a6bd-cabbd0fbf6ae" enabled="false').replace(b'b74c107d-1783-4919-b238-e2e4e7fbcc21" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Condition id="0" guid="ca73ce2f-a393-497e-b037-d2cf75728dfe" status="true" />',b'b74c107d-1783-4919-b238-e2e4e7fbcc21" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Condition id="1" guid="ca73ce2f-a393-497e-b037-d2cf75728dfe" status="true" />')
            with open(File_Check_Code, "wb") as f:
                f.write(rpl)
        if IDMODSKIN == '10915' and 'U1E1.xml' in file:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
                All = All.replace(b'</Event>',b'</Event>\n      <SkinOrAvatarList id="10915" />')
            with open(File_Check_Code, "wb") as f:
                f.write(All)
        if IDMODSKIN == '10915' and 'U2B0.xml' in file:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
                All = All.replace(b'<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="8b472108-87cf-4dbb-a6bd-cabbd0fbf6ae" enabled="true',b'<Track trackName="TriggerParticleTick1" eventType="TriggerParticleTick" guid="8b472108-87cf-4dbb-a6bd-cabbd0fbf6ae" enabled="false').replace(b'<Condition id="0" guid="cf853818-39cd-4abe-bc62-d19a9d5af975" status="true" />',b'<Condition id="1" guid="cf853818-39cd-4abe-bc62-d19a9d5af975" status="true" />').replace(b'<Condition id="1" guid="cf853818-39cd-4abe-bc62-d19a9d5af975" status="true" />',b'<Condition id="0" guid="cf853818-39cd-4abe-bc62-d19a9d5af975" status="true" />',1)
            with open(File_Check_Code, "wb") as f:
                f.write(All)
        if IDMODSKIN == '14111' and 'S1.xml' in file:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
                All = All.replace(b'14100',b'14111')
            with open(File_Check_Code, "wb") as f:
                f.write(All)

        if IDCHECK == '59802':
            with open(File_Check_Code, "rb") as f:
                All = f.read()
        
            tracks = re.findall(rb'(<Track trackName=".*?</Track>)', All, flags=re.DOTALL)
        
            for t in tracks:
                t_low = t.lower()
                if b"random" in t_low or b"spawnobjectduration" in t_low or b"spawnbullettick" in t_low or b"filtertargettype" in t_low or b"checkenergyconditionduration0" in t_low or b"setmaterialparamsduration" in t_low or b"setactorhudscaleduration0" in t_low or b"hittriggertick0" in t_low or b"removebufftick0" in t_low or b"stoptrack" in t_low:

                    continue
                All = All.replace(t, t.replace(b'<SkinOrAvatarList id="59802" />',
                                               b'<SkinOrAvatarList id="59898" />'))
        
            with open(File_Check_Code, "wb") as f:
                f.write(All)

        if IDCHECK == '59901' and file not in ['Back.xml', 'P10E2.xml', 'S1B1.xml']:
            with open(File_Check_Code, "rb") as f:
                All = f.read()
        
            for track in re.findall(rb'(<Track trackName=".*?</Track>)', All, flags=re.DOTALL):
                l = track.lower()
                if (b"random" in l or b'scalemeshduration0' in l or b'hittrigger' in l or b'spawnobjectduration' in l or b'spawnbullettick' in l or b'removebufftick' in l or b'setcollisiontick' in l):
                    continue
                new_track = re.sub(
                    rb'<SkinOrAvatarList id="59901"\s*/>',
                    b'<SkinOrAvatarList id="59998" />',
                    track
                )
        
                All = All.replace(track, new_track)
        
            with open(File_Check_Code, "wb") as f:
                f.write(All)
        
        if IDCHECK == '13706' and 'U1B0.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl = rpl.replace(b'<SkinOrAvatarList id="13706" />',b'<SkinOrAvatarList id="13700" />\r\n      <SkinOrAvatarList id="13701" />\r\n      <SkinOrAvatarList id="13702" />\r\n      <SkinOrAvatarList id="13703" />\r\n      <SkinOrAvatarList id="13704" />\r\n      <SkinOrAvatarList id="13705" />\r\n      <SkinOrAvatarList id="13707" />\r\n      <SkinOrAvatarList id="13708" />\r\n      <SkinOrAvatarList id="13709" />\r\n      <SkinOrAvatarList id="13706" />')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '13314' and 'skin14E2.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl = rpl.replace(b'SkinAvatarFilterType="9">',b'SkinAvatarFilterType="11">').replace(b'<String name="prefab" value="prefab_characters/prefab_hero/133_DiRenJie/DiRenJie_spell03_cutin01" refParamName="" useRefParam="false" />',b'<String name="prefab" value="prefab_skill_effects/hero_skill_effects/133_DiRenJie/13314/DiRenJie_spell03_cutin01" refParamName="" useRefParam="false" />')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '11620' and file not in ['S3.xml']:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl = rpl.replace(b'SkinAvatarFilterType="9">',b'SkinAvatarFilterType="Love">').replace(b'SkinAvatarFilterType="11">',b'SkinAvatarFilterType="9">').replace(b'SkinAvatarFilterType="Love">',b'SkinAvatarFilterType="11">').replace(b'11620_3/',b'11620_5/')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
            if 'Skin20E1.xml' in file:
                with open(File_Check_Code, 'rb') as f:
                    rpl = f.read().replace(b'SkinAvatarFilterType="9">',b'SkinAvatarFilterType="11">').replace(b'<SkinOrAvatarList id="11600" />',b'<SkinOrAvatarList id="23720" />')
                with open(File_Check_Code, 'wb') as f:
                    f.write(rpl)
        if IDCHECK == '13213':
            if file in ['A1.xml', 'A2.xml', 'A3.xml','Death.xml', 'P1E42.xml','P1E51.xml','PassiveE3.xml','S1E1.xml','S2.xml','S11B0.xml','S12B0.xml','U1.xml','U2.xml','U3.xml']:
                with open(File_Check_Code, 'rb') as f:
                    A1_CheckFile13213Code = f.read().replace(b'<SkinOrAvatarList id="13213" />',b'')
                    
                with open(File_Check_Code, 'wb') as f:
                    f.write(A1_CheckFile13213Code)
            if 'S1B0.xml' in file:
                with open(File_Check_Code, 'rb') as f:
                    S1B0_CheckFile13213Code = f.read().replace(b'<SkinOrAvatarList id="13213" />',b'',2)
                with open(File_Check_Code, 'wb') as f:
                    f.write(S1B0_CheckFile13213Code)
            if 'S1B1.xml' in file:
                with open(File_Check_Code, 'rb') as f:
                    S1B1_CheckFile13213Code = f.read().replace(b'  </Action>',b'    <Track trackName="TriggerParticle6" eventType="TriggerParticle" guid="536a47d0-fdc5-441e-b382-53866c442844" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" SkinAvatarFilterType="11">\n      <Event eventName="TriggerParticle" time="0.000" length="0.700" isDuration="true" guid="38ee198d-1e31-45e7-857a-06c00d811da8">\n        <TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01h" refParamName="" useRefParam="false"/>\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01a" refParamName="" useRefParam="false"/>\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01g" refParamName="" useRefParam="false"/>\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false"/>\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n        <String name="customTagName" value="" refParamName="" useRefParam="false"/>\n      </Event>\n    </Track>\n  </Action>')
                with open(File_Check_Code, 'wb') as f:
                    f.write(S1B1_CheckFile13213Code)
            
        if IDCHECK == '52414' and file not in ['Skin14E3.xml', 'S3.xml']:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'<SkinOrAvatarList id="52414" />',b'<SkinOrAvatarList id="52400" />\r\n      <SkinOrAvatarList id="52401" />\r\n      <SkinOrAvatarList id="52402" />\r\n      <SkinOrAvatarList id="52403" />\r\n      <SkinOrAvatarList id="52404" />\r\n      <SkinOrAvatarList id="52405" />\r\n      <SkinOrAvatarList id="52406" />\r\n      <SkinOrAvatarList id="52407" />\r\n      <SkinOrAvatarList id="52408" />\r\n      <SkinOrAvatarList id="52409" />\r\n      <SkinOrAvatarList id="52410" />\r\n      <SkinOrAvatarList id="52411" />\r\n      <SkinOrAvatarList id="52412" />\r\n      <SkinOrAvatarList id="52413" />\r\n      <SkinOrAvatarList id="52414" />')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        
        if IDCHECK == '52414' and 'S3B1.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'  <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticle" guid="7e9d5fca-8e56-45b0-9fb2-d2ba97cfa6d3" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="4.000" isDuration="true" guid="2840ce3c-5daa-47dd-ae0f-a7e9e1af4843">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Spell3_Bullet2" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)

        if IDCHECK == '52414' and 'A2B1.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'   <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="e32f0786-596a-4939-b208-9e2843159f17" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="754b4b2d-72b7-4144-8071-be31caec9ee7">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="4fc171ca-3e80-4093-912c-c06c051af438" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="3165ead7-a62f-44c9-86aa-6f83d43cef33">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '52414' and 'A2B1_1.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'   <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="cff934a4-b8b2-4700-b9be-35e209a2d7c7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.000" isDuration="true" guid="7e31eaa9-7be1-4cdc-9eaa-e0aedd9c8a57">\r\n        <TemplateObject name="targetId" objectName="fxobj" id="3" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="fxobj" id="3" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <bool name="bReverseXWhenCameraMirror" value="true" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="4341bfe0-43d1-4612-8ab3-e013e467c4f8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.000" isDuration="true" guid="a2ffa7b9-a1dd-4cec-b2eb-821c7abb74f7">\r\n        <TemplateObject name="targetId" objectName="fxobj" id="3" isTemp="true" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="fxobj" id="3" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_blue_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_green_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_red_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <bool name="bReverseXWhenCameraMirror" value="true" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '52414' and 'A2B2.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'    <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="4e917e68-d367-417c-9dc2-2b73bebc4ff0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="e39c580c-d239-40e1-8389-4b8ea0388c12">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Gunpoint_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="0389ac3e-66fa-4948-bb52-52497a1a08ca" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="bd40f6c2-91dd-41d0-8a27-bac13fe880ed">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Ground_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="abcf0f2c-4fc8-4540-9bc9-d93478c3149d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="210ac1ca-8938-4b13-ba06-c275f1f37810">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="1.020" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bReverseXWhenCameraMirro" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Tran_Thi_Nhung" eventType="TriggerParticleTick" guid="87a3c53b-26dc-4ab9-b7d3-fc4a7f94892d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="906a38df-d19f-46d7-b410-f0d716701c08">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_blue_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_green_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_Bullet_red_1" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <float name="lifeTime" value="1.020" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bReverseXWhenCameraMirro" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '52414' and 'S1E2.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="94c51195-cfac-4b34-b870-c33e5a708bed" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticle" time="0.000" length="6.000" isDuration="true" guid="7bc01d1d-6b9a-42c1-ac4d-186fda0762e4">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk1_FireRange_Plus_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk1_FireRange_Plus_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk1_FireRange_Plus_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlyFollowPos" value="true" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle8" eventType="TriggerParticle" guid="4aeed5e1-d9ad-4484-8ddc-dc2323bb9abd" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticle" time="0.000" length="6.000" isDuration="true" guid="d066c13b-6cf4-471a-b729-70b6b0a81e6f">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="bindPointName" value="Ef_Point" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick2" eventType="TriggerParticleTick" guid="0f190a6f-5d9a-4b96-bada-d922bea108f4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="9918467c-2184-482f-b34e-7608dcc8d916">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="bindPointName" value="Ef_Point" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle8" eventType="TriggerParticle" guid="a39df4a6-a717-45b1-9dd8-6b6ec21eb6a6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">\r\n      <Event eventName="TriggerParticle" time="0.000" length="6.000" isDuration="true" guid="5065bb18-39b8-4274-bcf4-0fc154e8acc5">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_blue_loop" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_green_loop" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Atk2_WeaponReady_red_loop" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="bindPointName" value="Ef_Point" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        if IDCHECK == '52414' and 'S2.xml' in file:
            with open(File_Check_Code, 'rb') as f:
                rpl = f.read()
                rpl =rpl.replace(b'</Action>',b'\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="54c88eab-3add-4df4-9566-41cef331421d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.400" isDuration="true" guid="575a287d-0390-4842-9214-f9dea0456111">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Spell2_Ground_blue" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Spell2_Ground_green" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/524_Capheny/52414/Spell2_Ground_red" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
            with open(File_Check_Code, 'wb') as f:
                f.write(rpl)
        
#-----------------------------------------------
    if IDCHECK == '15009':
        for file in ["BlueBuff.xml", "RedBuff_Slow.xml"]:
            duongdan = f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/{file}"
            giai(duongdan)
            with open(duongdan, 'rb') as f:
                content = f.read().replace(
                    b"CheckSkinIdVirtualTick", b"CheckHeroIdTick"
                    ).replace(
                    b'"skinId" value="15009"', b'"heroId" value="150"'
                    )
            with open(duongdan, 'wb') as f:
                f.write(content)
    if IDCHECK == '15013':
        Youtuber_Name = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/BlueBuff_CD.xml'
        giai(Youtuber_Name)
        with open(Youtuber_Name, 'rb') as f:
            noidung = f.read()
        noidung = noidung.replace(b"CheckSkinIdTick", b"CheckHeroIdTick")\
                         .replace(b'"skinId" value="15013"', b'"heroId" value="150"')\
                         .replace(b'prefab_skill_effects/hero_skill_effects/15013/', 
                                  b'prefab_skill_effects/hero_skill_effects/150_hanxin/15013/')
        with open(Youtuber_Name, 'wb') as f:
            f.write(noidung)

#-----------------------------------------------
    fixlag1 = '1'
    if fixlag1 == '1':
        path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'
        Function_Track_Guid_AddGetHoliday(path)
        PathBorn = os.path.join(f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/", "Born.xml")
        giai(PathBorn)
        path1 = [file for file in os.listdir(path) if file.endswith(("A1E1.xml", "A1E0.xml")) and os.path.isfile(os.path.join(path, file))]
        Code = []
        for file in path1:
            try:
                with open(os.path.join(path, file), encoding='utf-8') as F:
                    R = F.read()
                if "resourceName" in R:
                    for i in R.splitlines():
                        if "resourceName" in i:
                            i = i.replace("resourceName2", "resourceName")
                            i = i.replace("resourceName3", "resourceName")
                            if ID in i and i not in Code:
                                Code.append(i)
            except:
                pass
        
        CheckHero = f'  <Track trackName="None" eventType="CheckHeroIdTick" guid="{str(uuid.uuid4())}" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="{str(uuid.uuid4())}">\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <int name="heroId" value="IDSKIN" refParamName="" useRefParam="false" />\n      </Event>\n    </Track>\n'
        
        TG = f'    <Track trackName="None" eventType="TriggerParticleTick" guid="{str(uuid.uuid4())}" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Condition id="NUM" guid="{str(uuid.uuid4())}" status="true" />\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="{str(uuid.uuid4())}">\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\n\n      </Event>\n    </Track>\n'
        
        with open(PathBorn, encoding='utf-8') as F:
        	Read = F.read()
        
        kh = "</Action>"
        if kh in Read:
        	Read = Read.replace(kh, CheckHero + kh, 1)
        	Read = Read.replace(kh, '  ' + kh, 1)
        	NUM = Read.count('<Track trackName=')-1
        	Read = Read.replace("IDSKIN", ID[:3])
        for code in Code:
            New = TG.replace("\n\n", "\n" + code + "\n")
            print(repr(New.encode()))
            Read = Read.replace("  </Action>", New + "  </Action>")
        Read = Read.replace("NUM", str(NUM))

        with open(PathBorn, "w", encoding='utf-8') as F: F.write(Read)
#-----------------------------------------------
    if IDCHECK in ("50108","14111","11107","15009","13015","13314"):
        organSkin = f"Resources/{Ver}/Databin/Client/Actor/organSkin.bytes"
        organSkin_mod = f"{FolderMod}/Resources/{Ver}/Databin/Client/Actor/organSkin.bytes"
        shutil.copy(organSkin, organSkin_mod)
        giai(organSkin_mod)
        ID = IDCHECK
        file = open(organSkin_mod, "rb")
        IDN = str(hex(int(ID)))
        IDN = IDN[4:6] + IDN[2:4]
        IDN = bytes.fromhex(IDN)
        ALL_ID = []
        MD = int(ID[0:3] + "00")
        for IDNew in range(21):
            ALL_ID.append(str(MD))
            MD += 1
        ALL_ID.remove(ID)
        for x in range(20):
            IDK = str(hex(int(ALL_ID[x])))
            IDK = IDK[4:6] + IDK[2:4]
            IDK = bytes.fromhex(IDK)
            ALL_ID[x] = IDK
        Begin = file.read(140)
        Read = b"\x00"
        All = []
        while Read != b"":
            Read = file.read(36)
            if Read.find(IDN) != -1:
                All.append(Read)
            try:
                Max = Read[4] + (Read[5]*256)
                Max0 = str(hex(Max))
                if len(Max0) == 4:
                    Max0 = Max0[2:4] + "00"
                if len(Max0) == 5:
                    Max0 = Max0[3:5] + "0" + Max0[2]
                if len(Max0) == 6:
                    Max0 = Max0[4:6] + Max0[2:4]
                Max0 = bytes.fromhex(Max0)
            except:
                None
        file.close()
        file = open(organSkin_mod, "ab+")
        Read0 = file.read()
        for i in range(len(ALL_ID)):
            for j in range(len(All)):
                CT = All[j]
                if CT.find(IDN) != -1:
                    CT = CT.replace(IDN,ALL_ID[i])
                else:
                    CT = CT.replace(ALL_ID[i-1],ALL_ID[i])
                CTN = str(hex(Max0[0]+(Max0[1]*256)+1))
                if len(CTN) == 4:
                    CTN = CTN[2:4]
                if len(CTN) == 5:
                    CTN = CTN[3:5] + "0" + CTN[2]
                if len(CTN) == 6:
                    CTN = CTN[4:6] + CTN[2:4]
                CTN = bytes.fromhex(CTN)
                OZ = b" \x00\x00\x00"
                if len(CTN) == 1:
                    CT = CT.replace(OZ+CT[4:6],OZ+CTN+b"\x00",1)
                if len(CTN) == 2:
                    CT = CT.replace(OZ+CT[4:6],OZ+CTN,1)
                All[j] = CT
                XXX = file.write(CT)
                Max0 = CT[4:6]
        file.close()
        file = open(organSkin_mod, "rb")
        Read = file.read()
        Read = Read.replace(Begin[12:14],Max0,1)
        file.close()
        file = open(organSkin_mod, "wb")
        Z = file.write(Read)
        file.close()

#-----------------------------------------------
    if IDCHECK == '13706' or b"Skin_Icon_BackToTown" in dieukienmod or b"Skin_Icon_Animation" in dieukienmod:
        import uuid, os, re
        back_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
        with open(back_path, 'rb') as f:
            data = f.read()
        
        tracks = re.findall(rb'    <Track trackName=.*?</Track>', data, re.DOTALL)
        found_blocks = {}
        for b in tracks:
            if b'<int name="skinId" value="' in b and 'skin' not in found_blocks:
                found_blocks['skin'] = b
            elif b'value="born_back_reborn/huijidi_01"' in b and 'p1' not in found_blocks:
                found_blocks['p1'] = b
            elif b'value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01"' in b and 'p2' not in found_blocks:
                found_blocks['p2'] = b
            elif b'value="Gohome"' in b and 'clip1' not in found_blocks:
                found_blocks['clip1'] = b
            elif b'value="Home"' in b and b'value="Gohome"' not in b and 'clip2' not in found_blocks:
                found_blocks['clip2'] = b
            if len(found_blocks) == 5:
                break
        
            external_file = None
            
            for sf in ['_Back.xml', '_back.xml']:
                path = os.path.join(Files_Directory_Path, NAME_HERO, 'skill', IDMODSKIN + sf)
                if os.path.isfile(path):
                    external_file = path
                    break
            
            if not external_file:
                pass

        def insert_condition(block: bytes, condition_id: int) -> bytes:
            guid_match = re.search(rb'guid="([^"]+)"', block)
            guid = guid_match.group(1) if guid_match else b'unknown-guid'
            condition = f'      <Condition id="{condition_id}" guid="{str(uuid.uuid4())}" status="true" />'.encode()
            lines = block.splitlines()
            for j, line in enumerate(lines):
                if b'<Track trackName=' in line:
                    lines.insert(j + 1, condition)
                    break
            return b'\n'.join(lines)
        
        def clean_block(block: bytes) -> bytes:
            block = re.sub(rb'\s+SkinAvatarFilterType="[^"]+"', b'', block)
            block = re.sub(
                b'<int name="skinId" value="[^"]*" refParamName="" useRefParam="false" />',
                b'<int name="skinId" value="' + IDMODSKIN[:3].encode() + b'00' + b'" refParamName="" useRefParam="false" />',
                block
            )
            if IDMODSKIN in ['11620', '16707', '13311']:
                block = block.replace(
                    b'<String name="resourceName" value="" refParamName="strReturnCityFall" useRefParam="true" />',
                    b'<String name="resourceName" value="prefab_skill_effects/component_effects/' + IDMODSKIN.encode() + b'/' + IDMODSKIN.encode() +
                    b'_5/huijidi_01" refParamName="" useRefParam="false" />'
                ).replace(
                    b'<String name="resourceName" value="" refParamName="strReturnCityEffectPath" useRefParam="true" />',
                    b'<String name="resourceName" value="prefab_skill_effects/component_effects/' + IDMODSKIN.encode() + b'/' + IDMODSKIN.encode() +
                    b'_5/huicheng_tongyong_01" refParamName="" useRefParam="false" />'
                ).replace(
                    b'value="Gohome"',
                    b'value="' + IDMODSKIN.encode() + b'/Awaken/Home"'
                ).replace(
                    b'value="Home"',
                    b'value="' + IDMODSKIN.encode() + b'/Awaken/Home"'
                )
            # Thay thế đường dẫn resource
            block = block.replace(
                b'<String name="parentResourceName" value="born_back_reborn/huijidi_01" refParamName="" useRefParam="false" />', b''
            ).replace(
                b'<String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01" refParamName="" useRefParam="false" />', b''
            ).replace(
                b'<String name="resourceName" value="" refParamName="strReturnCityFall" useRefParam="true" />',
                b'<String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/NAME_HERO/IDMODSKIN/huijidi_01" refParamName="" useRefParam="true"/>'
            ).replace(
                b'<String name="resourceName" value="" refParamName="strReturnCityEffectPath" useRefParam="true" />',
                b'<String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/NAME_HERO/IDMODSKIN/huicheng_tongyong_01" refParamName="" useRefParam="true"/>'
            ).replace(
                b'NAME_HERO', NAME_HERO.encode()
            ).replace(
                b'IDMODSKIN', IDMODSKIN.encode()
            )
        
            # Trường hợp đặc biệt cho component_effects
            # Xoá dòng SkinOrAvatarList
            lines = block.splitlines()
            lines = [line for line in lines if b'<SkinOrAvatarList' not in line]
            cleaned = []
            skip = False
            for i, line in enumerate(lines):
                if b'<Vector3i name="scalingInt"' in line:
                    cleaned.append(line)
                    skip = True
                    continue
                if skip:
                    if b'</Event>' in line or b'</Track>' in line:
                        cleaned.append(line)
                        skip = False
                    continue
                cleaned.append(line)
        
            return b'\n'.join(cleaned)

        
        CODE_BV_HERO = []
        next_condition_id = data.count(b'<Track trackName=') 
        
        block_skin = clean_block(found_blocks['skin'])
        CODE_BV_HERO.append(block_skin)

        if external_file:
            with open(external_file, 'rb') as ef:
                external_data = ef.read()
            raw_blocks = re.findall(rb'    <Track trackName=.*?</Track>', external_data, re.DOTALL)
            for block in raw_blocks:
                block = insert_condition(block, next_condition_id)
                next_condition_id += 0
                CODE_BV_HERO.append(block)
        for k in ['p1', 'p2', 'clip1', 'clip2']:
            blk = clean_block(found_blocks[k])
            blk = insert_condition(blk, next_condition_id)
            next_condition_id += 0
            CODE_BV_HERO.append(blk)
        if IDMODSKIN == '16307':
            ryoma = b'    <Track trackName="PlayAnimationTick0" eventType="PlayAnimationTick" guid="6c6f287e-412d-4011-a513-b2727f068c3a" enabled="true" refParamName="" useRefParam="false" r="0.083" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="PlayAnimationTick" time="0.000" isDuration="false">\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n        <String name="clipName" value="Dance04_T2" refParamName="" useRefParam="false"/>\n        <float name="crossFadeTime" value="0.150" refParamName="" useRefParam="false"/>\n        <float name="playSpeed" value="1.000" refParamName="" useRefParam="false"/>\n        <int name="layer" value="3" refParamName="" useRefParam="false"/>\n        <int name="subLayer" value="0" refParamName="" useRefParam="false"/>\n        <bool name="loop" value="false" refParamName="" useRefParam="false"/>\n        <bool name="applyActionSpeed" value="false" refParamName="" useRefParam="false"/>\n        <bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n        <bool name="bNoTimeScale" value="false" refParamName="" useRefParam="false"/>\n        <bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n      </Event>\r\n    </Track>'
            ryoma = insert_condition(ryoma, next_condition_id)
            next_condition_id += 0
            CODE_BV_HERO.append(ryoma)
        injected = b'\n' + b'\n'.join(CODE_BV_HERO) + b'\n'
        if b'</Action>' in data:
            result = data.replace(b'</Action>', injected + b'  </Action>')
        else:
            pass
        with open(back_path, 'wb') as f:
            f.write(result)

            # --------SkinOrAvatarList-------
            with open(back_path, 'rb') as f:
                SkinOrAvatarList = f.read()
            
            SkinOrAvatarList = SkinOrAvatarList.replace(
                b'<SkinOrAvatarList id="' + IDMODSKIN.encode() + b'" />',
                b'<SkinOrAvatarList id="' + IDMODSKIN[:3].encode() + b'00" />'
            )
            
            with open(back_path, 'wb') as f:
                f.write(SkinOrAvatarList)

            print("    Back.xml hoàn tất")
#-----------------------------------------------
    GiaTocEdit = 2
    for haste_file in ['HasteE1.xml', 'HasteE1_leave.xml']:
        duonggia = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/{haste_file}'
        giai(duonggia)
        ID_SKIN_GT = int(IDCHECK)
        ID_SKIN_GT = b'\x00\x00' + ID_SKIN_GT.to_bytes(2, 'little')
        with open(Huanhua, 'rb') as f:
            ab = f.read()
        
        pos = ab.find(ID_SKIN_GT)
        if pos != -1:
            vt_bytes = ab[pos - 2:pos]
            vtr = int.from_bytes(vt_bytes, byteorder='little')
            vt1 = ab[pos - 2 : pos - 2 + vtr]
            DKMODGT = vt1.lower()
            if b'sprint' in DKMODGT or b'jiasu' in DKMODGT:
                try:
                    with open(duonggia, 'r', encoding='utf-8') as f:
                        text = f.read()
                except Exception as e:
                    continue
        
                tracks = re.findall(r'<Track[\s\S]*?</Track>', text)
                block_skinid = None
                block_effect = None
        
                for block in tracks:
                    if block_skinid is None and re.search(r'name=["\']skinId["\']', block):
                        block_skinid = block
                    elif block_effect is None and 'jiasu_tongyong_01' in block:
                        block_effect = block
                    if block_skinid and block_effect:
                        break
        
                if not block_skinid or not block_effect:
                    exit()
                def remove_lines_after_bUseTargetSkinEffect(block: str) -> str:
                    lines = block.splitlines()
                    new_lines = []
                    skip = False
                    for line in lines:
                        if skip:
                            if line.strip().startswith('</Event>'):
                                new_lines.append(line)
                                skip = False
                            continue
                        new_lines.append(line)
                        if '<bool name="bUseTargetSkinEffect"' in line:
                            skip = True
                    return '\n'.join(new_lines)
    
                # Sửa block skinId
                block_skinid = re.sub(
                    r'<int name="skinId" value="\d+" refParamName="" useRefParam="false" ?/>',
                    f'<int name="skinId" value="{IDMODSKIN[:3]}00" refParamName="" useRefParam="false" />',
                    block_skinid
                )
        
                # Sửa block effect
                block_effect = re.sub(r'^\s*<Condition[^>]*?\/>\s*?', '', block_effect, flags=re.MULTILINE)
                
                block_effect = block_effect.replace('common_effects', f'hero_skill_effects/{NAME_HERO}/{IDMODSKIN}')
        
                if IDMODSKIN == '13314':
                    block_effect = block_effect.replace('<Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />', '<Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />')
                if IDMODSKIN == '13314':
                    block_effect = block_effect.replace('jiasu_tongyong_01', 'EF_13314_DiRenJie_sprint_loop')
                elif IDMODSKIN == '11607':
                    block_effect = block_effect.replace('jiasu_tongyong_01', 'jingke_sprint_01')
                elif IDMODSKIN == '15009':
                    block_effect = block_effect.replace('jiasu_tongyong_01', 'T2_Spint').replace('<Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />', '<Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />')
                elif IDMODSKIN == '15015':
                    block_effect = block_effect.replace('jiasu_tongyong_01', '15015_HanXin_sprint_01')
                elif IDMODSKIN == '52414':
                    block_effect = block_effect.replace('jiasu_tongyong_01', '52414_Capheny_sprint_loop')
                elif IDMODSKIN == '54307':
                    block_effect = block_effect.replace('jiasu_tongyong_01', 'yao_sprint')
                elif IDMODSKIN == '13613':
                    block_effect = block_effect.replace('jiasu_tongyong_01', '13613_WuZeTian_sprint')
                elif IDMODSKIN == '16307':
                    block_effect = block_effect.replace('jiasu_tongyong_01', 'JuYouJing_jiasu_01')
                elif IDMODSKIN == '13118':
                    block_effect = block_effect.replace('jiasu_tongyong_01', '13118_Libai_sprint_01_loop')
                elif IDMODSKIN == '13210':
                    if haste_file == 'HasteE1.xml':
                        block_effect = block_effect.replace('jiasu_tongyong_01', 'MaKeBoLuo_Buff_Start')
                    else:
                        block_effect = block_effect.replace('jiasu_tongyong_01', 'MaKeBoLuo_Buff_Start')
                elif IDMODSKIN == '14111':
                    block_effect = block_effect.replace('JiaSu_tongyong_01', '14111_luoer_Sprint').replace(
                        '        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />', '        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />')
                block_effect = remove_lines_after_bUseTargetSkinEffect(block_effect)
    
                # Tính số track
                def count_tracks_above_action_name(filepath, action_name):
                    with open(filepath, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    count = 0
                    for line in lines:
                        if action_name in line:
                            break
                        if 'trackName' in line:
                            count += 1
                    return count
        
                track_count = count_tracks_above_action_name(duonggia, '</Project>')
                effect_lines = block_effect.splitlines()
                
                if GiaTocEdit == 1:
                    # Dùng CheckSkinIdTick → chèn Condition
                    insert_line = f'      <Condition id="{track_count}" guid="{str(uuid.uuid4())}" status="true" />'
                    if len(effect_lines) >= 2:
                        effect_lines.insert(2, insert_line)
                else:
                    # Dùng SkinOrAvatarList → thêm SkinAvatarFilterType="9" và <SkinOrAvatarList>
                    for i, line in enumerate(effect_lines):
                        if line.strip().startswith('<Track ') and 'SkinAvatarFilterType=' not in line:
                            effect_lines[i] = line.rstrip('>') + ' SkinAvatarFilterType="9">'
                            break
                    for i, line in enumerate(effect_lines):
                        if line.strip().startswith('</Event>'):
                            effect_lines.insert(i + 1, f'      <SkinOrAvatarList id="{IDMODSKIN[:3]}00" />')
                            break
                
                block_effect_final = '\n'.join(effect_lines).strip()
                block_skinid_final = block_skinid.strip() if GiaTocEdit == 1 else ''
                block_ghep = ''
                
                if block_skinid_final:
                    block_ghep += f'  {block_skinid_final}\n'
                block_ghep += f'  {block_effect_final}\n'
                if IDMODSKIN == '16707' and haste_file == 'HasteE1.xml':
                    with open(duonggia, 'r', encoding='utf-8') as f: 
                        rpl=f.read()
                        rpl = rpl.replace('JiaSu_tongyong_01','Wukong_Sprint_Idle')
                if IDMODSKIN == '16707' and haste_file == 'HasteE1_leave.xml':
                    with open(duonggia, 'r', encoding='utf-8') as f: 
                        rpl=f.read()
                        rpl = rpl.replace('JiaSu_tongyong_01','Wukong_Sprint')
                if IDMODSKIN == '13210' and haste_file == 'HasteE1.xml':
                    with open(duonggia, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    track_count = 0
                    for line in lines:
                        if '</Project>' in line:
                            break
                        if 'trackName' in line:
                            track_count += 1
                    block_ghep += f'    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="{str(uuid.uuid4())}" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Condition id="{track_count}" guid="{str(uuid.uuid4())}" status="true"/>\n      <Event eventName="TriggerParticle" time="0.000" length="4.000" isDuration="true" guid="{str(uuid.uuid4())}">\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false"/>\n        <TemplateObject name="objectSpaceId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false"/>\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/MaKeBoLuo_Buff_End" refParamName="" useRefParam="false"/>\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false"/>\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\n      </Event>\n      <SkinOrAvatarList id="13200" />\n    </Track>\n'
                pos = text.find('</Action>')
                if pos == -1:
                    pass
                    
                text_moi = text[:pos] + block_ghep +'  '+ text[pos:]
                with open(duonggia, 'w', encoding='utf-8') as f:
                    f.write(text_moi)
                    
                print(f"    [+] {os.path.basename(duonggia)} : Done")
#-----------------------------------------------
    try:
        if IDMODSKIN[:3] in ['150']:
            shutil.copy(
                f"Resources/{Ver}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes",
                f"./{FolderMod}/Resources/{Ver}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes"
            )
            giai(f"./{FolderMod}/Resources/{Ver}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes")
            with open(f"./{FolderMod}/Resources/{Ver}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes", 'rb') as f:
                killboard = f.read()
            if IDMODSKIN in ['15015']:
                killboard=killboard.replace(b'/18/',b'/20/')
            elif IDMODSKIN in ['15012']:
                killboard=killboard.replace(b'\x2C\x00\x00\x00\x10\x00\x00\x00\x1E\x00\x00\x00\x55\x49\x33\x44\x2F\x42\x61\x74\x74\x6C\x65\x2F\x42\x72\x6F\x61\x64\x63\x61\x73\x74\x2F\x31\x36\x2F\x7B\x30\x7D\x2F\x00\x01\x00\x00\x00\x00\x01',b'\x2B\x00\x00\x00\x10\x00\x00\x00\x1D\x00\x00\x00\x55\x49\x33\x44\x2F\x42\x61\x74\x74\x6C\x65\x2F\x42\x72\x6F\x61\x64\x63\x61\x73\x74\x2F\x39\x2F\x7B\x30\x7D\x2F\x00\x01\x00\x00\x00\x00\x01')
            else:
                killboard=killboard.replace(b'/18/',b'/16/')
        with open(f'./{FolderMod}/Resources/{Ver}/Databin/Client/Huanhua/ResKillBillboardCfg.bytes','wb') as f:
            f.write(killboard)
    except Exception as bug:
        pass
#-----------------------------------------------
    if IDMODSKIN == '15710':
        SceneBUFF02 = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/SceneBUFF02.xml'
        giai(SceneBUFF02)
        remove_lines = [
            b'<bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',
            b'<bool name="bEqual" value="false" refParamName="" useRefParam="false" />'
        ]
    
        with open(SceneBUFF02, 'rb') as f:
            lines = f.readlines()
        
        new_lines = []
        count = 0
        for line in lines:
            line = line.replace(b"CheckSkinIdTick", b"CheckHeroIdTick")
            
            line = line.replace(
                f'skinId" value="{IDCHECK}"'.encode('utf-8'), 
                f'heroId" value="{IDCHECK[:3]}"'.encode('utf-8')
            )
        
            if b'prefab_skill_effects/common_effects/jiasu_tongyong_01' in line:
                count += 1
                if count == 2:
                    new_path = f"prefab_skill_effects/hero_skill_effects/{NAME_HERO}/{IDCHECK}/jiasu_tongyong_01".encode('utf-8')
                    line = line.replace(
                        b'prefab_skill_effects/common_effects/jiasu_tongyong_01',
                        new_path
                    )
        
            if line.strip() not in remove_lines:
                new_lines.append(line)
        with open(SceneBUFF02, 'wb') as f:
            f.writelines(new_lines)
#-----------------------------------------------
    def zip_folder(folder_path, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_STORED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=folder_path)
                    zipf.write(file_path, arcname)
    if IDCHECK == "54402":
        giapcuongnoyan = input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
        if giapcuongnoyan.lower() == 'y':	
            with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                giai(file_path)
                with open (file_path, 'rb') as f:
                    noidung = f.read()
                    noidung = noidung.replace(b"</Action>", b"""  <Track trackName="Nhung" eventType="CheckHeroIdTick" guid="NhungAOV-54402" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="544" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="Nhung_AOV" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="0" guid="NhungAOV-54402" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="Nhung_AOV">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/544_Painter/54402/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>""")
                with open (file_path,'wb') as f : f.write(noidung)
                Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense') 
                try:
                    folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                    output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                    zip_folder(folder_path, output_path)
                except Exception as e:
                    print(e)
                shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
        if IDCHECK == "13011":
            giapcuongnoyan = 'y'#input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
            if giapcuongnoyan.lower() == 'y':	
                with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                    f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                    file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                    giai(file_path)
                    with open (file_path, 'rb') as f:
                        noidung = f.read()
                        noidung = noidung.replace(b"</Action>", b"""  <Track trackName="CheckHeroIdTick" eventType="CheckHeroIdTick" guid="54402-YanTanJiro" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="130" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="54402-YanTanJiro" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="0" guid="54402-YanTanJiro" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="54402-YanTanJiro">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/130_GongBenWuZang/13011/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>""")
                    with open (file_path,'wb') as f : f.write(noidung)
                    Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense')
                    try:
                        folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                        output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                        zip_folder(folder_path, output_path)
                    except Exception as e:
                        print(e)
                    shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
        if IDCHECK == "19007":
            giapcuongnoyan = 'y'#input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
            if giapcuongnoyan.lower() == 'y':	
                with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                    f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                    file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                    giai(file_path)
                    with open (file_path, 'rb') as f:
                        noidung = f.read()
                        noidung = noidung.replace(b"</Action>", b"""  <Track trackName="CheckHeroIdTick" eventType="CheckHeroIdTick" guid="54402-YanTanJiro" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="190" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="54402-YanTanJiro" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="0" guid="54402-YanTanJiro" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="54402-YanTanJiro">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/190_ZhuGeLiang/19007/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>""")
                    with open (file_path,'wb') as f : f.write(noidung)
                    Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense')
                    try:
                        folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                        output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                        zip_folder(folder_path, output_path)
                    except Exception as e:
                        print(e)
                    shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
        if IDCHECK == "13210":
            giapcuongnoyan =  'y'#input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
            if giapcuongnoyan.lower() == 'y':	
                with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                    f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                    file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                    giai(file_path)
                    with open (file_path, 'rb') as f:
                        noidung = f.read()
                        noidung = noidung.replace(b"</Action>", b"""  <Track trackName="CheckHeroIdTick" eventType="CheckHeroIdTick" guid="54402-YanTanJiro" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="132" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="54402-YanTanJiro" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="0" guid="54402-YanTanJiro" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="54402-YanTanJiro">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_MaKeBoLuo/13210/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>""")
                    with open (file_path,'wb') as f : f.write(noidung) 
                    Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense')
                    try:
                        folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                        output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                        zip_folder(folder_path, output_path)
                    except Exception as e:
                        print(e)
                    shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
        if IDCHECK == "15710":
            giapcuongnoyan =  'y'#input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
            if giapcuongnoyan.lower() == 'y':	
                with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                    f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                    file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                    giai(file_path)
                    with open (file_path, 'rb') as f:
                        noidung = f.read()
                        noidung = noidung.replace(b"</Action>", b"""  <Track trackName="CheckHeroIdTick" eventType="CheckHeroIdTick" guid="54402-YanTanJiro" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="132" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="54402-YanTanJiro" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="0" guid="54402-YanTanJiro" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="54402-YanTanJiro">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/157_BuZhiHuoWu/15710/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>""")
                    with open (file_path,'wb') as f : f.write(noidung)
                    Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense')
                    try:
                        folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                        output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                        zip_folder(folder_path, output_path)
                    except Exception as e:
                        print(e)
                    shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
    if IDMODSKIN == '59702':
        giapcuongnoyan =  'y'#input("\033[1;97m[\033[1;92m?\033[1;97m] SPECIAL: 54402 - MOD EFX GIÁP CUỒNG NỘ YAN Y/n \n[\033[1;92m•\033[1;97m] INPUT: ")
        if giapcuongnoyan.lower() == 'y':	
            with zipfile.ZipFile(f'Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes') as f:
                f.extractall(f'{FolderMod}/Resources/{Ver}/Ages/mod2/')
                file_path=f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense/1338E1.xml'
                giai(file_path)
                with open (file_path, 'rb') as f:
                    noidung = f.read()
                    noidung = noidung.replace(b'</Action>', b'  <Track trackName="CheckHeroIdTick" eventType="CheckHeroIdTick" guid="54402-YanTanJiro" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="597" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n        <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="3bb07807-0ec8-4d4a-a8fe-385f9e28e4c3" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="2b3af436-2730-4d8d-bb09-c9c742566e4e">\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/597_kuangtie/59702/kuangbao_buff_01" refParamName="" useRefParam="false" />\n        <String name="bindPointName" value="Bip001 L Hand" refParamName="" useRefParam="false" />\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\n      <Event>\n    </Track>\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="ea95a7f5-5cc8-457d-ba3e-11a5e66f1203" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="018aaa4e-cc46-4269-aaca-595cc79d1b4e">\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/597_kuangtie/59702/kuangbao_buff_01" refParamName="" useRefParam="false" />\n        <String name="bindPointName" value="Bip001 R Hand" refParamName="" useRefParam="false" />\n        <bool name="dontShowIfNoBindPoint" value="false" refParamName="" useRefParam="true" />\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>')
                    with open (file_path,'wb') as f : f.write(noidung)
                    Track_Guid_Skill(f'{FolderMod}/Resources/{Ver}/Ages/mod2/Prefab_Gear/Defense')
                    try:
                        folder_path = f'{FolderMod}/Resources/{Ver}/Ages/mod2/'
                        output_path = f'{FolderMod}/Resources/{Ver}/Ages/Prefab_Gear.pkg.bytes'
                        zip_folder(folder_path, output_path)
                    except Exception as e:
                        print(e)
                    shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Ages/mod2/', ignore_errors=True)
#-----------------------------------------------
    antidec = 'n'#input("ANTI_DECOMP__?: ").strip().lower()
    if antidec == 'y':
        enc(directory_path)
#-----------------------------------------------
    INFO_MOD = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/'
    with zipfile.ZipFile(f'Resources/{Ver}/Prefab_Characters/Actor_{IDINFO[:3]}_Infos.pkg.bytes') as f:
        f.extractall(INFO_MOD)
        f.close()
    duong_prefab = INFO_MOD + 'Prefab_Hero/'
    name_hero_list = os.listdir(duong_prefab)

    found = False
    for name in name_hero_list:
        path = os.path.join(duong_prefab, name)
        if name.lower().startswith(f"{IDINFO[:3]}_") and os.path.isdir(path):
            files = os.listdir(path)

            actorinfo_file = None
            for f in files:
                if f.lower() == f"{name.lower()}_actorinfo.bytes":
                    actorinfo_file = f
                    break
            if actorinfo_file is None:
                for f in files:
                    if f.lower().endswith('_actorinfo.bytes'):
                        actorinfo_file = f
                        break

            if actorinfo_file:
                newpath = os.path.join(path, actorinfo_file)
                giai(newpath)
                found = True
    def skincanmod(data):
        trc1=r.find(timtrc,r.find(b'SkinPrefabG'))
        vt1=r.find(b'JTCom0',trc1-300)
        a1=r[vt1-31:]
        a3=vt1 - 31
        skin1=a1[:4]
        skin2=int.from_bytes(skin1,byteorder='little')
        data=r[a3:a3+skin2]
        #open('kb','wb').write(data)
        return data
    op = newpath


    trc=IDINFO
    with open(op,'rb') as f:
        r=f.read()
        r1=r
        timtrc = trc.encode()
        f.close()
    #skin
    mkcam=b''
    teninfobv1=NAME_HERO
    if IDCHECK == '14111':
        teninfobv1='141_DiaoChan'
    tenefec2=teninfobv1.encode()
    tenefec=teninfobv1.lower().encode()
    newteneffec=tenefec[4:].capitalize()
    newteneffec=tenefec[:4]+newteneffec
    str1 = b"hero_skill_effects/" + tenefec2 + b"/"
    str2 = b"hero_skill_effects/" + tenefec + b"/"
    str3 = b"Hero_Skill_Effects/" + tenefec2 + b"/"
    str4 = b"Hero_Skill_Effects/" + tenefec + b"/"
    str5 = b"hero_skill_effects/" + newteneffec + b"/"
    str7 = b"Hero_Skill_Effects/" + newteneffec + b"/"
    IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
    idnew=IDCHECK.encode()+b"/"
    mkcam =b''
    new1=b''
    new1+=skincanmod(r)
    if IDCHECK == '13311':
        if phukienv == "vangv":
            new1=ngoaihinhvaneovvang
        if phukienv == "dov":
            new1=ngoaihinhvaneovdo
        if phukienv == '':
            new1=ngoaihinhvaneov
    if IDCHECK == '16707':
        new1=ngoaihinhkhieov
    if IDCHECK == '52007':
        if phukien == "do":
            new1=ngoaihinhdoveres
        if phukien == "xanh":
            new1=ngoaihinhxanhveres
    IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
    idnew=IDCHECK.encode()+b'/'
    ID1=IDCHECK.encode()
    if new1.find(b'prefab_skill_effects/hero_skill_effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
        FIND=new1.find(b'PreloadAnimatorEffects')-8
        VT1=new1[FIND:FIND+4]
        VTR=int.from_bytes(VT1,byteorder='little')
        VTM=new1[FIND:FIND+VTR]
        VTM9=VTM
        VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
        ELe=VTM.find(b'Element')-8
        ELe1=VTM.find(b'Element')-16
        VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
        DAU=VTM[ELe:ELe+4]
        VTR=int.from_bytes(DAU,byteorder='little')
        VTM1=VTM[ELe:ELe+VTR]#chuẩn
        VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
        VTCUOI=VTM[ELe:]#owr cuoois
        VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
        tinh=VTM.count(b'Element')
        VTM=VTCUOI
        KB=0
        CODEFULL=b''
        for i in range(tinh):
                ELe=VTM.find(b'Element')-8
                DAU=VTM[ELe:ELe+4]
                VTR=int.from_bytes(DAU,byteorder='little')
                VTM1=VTM[ELe:ELe+VTR]#chuẩn
                if VTM1.find(b'Vprefab_skill_effects/hero_skill_effects/') == -1:
                    CODEFULL+=VTM1
                    break
                VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                VTCUOI=VTM[VTR:]
                ELe1=VTM.find(b'Element')+7
                DAU1=VTM[ELe1:ELe1+4]
                VTR=int.from_bytes(DAU1,byteorder='little')
                VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                newvt=VTM1.find(b'Vprefab_skill_effects/')-8
                MOI=VTM1[newvt:newvt+4]
                VTR=int.from_bytes(MOI,byteorder='little')
                VTR3=VTM1[newvt:newvt+VTR]
                VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                VTM=VTCUOI
                CODEFULL+=CODE
        CODEFULL=CODEFULL.replace(str1,str1+ idnew).replace(str2,str2 + idnew)#.to_bytes(4,byteorder='little')
        CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
        new1=new1.replace(VTM9,CODEFULL)
        new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
        mkcam = b'\x05'#\x05
    if new1.find(b'Prefab_Skill_Effects/Hero_Skill_Effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
        FIND=new1.find(b'PreloadAnimatorEffects')-8
        VT1=new1[FIND:FIND+4]
        VTR=int.from_bytes(VT1,byteorder='little')
        VTM=new1[FIND:FIND+VTR]
        VTM9=VTM
        VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
        ELe=VTM.find(b'Element')-8
        ELe1=VTM.find(b'Element')-16
        VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
        DAU=VTM[ELe:ELe+4]
        VTR=int.from_bytes(DAU,byteorder='little')
        VTM1=VTM[ELe:ELe+VTR]#chuẩn
        VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
        VTCUOI=VTM[ELe:]#owr cuoois
        VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
        tinh=VTM.count(b'Element')
        VTM=VTCUOI
        KB=0
        CODEFULL=b''
        for i in range(tinh):
                ELe=VTM.find(b'Element')-8
                DAU=VTM[ELe:ELe+4]
                VTR=int.from_bytes(DAU,byteorder='little')
                VTM1=VTM[ELe:ELe+VTR]#chuẩn
                if VTM1.find(b'VPrefab_Skill_Effects/Hero_Skill_Effects/') == -1:
                    CODEFULL+=VTM1
                    break
                VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                VTCUOI=VTM[VTR:]
                ELe1=VTM.find(b'Element')+7
                DAU1=VTM[ELe1:ELe1+4]
                VTR=int.from_bytes(DAU1,byteorder='little')
                VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                newvt=VTM1.find(b'VPrefab_Skill_Effects/')-8
                MOI=VTM1[newvt:newvt+4]
                VTR=int.from_bytes(MOI,byteorder='little')
                VTR3=VTM1[newvt:newvt+VTR]
                VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                VTM=VTCUOI
                CODEFULL+=CODE
        CODEFULL=CODEFULL.replace(str3,str3 + idnew).replace(str4,str4 + idnew)#.to_bytes(4,byteorder='little')
        CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
        new1=new1.replace(VTM9,CODEFULL)
        new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
        mkcam = b'\x05'#\x05
    skinmoi=new1
    skinprefag=r.find(b'SkinPrefabG')-8
    tinhskinpre=r[skinprefag:skinprefag+4]
    tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
    tinhskinpre2=r[skinprefag:skinprefag+tinhskinpre1] #
    JTCom0 = tinhskinpre2.count(b"JTCom0")
    beginskin=tinhskinpre2[:101]
    CodeSkinNew=beginskin+new1*JTCom0 #
    tinhCodeSkinNew1=CodeSkinNew[:93]
    tinhCodeSkinNew=CodeSkinNew[93:]
    Elenmen=len(tinhCodeSkinNew).to_bytes(4,byteorder='little')+tinhCodeSkinNew[4:]
    SkinPrefag1=tinhCodeSkinNew1+Elenmen
    SkinPrefag=len(SkinPrefag1).to_bytes(4,byteorder='little')+SkinPrefag1[4:]
    codeskinnew=r1.replace(tinhskinpre2,SkinPrefag)

    def ArtSkinPrefabLOD(data3):
        a=skinmoi.find(b'\x00ArtSkinPrefabLOD')-7
        a10=skinmoi.find(b'\x00ArtSkinPrefabLOD')-3
        a3=skinmoi[a:a+8]
        a4=a3[4:]
        a2=skinmoi[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=skinmoi[a:a+vitri]
        a25=skinmoi[a10:a10+vitri2]
        a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD',b'\x00ArtPrefabLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data3=len(code).to_bytes(4,byteorder='little')+code[4:]
        return data3 
    def ArtSkinLobbyShowLOD(data4):
        a=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-7
        a10=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-3
        a3=skinmoi[a:a+8]
        a4=a3[4:]
        a2=skinmoi[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=skinmoi[a:a+vitri]
        a25=skinmoi[a10:a10+vitri2]
        a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyShowLOD',b'\x00ArtLobbyShowLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data4=len(code).to_bytes(4,byteorder='little')+code[4:]
        return data4
    def ArtSkinLobbyIdleShowLOD(data4):
        a = camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD') - 7
        a10 = camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD') - 3
        a3 = camSkin[a:a+8]
        a4 = a3[4:]
        a2 = camSkin[a:a+4]
        vitri = int.from_bytes(a2, byteorder='little')
        ne = camSkin[vitri:]
        vitri2 = int.from_bytes(a4, byteorder='little')
        a5 = camSkin[a:a+vitri]
        a25 = camSkin[a10:a10+vitri2]
        a22 = camSkin[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyIdleShowLOD', b'\x00ArtLobbyIdleShowLOD')
        a13 = len(a22).to_bytes(4, byteorder='little') + a22[4:]
        code = a5.replace(a25, a13)
        data4 = len(code).to_bytes(4, byteorder='little') + code[4:] + ne
        return data4
#-----------------------------------------------
    def ArtPrefabLODnew(data):
        a = ab.find(b'\x00ArtPrefabLOD') - 7
        a2 = ab[a:a+4]
        a3 = ab[a:a+5]
        a4 = a3[4:5]  # số 10
        vitri = int.from_bytes(a2, byteorder='little')
        data = ab[a:a+vitri]
        return data

    def ArtPrefabLODExnew(data4):
        a = ab.find(b'\x00ArtPrefabLODEx') - 7
        a2 = ab[a:a+4]
        a3 = ab[a:a+5]
        a4 = a3[4:5]  # số 10
        vitri = int.from_bytes(a2, byteorder='little')
        data4 = ab[a:a+vitri]
        return data4
#-----------------------------------------------
    def ArtSkinPrefabLODnew(data3):
        a = ab.find(b'\x00ArtSkinPrefabLOD') - 7
        a10 = ab.find(b'\x00ArtSkinPrefabLOD') - 3
        a3 = ab[a:a+8]
        a4 = a3[4:]
        a2 = ab[a:a+4]
        vitri = int.from_bytes(a2, byteorder='little')
        vitri2 = int.from_bytes(a4, byteorder='little')
        a5 = ab[a:a+vitri]
        a25 = ab[a10:a10+vitri2]
        a22 = ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD', b'\x00ArtPrefabLOD')
        a13 = len(a22).to_bytes(4, byteorder='little') + a22[4:]
        code = a5.replace(a25, a13)
        data3 = len(code).to_bytes(2, byteorder='little') + code[2:]
        return data3
#-----------------------------------------------
    def ArtSkinPrefabLODExnew(data2):
        a = ab.find(b'\x00ArtSkinPrefabLODEx') - 7
        a10 = ab.find(b'\x00ArtSkinPrefabLODEx') - 3
        a3 = ab[a:a+8]
        a4 = a3[4:]
        a2 = ab[a:a+4]
        vitri = int.from_bytes(a2, byteorder='little')
        vitri2 = int.from_bytes(a4, byteorder='little')
        a5 = ab[a:a+vitri]
        a25 = ab[a10:a10+vitri2]
        a22 = ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLODEx', b'\x00ArtPrefabLODEx')
        a13 = len(a22).to_bytes(4, byteorder='little') + a22[4:]
        code = a5.replace(a25, a13)
        data2 = len(code).to_bytes(4, byteorder='little') + code[4:]
        return data2

    #codeskinmd
    SkinMD=r[:skinprefag]

    #skinmd Art
    Art=SkinMD.find(b'ArtPrefabLOD')-8
    tinhskinpre=SkinMD[Art:Art+4]
    tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
    tinhskinpre2=SkinMD[Art:Art+tinhskinpre1] #
    #skinmd ArtLobbyShowLOD
    ArtLobby=SkinMD.find(b'ArtLobbyShowLOD')-8
    tinhArtLobby=SkinMD[ArtLobby:ArtLobby+4]
    tinhArtLobby1=int.from_bytes(tinhArtLobby,byteorder='little')
    tinhArtLobby2=SkinMD[ArtLobby:ArtLobby+tinhArtLobby1] #
    ArtSkinPrefab=b''
    ArtSkinPrefab+=ArtSkinPrefabLOD(skinmoi)
    CodeNewMD=SkinMD.replace(tinhskinpre2,ArtSkinPrefab)
    ArtSkinLobby=b''
    ArtSkinLobby+=ArtSkinLobbyShowLOD(skinmoi)
    CodeNewMD=CodeNewMD.replace(tinhArtLobby2,ArtSkinLobby)
    ArtLobbyIdle=CodeNewMD.find(b'ArtLobbyIdleShowLOD0')-8
    cammd=CodeNewMD[ArtLobbyIdle:999999]
    ArtLobbyIdleSkin=skinmoi.find(b'ArtSkinLobbyIdleShowLOD')-8
    camSkin=skinmoi[ArtLobbyIdleSkin:999999]
    camSkin=ArtSkinLobbyIdleShowLOD(camSkin)
    if mkcam == b'\x05':
        camSkin=camSkin.replace(CODEFULL,b'')
    CodeNewMD=CodeNewMD.replace(cammd,camSkin)
    CodeFull=codeskinnew.replace(SkinMD,CodeNewMD)
    RootDtrc=CodeFull[:84]
    RootDsau=CodeFull[84:]
    RootD1=RootDsau[8:12]
    VTR=int.from_bytes(RootD1,byteorder='little')#ArtPrefabLOD
    m=RootDsau.find(b'ArtPrefabLOD')-8
    FIXTRIEUVAN=b'\x61\x00\x00\x00\x19\x00\x00\x00\x75\x73\x65\x53\x74\x61\x74\x65\x44\x72\x69\x76\x65\x6E\x4D\x65\x63\x61\x6E\x69\x6D\x3C\x00\x00\x00\x03\x00\x00\x00\x0D\x00\x00\x00\x06\x00\x00\x00\x4A\x54\x50\x72\x69\x1A\x00\x00\x00\x08\x00\x00\x00\x54\x79\x70\x65\x53\x79\x73\x74\x65\x6D\x2E\x42\x6F\x6F\x6C\x65\x61\x6E\x0D\x00\x00\x00\x05\x00\x00\x00\x56\x54\x72\x75\x65\x04\x00\x00\x00'
    #if IDCHECK == '12912':
        #RootDsau=RootDsau[:VTR+8]+FIXTRIEUVAN+RootDsau[m:] 
    tinhRootDsau=len(RootDsau).to_bytes(4,byteorder='little')+RootDsau[4:]
    tinhRootDtrc=RootDtrc+tinhRootDsau
    CodeDayDu=len(tinhRootDtrc).to_bytes(4,byteorder='little')+tinhRootDtrc[4:]
    CodeDayDu=CodeDayDu.replace(b"Light<",b"00000<")
    CodeDayDu = CodeDayDu.replace(b"imeline<", b"1234567<")
    CodeDayDu=CodeDayDu.replace(b'_LOD2',b'_LOD1').replace(b'_LOD3',b'_LOD1').replace(b'_Show2\x04',b'_Show1\x04').replace(b'_Show3\x04',b'_Show1\x04')
    tinhcam=CodeDayDu[:89]
    with open(op,'wb')as f: f.write(CodeDayDu)
    o=open(op,'rb')
    h=o.read(92)
    k=0
    while True:
        r1=o.read(4)
        if r1==b'':
            break
        KB=r1.hex()
        KB=KB[6:8]+KB[4:6]+KB[2:4]+KB[0:2]
        KB=int(KB,16)
        O=r1+o.read(KB-4)
        k+=1
    o.close()
    k=k.to_bytes(1,byteorder='little')
    tinhcam1=CodeDayDu[:88]+k
    CodeDayDu=CodeDayDu.replace(tinhcam,tinhcam1)
    with open(op,'wb')as f: f.write(CodeDayDu)
    print(f'    {os.path.basename(actorinfo_file)}')
    print('   Actor_'+IDINFO[:3]+'_Infos.pkg.bytes'+' Done')
    

#-----------------------------------------------
    SkinSpecial = IDMODSKIN
    IDM = IDMODSKIN
    if SkinSpecial in ['19015', '11620', '13118', '54805','13213','11215'] or IDM[:3] == '196':

        if IDM[:3] == '196':
            if b"Skin_Icon_Skill" in dieukienmod:
                giai(f'./{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
                LC = '1'
                Directory = f'./{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes'
                process_directory(Directory, LC)
                with open(Directory, 'rb') as code_elsu:
                    elsu = code_elsu.read()
                    elsu = elsu.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/196_Elsu/BaiLiShouYue_attack02_spell01_LOD', b'Prefab_Skill_Effects/Hero_Skill_Effects/196_Elsu/' + IDCHECK.encode() + b'/BaiLiShouYue_attack02_spell01_LOD')
                with open(Directory, 'wb') as f:
                    f.write(elsu)
                LC = '2'
                Directory = f'./{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes'
                process_directory(Directory, LC)
                #-----------------------------------------------
        if IDM == "19015":
            Directory = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/190_ZhuGeLiang/190_ZhuGeLiang_actorinfo.bytes'
    
            LC = '1'
            process_directory(Directory, LC)
            with open(Directory, 'rb') as code_tulen:
                tulen = code_tulen.read()
                tulen = tulen.replace(
                    b'<useMecanim var="String" type="System.Boolean" value="True"/>',
                    b''
                )
    
            with open(Directory, 'wb') as f:
                f.write(tulen)
            print('\tRemove ' + b'<useMecanim var="String" type="System.Boolean" value="True"/>'.decode())

            LC = '2'
            process_directory(Directory, LC)
#-----------------------------------------------
        if IDM == "17408":
            Directory = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/174_YuJi/174_YuJi_actorinfo.bytes'
    
            LC = '1'
            process_directory(Directory, LC)
            with open(Directory, 'rb') as code_tulen:
                tulen = code_tulen.read()
                tulen = tulen.replace(b'<useMecanim var="String" type="System.Boolean" value="True"/>',b'',1)
    
            with open(Directory, 'wb') as f:
                f.write(tulen)
            print('\tRemove ' + b'<useMecanim var="String" type="System.Boolean" value="True"/>'.decode())
            LC = '2'
            process_directory(Directory, LC)
#-----------------------------------------------
        if IDM == '11620':
            player = input('   Phụ Kiện\n   1. Ngân Nguyệt Lưu\n   2. Hồng Quang Chiến Ngọc\n   3. No Component\n >>> ')
            if player == '1':
                Directory = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/116_JingKe/116_JingKe_actorinfo.bytes'
                LC = '1'
                process_directory(Directory, LC)
                with open(Directory, 'rb') as f:
                    pk1 = f.read()
                    pk1 = pk1.replace(
                        b'AW1', b'AW5').replace(b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>', b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>\n  <ArtSkinLobbyShowMovie var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_Movie"/>').replace(b'116_JingKe/11621_JingKe_AW5_LOD', b'116_JingKe/Component/11621_JingKe_RT_3_LOD').replace(b'116_JingKe/11621_JingKe_AW5_Show', b'116_JingKe/Component/11621_JingKe_RT_3_Show')
        
                with open(Directory, 'wb') as f:
                    f.write(pk1)
        
                LC = '2'
                process_directory(Directory, LC)
            if player == '2':
                Directory = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/116_JingKe/116_JingKe_actorinfo.bytes'
                LC = '1'
                process_directory(Directory, LC)
                with open(Directory, 'rb') as f:
                    pk2 = f.read()
                    pk2 = pk2.replace(
                        b'AW1', b'AW5').replace(b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>', b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>\n  <ArtSkinLobbyShowMovie var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_Movie"/>').replace(b'116_JingKe/11621_JingKe_AW5_LOD', b'116_JingKe/Component/11621_JingKe_RT_2_LOD').replace(b'116_JingKe/11621_JingKe_AW5_Show', b'116_JingKe/Component/11621_JingKe_RT_2_Show')
        
                with open(Directory, 'wb') as f:
                    f.write(pk2)
        
                LC = '2'
                process_directory(Directory, LC)
                
            if player == '3':
                Directory = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/116_JingKe/116_JingKe_actorinfo.bytes'
                LC = '1'
                process_directory(Directory, LC)
                with open(Directory, 'rb') as f:
                    nopk = f.read()
                    nopk = nopk.replace(
                        b'AW1', b'AW5').replace(b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>', b'<ArtSkinLobbyShowCamera var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW5_Cam"/>\n  <ArtSkinLobbyShowMovie var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_Movie"/>')
        
                with open(Directory, 'wb') as f:
                    f.write(nopk)
        
                LC = '2'
                process_directory(Directory, LC)
        if IDM in ['54805','13118','13213','11215']:
            shutil.rmtree(f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/')
            idg = IDINFO
            pf = idg[:3]
            ip = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/'
            pkg = f'Resources/{Ver}/Prefab_Characters/Actor_{pf}_Infos.pkg.bytes'
            
            with zipfile.ZipFile(pkg, 'r') as f:
                f.extractall(ip)
            def auto_rename_bytes_xml(folder):
                count = 0
                for root, _, files in os.walk(folder):
                    for file in files:
                        old_path = os.path.join(root, file)
            
                        if file.endswith('.bytes'):
                            new_file = file[:-6] + '.xml'
                        elif file.endswith('.xml'):
                            new_file = file[:-4] + '.bytes'
                        else:
                            continue
            
                        new_path = os.path.join(root, new_file)
            
                        if os.path.exists(new_path):
                            continue
            
                        os.rename(old_path, new_path)
                        count += 1
            def is_main(f):
                l = f.lower()
                return (
                    l.endswith('_actorinfo.bytes')
                    and 'tutorial' not in l
                    and 'tutorail' not in l
                    and 'xinshou' not in l
                    and 'racenpc' not in l
                )
            
            af = None
            for r, _, fs in os.walk(ip):
                vf = [f for f in fs if is_main(f)]
                if vf:
                    for f in vf:
                        if f.lower().startswith(idg.lower() + '_'):
                            af = os.path.join(r, f)
                            break
                    if not af:
                        af = os.path.join(r, vf[0])
                    break
            
            if not af:
                exit()
            
            giai(af)
            process_directory(af, '1')
            auto_rename_bytes_xml(os.path.dirname(af))
            
            axml = af.replace(".bytes", ".xml")
            if not os.path.exists(axml):
                exit()
            
            if idg == '5486':
                p = f'{FolderMod}/Resources/{Ver}/Prefab_Characters/mod/Prefab_Hero/548_SunCe/548_SunCe_actorinfo.xml'
                with open(p, 'rb') as f:
                    b = f.read()
                    b = b.replace(b'<useNewMecanim var="String" type="System.Boolean" value="True"/>', b'', 1)
                    b = b.replace(b'<oriSkinUseNewMecanim var="String" type="System.Boolean" value="True"/>', b'', 1)
                with open(p, 'wb') as f:
                    f.write(b)
        
            def find_skin(txt, sid):
                tg = '<Element var="Com" type="Assets.Scripts.GameLogic.SkinElement">'
                pos = 0
                while True:
                    si = txt.find(tg, pos)
                    if si == -1:
                        break
                    ei, oc = si, 0
                    for m in re.finditer(r'<(/?Element\b[^>]*)>', txt[si:]):
                        t = m.group(1)
                        ei = si + m.end()
                        if t.endswith('/'): continue
                        elif t.startswith('/'): oc -= 1
                        else: oc += 1
                        if oc == 0: break
                    seg = txt[si:ei]
                    if f'/{sid}_' in seg or f'/{sid}' in seg:
                        try:
                            ET.fromstring(f"<Root>{seg}</Root>")
                            return seg
                        except: return None
                    pos = ei
                return None
            
            def find_prefab(txt, sid):
                pos = 0
                while True:
                    si = txt.find('<ArtPrefabLOD', pos)
                    if si == -1: break
                    ei = txt.find('<SkinPrefab var="Array" type="Assets.Scripts.GameLogic.SkinElement[]">', si)
                    if ei == -1: break
                    seg = txt[si:ei]
                    print(f"[DEBUG] {seg}")
                    if f"/{sid}_" in seg or f"/{sid}" in seg:
                        return seg
                    pos = ei + 1
                return None
            
            with open(axml, "r", encoding="utf-8") as f:
                txt = f.read()
            
            new_txt = txt
            src_id = idg
            
            for i in range(1, 31):
                dst_id = f"{pf}{i}"
                if dst_id == src_id:
                    continue
                try:
                    seg_src = find_prefab(new_txt, src_id) or find_skin(new_txt, src_id)
                    seg_dst = find_prefab(new_txt, dst_id) or find_skin(new_txt, dst_id)
                    if seg_src and seg_dst:
                        new_txt = new_txt.replace(seg_dst, seg_src)
                except: pass
            
            with open(axml, "w", encoding="utf-8") as f:
                f.write(new_txt)
            
            with open(axml, "rb") as f:
                d = f.read().decode('utf8')
            d = d.replace('<ArtSkinPrefabLOD var="Array" type="System.String[]">', '<ArtPrefabLOD var="Array" type="System.String[]">', 1)
            d = d.replace('</ArtSkinPrefabLOD>', '</ArtPrefabLOD>', 1)
            d = d.replace('<ArtSkinPrefabLODEx', '<ArtPrefabLODEx', 1)
            d = d.replace('</ArtSkinPrefabLODEx>', '</ArtPrefabLODEx>', 1)
            d = d.replace('<ArtSkinLobbyIdleShowLOD var="Array" type="System.String[]">', '<ArtLobbyIdleShowLOD var="Array" type="System.String[]">', 1)
            d = d.replace('</ArtSkinLobbyIdleShowLOD>', '</ArtLobbyIdleShowLOD>', 1)
            d = d.replace('<ArtSkinLobbyShowLOD var="Array" type="System.String[]">', '<ArtLobbyShowLOD var="Array" type="System.String[]">', 1)
            d = d.replace('</ArtSkinLobbyShowLOD>', '</ArtLobbyShowLOD>', 1)
            d = d.replace('<Element var="Com" type="Assets.Scripts.GameLogic.SkinElement">', '', 1)
            d = re.sub(r'<ActorName var="String" type="System.String" value=".*?"/>','<ActorName var="String" type="System.String" value="Mod_By_Tran_Thi_Nhung"/>',d)
            d = d.replace('LOD3','LOD1').replace('LOD2','LOD1').replace('Show3','Show1').replace('Show2','Show1')
            d = re.sub(
                r'[ \t]*<ArtSkinLobbyNode var="String" type="System.String" value="Prefab_Characters/Prefab_Hero/531_keera/5312_Keera_Show1_Node"/>\s*\n?',
                '', d, count=1
            )
            d = d.replace('    </Element><SkinPrefab var="Array" type="Assets.Scripts.GameLogic.SkinElement[]">', '  <SkinPrefab var="Array" type="Assets.Scripts.GameLogic.SkinElement[]">')
            
            with open(axml, "w", encoding="utf-8") as f:
                f.write(d)
            print('\t\t'+'Fix Đứng Animation')
            def clean(axml):
                with open(axml, 'r', encoding='utf-8') as f:
                    lns = f.readlines()
            
                new = []
                i = 0
                while i < len(lns):
                    c = lns[i].strip()
                    n = lns[i + 1].strip() if i + 1 < len(lns) else ""
                    if c == "</Element>" and (n.startswith('<SkinPrefab') or n.startswith("<CrossFadeTime") or n.startswith("<FallbackSkinId")):
                        i += 1
                        continue
                    new.append(lns[i])
                    i += 1
            
                with open(axml, 'w', encoding='utf-8') as f:
                    f.writelines(new)
            
            clean(axml)
            auto_rename_bytes_xml(os.path.dirname(axml))
            process_directory(af, '2')
#-----------------------------------------------
    with zipfile.ZipFile(FolderMod+f"/Resources/{Ver}/Prefab_Characters/Actor_"+IDMODSKIN[:3]+"_Infos.pkg.bytes", 'w', zipfile.ZIP_STORED) as z:
        for r, d, f in os.walk(FolderMod+f'/Resources/{Ver}/Prefab_Characters/mod/'):
            for file in f:
                p = os.path.join(r, file)
                z.write(p, os.path.relpath(p, FolderMod+'/Resources/'+Ver+'/Prefab_Characters/mod/'))
        shutil.rmtree(FolderMod+'/Resources/'+Ver+'/Prefab_Characters/mod/')
#-----------------------------------------------
    with zipfile.ZipFile(FolderMod+'/Resources/'+Ver+'/Ages/Prefab_Characters/Prefab_Hero/Actor_'+IDMODSKIN[:3]+"_Actions.pkg.bytes", 'w', zipfile.ZIP_STORED) as z:
        for r, d, f in os.walk(FolderMod+f'/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod4/'):
            for file in f:
                p = os.path.join(r, file)
                z.write(p, os.path.relpath(p, FolderMod+f'/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod4/'))
    shutil.rmtree(FolderMod+f'/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod4/')
#-----------------------------------------------
with zipfile.ZipFile(f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes"
, 'w', zipfile.ZIP_STORED) as z:
    for root, _, files in os.walk(f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1"):
        for f in files:
            fp = os.path.join(root, f)
            z.write(fp, os.path.relpath(fp, f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1"))

shutil.rmtree(f"{FolderMod}/Resources/{Ver}/Ages/Prefab_Characters/Prefab_Hero/mod1")
shutil.rmtree("mod5", ignore_errors=True)
#-----------------------------------------------