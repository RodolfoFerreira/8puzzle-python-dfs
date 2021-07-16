from random import getrandbits, randint, random, choice
import time

def create_instance():
    return { 
        'experiencia': randint(1,3), 
        'salario': randint(100000, 800000) / 100 
    }
    
def create_list_instances(nmax = 20):
    return [create_instance() for _ in range(nmax)]

def create_individual(nmax):
    return [ randint(0, 1) for x in range(nmax) ]

def create_population(npop, nmax):
    return [ create_individual(nmax) for x in range(npop) ]

def fitness_func(individuo, salario_maximo, desenvolvedores_disponiveis):
    exp_total, salario_total = 0, 0
    for indice, valor in enumerate(individuo):
        exp_total += (individuo[indice] * desenvolvedores_disponiveis[indice]['experiencia'])
        salario_total += (individuo[indice] * desenvolvedores_disponiveis[indice]['salario'])

    if (salario_maximo - salario_total) < 0:
        return -1
        
    return exp_total

def media_fitness_func(populacao, salario_maximo, desenvolvedores_disponiveis):
    summed = sum(fitness_func(x, salario_maximo, desenvolvedores_disponiveis) for x in populacao if fitness_func(x, salario_maximo, desenvolvedores_disponiveis) >= 0)
    return summed / (len(populacao) * 1.0)

def selecao_roleta(parents):
    def sortear(fitness_total, indice_a_ignorar=-1):
        roleta, acumulado, valor_sorteado = [], 0, random()

        if indice_a_ignorar!=-1:
            fitness_total -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar==indice:
                continue
            acumulado += i
            roleta.append(acumulado/fitness_total)
            if roleta[-1] >= valor_sorteado:
                return indice
    
    valores = list(zip(*parents))
    fitness_total = sum(valores[0])

    parent_1_index = sortear(fitness_total) 
    parent_2_index = sortear(fitness_total, parent_1_index)

    parent_1 = valores[1][parent_1_index]
    parent_2 = valores[1][parent_2_index]
    
    return parent_1, parent_2

def reproduce(x, y):
    meio = len(x) // 2
    filho = x[:meio] + y[meio:]
    return filho

def mutation(x):
    idx = randint(0, len(x)-1)
    if x[idx] == 1:
        x[idx] = 0
    else:
        x[idx] = 1
    
    return x

def genetic_algorithm(populacao, salario_maximo, desenvolvedores_disponiveis, npop, mutate_rate=0.05): 
    parents = [ [fitness_func(x, salario_maximo, desenvolvedores_disponiveis), x] for x in populacao if fitness_func(x, salario_maximo, desenvolvedores_disponiveis) >= 0]
    parents.sort(reverse=True)
    
    children = []
    while len(children) < npop:
        parent_1, parent_2 = selecao_roleta(parents)
        children.append(reproduce(parent_1, parent_2))
    
    for individuo in children:
        if random() <= mutate_rate:
            individuo = mutation(individuo)

    return children

niveis = {
    1: 'Júnior',
    2: 'Pleno',
    3: 'Senior'
} 
desenvolvedores_disponiveis = create_list_instances()
salario_maximo = 48900
npop = 50
steps = 100
nmax = len(desenvolvedores_disponiveis)

populacao = create_population(npop, nmax)
historico_de_fitness = [media_fitness_func(populacao, salario_maximo, desenvolvedores_disponiveis)]
for i in range(steps):
    populacao = genetic_algorithm(populacao, salario_maximo, desenvolvedores_disponiveis, npop)
    historico_de_fitness.append(media_fitness_func(populacao, salario_maximo, desenvolvedores_disponiveis))

for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de experiencia da equipe: ", dados)

print("Salário máximo: R$ ",salario_maximo,"\n\nDesenvolvedores disponíveis:")
for indice,i in enumerate(desenvolvedores_disponiveis):
    print("Item ",indice+1,": Nível: ",niveis[i['experiencia']]," | Salário Total: R$ ",i['salario'])
    
print("\nPossíveis equipes: ")
for i in range(5):
    print("Equipe: ", i + 1, "\n")
    [print("Nível: ", niveis[desenvolvedores_disponiveis[idx]['experiencia']], " | Salário: R$ ", desenvolvedores_disponiveis[idx]['salario']) for idx, item in enumerate(populacao[i]) if item != 0]
    print("\n")