import pandas as pd
import os
from tkinter import *
from tkinter import filedialog, messagebox

class FileSelector:
    def __init__(self):
        # 创建主窗口
        self.root = Tk()
        self.root.withdraw()  # 隐藏主窗口，但不影响对话框
        
        # 将窗口置于屏幕中央
        self.center_window()
        
    def center_window(self):
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 计算窗口位置
        x = (screen_width - 200) // 2
        y = (screen_height - 100) // 2
        
        # 设置窗口位置
        self.root.geometry(f"200x100+{x}+{y}")
        
    def select_file(self):
        # 显示文件选择对话框
        file_path = filedialog.askopenfilename(
            title="请选择Excel文件",
            filetypes=[("Excel files", "*.xlsx")],
            initialdir=os.path.expanduser("~")  # 从用户主目录开始
        )
        return file_path
        
    def save_file(self):
        # 显示保存文件对话框
        file_path = filedialog.asksaveasfilename(
            title="保存积分排名",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            initialdir=os.path.expanduser("~")  # 从用户主目录开始
        )
        return file_path
    
    def cleanup(self):
        self.root.destroy()

def calculate_points(row):
    score = row['对阵比分'].split(':')
    winner_score = int(score[0])
    loser_score = int(score[1])
    
    points = {
        row['胜者姓名']: 0,
        row['败者姓名']: 0
    }
    
    if winner_score == 2 and loser_score == 0:
        points[row['胜者姓名']] = 3
        points[row['败者姓名']] = 0
    elif winner_score == 2 and loser_score == 1:
        points[row['胜者姓名']] = 2
        points[row['败者姓名']] = 1
        
    return points

def analyze_matches(df):
    group_points = {}
    match_counts = {}
    player_groups = {}  # 新增：记录每个选手所属的组别
    
    for _, row in df.iterrows():
        group = row['比赛组别']
        points = calculate_points(row)
        
        winner = row['胜者姓名']
        loser = row['败者姓名']
        
        # 记录选手所属组别
        player_groups[winner] = group
        player_groups[loser] = group
        
        if winner not in match_counts:
            match_counts[winner] = {}
        if loser not in match_counts:
            match_counts[loser] = {}
            
        match_counts[winner][loser] = match_counts[winner].get(loser, 0) + 1
        match_counts[loser][winner] = match_counts[loser].get(winner, 0) + 1
        
        if group not in group_points:
            group_points[group] = {}
            
        for player, point in points.items():
            if player not in group_points[group]:
                group_points[group][player] = 0
            group_points[group][player] += point
    
    # 处理积分排名
    results = []
    for group, players in group_points.items():
        for player, points in players.items():
            if points > 0:
                results.append({
                    '比赛组别': group,
                    '选手姓名': player,
                    '总积分': points
                })
    
    result_df = pd.DataFrame(results)
    group_order = {'高级组': 1, '中级组': 2, '初级组': 3}
    result_df['组别顺序'] = result_df['比赛组别'].map(group_order)
    result_df = result_df.sort_values(['组别顺序', '总积分'], ascending=[True, False])
    result_df = result_df.drop('组别顺序', axis=1)
    
    # 创建对阵统计，按组别分类
    match_records = []
    all_players = sorted(match_counts.keys())
    
    for player1 in all_players:
        for player2 in all_players:
            if player1 < player2:  # 只处理一次每对选手
                count = match_counts[player1].get(player2, 0)
                if count > 0:  # 只添加有比赛记录的对阵
                    group1 = player_groups[player1]
                    match_records.append({
                        '组别': group1,
                        '选手1': player1,
                        '选手2': player2,
                        '对阵次数': count
                    })
    
    match_df = pd.DataFrame(match_records)
    
    # 如果有对阵记录，按组别和对阵次数排序
    if not match_df.empty:
        # 添加组别顺序用于排序
        match_df['组别顺序'] = match_df['组别'].map(group_order)
        match_df = match_df.sort_values(['组别顺序', '对阵次数'], ascending=[True, False])
        match_df = match_df.drop('组别顺序', axis=1)  # 删除辅助排序列
    
    return result_df, match_df

def print_formatted_table(result_df):
    # 获取最大名字长度，用于对齐
    max_name_length = max(len(str(name)) for name in result_df['选手姓名'])
    max_name_length = max(max_name_length, 4)  # 确保至少4个字符宽度
    
    # 打印表头
    print("组别" + " " * (max_name_length - 2) + "姓名" + " " * 4 + "积分")
    print("-" * (max_name_length + 12))  # 打印分隔线
    
    # 按组别打印
    current_group = None
    for _, row in result_df.iterrows():
        if current_group != row['比赛组别']:
            current_group = row['比赛组别']
            if _ != 0:  # 不是第一行时打印分隔线
                print("-" * (max_name_length + 12))
        
        # 如果是该组的第一行，打印组别
        if _ == 0 or result_df.iloc[_-1]['比赛组别'] != current_group:
            group_name = current_group
        else:
            group_name = ""
        
        # 计算对齐所需的空格
        name_spaces = " " * (max_name_length - len(str(row['选手姓名'])))
        score_spaces = " " * (6 - len(str(row['总积分'])))
        
        # 打印行
        if group_name:
            group_spaces = " " * (max_name_length - len(group_name))
            print(f"{group_name}{group_spaces}{row['选手姓名']}{score_spaces}{row['总积分']}")
        else:
            print(" " * len(current_group) + " " * (max_name_length - len(current_group)) + 
                  f"{row['选手姓名']}{score_spaces}{row['总积分']}")

def print_formatted_matches(match_df):
    if match_df.empty:
        print("没有任何对阵记录")
        return
        
    current_group = None
    for _, row in match_df.iterrows():
        if current_group != row['组别']:
            current_group = row['组别']
            print(f"\n{current_group}:")
        print(f"  {row['选手1']} vs {row['选手2']}: {row['对阵次数']}场")

def main():
    try:
        file_selector = FileSelector()
        file_path = file_selector.select_file()
        
        if not file_path:
            print("未选择文件，程序退出")
            return
        
        print(f"正在读取文件: {file_path}")
        df = pd.read_excel(file_path)
        
        required_columns = ['比赛时间', '比赛组别', '胜者姓名', '对阵比分', '败者姓名', '比赛地点']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"错误：Excel文件缺少以下列：{', '.join(missing_columns)}")
            return
        
        result_df, match_df = analyze_matches(df)
        
        # 打印积分排名
        print("\n积分排名：")
        print_formatted_table(result_df)
        
        # 打印对阵统计
        print("\n选手对阵次数统计：")
        print_formatted_matches(match_df)
        
        output_path = file_selector.save_file()
        
        if output_path:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                result_df.to_excel(writer, sheet_name='积分排名', index=False)
                match_df.to_excel(writer, sheet_name='对阵统计', index=False)
            print(f"\n结果已保存到：{output_path}")
    
    except Exception as e:
        print(f"发生错误：{str(e)}")
        messagebox.showerror("错误", str(e))
    
    finally:
        if file_selector:
            file_selector.cleanup()

if __name__ == "__main__":
    main()