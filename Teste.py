import tkinter as tk



class Env:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for i in range(self.width)] for i in range(height)]
        self.start_position = list()
        self.goal_position = list()

    def Obstacle(self, obstaclesList):
        for i in obstaclesList:
            if 0 <= i[0] < self.width and 0 <= i[1] < self.height:
                self.grid[i[0]][i[1]] = 'X'

    def setGoal(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y] = 'G'
            self.goal_position = [x, y]

    def setStart(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y] = 'S'
            self.start_position = [x, y]

    def showGrid(self):
        for i in self.grid:
            print(i)

    def getGrid(self):
        return self.grid

    def setGridCost(self, obj):
        gridCost = self.getGrid()
        for i in obj:
            gridCost[obj[i][0]][obj[i][1]] = i

        return gridCost



    def getStart(self):
        return self.start_position

    def getGoal(self):
        return self.goal_position


class Search:
    def __init__(self, w, h, start_x, start_y, goal_x, goal_y, obs):
        '''listObstacles = [
                         [0,5],[1,5],[2,5],[2,4],
                         [2,3],[2,2],[3,2],[4,2],
                         [5,2],[4,4],[5,4],[6,4],
                         [7,4],[7,3],[8,3],[9,3]
                         ]'''
        self.env = Env(w,h)
        self.env.Obstacle(obs)
        self.env.setGoal(goal_x,goal_y)
        self.env.setStart(start_x,start_y)
        self.traveledList = list()
        self.position = self.env.getStart()
        #self.env.showGrid()
        #self.traveledList.append([9,5])

    def Manhattan(self, S_position, G_position):
        return abs(S_position[0] - G_position[0]) + abs(S_position[1] - G_position[1])

    def getNeighbors(self, S_position):
        grid = self.env.getGrid()
        neighbors = []
        if 0 <= S_position[0] + 1 < 10:
            if grid[S_position[0] + 1][S_position[1]] == ' ' or grid[S_position[0] + 1][S_position[1]] == 'G':
                #S_position_new = [S_position[0] + 1, S_position[1]]
                if [S_position[0] + 1, S_position[1]] not in self.traveledList:
                    neighbors.append([S_position[0] + 1, S_position[1]])
                    self.traveledList.append([S_position[0] + 1, S_position[1]])

        if 0 <= S_position[1] + 1 < 10:
            if grid[S_position[0]][S_position[1] + 1] == ' ' or grid[S_position[0]][S_position[1] + 1] == 'G':
                #S_position_new = [S_position[0], S_position[1] + 1]
                if [S_position[0], S_position[1] + 1] not in self.traveledList:
                    neighbors.append([S_position[0], S_position[1] + 1])
                    self.traveledList.append([S_position[0], S_position[1] + 1])

        if 0 <= S_position[0] - 1 < 10:
            if grid[S_position[0] - 1][S_position[1]] == ' ' or grid[S_position[0] - 1][S_position[1]] == 'G':
                #S_position_new = [S_position[0] - 1, S_position[1]]
                if [S_position[0] - 1, S_position[1]] not in self.traveledList:
                    neighbors.append([S_position[0] - 1, S_position[1]])
                    self.traveledList.append([S_position[0] - 1, S_position[1]])

        if 0 <= S_position[1] - 1 < 10:
            if grid[S_position[0]][S_position[1] - 1] == ' ' or grid[S_position[0]][S_position[1] - 1] == 'G':
                #S_position_new = [S_position[0], S_position[1] - 1]
                if [S_position[0], S_position[1] - 1] not in self.traveledList:
                    neighbors.append([S_position[0], S_position[1] - 1])
                    self.traveledList.append([S_position[0], S_position[1] - 1])

        return neighbors

    def traveledPositions(self, traveledBlock):
        if self.env.grid[traveledBlock[0]][traveledBlock[1]] != 'S' and self.env.grid[traveledBlock[0]][traveledBlock[1]] != 'G':
            self.env.grid[traveledBlock[0]][traveledBlock[1]] = 'O'
        #return self.env.getGrid()

    def nextStep(self, position):
        neighbors = self.getNeighbors(position)
        dict_neighbors = dict()
        neighbors_list = list()
        for i in neighbors:
            dict_neighbors[self.Manhattan(i, self.env.getGoal())] = i
            neighbors_list.append(self.Manhattan(i, self.env.getGoal()))
        minor_value = self.minorValue(neighbors_list)
        return dict_neighbors[minor_value], dict_neighbors

    def minorValue(self, list_values):
        i = float("inf")
        for nr in list_values:
            if nr < i:
                i = nr
        return i

    def main(self):
        #while(self.position != self.env.getGoal()):
            #self.traveledPositions(self.position)
            #self.position = self.nextStep(self.position)
            #print("Posição atual: ", self.position)
            #self.env.showGrid()
        if (self.env.getGoal() != self.position):
            self.traveledPositions(self.position)
            obj_positions = self.nextStep(self.position)
            self.position = obj_positions[0]
            self.env.setGridCost(obj_positions[1])
            return self.env.getGrid()
        return self.env.getGrid()


def fechar_janela():
    janela_entrada_dados.quit()
    janela_entrada_dados.destroy()

lista_dados = list()
def processar_e_avancar():

    width = entrada_width.get()
    height = entrada_height.get()
    start_x = entrada_start_x.get()
    start_y = entrada_start_y.get()
    goal_x = entrada_goal_x.get()
    goal_y = entrada_goal_y.get()

    #janela_entrada_dados.withdraw()

    #janela_obstacles_coleta.decoinfy()
    lista_dados.append(width)
    lista_dados.append(height)
    lista_dados.append(start_y)
    lista_dados.append(start_y)
    lista_dados.append(goal_x)
    lista_dados.append(goal_y)

    fechar_janela()


janela_entrada_dados = tk.Tk()
janela_entrada_dados.title("Informações da Matriz")

rotulo_width = tk.Label(janela_entrada_dados, text="Largura: ")
rotulo_width.pack()
entrada_width = tk.Entry(janela_entrada_dados)
entrada_width.pack()

rotulo_height = tk.Label(janela_entrada_dados, text="Altura: ")
rotulo_height.pack()
entrada_height = tk.Entry(janela_entrada_dados)
entrada_height.pack()

rotulo_start_x = tk.Label(janela_entrada_dados, text="Inicio (x): ")
rotulo_start_x.pack()
entrada_start_x = tk.Entry(janela_entrada_dados)
entrada_start_x.pack()

rotulo_start_y = tk.Label(janela_entrada_dados, text="Inicio (y): ")
rotulo_start_y.pack()
entrada_start_y = tk.Entry(janela_entrada_dados)
entrada_start_y.pack()

rotulo_goal_x = tk.Label(janela_entrada_dados, text="Objetivo (x): ")
rotulo_goal_x.pack()
entrada_goal_x = tk.Entry(janela_entrada_dados)
entrada_goal_x.pack()

rotulo_goal_y = tk.Label(janela_entrada_dados, text="Objetivo (y): ")
rotulo_goal_y.pack()
entrada_goal_y = tk.Entry(janela_entrada_dados)
entrada_goal_y.pack()

# Botão para processar os dados e avançar para a próxima página
botao_processar = tk.Button(janela_entrada_dados, text="Processar Dados e Avançar", command=processar_e_avancar)
botao_processar.pack()

janela_entrada_dados.mainloop()

# Função para adicionar um item à lista
def adicionar_item():
    item = entrada_item.get()
    if item:
        minha_lista.append(item)
        atualizar_lista_obs()

# Função para atualizar a lista na interface
def atualizar_lista_obs():
    lista_text.delete(1.0, tk.END)  # Limpa o conteúdo atual
    lista_text.insert(tk.END, "\n".join(minha_lista))  # Insere a lista atualizada

def fechar_janela_2():
    janela_entrada_obs.quit()
    janela_entrada_obs.destroy()

# Configuração da janela
janela_entrada_obs = tk.Tk()
janela_entrada_obs.title("Adicionar Itens à Lista")

# Campo de entrada para o item
rotulo_item = tk.Label(janela_entrada_obs, text="Digite um item:")
rotulo_item.pack()
entrada_item = tk.Entry(janela_entrada_obs)
entrada_item.pack()

# Botão para adicionar o item à lista
botao_adicionar = tk.Button(janela_entrada_obs, text="Adicionar à Lista", command=adicionar_item)
botao_adicionar.pack()

# Texto para exibir a lista
lista_text = tk.Text(janela_entrada_obs, height=10, width=30)
lista_text.pack()

# Botão para adicionar o item à lista
botao_fechar = tk.Button(janela_entrada_obs, text="Próxima Página", command=fechar_janela_2)
botao_fechar.pack()

# Lista inicial vazia
minha_lista = []

# Executar a interface
janela_entrada_obs.mainloop()


def minha_lista_conversor():
    lista = list()
    lista_holder = list()
    if len(minha_lista)%2 == 1:
        minha_lista.append(0)

    for i in range(0,len(minha_lista), 2):
        lista_holder = []
        lista_holder.append(int(minha_lista[i]))
        lista_holder.append(int(minha_lista[i+1]))
        lista.append(lista_holder)
    return lista
    

#print(minha_lista)


search = Search(int(lista_dados[0]), int(lista_dados[1]), int(lista_dados[2]), int(lista_dados[3]), int(lista_dados[4]), int(lista_dados[5]), minha_lista_conversor())

# Lista predefinida com números inteiros de 1 a 3
minha_lista = search.env.getGrid()

# Função para atualizar a lista na interface e adicionar um novo número
def atualizar_lista():
    #maior_valor = max(minha_lista) if minha_lista else 0  # Encontra o maior valor na lista
    #novo_numero = maior_valor + 1
    #minha_lista.append(novo_numero)  # Adiciona o novo número à lista
    minha_lista = search.main()
    lista_text.delete(1.0, tk.END)  # Limpa o conteúdo atual
    lista_text.insert(tk.END, "\n".join(map(str, minha_lista)))  # Insere a lista atualizada
    #minha_lista = search.main()

# Configuração da janela
janela = tk.Tk()
janela.title("Exemplo de Interface")

# Texto para exibir a lista
lista_text = tk.Text(janela, height=10, width=50)
lista_text.pack()

# Botão para atualizar a lista e adicionar um novo número
botao_atualizar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista)
botao_atualizar.pack()

# Exibe a lista inicial
atualizar_lista()

# Executa a interface
janela.mainloop()