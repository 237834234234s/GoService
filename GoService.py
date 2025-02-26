class TeamMember:
    def __init__(self, role, name):
        self.role = role
        self.name = name
    
    def __str__(self):
        return f"{self.role}: {self.name}"

go_service_team = [
    TeamMember("Менеджер проєкту", "Іван Петренко"),
    TeamMember("Front-end Розробник", "Олена Коваленко"),
    TeamMember("Back-end Розробник", "Максим Дорошенко"),
    TeamMember("UX/UI Дизайнер", "Світлана Левченко"),
    TeamMember("Маркетолог", "Андрій Бондар"),
]

print("Склад команди GoService:")
for member in go_service_team:
    print(member)
