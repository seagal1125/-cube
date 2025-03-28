#facelet = "WWWWWROWB rbbyryyoy wbwogobgg  orogybgbb rggwogyyy orgrboryr".lower().replace(' ', '')
#facelet = "YWGBWWOWW rryrrbobr bgggggorb  wyyyyrbgy oywboowog rogobwbyr".lower().replace(' ', '')
#facelet = "gwowwgbbg oryrrowrr oowggyyob ryowybggb royboyrbbgrygbywww".lower().replace(' ', '')
#facelet = "wbowwgwwb oyybrrbry bgyggywoo rywrywgbb goryooybggoogbrrwr".lower().replace(' ', '')
#facelet = "yoyyryrbb bggogowbw  gbbgyboro yyywogrgg ryrrboorg".lower().replace(' ', '')
facelet = "bobgwggby owrbrwogy wrgwgogbw oybryrbrr oyroobwyw yyyobggwr".lower().replace(' ', '')
# 自訂顏色代碼對應
color_name = {
    'o': 'orange',
    'r': 'red',
    'w': 'white',
    'b': 'blue',
    'y': 'yellow',
    'g': 'green'
}

# 直接定義顏色到面的映射
color_to_face = {
    'w': 'U',  # white -> Up
    'y': 'D',  # yellow -> Down
    'g': 'F',  # green -> Front
    'b': 'B',  # blue -> Back
    'o': 'L',  # orange -> Left
    'r': 'R'   # red -> Right
}

# 轉換
converted = ''.join(color_to_face[c] for c in facelet)

print("轉換後 WCA Facelet 字串：")
print(converted.upper())

from collections import Counter

#facelets = "LUBUURUUUDLDDRDRBBBFFLFLUBUDDDULFRFFFBBFDBLRLRDRRBLLRF"
print(Counter(converted.upper()))