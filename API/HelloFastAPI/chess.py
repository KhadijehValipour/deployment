from fastapi import FastAPI, HTTPException, status

app = FastAPI()

pieces = {

    "pawn": {
        "name": "Pawn",
        "description": "The pawn is the most numerous piece in the game of chess.",
        "image_url": "https://files.fm/f/nwcyqjwmuu"
        } ,

    "bishop": {
        "name": "Bishop",
        "description" :"The bishop moves diagonally across the board.",
        "image_url": "https://files.fm/f/j879mkru3w"
        } ,
    
    "knight": {
        "name": "Knight",
        "description": "The knight moves in an 'L' shape, two squares in one direction and then one square perpendicular.",
        "image_url": "https://files.fm/f/w8vvqgtkbv"
         } ,
    
     
    "rook": {
        "name": "Rook",
        "description": "The rook moves horizontally or vertically across the board.",
        "image_url": "https://files.fm/f/esqzxtupe2"
    },
    "queen": {
        "name": "Queen",
        "description": "The queen combines the power of the rook and bishop, moving horizontally, vertically, and diagonally.",
        "image_url": "https://files.fm/f/esqzxtupe2"
    },
    "king": {
        "name": "King",
        "description": "The king is the most important piece, but moves only one square in any direction.",
        "image_url": "https://files.fm/f/esqzxtupe2"
    }

}

@app.get("/")
def root():
    return {"message": "Welcome to the Chess Pieces API. Use /pieces to get a list of all chess pieces."}


@app.get("/pieces")
def get_pieces():
    return pieces

@app.get("/pieces/{pieces_name}")
def get_pieces(pieces_name: str):
    if pieces_name in pieces:
        return pieces[pieces_name]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
    
@app.get("/pieces/{pieces_name}/image")
def get_pieces_image(pieces_name: str):
    if pieces_name in pieces:
        return {"image_url":pieces[pieces_name]["image_url"]}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")





