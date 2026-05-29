def rect_area(w, h):
    return w * h

w, h = map(int, input().split())

print(rect_area(w, h))
print(rect_area(h=h, w=w))