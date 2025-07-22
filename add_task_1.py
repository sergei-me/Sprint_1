types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def del_dubl(dict):
    uniq_tickets = {}
    uniq_list = []
    for k, v in tickets.items():
        new_v = []
        for i in v:
            if i in uniq_list:
                pass
            else:
                new_v.append(i)
                uniq_list.append(i)
        uniq_tickets[k] = new_v
    return uniq_tickets

def new_dict(dict1, dict2):
    tickets_by_type = { v: del_dubl(tickets)[k] for k, v in types.items() }
    return tickets_by_type

print(new_dict(types, tickets))