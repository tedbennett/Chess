### TODO

- Need to redo check_move() algorithm
- Movement validity needs refactor, order of checking seems off
- Valid moves
    - pawn diagonal move to take may be tricky
    - previously piece class would query the board if the space was occupied
    - already doing that to see if piece was taken, but are checking if valid 
    move before this.