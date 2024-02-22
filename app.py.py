from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_game', methods=['POST'])
def play_game():
    moves = {'T': 'Tiger Claw', 'M': 'Monkey Grip', 'C': 'Crane Kick'}

    user_move = request.form['move']
    comp_move = random.choice(list(moves.values()))

    result = determine_winner(user_move, comp_move)

    return render_template('result.html', user_move=user_move, comp_move=comp_move, result=result)

def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    elif (user_move == 'Tiger Claw' and computer_move == 'Monkey Grip') or \
         (user_move == 'Monkey Grip' and computer_move == 'Crane Kick') or \
         (user_move == 'Crane Kick' and computer_move == 'Tiger Claw'):
        return "You win!"
    else:
        return "You lose!"

if __name__ == '__main__':
    app.run(debug=True)
