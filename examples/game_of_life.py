# AUTOGENERATED! DO NOT EDIT! File to edit: game_of_life.ipynb.

# %% auto 0
__all__ = ['css', 'gridlink', 'app', 'rt', 'grid', 'running', 'update_grid', 'Grid', 'Home', 'get', 'post']

# %% game_of_life.ipynb 2
from fasthtml import *

css = Style(
    '#grid { display: grid; grid-template-columns: repeat(20, 20px); grid-template-rows: repeat(20, 20px);gap: 1px; }',
    '.cell { width: 20px; height: 20px; border: 1px solid black; }',
    '.alive { background-color: green; }',
    '.dead { background-color: white; }'
)

# Flexbox CSS (http://flexboxgrid.com/)
gridlink = Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css", type="text/css")

app = FastHTML(hdrs=(picolink, gridlink, css))
rt = app.route

# %% game_of_life.ipynb 3
grid = [[0 for _ in range(20)] for _ in range(20)]

def update_grid(grid: List[List[int]]) -> List[List[int]]:
    new_grid = [[0 for _ in range(20)] for _ in range(20)]

    def count_neighbors(x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                count += grid[nx][ny]
        return count

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

# %% game_of_life.ipynb 4
def Grid():
    cells = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            cell_class = 'alive' if cell else 'dead'
            cell = Div(cls=f'cell {cell_class}', hx_post='/update', hx_vals={'x': x, 'y': y}, hx_swap='innerHTML', hx_target='#gol', hx_trigger='click')
            cells.append(cell)
    
    return Div(*cells, id='grid')

# %% game_of_life.ipynb 5
def Home():
    # grid = Grid()
    gol = Div(id='gol', hx_trigger="load, every 1s", hx_get="/poll", hx_swap="innerHTML", cls='row center-xs', hx_target='#gol')
    run_btn = Button('Run', id='run', cls='col-xs-2', hx_post='/run', hx_target='#gol', hx_swap='innerHTML')
    pause_btn = Button('Pause', id='pause', cls='col-xs-2', hx_post='/pause', hx_target='#gol', hx_swap='innerHTML')
    reset_btn = Button('Reset', id='reset', cls='col-xs-2', hx_post='/reset', hx_target='#gol', hx_swap='innerHTML')

    return (
        Title('Game of Life'), Main(
            gol, Div(
                run_btn, pause_btn, reset_btn, cls='row center-xs'
            ),
        )
    )

# %% game_of_life.ipynb 7
@rt('/')
def get():
    return Home()

# %% game_of_life.ipynb 8
@rt('/poll')
def get():
    global running, grid
    if running:
        grid = update_grid(grid)
    return Grid()

# %% game_of_life.ipynb 9
@rt('/update')
async def post(x: int, y: int):
    global grid
    grid[y][x] = 1 if grid[y][x] == 0 else 0
    return Grid()

# %% game_of_life.ipynb 10
running = False
@rt('/run')
async def post():
    global running
    running = True
    return Grid()

# %% game_of_life.ipynb 11
@rt("/reset")
async def post():
    global grid, running
    grid = [[0 for _ in range(20)] for _ in range(20)]
    running = False
    return Grid()

# %% game_of_life.ipynb 12
@rt('/pause')
async def post():
    global running
    running = False
    return Grid()