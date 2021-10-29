from turtle import *
A = [30] * 6
D = [30, -360, -120, -120, -360, 120 ]
for a, d in zip(A, D):
    left(d)
    forward(a)
left(90)
mainloop()