import simpleguitk as simplegui,math



W = 1000
H =   600
r= 200
n =1
angle = 0
points=[]
angleSum = 360/n
count =1


def find_point(angle_sum, radius):
  coordiante = []
  coordiante.append(math.cos(math.radians(angle_sum+angle)) * radius)
  coordiante.append(math.sin(math.radians(angle_sum+angle)) * radius)
  points.append(coordiante)


def draw(canvas):
    global count,n,points,angleSum,r,angle

    points = []
    for i in range(0, n):
        find_point(angleSum*i+1, r)
    for i in range(0,n):
        canvas.draw_line(((W / 2)+points[i][0],(H / 2)+points[i][1]), ((W / 2)+points[(i+1)%n][0],(H / 2)+points[(i+1)%n][1]), 1, 'green')
        for x in range(0,n):
            canvas.draw_line(((W / 2) + points[i][0], (H / 2) + points[i][1]),((W / 2) + points[x][0], (H / 2) + points[x][1]), 1, 'green')
    angle = angle + 1
    if (count%60) == 0:
        n = n+1
        points = []
        angleSum = 360 / n
    count = count + 1


frame = simplegui.create_frame("Points", W, H)
frame.set_draw_handler(draw)

frame.start()

