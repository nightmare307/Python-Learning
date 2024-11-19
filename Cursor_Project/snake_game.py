import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
TONGUE_COLOR = (255, 150, 150)
FRUIT_COLORS = {
    'apple': (255, 0, 0),
    'banana': (255, 255, 0),
    'orange': (255, 165, 0),
    'watermelon': (144, 238, 144)
}

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
INITIAL_SPEED = 1  # 初始速度倍数
BASE_GAME_SPEED = 15  # 基础游戏速度

# 创建游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 7  # 修改初始长度为7
        # 创建初始蛇身
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2
        self.positions = [(center_x - i * BLOCK_SIZE, center_y) for i in range(7)]  # 创建7个初始位置
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN  # 初始颜色
        self.body_color = DARK_GREEN  # 初始身体颜色
        self.pattern_color = LIGHT_GREEN  # 初始花纹颜色
        self.score = 0
        self.is_eating = False
        self.eating_timer = 0
        self.eating_duration = 10
        self.tongue_out = False
        self.tongue_timer = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*BLOCK_SIZE)) % WINDOW_WIDTH, (cur[1] + (y*BLOCK_SIZE)) % WINDOW_HEIGHT)
        if new in self.positions[3:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return True

    def draw(self, surface):
        for i, pos in enumerate(self.positions):
            if i == 0:  # 蛇头
                # 绘制基本蛇头
                pygame.draw.rect(surface, self.color, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
                
                # 添加光影效果
                highlight = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE//2))
                highlight.set_alpha(100)
                highlight.fill(LIGHT_GREEN)
                surface.blit(highlight, (pos[0], pos[1]))
                
                # 添加眼睛和瞳孔
                eye_color = (0, 0, 0)
                eye_size = BLOCK_SIZE // 4
                pupil_color = (255, 255, 255)
                pupil_size = eye_size // 2

                # 根据方向绘制眼睛
                if self.direction == UP:
                    eye_positions = [(pos[0] + eye_size, pos[1] + eye_size),
                                   (pos[0] + BLOCK_SIZE - eye_size, pos[1] + eye_size)]
                elif self.direction == DOWN:
                    eye_positions = [(pos[0] + eye_size, pos[1] + BLOCK_SIZE - eye_size),
                                   (pos[0] + BLOCK_SIZE - eye_size, pos[1] + BLOCK_SIZE - eye_size)]
                elif self.direction == LEFT:
                    eye_positions = [(pos[0] + eye_size, pos[1] + eye_size),
                                   (pos[0] + eye_size, pos[1] + BLOCK_SIZE - eye_size)]
                else:  # RIGHT
                    eye_positions = [(pos[0] + BLOCK_SIZE - eye_size, pos[1] + eye_size),
                                   (pos[0] + BLOCK_SIZE - eye_size, pos[1] + BLOCK_SIZE - eye_size)]

                for eye_pos in eye_positions:
                    pygame.draw.circle(surface, eye_color, eye_pos, eye_size)
                    pygame.draw.circle(surface, pupil_color, 
                                     (eye_pos[0] + pupil_size//2, eye_pos[1]), pupil_size)

                # 添加吃东西的动画效果
                mouth_open = self.is_eating and (self.eating_timer < self.eating_duration/2)
                if mouth_open:
                    # 张嘴效果
                    mouth_color = (200, 100, 100)  # 口腔颜色
                    mouth_size = BLOCK_SIZE // 3
                    mouth_pos = None
                    
                    if self.direction == UP:
                        mouth_pos = (pos[0] + BLOCK_SIZE//2, pos[1])
                    elif self.direction == DOWN:
                        mouth_pos = (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE)
                    elif self.direction == LEFT:
                        mouth_pos = (pos[0], pos[1] + BLOCK_SIZE//2)
                    else:  # RIGHT
                        mouth_pos = (pos[0] + BLOCK_SIZE, pos[1] + BLOCK_SIZE//2)
                    
                    pygame.draw.circle(surface, mouth_color, mouth_pos, mouth_size)
                    
                    # 添加舌头
                    tongue_length = BLOCK_SIZE // 2
                    tongue_width = BLOCK_SIZE // 6
                    
                    if self.direction == UP:
                        pygame.draw.rect(surface, TONGUE_COLOR, 
                            (pos[0] + BLOCK_SIZE//2 - tongue_width//2, 
                             pos[1] - tongue_length,
                             tongue_width, tongue_length))
                    elif self.direction == DOWN:
                        pygame.draw.rect(surface, TONGUE_COLOR,
                            (pos[0] + BLOCK_SIZE//2 - tongue_width//2,
                             pos[1] + BLOCK_SIZE,
                             tongue_width, tongue_length))
                    elif self.direction == LEFT:
                        pygame.draw.rect(surface, TONGUE_COLOR,
                            (pos[0] - tongue_length,
                             pos[1] + BLOCK_SIZE//2 - tongue_width//2,
                             tongue_length, tongue_width))
                    else:  # RIGHT
                        pygame.draw.rect(surface, TONGUE_COLOR,
                            (pos[0] + BLOCK_SIZE,
                             pos[1] + BLOCK_SIZE//2 - tongue_width//2,
                             tongue_length, tongue_width))

                if self.is_eating:
                    self.eating_timer += 1
                    if self.eating_timer >= self.eating_duration:
                        self.is_eating = False
                        self.eating_timer = 0

            else:  # 蛇身
                # 绘制圆角矩形
                radius = BLOCK_SIZE // 4
                rect = pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(surface, self.body_color, rect, border_radius=radius)
                
                # 添加花纹
                pattern_color = self.pattern_color
                pattern_offset = BLOCK_SIZE // 6
                
                # 绘制菱形花纹
                points = [
                    (pos[0] + BLOCK_SIZE//2, pos[1] + pattern_offset),
                    (pos[0] + BLOCK_SIZE - pattern_offset, pos[1] + BLOCK_SIZE//2),
                    (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE - pattern_offset),
                    (pos[0] + pattern_offset, pos[1] + BLOCK_SIZE//2)
                ]
                pygame.draw.polygon(surface, pattern_color, points)

                # 添加光影效果
                highlight = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE//3))
                highlight.set_alpha(50)
                highlight.fill(LIGHT_GREEN)
                surface.blit(highlight, (pos[0], pos[1]))

    def change_color(self, fruit_type):
        # 根据水果类型改变蛇的颜色
        if fruit_type == 'apple':
            self.color = FRUIT_COLORS['apple']
            self.body_color = (200, 0, 0)  # 深红色
            self.pattern_color = (255, 100, 100)  # 浅红色
        elif fruit_type == 'banana':
            self.color = FRUIT_COLORS['banana']
            self.body_color = (200, 200, 0)  # 深黄色
            self.pattern_color = (255, 255, 100)  # 浅黄色
        elif fruit_type == 'orange':
            self.color = FRUIT_COLORS['orange']
            self.body_color = (200, 100, 0)  # 深橙色
            self.pattern_color = (255, 200, 100)  # 浅橙色
        elif fruit_type == 'watermelon':
            self.color = FRUIT_COLORS['watermelon']
            self.body_color = (100, 200, 100)  # 深绿色
            self.pattern_color = (150, 255, 150)  # 浅绿色

class Food:
    def __init__(self, count=1):
        self.positions = []
        self.types = []
        self.count = count
        self.fruit_types = ['apple', 'banana', 'orange', 'watermelon']  # 水果类型列表
        self.randomize_all_positions()

    def randomize_position(self):
        while True:
            new_pos = (random.randint(0, (WINDOW_WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE,
                      random.randint(0, (WINDOW_HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE)
            if new_pos not in self.positions:
                self.positions.append(new_pos)
                # 随机选择一个水果类型
                self.types.append(random.choice(self.fruit_types))
                break

    def randomize_all_positions(self):
        self.positions = []
        self.types = []
        for _ in range(self.count):
            self.randomize_position()

    def draw(self, surface):
        for pos, fruit_type in zip(self.positions, self.types):
            if fruit_type == 'apple':
                # 绘制苹果
                pygame.draw.circle(surface, FRUIT_COLORS[fruit_type], 
                                 (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE//2), 
                                 BLOCK_SIZE//2)
                # 添加苹果柄和叶子
                pygame.draw.line(surface, (101, 67, 33),
                               (pos[0] + BLOCK_SIZE//2, pos[1] + 2),
                               (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE//4),
                               2)
                pygame.draw.ellipse(surface, GREEN,
                                  (pos[0] + BLOCK_SIZE//2, pos[1], BLOCK_SIZE//4, BLOCK_SIZE//4))
                
            elif fruit_type == 'banana':
                # 绘制弧形香蕉
                pygame.draw.arc(surface, FRUIT_COLORS[fruit_type],
                              (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE),
                              0.5, 4, BLOCK_SIZE//2)
                
            elif fruit_type == 'orange':
                # 绘制橙子及其纹理
                pygame.draw.circle(surface, FRUIT_COLORS[fruit_type],
                                 (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE//2),
                                 BLOCK_SIZE//2)
                pygame.draw.arc(surface, (255, 140, 0),
                              (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE),
                              0, 3.14, 2)
                
            elif fruit_type == 'watermelon':
                # 绘制西瓜片
                pygame.draw.circle(surface, FRUIT_COLORS[fruit_type],
                                 (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE//2),
                                 BLOCK_SIZE//2)
                # 添加条纹和籽
                for i in range(3):
                    offset = i * BLOCK_SIZE//4
                    pygame.draw.line(surface, DARK_GREEN,
                                   (pos[0] + offset, pos[1]),
                                   (pos[0] + offset, pos[1] + BLOCK_SIZE),
                                   2)
                pygame.draw.circle(surface, BLACK,
                                 (pos[0] + BLOCK_SIZE//2, pos[1] + BLOCK_SIZE//2),
                                 2)

            # 为所有水果添加光泽效果
            highlight = pygame.Surface((BLOCK_SIZE//4, BLOCK_SIZE//4))
            highlight.set_alpha(100)
            highlight.fill(WHITE)
            surface.blit(highlight, (pos[0] + BLOCK_SIZE//4, pos[1] + BLOCK_SIZE//4))

# 定义方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.options = ['Resume', 'New Game', 'Food Count: < 1 >', 'Speed: < 1.0x >', 'Exit']
        self.selected = 0
        self.food_count = 1
        self.speed_multiplier = 1.0
        self.rects = []  # 存储每个选项的矩形区域
        self.left_arrows = []  # 存储左箭头的矩形区域
        self.right_arrows = []  # 存储右箭头的矩形区域

    def draw(self, surface):
        menu_height = 40 * len(self.options)
        start_y = (WINDOW_HEIGHT - menu_height) // 2

        # 绘制半透明背景
        s = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        s.set_alpha(128)
        s.fill(BLACK)
        surface.blit(s, (0, 0))

        # 更新选项文本
        self.options[2] = f'Food Count: < {self.food_count} >'
        self.options[3] = f'Speed: < {self.speed_multiplier:.1f}x >'
        
        self.rects = []  # 清空旧的矩形列表
        self.left_arrows = []  # 清空左箭头列表
        self.right_arrows = []  # 清空右箭头列表

        for i, option in enumerate(self.options):
            color = WHITE if i == self.selected else GRAY
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(WINDOW_WIDTH//2, start_y + 40 * i))
            self.rects.append(rect)
            surface.blit(text, rect)

            # 修正箭头点击区域的计算
            if i in [2, 3]:  # Food Count 和 Speed 选项
                # 计算 "<" 和 ">" 的确切位置
                text_width = rect.width
                text_center = rect.centerx
                
                # 找到箭头在文本中的位置
                left_arrow_pos = option.find('<')
                right_arrow_pos = option.find('>')
                
                # 计算箭头前的文本宽度
                left_text = option[:left_arrow_pos]
                right_text = option[:right_arrow_pos]
                left_width = self.font.render(left_text, True, color).get_width()
                right_width = self.font.render(right_text, True, color).get_width()
                
                # 创建箭头的点击区域
                arrow_height = rect.height
                arrow_width = 20
                
                left_arrow_rect = pygame.Rect(
                    text_center - text_width//2 + left_width,
                    rect.y,
                    arrow_width,
                    arrow_height
                )
                
                right_arrow_rect = pygame.Rect(
                    text_center - text_width//2 + right_width,
                    rect.y,
                    arrow_width,
                    arrow_height
                )
                
                self.left_arrows.append(left_arrow_rect)
                self.right_arrows.append(right_arrow_rect)

                # 当选中时显示箭头的点击区域（调试用，可以注释掉）
                if self.selected == i:
                    pygame.draw.rect(surface, GRAY, left_arrow_rect, 1)
                    pygame.draw.rect(surface, GRAY, right_arrow_rect, 1)

    def handle_mouse_motion(self, pos):
        # 检查鼠标是否悬停在选项上
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(pos):
                self.selected = i
                return

    def handle_click(self, pos):
        # 处理箭头点击
        for i, (left_arrow, right_arrow) in enumerate(zip(self.left_arrows, self.right_arrows)):
            if left_arrow.collidepoint(pos):
                if i == 0:  # Food Count
                    self.food_count = max(1, self.food_count - 1)
                    return True, "food"
                elif i == 1:  # Speed
                    self.speed_multiplier = max(0.5, self.speed_multiplier - 0.1)
                    return True, "speed"
            elif right_arrow.collidepoint(pos):
                if i == 0:  # Food Count
                    self.food_count = min(10, self.food_count + 1)
                    return True, "food"
                elif i == 1:  # Speed
                    self.speed_multiplier = min(3.0, self.speed_multiplier + 0.1)
                    return True, "speed"
        
        # 处理普通选项击
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(pos):
                return True, i
        return False, None

def main():
    snake = Snake()
    food = Food()
    menu = Menu()
    running = True
    paused = False
    game_speed = BASE_GAME_SPEED * menu.speed_multiplier

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                elif paused:
                    if event.key == pygame.K_UP:
                        menu.selected = (menu.selected - 1) % len(menu.options)
                    elif event.key == pygame.K_DOWN:
                        menu.selected = (menu.selected + 1) % len(menu.options)
                    elif event.key == pygame.K_LEFT:
                        if menu.selected == 2:  # 食物数量
                            menu.food_count = max(1, menu.food_count - 1)
                            food = Food(menu.food_count)
                        elif menu.selected == 3:  # 速度
                            menu.speed_multiplier = max(0.5, menu.speed_multiplier - 0.1)
                            game_speed = BASE_GAME_SPEED * menu.speed_multiplier
                    elif event.key == pygame.K_RIGHT:
                        if menu.selected == 2:  # 食物数量
                            menu.food_count = min(10, menu.food_count + 1)
                            food = Food(menu.food_count)
                        elif menu.selected == 3:  # 速度
                            menu.speed_multiplier = min(3.0, menu.speed_multiplier + 0.1)
                            game_speed = BASE_GAME_SPEED * menu.speed_multiplier
                    elif event.key == pygame.K_RETURN:
                        if menu.selected == 0:    # Resume
                            paused = False
                        elif menu.selected == 1:  # New Game
                            snake = Snake()
                            food = Food(menu.food_count)
                            paused = False
                        elif menu.selected == 4:  # Exit
                            pygame.quit()
                            sys.exit()
                elif not paused:
                    if event.key == pygame.K_UP and snake.direction != DOWN:
                        snake.direction = UP
                    elif event.key == pygame.K_DOWN and snake.direction != UP:
                        snake.direction = DOWN
                    elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                        snake.direction = LEFT
                    elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                        snake.direction = RIGHT
            elif event.type == pygame.MOUSEMOTION and paused:
                menu.handle_mouse_motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                if event.button == 1:  # 左键点击
                    clicked, result = menu.handle_click(event.pos)
                    if clicked:
                        if result == "food":
                            food = Food(menu.food_count)
                        elif result == "speed":
                            game_speed = BASE_GAME_SPEED * menu.speed_multiplier
                        elif result == 0:    # Resume
                            paused = False
                        elif result == 1:  # New Game
                            snake = Snake()
                            food = Food(menu.food_count)
                            paused = False
                        elif result == 4:  # Exit
                            pygame.quit()
                            sys.exit()

        if not paused:
            if not snake.update():
                running = False

            # 检查是否吃到食物
            head_pos = snake.get_head_position()
            for i, pos in enumerate(food.positions[:]):
                if head_pos == pos:
                    snake.length += 1
                    snake.score += 1
                    snake.is_eating = True
                    snake.eating_timer = 0
                    # 改变蛇的颜色
                    snake.change_color(food.types[i])
                    food.positions.remove(pos)
                    food.types.pop(i)
                    food.randomize_position()

        # 绘制游戏界面
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        
        # 显示分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        if paused:
            menu.draw(screen)
        
        pygame.display.update()
        clock.tick(game_speed)

    # 游戏结束处理
    game_over_menu = Menu()
    game_over_menu.options = ['Play Again', 'Exit']
    game_over_menu.selected = 0
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_over_menu.selected = (game_over_menu.selected - 1) % len(game_over_menu.options)
                elif event.key == pygame.K_DOWN:
                    game_over_menu.selected = (game_over_menu.selected + 1) % len(game_over_menu.options)
                elif event.key == pygame.K_RETURN:
                    if game_over_menu.selected == 0:  # Play Again
                        main()  # 重新开始游戏
                        return
                    else:  # Exit
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                game_over_menu.handle_mouse_motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    for i, rect in enumerate(game_over_menu.rects):
                        if rect.collidepoint(event.pos):
                            if i == 0:  # Play Again
                                main()
                                return
                            else:  # Exit
                                pygame.quit()
                                sys.exit()

        # 绘制游戏结束界面
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        
        # 显示游戏结束文本
        font = pygame.font.Font(None, 48)
        game_over_text = font.render(f'Game Over! Final Score: {snake.score}', True, WHITE)
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//3))
        screen.blit(game_over_text, text_rect)

        # 绘制结束菜单
        game_over_menu.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main() 