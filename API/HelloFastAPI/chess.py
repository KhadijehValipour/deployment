import uvicorn
from fastapi import FastAPI, HTTPException, status
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI()

pieces = {

    "pawn": {
        "name": "Pawn",
        "description": "The pawn is the most numerous piece in the game of chess.",
        "image_url": "https://files.fm/f/nwcyqjwmuu",
        "image": "assents/sarbaz.jpg"
        } ,

    "bishop": {
        "name": "Bishop",
        "description" :"The bishop moves diagonally across the board.",
        "image_url": "https://files.fm/f/j879mkru3w",
        "image": "assents/fil.jpg"
        } ,
    
    "knight": {
        "name": "Knight",
        "description": "The knight moves in an 'L' shape, two squares in one direction and then one square perpendicular.",
        "image_url": "https://files.fm/f/w8vvqgtkbv",
        "image": "assents/asb.jpg"
         } ,
    
     
    "rook": {
        "name": "Rook",
        "description": "The rook moves horizontally or vertically across the board.",
        "image_url": "https://files.fm/f/esqzxtupe2",
        "image" : "assents/ghale.jpg"
    },
    "queen": {
        "name": "Queen",
        "description": "The queen combines the power of the rook and bishop, moving horizontally, vertically, and diagonally.",
        "image_url": "https://files.fm/f/esqzxtupe2",
        "image": "assents/vazir.jpg"
    },
    "king": {
        "name": "King",
        "description": "The king is the most important piece, but moves only one square in any direction.",
        "image_url": "https://files.fm/f/esqzxtupe2",
        "image": "assents/shah.jpg"
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
    pieces_name_lower= pieces_name.lower()
    if pieces_name_lower in pieces:
        return pieces[pieces_name_lower]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
    
@app.get("/pieces/image")
def read_image():
    image_path= Path("assents/chess-pieces-3d-color-vector-37451508.jpg")
    return FileResponse(image_path)


@app.get("/pieces/{pieces_name}/image")
def get_pieces_image(pieces_name: str):
    pieces_name_lower = pieces_name.lower()
    if pieces_name_lower in pieces:
        images = pieces[pieces_name_lower]
        image_path = images["image"]
        return FileResponse(image_path)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")





