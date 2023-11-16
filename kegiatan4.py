import math

def transformations():
    P = (3, 5)

    def translate(x, y, tx, ty):# memindahkan bangunan geometri di bidang dengan jarak yang konstan
        return x + tx, y + ty

    def dilate(x, y, sx, sy):# mengubah ukuran suatu bangunan geometri
        return x * sx, y * sy

    def rotate(x, y, angle):# memutar bangunan geometri
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)
        return x * cos_val - y * sin_val, x * sin_val + y * cos_val

    print("Koordinat setelah translasi:", translate(P[0], P[1], 2, -1))
    print("Koordinat setelah dilatasi:", dilate(P[0], P[1], 2, -1))
    print("Koordinat setelah rotasi:", rotate(P[0], P[1], 30))

transformations()