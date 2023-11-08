let play_board = ["", "", "", "", "", "", "", "", ""];
const player = "O";
const computer = "X";
let board_full = false;


const render_board = () => {
    const board_container = document.querySelector(".play-area");
    board_container.innerHTML = "";
    play_board.forEach((e,i) => {
        board_container.innerHTML += `<div id="block_${i}" class="block" onclick="addPlayerMove(${i})">${play_board[i]}</div>`;
        if(e == player || e == computer) {
            document.querySelector(`#block_${i}`).classList.add("occupied");
        }
    });
};


render_board();

const game_loop = () => {
    render_board();
}

const nextValue = e => {
    if (e == "") {
        return "O";
    } else if (e == "X") {
        return "";
    } else {
        return "X";
    }
};

const addPlayerMove = e => {
    console.log(`index: ${e}`)
    play_board[e] = nextValue(play_board[e]);
    game_loop();
};

const reset_board = () => {
    play_board = ["", "", "", "", "", "", "", "", ""];
    board_full = false;
    render_board();
}
