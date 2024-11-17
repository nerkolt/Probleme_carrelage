import tkinter as tk
from random import randint

# Définir une variable globale pour suivre le numéro de tuile actuel pour les formes en L
tile_number = 0

def create_board(size):
    # Initialiser un échiquier de taille n x n rempli de zéros
    return [[0] * size for _ in range(size)]

def place_defective_cell(board):
    # Placer une cellule défectueuse de manière aléatoire sur l'échiquier
    size = len(board)
    row, col = randint(0, size - 1), randint(0, size - 1)
    board[row][col] = -1  # Marquer la cellule défectueuse avec -1
    print(f"Défectueuse cellule placée aux coordonnées: ({row}, {col})") # Afficher les coordonnées de la cellule défectueuse
    return row, col

def tile_board(board, size, top_row, top_col, defect_row, defect_col):# la fonction recursive
    global tile_number
    if size == 2:
        # Cas de base pour un échiquier 2x2
        tile_number += 1  # Incrémenter le numéro de tuile
        for i in range(size):
            for j in range(size):
                # Placer la tuile sur les cellules qui ne sont pas défectueuses
                if not (top_row + i == defect_row and top_col + j == defect_col):
                    board[top_row + i][top_col + j] = tile_number
        return

    # Incrémenter le numéro de tuile pour cette étape de division
    tile_number += 1
    current_tile = tile_number  # Store the current tile number / Stocker le numéro de tuile actuel
    half_size = size // 2  # Calculate half the size of the board / Calculer la moitié de la taille de l'échiquier

    # Déterminer quel sous-échequier contient la cellule défectueuse
    sub_board_with_defect = (
        0 if defect_row < top_row + half_size and defect_col < top_col + half_size else
        1 if defect_row < top_row + half_size else
        2 if defect_col < top_col + half_size else
        3
    )

    # Placer la forme en L au centre pour couvrir les trois autres sous-échéquiers
    central_positions = [
        (top_row + half_size - 1, top_col + half_size - 1),
        (top_row + half_size - 1, top_col + half_size),
        (top_row + half_size, top_col + half_size - 1),
        (top_row + half_size, top_col + half_size)
    ]
    
    # Marquer la forme en L pour les trois sous-échéquiers sans défaut
    for i, (r, c) in enumerate(central_positions):
        if i != sub_board_with_defect:
            board[r][c] = current_tile

    # Appliquer la récursivité pour chaque sous-échequier avec la cellule défectueuse ajustée
    tile_board(board, half_size, top_row, top_col, *(
        (defect_row, defect_col) if sub_board_with_defect == 0 else central_positions[0]))
    tile_board(board, half_size, top_row, top_col + half_size, *(
        (defect_row, defect_col) if sub_board_with_defect == 1 else central_positions[1]))
    tile_board(board, half_size, top_row + half_size, top_col, *(
        (defect_row, defect_col) if sub_board_with_defect == 2 else central_positions[2]))
    tile_board(board, half_size, top_row + half_size, top_col + half_size, *(
        (defect_row, defect_col) if sub_board_with_defect == 3 else central_positions[3]))

def display_board(board):
    size = len(board)  # Obtenir la taille de l'échiquier
    cell_size = 300 // size  # Définir la taille des cellules pour l'affichage
    root = tk.Tk()  #Initialiser la fenêtre principale Tkinter
    root.title(" Problème de carrelage ")
    canvas = tk.Canvas(root, width=size * cell_size, height=size * cell_size)
    canvas.pack()  # Placer le canevas pour l'affichage

    # Définir des couleurs pour les tuiles pour distinguer les L shapes 
    colors = [
    'red', 
    'blue', 
    'green', 
    'yellow', 
    'orange', 
    'purple', 
    'pink', 
    'brown', 
    'cyan', 
    'magenta', 
    'lime'
]
    '''
     #Autre couleurs qui peuvent être plus claire
colors = [
    'lightcoral',       
    'peachpuff',        
    'gold',             
    'palegreen',        
    'mediumseagreen',   
    'skyblue',         
    'lightsteelblue',  
    'mediumpurple',    
    'plum',             
    'lavender',         
    'mistyrose'        
]
'''
    for r in range(size):
        for c in range(size):
            # Déterminer la couleur pour les cellules défectueuses ou normales
            color = 'black' if board[r][c] == -1 else colors[board[r][c] % len(colors)]
            x1, y1 = c * cell_size, r * cell_size  # Coin supérieur gauche de la cellule
            x2, y2 = x1 + cell_size, y1 + cell_size  # Coin inférieur droit de la cellule
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)  # Dessiner la cellule
            if board[r][c] != -1:
                # Afficher le numéro de tuile dans la cellule
                canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text=str(board[r][c]), fill='black')

    root.mainloop()  # Exécuter la boucle principale Tkinter


# Initialiser l'échiquier et placer la cellule défectueuse
n = 8  # Taille de l'échiquier, doit être une puissance de 2
board = create_board(n)
defect_row, defect_col = place_defective_cell(board)  #  Positionner la cellule défectueuse
tile_board(board, n, 0, 0, defect_row, defect_col)  # Commencer le processus de carrelage

# Afficher l'échiquier final après carrelage
display_board(board)