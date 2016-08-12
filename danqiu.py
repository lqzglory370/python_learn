from tkinter import *
import random
import time
class Ball:     #两个参数，画布和球的颜色
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        #左上角坐标和右下角坐标，椭圆填充颜色。
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)      #混排元组元素
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        #获取当前画布高度
        self.canvas_width = self.canvas.winfo_width()
        #获取当前画布的宽度
        self.hit_bottom = False
        self.score = 0

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #通过id返回画布上任何画好的东西的x、y坐标。
        
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.itemconfig(paddle.tip2, state='normal')
            canvas.itemconfig(paddle.tip3, state='normal')
            canvas.itemconfig(self.tip4, state='normal')
        if self.hit_paddle(pos) == True:      
            self.score = self.score+1
            self.tip4 = canvas.create_text(320, 250, text=self.score, font=('Helvetica',20), state='hidden')
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        #四个if控制小球在碰到边界时返回，而不消失。

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.begin)
        self.ready = False
        self.tip1 = canvas.create_text(250, 200, text='Click to Start the Game.', fill='black', font=('Helvetica',20))
        self.tip2 = canvas.create_text(250, 200, text='Game Over !', fill='black', font=('Helvetica',20), state='hidden')
        self.tip3 = canvas.create_text(200, 250, text='Your Score is : ', font=('Helvetica',20), state='hidden')
         
            
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        #在x变量的方向上移动球拍
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        #这组if判断是否撞到了左右边界

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def begin(self, evt):
        canvas.itemconfig(self.tip1, state='hidden')
        self.ready = True

tk = Tk()
tk.title("Game")        #文件标题
tk.resizable(0, 0)      #使窗口大小不可调整（0, 0）表示水平和垂直方向
tk.wm_attributes("-topmost", 1)     #包含画布的窗口放在所有其他窗口之前
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
#highlightthickness默认值为0，不带高亮边框
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.hit_bottom == False and paddle.ready == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    
