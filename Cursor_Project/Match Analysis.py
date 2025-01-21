import pandas as pd
import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

class FileSelector:
    def __init__(self):
        # 创建主窗口
        self.root = Tk()
        self.root.title("比赛积分统计程序")
        
        # 设置窗口大小和位置
        self.center_window()
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        
        # 配置主窗口的网格权重
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # 配置主框架的网格权重
        main_frame.grid_columnconfigure(0, weight=3)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)  # 让预览区域可以扩展
        
        # 文件路径显示
        self.file_path = StringVar()
        path_entry = ttk.Entry(main_frame, textvariable=self.file_path, width=50)
        path_entry.grid(row=0, column=0, padx=5, pady=5)
        
        # 选择文件按钮
        select_btn = ttk.Button(main_frame, text="选择Excel文件", command=self.select_file)
        select_btn.grid(row=0, column=1, padx=5, pady=5)
        
        # 创建按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # 分析按钮
        analyze_btn = ttk.Button(button_frame, text="开始分析", command=self.analyze)
        analyze_btn.pack(side=LEFT, padx=10)
        
        # 退出按钮
        exit_btn = ttk.Button(button_frame, text="退出程序", command=self.cleanup)
        exit_btn.pack(side=LEFT, padx=10)
        
        # 创建表格切换按钮框架
        self.sheet_frame = ttk.Frame(main_frame)
        self.sheet_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky='ew')
        self.sheet_frame.grid_remove()  # 初始隐藏
        
        # 创建表格切换按钮
        self.rank_btn = ttk.Button(self.sheet_frame, text="积分排名", command=lambda: self.switch_table('rank'))
        self.rank_btn.pack(side=LEFT, padx=5)
        
        self.match_btn = ttk.Button(self.sheet_frame, text="对阵统计", command=lambda: self.switch_table('match'))
        self.match_btn.pack(side=LEFT, padx=5)
        
        # 创建表格预览区域
        self.preview_frame = ttk.Frame(main_frame)
        self.preview_frame.grid(row=3, column=0, columnspan=2, pady=5, sticky=(N, W, E, S))
        
        # 配置预览框架的网格权重
        self.preview_frame.grid_columnconfigure(0, weight=1)
        self.preview_frame.grid_rowconfigure(0, weight=1)
        
        # 创建表格
        self.tree = ttk.Treeview(self.preview_frame)
        self.tree.grid(row=0, column=0, sticky=(N, W, E, S))  # 使用grid而不是pack
        
        # 添加垂直滚动条
        vsb = ttk.Scrollbar(self.preview_frame, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky=(N, S))
        
        # 添加水平滚动条
        hsb = ttk.Scrollbar(self.preview_frame, orient="horizontal", command=self.tree.xview)
        hsb.grid(row=1, column=0, sticky=(E, W))
        
        # 配置树形表格的滚动
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # 初始隐藏预览区域
        self.preview_frame.grid_remove()
        
        # 下载按钮改名为导出按钮（初始隐藏）
        self.download_btn = ttk.Button(button_frame, text="导出", command=self.save_file)
        self.download_btn.pack(side=LEFT, padx=10)
        self.download_btn.pack_forget()
        
        # 保存分析结果的变量
        self.result_df = None
        self.match_df = None
        
        self.selected_file = None
        
    def center_window(self):
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 设置窗口大小
        window_width = 630
        window_height = 120
        
        # 计算窗口位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # 设置窗口位置和大小
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="请选择Excel文件",
            filetypes=[("Excel files", "*.xlsx")],
            initialdir=os.path.expanduser("~")
        )
        if file_path:
            self.file_path.set(file_path)
            self.selected_file = file_path
            
    def switch_table(self, table_type):
        """切换显示的表格"""
        # 清空现有表格
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if table_type == 'rank':
            df = self.result_df
            self.rank_btn.state(['disabled'])
            self.match_btn.state(['!disabled'])
        else:
            df = self.match_df
            self.match_btn.state(['disabled'])
            self.rank_btn.state(['!disabled'])
            
        # 设置表格列
        self.tree['columns'] = list(df.columns)
        self.tree['show'] = 'headings'
        
        # 设置列标题和列宽
        for column in df.columns:
            self.tree.heading(column, text=column)
            # 根据内容设置合适的列宽
            max_width = max(
                len(str(df[column].max())),
                len(column)
            ) * 10 + 20  # 添加一些额外空间
            self.tree.column(column, width=max_width, minwidth=50)
        
        # 添加数据
        for _, row in df.iterrows():
            self.tree.insert('', END, values=list(row))
            
    def analyze(self):
        if not self.selected_file:
            messagebox.showwarning("警告", "请先选择Excel文件！")
            return
            
        try:
            df = pd.read_excel(self.selected_file)
            self.result_df, self.match_df = analyze_matches(df)
            
            # 显示表格切换按钮和预览区域
            self.sheet_frame.grid()
            self.preview_frame.grid()
            
            # 默认显示积分排名表格
            self.switch_table('rank')
            
            # 显示下载按钮
            self.download_btn.pack(side=LEFT, padx=10)
            
            # 调整窗口大小并设置最小尺寸
            self.root.geometry("800x600")
            self.root.minsize(800, 600)  # 设置最小窗口大小
            
        except Exception as e:
            messagebox.showerror("错误", str(e))
    
    def save_file(self):
        """保存文件功能"""
        if self.result_df is None or self.match_df is None:
            messagebox.showwarning("警告", "没有可保存的数据！")
            return
            
        save_path = filedialog.asksaveasfilename(
            title="保存分析结果",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            initialdir=os.path.dirname(self.selected_file)
        )
        
        if save_path:
            try:
                with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                    self.result_df.to_excel(writer, sheet_name='积分排名', index=False)
                    self.match_df.to_excel(writer, sheet_name='对阵统计', index=False)
                messagebox.showinfo("成功", f"结果已保存到：{save_path}")
            except Exception as e:
                messagebox.showerror("错误", f"保存文件时出错：{str(e)}")
    
    def cleanup(self):
        """退出程序"""
        if messagebox.askokcancel("确认退出", "确定要退出程序吗？"):
            self.root.quit()
            self.root.destroy()
    
    def run(self):
        self.root.mainloop()

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
        file_selector.run()
    except Exception as e:
        print(f"发生错误：{str(e)}")
        messagebox.showerror("错误", str(e))

if __name__ == "__main__":
    main()