
def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    valor = 0
    # permanencia_horario = []
    # print("target: ", target_time)
    for periodo in permanence_period:
        # print('here ~~~>', periodo[0], periodo[1])
        if (periodo[0] is None or periodo[1] is None or target_time is None):
            return None
        if (not isinstance(periodo[0], int) or
                not isinstance(periodo[1], int)):
            return None
        if ((periodo[0]) <= (target_time) <= (periodo[1])):
            # print("aqui ------>", periodo[0], target_time, periodo[1])
            # print(int(periodo[0]) >= int(target_time) <= int(periodo[1]))
            valor += 1

    return valor
    raise NotImplementedError


if __name__ == "__main__":
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    x = study_schedule(permanence_period, 2)
    print(x)
