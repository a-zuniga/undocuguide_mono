scholarship_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "deadline": {"type": "string", "format": "data-time"},
        "amount": {"type": "number"},
        "url": {"type": "string"},
    },
    "required": ["name", "amount", "deadline"],
}

class Scholarship:
    def __init__(self, name, description, amount, deadline, url):
        self.name = name
        self.description = description
        self.amount = amount
        self.deadline = deadline
        self.url = url