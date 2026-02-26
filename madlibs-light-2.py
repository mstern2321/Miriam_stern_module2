# Day 1 Dictionary Mad Libs (NO nested dictionaries)
# -------------------------------------------------
# You are GIVEN: TEMPLATE, PROMPTS, RULES, state
# You must COMPLETE the TODO functions:
#   1) validate_input
#   2) collect_answers
#   3) score_answers
#   4) play_once
#from IPython.terminal import prompts

# from loops_mini_exam_questions import user_input
"""
Miriam Stern 
This is a mad libs game that was created by using dictionaries to store the players answers. 
"""
TEMPLATE = (
    "I was waiting for the {adj1} train at {num1} o’clock when a {noun1} "
    "{verb_past1} past me and shouted, “{exclaim1}!” "
    "I grabbed my {noun2} and ran {num2} steps to the {noun3}."
)

# PROMPTS is a dictionary:
#   key   = placeholder name (must match TEMPLATE placeholders)
#   value = what we ask the user to type
PROMPTS = {
    "adj1": "Enter an adjective",
    "num1": "Enter a number (0-23)",
    "noun1": "Enter a noun",
    "verb_past1": "Enter a past-tense verb",
    "exclaim1": "Enter an exclamation (one word)",
    "noun2": "Enter a noun",
    "num2": "Enter a number (1-500)",
    "noun3": "Enter a noun",
}

# RULES is a dictionary:
#   key   = placeholder name (only for some placeholders)
#   value = a rule dictionary describing how to validate the input
#  we access a dictionary within a dictionary like it is a nested loop
#  For instance, to access num1's max value 23 : RULES["num1"]["max"]
#  To access the value word of exclaim1 : RULES["exclaim1"]["type"]

RULES = {
    "num1": {"type": "int", "min": 0, "max": 23},
    "num2": {"type": "int", "min": 1, "max": 500},
    "exclaim1": {"type": "word"},
}

# state tracks information across multiple plays
state = {
    "plays_total": 0,
    "best_score": None,
}


def validate_input(key, raw, rules):
    """
    Validate ONE user entry.

    Parameters:
      key   : the placeholder key (example: "num1" or "noun2")
      raw   : the user's raw input (a string)
      rules : the RULES dictionary

    Return:
      (ok, value, error_message)
        ok = True/False
        value = cleaned value (string or int) if ok is True, else None
        error_message = "" if ok is True, else a message to show the user

    Rules supported:
      - If key NOT in rules: accept any non-empty string (strip whitespace)
      - {"type":"int", "min":..., "max":...}
      - {"type":"word"}  -> one word only (no spaces), not empty

    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]  
    """
    # TODO 1: get the rule for this key using rules.get(key)
    rule = rules.get(key)
    # TODO 2: if there is NO rule, return (True, stripped_input, "")
    stripped_input = raw.strip()
    if rule is None:
        if stripped_input == "":
            return False, None, "Please enter a valid string"
        return True, stripped_input, ""
    # TODO 3: if type == "int":
    #         - try to convert stripped_input to int
    #         - if it fails, return (False, None, "Please enter a valid integer.")
    #         - enforce min/max if present
    if rule.get("type") == "int":
        try:
            stripped_input = int(stripped_input) # Try to convert to integer
        except ValueError:
            return False, None, "Please enter a valid integer"
        if stripped_input < rule.get("min") or stripped_input > rule.get("max"):
            return False, None, "Please enter a valid integer"
        return True, stripped_input, ""

    # TODO 4: if type == "word":
    #         - stripped input must be non-empty
    #         - must NOT contain spaces
    if rule.get("type") == "word":
        if stripped_input == "":
            return False, None, "Please enter a valid word"
        if " " in stripped_input:
            return False, None, "Please enter a valid word"
        else:
            return True, stripped_input, ""

    # TODO 5: if unknown rule type, treat it like a normal string

    return True, stripped_input, ""


def collect_answers(prompts, rules):
    """
    Build the answers dictionary.

    prompts: PROMPTS dict (placeholder -> prompt)
    rules  : RULES dict (placeholder -> rule)
    
    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"] 

    Returns:
      answers dict where:
        key   = placeholder name (example: "noun1")
        value = validated user input (string or int)

    Requirements:
      - Start with answers = {}
      - Loop through prompts.items()
      - For each key:
          keep prompting until validate_input(...) returns ok=True
      - Store answers using answers[key] = value
    """
    # TODO: implement collect_answers
    # Hint: you'll want a while True loop inside the for-loop
    answers = {}
    for key, prompt in prompts.items():
        while True:
            raw = input(f"{prompt}: ") # Prints the prompt and stores users answer
            ok, value, error = validate_input(key, raw, rules) # unpacks tuple from validate_input
            if ok: # if ok = True then the value is stored in the answers dictionary
                answers[key]=value
                break
            else:
                print(error)
    return answers






def score_answers(answers, rules):
    """
    Compute a score for one round.

    Recommended scoring:
      - +1 for each answer key in answers
      - +2 bonus if that key also appears in rules

    Example:
      If answers has 8 keys, and 3 keys are in rules:
        score = 8*1 + 3*2 = 14


    How to use the RULES dictionary :
     - we access a dictionary within a dictionary like it is a nested loop
     - For instance, to access num1's max value 23 : RULES["num1"]["max"]
     -  To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    # TODO: implement score_answers
    # Requirements:
    #   - iterate over the dictionary keys in answers (for key in answers:)
    #   - use membership test (if key in rules:)
    score = 0
    for key in answers:
        score += 1
        if key in rules: # 2 points if key in answers and rules
            score += 2
    return score


def play_once():
    """
    Play one round of Mad Libs.

    Steps:
      1) Collect answers into a dictionary
      2) Fill TEMPLATE using TEMPLATE.format_map(answers)
      3) Score the round
      4) Update state:
          - plays_total increases by 1
          - best_score updates if this score is higher
      5) Print:
          - completed story
          - answers dict
          - score
    """
    print("\nFill in the blanks (you won't see the full story until the end!)\n")

    # TODO 1: answers = collect_answers(PROMPTS, RULES)
    answers = collect_answers(PROMPTS, RULES)
    # TODO 2: finished = TEMPLATE.format_map(answers)
    finished = TEMPLATE.format_map(answers)
    # TODO 3: score = score_answers(answers, RULES)
    score = score_answers(answers, RULES)
    # TODO 4: update state["plays_total"] and state["best_score"]
    state["plays_total"] += 1
    if state["best_score"] is None or score > state["best_score"]:
        state["best_score"] = score

    # TODO 5: print the finished story + answers dict + score
    print(f"Finished story: {finished}")
    print(f"Answers: {answers}")
    print(f"Your score is: {score}")

    with open("write.txt", "a") as file:
        file.write(finished + "\n")





def main():
    """

    What main  does:
    - Repeatedly asks the user if they want to play
    - Calls play_once() when the user says 'y'
    - Stops when the user says 'n'
    - Prints a summary using the state dictionary
    """

    print("Mad Libs ")

    # TODO (READ ONLY): This while loop keeps the program running
    # until the user chooses to stop.
    user_input = None
    while user_input != "n":



        # TODO (READ ONLY): Get user choice and normalize it
        user_input = input("Do you want to play ('y' or 'n') ").lower().strip()

        # TODO (READ ONLY): Stop the game loop if user types 'n'
        if user_input == "n":
            break

        # TODO (READ ONLY): Play one full round if user types 'y'
        if user_input == "y":
            play_once()
        # TODO (READ ONLY): Any other input is invalid
        else:
            print("Please enter 'y' or 'n'")



    # TODO (READ ONLY): After the loop ends, print summary info
    # using the state dictionary.
    for key, value in state.items():
        print(f"{key}: {value}")




if __name__ == "__main__":
    main()
