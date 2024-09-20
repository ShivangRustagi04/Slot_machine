from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Symbols and their respective frequencies and payouts
symbols = ['A', 'B', 'C', 'Jackpot']
payouts = {'A': 5, 'B': 10, 'C': 15, 'Jackpot': 100}
frequencies = {'A': 0.4, 'B': 0.3, 'C': 0.2, 'Jackpot': 0.1}

# Simulate a slot machine spin
def spin_reel():
    reel = random.choices(symbols, [frequencies[s] for s in symbols], k=3)
    return reel

def calculate_winnings(middle_row):
    if len(set(middle_row)) == 1:  # all symbols are the same
        symbol = middle_row[0]
        return payouts[symbol]
    return 0

@app.route('/')
def index():
    return render_template('index.html')


# Main simulation route
@app.route('/spin')
def spin():
    num_spins = int(request.args.get('num_spins', 1))
    
    total_winnings = 0
    jackpot_wins = 0
    spins_data = []
    
    for spin_num in range(num_spins):
        grid = [spin_reel(), spin_reel(), spin_reel()]
        middle_row = [grid[0][1], grid[1][1], grid[2][1]]  # Middle row is index 1 of each reel
        winnings = calculate_winnings(middle_row)
        
        if middle_row == ['Jackpot', 'Jackpot', 'Jackpot']:
            jackpot_wins += 1
        
        total_winnings += winnings
        
        spins_data.append({
            'grid': grid,
            'middle_row': middle_row,
            'winnings': winnings
        })
    
    rtp = (total_winnings / (num_spins * 1)) * 100  # assuming 1 unit bet per spin
    
    # Simulate a basic ML prediction (using a placeholder value here)
    predicted_win_probability = round(random.uniform(0.1, 0.5), 2)
    
    return jsonify({
        'spins': spins_data,
        'total_winnings': total_winnings,
        'total_jackpot_wins': jackpot_wins,
        'rtp': round(rtp, 2),
        'predicted_win_probability': predicted_win_probability
    })

if __name__ == '__main__':
    app.run(debug=True)
