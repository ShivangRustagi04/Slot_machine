function startSpins() {
    const numSpins = document.getElementById('num-spins').value;
    
    fetch(`/spin?num_spins=${numSpins}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        let results = '';
        
        data.spins.forEach((spin, index) => {
            results += `Spin ${index + 1}:<br>`;
            results += `[${spin.grid[0]}]<br>`;
            results += `[${spin.grid[1]}]<br>`;
            results += `[${spin.grid[2]}]<br>`;
            results += `Middle row: ${spin.middle_row.join(', ')}<br>`;
            results += `Winnings: ${spin.winnings}<br><br>`;
        });
        
        results += `--- Simulation Results ---<br>`;
        results += `Total Jackpot Wins: ${data.total_jackpot_wins}<br>`;
        results += `Total Winnings: ${data.total_winnings}<br>`;
        results += `Return to Player (RTP): ${data.rtp}%<br>`;
        results += `Predicted probability of a win in the next spin: ${data.predicted_win_probability}<br>`;

        document.querySelector('.result-display').innerHTML = results;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
