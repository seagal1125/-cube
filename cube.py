import pycuber as pc
import kociemba
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# ✅ 對應顏色名稱 → RGB
color_map = {
    'white': 'white',
    'yellow': 'yellow',
    'red': 'red',
    'orange': 'orange',
    'blue': 'blue',
    'green': 'green'
}

# ✅ 畫 3x3 貼紙方格
def draw_face(ax, face, start_x, start_y):
    for i in range(3):
        for j in range(3):
            color = color_map[face[i][j].colour]
            square = plt.Rectangle((start_x + j, start_y + i), 1, 1, facecolor=color, edgecolor='black')
            ax.add_patch(square)

# ✅ 畫展開六面
def draw_cube_on_ax(ax, cube):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    face_coords = {
        'U': (3, 9),
        'L': (0, 6),
        'F': (3, 6),
        'R': (6, 6),
        'B': (9, 6),
        'D': (3, 3)
    }
    for face in ['U', 'L', 'F', 'R', 'B', 'D']:
        face_data = cube.get_face(face)
        x, y = face_coords[face]
        draw_face(ax, face_data, x, y)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)

# ✅ 隨機打亂公式
def generate_scramble(n=20):
    moves = ['U', 'D', 'L', 'R', 'F', 'B']
    suffixes = ['', "'", '2']
    scramble = []
    prev_move = ''
    for _ in range(n):
        move = random.choice(moves)
        while move == prev_move:
            move = random.choice(moves)
        prev_move = move
        scramble.append(move + random.choice(suffixes))
    return ' '.join(scramble)

# ✅ 轉換為 Kociemba 格式字串（中心格定義六面）
def to_facelet_str(cube):
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    colour_to_facelet = {
        cube.get_face('U')[1][1].colour: 'U',
        cube.get_face('R')[1][1].colour: 'R',
        cube.get_face('F')[1][1].colour: 'F',
        cube.get_face('D')[1][1].colour: 'D',
        cube.get_face('L')[1][1].colour: 'L',
        cube.get_face('B')[1][1].colour: 'B'
    }

    result = ''
    for face in face_order:
        for row in cube.get_face(face):
            for sticker in row:
                result += colour_to_facelet[sticker.colour]
    return result

# ▶ 主程式
cube = pc.Cube()
scramble_formula = generate_scramble()
print("🔀 打亂步驟：", scramble_formula)
cube(pc.Formula(scramble_formula))

# ✅ 儲存每一步狀態
states = [cube.copy()]

# ✅ 解法
facelets = to_facelet_str(cube)
print("Kociemba 字串：", facelets)
solution = kociemba.solve(facelets)
print("🧩 解法步驟：", solution)

# ✅ 模擬每一步
for step in solution.split():
    cube(step)
    states.append(cube.copy())

# ✅ 畫動畫
fig, ax = plt.subplots()

def update(frame):
    draw_cube_on_ax(ax, states[frame])
    ax.set_title(f"第 {frame}/{len(states)-1} 步")

ani = animation.FuncAnimation(fig, update, frames=len(states), interval=800)
plt.show()

# ✅ 輸出成 GIF（可選）
# ani.save("cube_solution.gif", writer="pillow", fps=1)