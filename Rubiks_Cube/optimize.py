from Rubiks_Cube import cube

X_ROT_CW = {
    'U': 'F',
    'B': 'U',
    'D': 'B',
    'F': 'D',
    'E': 'Si',
    'S': 'E',
    'Y': 'Z',
    'Z': 'Yi',
}
Y_ROT_CW = {
    'B': 'L',
    'R': 'B',
    'F': 'R',
    'L': 'F',
    'S': 'Mi',
    'M': 'S',
    'Z': 'X',
    'X': 'Zi'
}
Z_ROT_CW = {
    'U': 'L',
    'R': 'U',
    'D': 'R',
    'L': 'D',
    'E': 'Mi',
    'M': 'E',
    'Y': 'Xi',
    'X': 'Y',
}
X_ROT_CC = {v: k for k, v in X_ROT_CW.items()}
Y_ROT_CC = {v: k for k, v in Y_ROT_CW.items()}
Z_ROT_CC = {v: k for k, v in Z_ROT_CW.items()}


def get_rot_table(rot):
    if rot   == 'X':  return X_ROT_CW
    elif rot == 'Xi': return X_ROT_CC
    elif rot == 'Y':  return Y_ROT_CW
    elif rot == 'Yi': return Y_ROT_CC
    elif rot == 'Z':  return Z_ROT_CW
    elif rot == 'Zi': return Z_ROT_CC


def _invert(move):
    if move.endswith('i'):
        return move[:1]
    return move + 'i'


def apply_repeat_three_optimization(moves):
    """ R, R, R --> Ri """
    changed = False
    i = 0
    while i < len(moves) - 2:
        if moves[i] == moves[i+1] == moves[i+2]:
            moves[i:i+3] = [_invert(moves[i])]
            changed = True
        else:
            i += 1
    if changed:
        apply_repeat_three_optimization(moves)


def apply_do_undo_optimization(moves):
    """ R Ri --> <nothing>, R R Ri Ri --> <nothing> """
    changed = False
    i = 0
    while i < len(moves) - 1:
        if _invert(moves[i]) == moves[i+1]:
            moves[i:i+2] = []
            changed = True
        else:
            i += 1
    if changed:
        apply_do_undo_optimization(moves)


def _unrotate(rot, moves):
    rot_table = get_rot_table(rot)
    result = []
    for move in moves:
        if move in rot_table:
            result.append(rot_table[move])
        elif _invert(move) in rot_table:
            result.append(_invert(rot_table[_invert(move)]))
        else:
            result.append(move)
    return result


def apply_no_full_cube_rotation_optimization(moves):
    rots = {'X', 'Y', 'Z', 'Xi', 'Yi', 'Zi'}
    changed = False
    i = 0
    while i < len(moves):
        if moves[i] not in rots:
            i += 1
            continue

        for j in reversed(range(i + 1, len(moves))):
            if moves[j] == _invert(moves[i]):
                moves[i:j+1] = _unrotate(moves[i], moves[i+1:j])
                changed = True
                break
        i += 1
    if changed:
        apply_no_full_cube_rotation_optimization(moves)


def optimize_moves(moves):
    result = list(moves)
    apply_no_full_cube_rotation_optimization(result)
    apply_repeat_three_optimization(result)
    apply_do_undo_optimization(result)
    return result
