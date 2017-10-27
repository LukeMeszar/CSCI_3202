import itertools

def generate_codes():
    colors = ["Red", "Blue", "Orange", "White"]
    states = list(itertools.product(colors,colors,colors))
    return states

def get_users_code():
    code = input('Enter your code in form "Color1,Color2,Color3": ')
    #going to assume user inputs code correctly
    code = code.split(",")
    return(code)

def guess_code(response,prev_guess,codes_list):
#    print("response,prev_guess,codes_list",response,prev_guess,codes_list)
    if response == 0: #first guess
        return [["Red", "Blue", "Blue"],codes_list]
    new_codes_list = remove_codes(response,prev_guess,codes_list)
    print(len(new_codes_list))
    #return (minimax(new_codes_list),new_codes_list)
    return [new_codes_list[0],new_codes_list]

def minimax(codes_list):
    best_move_list = [] #{H(g)}
    for guess in codes_list:
        responses_for_guess = [] #Z(g)
        for possible_code in codes_list:
            if guess != possible_code:
                responses_for_guess.append(calculate_response\
                (guess,list(possible_code))) #R(g,s)
        goodness_array = [] #G(g,z)
        for z in responses_for_guess:
            temp_array = []
            for secret in codes_list:
                if calculate_response(guess,list(secret)) != z:
                    temp_array.append(secret)
            goodness_array.append(len(temp_array))
        #print(goodness_array)
        score = min(goodness_array)
        print(score)
        best_move_list.append((score,guess))
    print(best_move_list)
    print(max(best_move_list))
    return max(best_move_list)[1]


def calculate_response(guess,code):
    correct_col_and_pos = 0
    correct_col = 0
    colors_seen_correct = []
#    print("guess,code",guess,code)
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



def submit_code(guessed_code,users_code):
    print("Your secret code: ", users_code, "\n") #so player doesn't forget
    print("Computer's guess", guessed_code, "\n")
    response = input('Enter your response in the form #1,#1 \n where #1 is \
     number of correct  color and correct position \n and #2 is number of \
     correct colors in incorrect positions\n') #again, no input sanitation
    response_array = response.split(",")
    response_array = [int(x) for x in response_array]
    return response_array

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
            print("Game won")
            won = True

        moves_remaining -= 1


if __name__ == "__main__":
    game_loop(get_users_code(),generate_codes())
    #guess_code([1,0],["Red", "Blue", "Blue"],generate_codes())
