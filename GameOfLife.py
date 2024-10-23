import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensiones
N = 50

# Inicialización
def random_grid(N):
    return np.random.choice([0, 1], N * N, p=[0.8, 0.2]).reshape(N, N)

# Vecinos vivos
def count_neighbors(grid, i, j):
    # posiciones de los vecinos
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), 
                 (i, j-1),           (i, j+1), 
                 (i+1, j-1), (i+1, j), (i+1, j+1)]
    
    # Contar vecinos
    count = 0
    for x, y in neighbors:
        if 0 <= x < N and 0 <= y < N:
            count += grid[x, y]
    return count

# Reglas
def update(grid):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            neighbors_alive = count_neighbors(grid, i, j)
            
            # Si la célula está viva
            if grid[i, j] == 1:
                if neighbors_alive < 2 or neighbors_alive > 3:
                    new_grid[i, j] = 0
            # Si la célula está muerta
            else:
                if neighbors_alive == 3:
                    new_grid[i, j] = 1
    return new_grid

# animación
def animate(frame, img, grid):
    new_grid = update(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Inicializar el tablero
grid = random_grid(N)

# Crearanimación
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')

# Crear la animación
ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=10, interval=200)

plt.show()
