# slot Machine Simulation with Paylines and RTP Calculation
## Project Overview
This project is a simulation of a 3x3 slot machine with a middle payline, built using Flask for the web interface and basic logic for simulating spins. It allows users to specify the number of spins, simulates the results, and calculates the Return to Player (RTP) as well as the total winnings and jackpot occurrences.

## Features
### Slot Machine Mechanics:

A 3x3 grid with 3 spinning reels.
Symbols include A, B, C, and a special Jackpot symbol.
Only the middle row is considered for winning.
Each symbol has a frequency and a payout value:
A: Appears 40% of the time, 5 units payout.
B: Appears 30% of the time, 10 units payout.
C: Appears 20% of the time, 15 units payout.
Jackpot: Appears 10% of the time, 100 units payout.
Winning Conditions:

A win occurs when all 3 symbols in the middle row are the same.
Three Jackpot symbols in the middle row result in a jackpot win.
Simulation & Output:

Users can simulate n spins at a time.
For each spin, the symbols are displayed, the winnings are calculated, and RTP is computed.
A simple ML prediction model estimates the probability of winning on the next spin (using random probability simulation for now).
Results Display:

Total number of jackpot wins.
Total winnings across all spins.
Return to Player (RTP) percentage after all spins.
Predicted probability of a win in the next spin.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Script

```bash
python app.py
```

## File Structure

```bash
slot-machine-simulation/
│
├── static/
│   ├── images/
│   │   └── jackpot-image.png   
│   ├── styles.css             
│   └── script.js               
│
├── templates/
│   └── index.html             
│
├── app.py              
├── requirements.txt    
└── README.md           
```
