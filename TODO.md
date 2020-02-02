### TODO

- ~~Need to redo check_move() algorithm~~
- ~~Movement validity needs refactor, order of checking seems off~~
    
- ~~Collision~~ DONE
    - ~~Need to draw up a path a piece is taking.~~
    - ~~This can be done in check_move~~
    - ~~After the move is declared valid by type~~
    
- ~~check_move algorithm~~ DONE
    - ~~if move is not valid by piece type:~~
        - ~~reset~~
    - ~~if there is another piece in the way and not of type Knight:~~
        - ~~reset~~
    - ~~if there is another piece at the end and of same colour:~~
        - ~~reset~~
    - ~~else move is valid; commit~~
    
- Valid moves
    - pawn diagonal move to take may be tricky
    - previously piece class would query the board if the space was occupied
    - already doing that to see if piece was taken, but are checking if valid 
    move before this.
    - Need to add the other moves too
 
- sockets
    - before implementing proper end game and special move mechanics, want to 
    implement the online and turn capabilities.


### In the future:
- en passant
    - requires knowledge of the previous player's turn
- castling
    - since the pieces can never have moved, need to store this state
    - Need a special 'check_move' to see if there are any pieces between the rook
    and king
    - need to determine which rook in question
- promotion
    - very easy to implement, just replace the piece in the piece list
    
issue with these special moves is that they break down the separation between
the Piece and Board classes e.g will require a lot of piece specific move checking
functions in the Board class.

- check and game end mechanics
    - check will probably need a lot of work, since must iterate over all
    possible moves to see if a move will put the game into check, or if a move
    will get the game out of check
    - checkmate too
    - will be good to implement with a computer player to play against
