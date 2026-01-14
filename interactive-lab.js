/* ============================
   Tic Tac Toe With AI (Fixed)
============================ */

let tttBoard = Array(9).fill("");
let tttCurrentPlayer = "X";
let tttGameActive = true;
let tttMode = "human";

let boardEl, statusEl, resetBtn, modeRadios;

const winPatterns = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];

/* ---------- Initialize ---------- */
document.addEventListener("DOMContentLoaded", () => {

    boardEl = document.getElementById("ttt-board");
    statusEl = document.getElementById("ttt-status");
    resetBtn = document.getElementById("ttt-reset");
    modeRadios = document.querySelectorAll('input[name="mode"]');

    resetBtn.addEventListener("click", initBoard);

    modeRadios.forEach(radio => {
        radio.addEventListener("change", e => {
            tttMode = e.target.value;
            initBoard();
        });
    });

    initBoard();
});

/* ---------- Build Board ---------- */

function initBoard() {
    boardEl.innerHTML = "";
    tttBoard = Array(9).fill("");
    tttCurrentPlayer = "X";
    tttGameActive = true;
    statusEl.textContent = "Player X's turn";

    for (let i = 0; i < 9; i++) {
        const cell = document.createElement("div");
        cell.className = "ttt-cell";
        cell.dataset.index = i;
        cell.addEventListener("click", onCellClick);
        boardEl.appendChild(cell);
    }
}

/* ---------- Gameplay ---------- */

function onCellClick(e) {
    const index = e.target.dataset.index;

    if (!tttGameActive || tttBoard[index] !== "") return;

    makeMove(index, tttCurrentPlayer);

    if (!tttGameActive) return;

    if (tttMode === "computer" && tttCurrentPlayer === "O") {
        setTimeout(computerMove, 350);
    }
}

function makeMove(index, player) {
    tttBoard[index] = player;
    boardEl.children[index].textContent = player;

    if (checkWin(player)) {
        statusEl.textContent = `Player ${player} wins!`;
        tttGameActive = false;
        return;
    }

    if (!tttBoard.includes("")) {
        statusEl.textContent = "Draw!";
        tttGameActive = false;
        return;
    }

    tttCurrentPlayer = player === "X" ? "O" : "X";
    statusEl.textContent = `Player ${tttCurrentPlayer}'s turn`;
}

function checkWin(player) {
    return winPatterns.some(pattern =>
        pattern.every(i => tttBoard[i] === player)
    );
}

/* ---------- Computer AI ---------- */

function computerMove() {
    if (!tttGameActive) return;

    const emptyCells = tttBoard
        .map((v, i) => v === "" ? i : null)
        .filter(v => v !== null);

    const randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];
    makeMove(randomIndex, "O");
}
