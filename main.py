import requests

BASE_URL = "http://127.0.0.1:8000"

while True:
    print("---" * 25)
    print("Select: | 1. Add Note | 2. Update Note | 3. Delete Note | 4. View Notes |")

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                note_id = int(input("Enter ID: "))
                title = input("Enter title: ")
                content = input("Enter content: ")
                response = requests.post(f"{BASE_URL}/notes", json = {"id": note_id, "title": title, "content": content})
                if response.status_code == 200:
                    print("Added:", response.json())
                else:
                    print("Note with this id already exists.")

            case 2:
                note_id = int(input("Enter ID of note to update: "))
                title = input("Enter new title: ")
                content = input("Enter new content: ")
                response = requests.put(f"{BASE_URL}/notes/{note_id}", json = {"id": note_id, "title": title, "content": content})
                if response.status_code == 200:
                    print("Updated:", response.json())
                else:
                    print("Cannot update note.")

            case 3:
                note_id = int(input("Enter ID of note to delete: "))
                response = requests.delete(f"{BASE_URL}/notes/{note_id}")
                if response.status_code == 200:
                    print("Deleted:", response.json())
                else:
                    print("Cannot delete note.")

            case 4:
                response = requests.get(f"{BASE_URL}/notes")
                notes = response.json()
                if not notes:
                    print("No notes found.")
                else:
                    for note in notes:
                        print(f"[{note['id']}] {note['title']}: {note['content']}")

            case _:
                print("You should enter a valid choice!")

    except ValueError:
        print("You should enter a number.")


