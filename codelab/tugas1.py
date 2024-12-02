def create_board(width, height):
    return [['o' if (i + j) % 2 == 0 else 'x' for i in range(width)] for j in range(height)]

# Contoh penggunaan
pola1 = create_board(5, 5)
for row in pola1:
    print(row)


def chessboard(papan):
    return [['#' if cell == 'o' else '+' for cell in row] for row in papan]

# Contoh penggunaan
pola1 = create_board(5, 5)  # Nested list dari kode sebelumnya
pola2 = chessboard(pola1)

for row in pola2:
    print(row)
