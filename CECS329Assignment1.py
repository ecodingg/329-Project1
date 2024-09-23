#Names: Eden Doss-Fillmore, Noah Daniels, Angelo Cervana
#Tools used: Visual Studio Code, Discord, GitHub, Python, ChatGPT
#GitHub Link: https://github.com/ecodingg/329-Project1

class DFA:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.build_dfa()

    def build_dfa(self):
        self.states = {}
        state_id = 0
        self.start_state = state_id

        # Create states for matching the first name
        current_state = state_id
        for char in self.first_name:
            next_state = state_id + 1
            self.states[state_id] = {}
            self.states[state_id][char] = next_state
            state_id = next_state
            current_state = next_state

        # Intermediate state after matching the first name
        self.first_name_end_state = current_state

        # Create states for matching the last name
        self.last_name_start_state = state_id
        for char in self.last_name:
            next_state = state_id + 1
            self.states[state_id] = {}
            self.states[state_id][char] = next_state
            state_id = next_state

        # Final accepting state
        self.accepting_state = state_id
        self.states[self.accepting_state] = {}

        # Initialize transitions for characters not in the current state dictionary
        for state in range(self.accepting_state + 1):
            if state not in self.states:
                self.states[state] = {}
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char not in self.states[state]:
                    # og code that had a bug
                    """if state >= self.last_name_start_state:
                        self.states[state][char] = self.accepting_state
                    else:
                        self.states[state][char] = self.start_state"""
                    # potential fix
                    if self.start_state <= state < self.first_name_end_state:
                        self.states[state][char] = self.start_state
                    elif self.last_name_start_state <= state < self.accepting_state:
                        self.states[state][char] = self.last_name_start_state
                    else:
                        self.states[state][char] = self.accepting_state

    def process_input(self, input_string):
        state = self.start_state
        index = 0
        first_name_found = False

        # Step 1: Find the first occurrence of the first name
        while index < len(input_string):
            char = input_string[index]
            if char in self.states[state]:
                state = self.states[state][char]
                if state == self.first_name_end_state:
                    first_name_found = True
                    # Move to the state to start searching for the last name
                    state = self.last_name_start_state
                    break
            else:
                state = self.start_state
            index += 1

        # Check if the first name was found
        if not first_name_found:
            return False  # The first name was not found

        # Step 2: Try to match the last name after finding the first name
        while index < len(input_string):
            char = input_string[index]
            if char in self.states[state]:
                state = self.states[state][char]
                if state == self.accepting_state:
                    return True
            else:
                # Ensure we correctly handle the case where we are not matching
                if state >= self.last_name_start_state:
                    state = self.accepting_state
                else:
                    state = self.last_name_start_state
            index += 1

        return False
    
class NFA:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.build_nfa()

    def build_nfa(self):
        self.states = {}
        state_id = 0
        self.start_state = state_id

        # Create states for matching the first name
        current_state = state_id
        for char in self.first_name:
            next_state = state_id + 1
            self.states[state_id] = {}
            self.states[state_id][char] = next_state
            state_id = next_state
            current_state = next_state

        # Intermediate state after matching the first name
        self.first_name_end_state = current_state

        # Create states for matching the last name
        self.last_name_start_state = state_id
        for char in self.last_name:
            next_state = state_id + 1
            self.states[state_id] = {}
            self.states[state_id][char] = next_state
            state_id = next_state

        # Final accepting state
        self.accepting_state = state_id
        self.states[self.accepting_state] = {}

        # Initialize transitions for characters not in the current state dictionary
        for state in range(self.accepting_state + 1):
            if state not in self.states:
                self.states[state] = {}
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char not in self.states[state]:
                    # og code that had a bug
                    """if state >= self.last_name_start_state:
                        self.states[state][char] = self.accepting_state
                    else:
                        self.states[state][char] = self.start_state"""
                    # potential fix
                    if self.start_state <= state < self.first_name_end_state:
                        self.states[state][char] = self.start_state
                    elif self.last_name_start_state <= state < self.accepting_state:
                        self.states[state][char] = self.last_name_start_state
                    else:
                        self.states[state][char] = self.accepting_state
    
    def process_input(self, input_string):
        state = self.start_state
        index = 0
        first_name_found = False

        # Step 1: Find the first occurrence of the first name
        while index < len(input_string):
            char = input_string[index]
            if char in self.states[state]:
                state = self.states[state][char]
                if state == self.first_name_end_state:
                    first_name_found = True
                    # Move to the state to start searching for the last name
                    state = self.last_name_start_state
                    break
            else:
                state = self.start_state
            index += 1

        # Check if the first name was found
        if not first_name_found:
            return False  # The first name was not found

        # Step 2: Try to match the last name after finding the first name
        while index < len(input_string):
            char = input_string[index]
            if char in self.states[state]:
                state = self.states[state][char]
                if state == self.accepting_state:
                    return True
            else:
                # Ensure we correctly handle the case where we are not matching
                if state >= self.last_name_start_state:
                    state = self.accepting_state
                else:
                    state = self.last_name_start_state
            index += 1

        return False

def main():
    while True:
        # Get names from the user
        first_name = input("Enter the first name (or type 'exit' to quit): ").strip().lower()
        if first_name == 'exit':
            break
        last_name = input("Enter the last name: ").strip().lower()
        
        dfa = DFA(first_name, last_name)
        nfa = NFA(first_name, last_name)

        test_cases = ['noah', 'daniel', 'noahdanie', 'noahdaniel', 'qfoenwfinoahdanielwion', '', 'danielnoah']

        for i in test_cases:
            print('\nTesting test case:', i)
            test_case = i.strip().lower()
            if(dfa.process_input(test_case) or nfa.process_input(test_case)):
                result = True
            print(f"Input: {test_case} -> {'Accepted' if result else 'Rejected'}")

        while True:
            print("\nEnter manual test cases (one per line). Type 'exit' to stop:")
            test_case = input().strip().lower()
            if test_case == 'exit':
                print("Empty line detected, exiting test cases loop.")
                break  # Exit the test cases loop
            
            if(dfa.process_input(test_case) or nfa.process_input(test_case)):
                result = True
            print(f"Input: {test_case} -> {'Accepted' if result else 'Rejected'}")
        
        # After exiting the test cases loop, prompt for new names or exit
        print("\nReady for new names or type 'exit' to quit.")

main()
