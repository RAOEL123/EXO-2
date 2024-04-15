def get_minimized_form():
    variables = input("Entrez les variables de la fonction (ex: A,B,C): ").split(',')
    num_variables = len(variables)
    
    truth_table = {}
    print("Entrez les valeurs de la table de vérité pour la fonction en utilisant 0 pour False et 1 pour True:")
    while True:
        row = input("Entrez une ligne de la table de vérité (ex: 101 pour A=True, B=False, C=True) ou q pour terminer: ")
        if row.lower() == 'q':
            break
        truth_values = [int(val) for val in row]
        input_values = tuple(truth_values[:-1])
        output_value = truth_values[-1]
        truth_table[input_values] = output_value
        
    groups = {}
    print("Entrez les groupes de 1 dans le tableau de Karnaugh en utilisant les indices (ex: 00, 01, 11, 10) ou q pour terminer:")
    while True:
        group = input("Entrez un groupe de 1 ou q pour terminer: ")
        if group.lower() == 'q':
            break
        group_values = [int(val) for val in group]
        groups[tuple(group_values)] = True
        
    minimized_terms = []
    for group in groups.keys():
        term = ''
        for i in range(num_variables):
            if group[i] == 0:
                term += variables[i] + "'"
            elif group[i] == 1:
                term += variables[i]
        minimized_terms.append(term)
    
    minimized_form = ' + '.join(minimized_terms)
    print("La forme minimale de la fonction logique est: {}".format(minimized_form))

# Appel de la fonction pour obtenir la forme minimale
get_minimized_form()