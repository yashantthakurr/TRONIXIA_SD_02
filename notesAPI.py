from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Note(BaseModel):
    id: int
    title: str
    content: str

notes: List[Note] = []

@app.get("/")
def readRoot():
    return {"message": "Welcome to Notes API"}

@app.get("/notes")
def getNotes():
    return notes

@app.post("/notes")
def addNote(note: Note):
    if any(existing.id == note.id for existing in notes):
        raise HTTPException(status_code = 409, detail = f"Note with ID {note.id} already exists.")
    notes.append(note)
    return note

@app.put("/notes/{noteId}")
def updateNote(noteId: int, updatedNote: Note):
    for index, note in enumerate(notes):
        if note.id == noteId:
            notes[index] = updatedNote
            return updatedNote
    raise HTTPException(status_code = 404, detail = "Note not found.")

@app.delete("/notes/{noteId}")
def deleteNote(noteId: int):
    for index, note in enumerate(notes):
        if note.id == noteId:
            deletedNote = notes.pop(index)
            return deletedNote
    raise HTTPException(status_code = 404, detail = "Note not found.")

