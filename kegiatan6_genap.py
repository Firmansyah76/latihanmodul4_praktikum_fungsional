def point(x, y):
    return x, y

def line_equation_of(pl, M):
    # Menghitung nilai C (konstanta)
    x, y = pl
    C = y - M * x

    # Membuat dan mengembalikan persamaan garis
    return f"y = {M:.2f}x + {C:.2f}"

# Titik (6, -2) dan gradien -2
point_l = point(3, -6)
gradien = -4  # Ubah gradien sesuai dengan pernyataan

# Mencetak persamaan garis yang melalui titik (6, -2) dan bergradien -2
print("Persamaan garis yang melalui titik (3, -6) dan bergradien -4:")
print(line_equation_of(point_l, gradien))