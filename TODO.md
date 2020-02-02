### TODO

- Need to redo check_move() algorithm
- Movement validity needs refactor, order of checking seems off
- Valid moves
    - pawn diagonal move to take may be tricky
    - previously piece class would query the board if the space was occupied
    - already doing that to see if piece was taken, but are checking if valid 
    move before this.
    
- Collision
    - Need to draw up a path a piece is taking.
    - This can be done in check_move
    - After the move is declared valid by type
    
- check_move algorithm
    - if move is not valid by piece type:
        - reset
    - if there is another piece in the way and not of type Knight:
        - reset
    - if there is another piece at the end and of same colour:
        - reset
    - else move is valid; commit