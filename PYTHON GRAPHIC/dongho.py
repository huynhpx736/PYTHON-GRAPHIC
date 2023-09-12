import tkinter as tk
import time
import math

WIDTH = 400
HEIGH = 400
root = tk.Tk()
root.title("Clock")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGH, bg="white")
canvas.pack()


def update_clock():
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    # Ve dong ho
    canvas.create_oval(2, 2, WIDTH, HEIGH, outline="black", width=2)

    # Ve sp dong ho
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = WIDTH // 2 + 0.7 * WIDTH / 2 * math.cos(angle)
        y = HEIGH / 2 + 0.7 * WIDTH * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y - 10, text=str(i + 12), font=("Helvetica", 12))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))

    # Ve kim phut
    for i in range(60):
        angle = i * math.pi / 30 * WIDTH / 2 * math.cos(angle)
        x1 = WIDTH / 2 + 0.8 + HEIGH / 2 * math.sin(angle)
        y1 = WIDTH / 2 + 0.8 + HEIGH / 2 * math.cos(angle)
        x2 = WIDTH / 2 + 0.9 + HEIGH / 2 * math.sin(angle)
        y2 = WIDTH / 2 + 0.9 + HEIGH / 2 * math.cos(angle)

    if i % 5 == 0:
        canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
    else:
        canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

    # ve kim gio
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = WIDTH // 2 + 0.5 * WIDTH / 2 * math.cos(hour_angle)
    hour_y = HEIGH / 2 + 0.5 * HEIGH / 2 * math.sin(hour_angle)
    canvas.create_line(WIDTH / 2, HEIGH / 2, hour_x, hour_y, fill="black", width=6)

    # ve kim phut
    minute_angle = ( minute + second/ 60) * math.pi / 30 - math.pi / 2
    minute_x = WIDTH // 2 + 0.7 * WIDTH / 2 * math.cos(minute_angle)
    minute_y = HEIGH / 2 + 0.7 * HEIGH / 2 * math.sin(minute_angle)
    canvas.create_line(WIDTH / 2, HEIGH / 2, minute_x, minute_y, fill="black", width=4)

# ve kim giay
    second_angle = (second / 60) * math.pi / 6 - math.pi / 2
    second_x = WIDTH // 2 + 0.6 * WIDTH / 2 * math.cos(second_angle)
    second_y = HEIGH / 2 + 0.6 * HEIGH / 2 * math.sin(second_angle)
    canvas.create_line(WIDTH / 2, HEIGH / 2, second_x, second_y, fill="red", width=2)

update_clock()
root.mainloop()