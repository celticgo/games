# Cybersecurity Role Selector Game
def welcome():
    print("Welcome to the Cybersecurity Role Selector Game!")
    print("Answer the following questions to find a role that fits your skills and interests.")


# Questions to determine the role
def ask_questions():
    print("\nFor each question, choose the answer that best describes you.")

    # Scores for each role
    scores = {
        "Security Analyst": 0,
        "Penetration Tester": 0,
        "Incident Responder": 0,
        "Security Architect": 0,
        "Compliance Analyst": 0
    }

    # Question 1
    print("\n1. What do you enjoy most?")
    print("a) Investigating and analyzing data for suspicious activities")
    print("b) Finding vulnerabilities in systems")
    print("c) Responding to and managing incidents and crises")
    print("d) Designing secure systems and networks")
    print("e) Ensuring organizations follow security policies and standards")

    answer = input("Your answer (a/b/c/d/e): ").lower()
    if answer == "a":
        scores["Security Analyst"] += 1
    elif answer == "b":
        scores["Penetration Tester"] += 1
    elif answer == "c":
        scores["Incident Responder"] += 1
    elif answer == "d":
        scores["Security Architect"] += 1
    elif answer == "e":
        scores["Compliance Analyst"] += 1

    # Question 2
    print("\n2. How do you prefer working?")
    print("a) Monitoring and reviewing logs for unusual activity")
    print("b) Running simulations to test security defenses")
    print("c) Being the first to respond to security alerts and breaches")
    print("d) Planning and creating long-term secure network structures")
    print("e) Conducting audits and reviewing compliance with regulations")

    answer = input("Your answer (a/b/c/d/e): ").lower()
    if answer == "a":
        scores["Security Analyst"] += 1
    elif answer == "b":
        scores["Penetration Tester"] += 1
    elif answer == "c":
        scores["Incident Responder"] += 1
    elif answer == "d":
        scores["Security Architect"] += 1
    elif answer == "e":
        scores["Compliance Analyst"] += 1

    # Question 3
    print("\n3. What are your strengths?")
    print("a) Analyzing data and recognizing patterns")
    print("b) Identifying and exploiting system vulnerabilities")
    print("c) Thinking quickly in high-stress situations")
    print("d) Designing robust security solutions")
    print("e) Attention to detail and understanding regulations")

    answer = input("Your answer (a/b/c/d/e): ").lower()
    if answer == "a":
        scores["Security Analyst"] += 1
    elif answer == "b":
        scores["Penetration Tester"] += 1
    elif answer == "c":
        scores["Incident Responder"] += 1
    elif answer == "d":
        scores["Security Architect"] += 1
    elif answer == "e":
        scores["Compliance Analyst"] += 1

    return scores


# Calculate the best role based on the scores
def calculate_role(scores):
    max_score = max(scores.values())
    best_roles = [role for role, score in scores.items() if score == max_score]

    print("\nBased on your answers, you might be interested in one of the following roles:")
    for role in best_roles:
        print(f"- {role}")


# Main game function
def play_game():
    welcome()
    scores = ask_questions()
    calculate_role(scores)


# Start the game
play_game()
