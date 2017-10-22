import itertools

def generate_codes():
    colors = ["Red", "Blue", "Orange", "White"]
    states = list(itertools.product(colors,colors,colors))
    print(states[0])
    return states

def get_users_code():
    code = input('Enter your code in form "Color1,Color2,Color3": ')
    #going to assume user inputs code correctly
    code = code.split(",")
    return(code)

def guess_code(response,prev_guess,codes_list):
    if response == 0: #first guess
        return ["Red", "Blue", "Blue"]
    new_codes_list = remove_codes(response,prev_guess,codes_list)

def remove_codes(response, prev_guess, codes_list):
    pass

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
    code_to_guess = guess_code(0,codes_list)
    response = submit_code(code_to_guess, users_code)
    if response == [3,0]:
        print("Game won")
        won = True
    while not won and moves_remaining != 0:
        code_to_guess = guess_code(response,code_to_guess,codes_list)
        response = submit_code(code_to_guess,users_code)
        if response == [3,0]:
            print("Game won")
            won = True
        moves_remaining -= 1


if __name__ == "__main__":
    #game_loop(get_users_code(),generate_codes())
    remove_codes([0,0],["Blue", "Blue", "Orange"],generate_codes())
