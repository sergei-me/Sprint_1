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
uniq_tickets = {}
uniq_list = []

def del_dubl(dict):
    for k, v in tickets.items():
        new_v = []
        for i in v:
            if i in uniq_list:
                pass
            else:
                new_v.append(i)
                uniq_list.append(i)
        uniq_tickets[k] = new_v

del_dubl(tickets)

print(uniq_tickets)