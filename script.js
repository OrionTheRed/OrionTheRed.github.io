document.addEventListener("DOMContentLoaded", function() {
    const moves = ["rock", "paper", "scissors"];

    function computerMove() {
        return moves[Math.floor(Math.random() * moves.length)];
    }

    function determineWinner(playerMove, computerMove) {
        if (playerMove === computerMove) {
            return "It's a tie!";
        } else if (
            (playerMove === "rock" && computerMove === "scissors") ||
            (playerMove === "paper" && computerMove === "rock") ||
            (playerMove === "scissors" && computerMove === "paper")
        ) {
            return "You win!";
        } else {
            return "You lose!";
        }
    }

    document.querySelectorAll("button").forEach(function(button) {
        button.addEventListener("click", function() {
            const playerMove = this.id;
            const compMove = computerMove();
            const result = determineWinner(playerMove, compMove);
            document.getElementById("result").textContent = result;
        });
    });

    document.getElementById("play-again").addEventListener("click", function() {
        document.getElementById("result").textContent = "";
    });
});
