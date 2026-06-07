# 1) Students dictionary

students = {
    "Giorgi": {
        "score": 95,
        "attendance": 90
    },
    "Nika": {
        "score": 88,
        "attendance": 85
    },
    "Luka": {
        "score": 92,
        "attendance": 95
    }
}

# ყველაზე მაღალი ქულის მქონე სტუდენტი
best_student = max(students, key=lambda x: students[x]["score"])
print("ყველაზე მაღალი ქულა აქვს:", best_student)

# საშუალო ქულა
average_score = sum(student["score"] for student in students.values()) / len(students)
print("საშუალო ქულა:", average_score)


# 2) Products dictionary

products = {
    "laptop": {"price": 3000, "stock": 4},
    "phone": {"price": 1500, "stock": 10},
    "tablet": {"price": 1200, "stock": 0}
}

# მარაგში არსებული პროდუქტები
print("მარაგში არსებული პროდუქტები:")
for product, info in products.items():
    if info["stock"] > 0:
        print(product)

# ჯამური ღირებულება
total_value = 0

for info in products.values():
    total_value += info["price"] * info["stock"]

print("ყველა პროდუქტის ჯამური ღირებულება:", total_value)


# 3) Footballers dictionary

footballers = {
    "Messi": {
        "goals": 25,
        "assists": 12
    },
    "Ronaldo": {
        "goals": 30,
        "assists": 8
    }
}

# ახალი ფეხბურთელის დამატება
footballers["Mbappe"] = {
    "goals": 22,
    "assists": 10
}

# ერთ ფეხბურთელს გოლების დამატება
footballers["Messi"]["goals"] += 5

# ყველაზე მეტი გოლის მქონე ფეხბურთელი
top_scorer = max(footballers, key=lambda x: footballers[x]["goals"])
print("ყველაზე მეტი გოლი აქვს:", top_scorer)


# 4) Employees dictionary

employees = {
    "Giorgi": {"salary": 2500, "position": "Manager"},
    "Nika": {"salary": 1800, "position": "Developer"},
    "Luka": {"salary": 1500, "position": "Designer"}
}

# ხელფასების გაზრდა 10%-ით
for employee in employees:
    employees[employee]["salary"] *= 1.1

# ყველაზე მაღალი ხელფასის მქონე თანამშრომელი
highest_paid = max(employees, key=lambda x: employees[x]["salary"])
print("ყველაზე მაღალი ხელფასი აქვს:", highest_paid)

# ყველა ხელფასის ჯამი
total_salary = sum(employee["salary"] for employee in employees.values())
print("ყველა ხელფასის ჯამი:", total_salary)