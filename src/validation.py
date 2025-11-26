def validate_note_input(data):
    if not data.get("title") or not data.get("content"):
        return False
    if "<script>" in data["title"].lower() or "<script>" in data["content"].lower():
        return False
    return True
