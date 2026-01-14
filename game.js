(function initTicTacToe() {

    console.log("TicTacToe starting...");

    const boardEl   = document.getElementById("ttt-board");
    const statusEl  = document.getElementById("ttt-status");
    const resetBtn  = document.getElementById("ttt-reset");
    const modeRadios = document.querySelectorAll('input[name="mode"]');

    if (!boardEl) {
        console.error("ERROR: #ttt-board not found");
        return;
    }

    let board = Array(9).fill("");
    let currentPlayer = "X";
    let gameActive = true;
    let mode = "human";

    const winPatterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];

    function buildBoard() {
        boardEl.innerHTML = "";
        board = Array(9).fill("");
        currentPlayer = "X";
        gameActive = true;
        statusEl.textContent = "Player X's turn";

        for (let i = 0; i < 9; i++) {
            const cell = document.createElement("div");
            cell.className = "ttt-cell";
            cell.dataset.index = i;
            cell.addEventListener("click", onCellClick);
            boardEl.appendChild(cell);
        }
    }

    function onCellClick(e) {
        const index = e.target.dataset.index;
        if (!gameActive || board[index] !== "") return;

        makeMove(index, currentPlayer);

        if (gameActive && mode === "computer" && currentPlayer === "O") {
            setTimeout(computerMove, 300);
        }
    }

    function makeMove(index, player) {
        board[index] = player;
        boardEl.children[index].textContent = player;

        if (checkWin(player)) {
            statusEl.textContent = `Player ${player} wins!`;
            gameActive = false;
            return;
        }

        if (!board.includes("")) {
            statusEl.textContent = "Draw!";
            gameActive = false;
            return;
        }

        currentPlayer = player === "X" ? "O" : "X";
        statusEl.textContent = `Player ${currentPlayer}'s turn`;
    }

    function checkWin(player) {
        return winPatterns.some(p => p.every(i => board[i] === player));
    }

    function computerMove() {
        const empty = board
            .map((v,i) => v === "" ? i : null)
            .filter(v => v !== null);

        const move = empty[Math.floor(Math.random() * empty.length)];
        makeMove(move, "O");
    }

    resetBtn.addEventListener("click", buildBoard);

    modeRadios.forEach(radio => {
        radio.addEventListener("change", e => {
            mode = e.target.value;
            buildBoard();
        });
    });

    buildBoard();

})();
