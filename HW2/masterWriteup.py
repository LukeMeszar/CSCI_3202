def guess_code(response,prev_guess,codes_list):
    if response == 0: #first guess
        return [["Red", "Blue", "Blue"],codes_list] #make random first guess
    new_codes_list = remove_codes(response,prev_guess,codes_list)
    return [new_codes_list[0],new_codes_list]

def calculate_response(guess,code):
    correct_col_and_pos = 0
    correct_col = 0
    colors_seen_correct = []
    for i in range(len(guess)):
        if guess[i] == code[i]:
            correct_col_and_pos += 1
            colors_seen_correct.append(guess[i])#allows black peg to take
            #precedence
    for i in range(len(guess)):
        if guess[i] in code and guess[i] not in colors_seen_correct:
                correct_col += 1
                code.remove(guess[i])
    return [correct_col_and_pos, correct_col]

def remove_codes(response, prev_guess, codes_list):
    print("prev_guess",prev_guess)
    new_codes_list = codes_list[:]
    for code in codes_list:
        list_code = list(code)
        if response != calculate_response(prev_guess,list_code):
            new_codes_list.remove(code)
    return new_codes_list

def game_loop(users_code,codes_list):
    won = False
    moves_remaining = 5
    code_to_guess, new_codes_list = guess_code(0,-1,codes_list)
    response = submit_code(code_to_guess, users_code)
    if response == [3,0]:
        print("Game won")
        won = True
    new_codes_list = codes_list[:]
    while not won and moves_remaining != 0:
        code_to_guess,new_codes_list = guess_code(response,code_to_guess,new_codes_list)

        response = submit_code(code_to_guess,users_code)
        if response == [3,0]:
            print("Game won by computer")
            won = True

        moves_remaining -= 1
