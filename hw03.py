"""
Circles

Name: Russell Harvey
File: hw03
"""

import turtle as tt

def draw_circles(radius, instances):
    if instances == 1:
        tt.circle(radius)
    elif instances > 1:
        tt.circle(radius)
        tt.up()
        tt.left(90)
        tt.fd(radius)
        tt.right(90)
        tt.fd(radius)
        tt.down()
        draw_circles(radius / 2, instances - 1)
        tt.up()
        tt.left(180)
        tt.fd(radius * 2)
        tt.left(180)
        tt.down()
        draw_circles(radius / 2, instances - 1)
        tt.up()
        tt.fd(radius)
        tt.right(90)
        tt.fd(radius)
        tt.left(90)

def main():
    n = input("Please input an 'N' value (depth of the function): ")
    n = int(n)
    draw_circles(100, n)

main()