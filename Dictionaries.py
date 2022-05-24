colors = {}
colors["Blue"] = "Azul"
colors["Red"] = "Vermelho"
colors["Black"] = "Preto"
colors["Purple"] = "Roxo"
colors["Grey"] = "Cinza"
colors["Yellow"] = "Amarelo"
colors["Green"] = "Verde"
colors["Pink"] = "Cor de rosa"
e_list = []
count = 1
for key in colors:
    print(str(count) + " " + key + " = " + colors[key])
    count += 1
if " e " in key:
    e_list.append(key)


print(e_list)

## x = {}
##for c in txt:
####if c not in x:
######x[c] = 0
####x[c] = x[c] + 1