# Define the logic gate functions
def AND_gate(input1, input2):
    return input1 & input2

def OR_gate(input1, input2):
    return input1 | input2

def NOT_gate(input):
    return not input

# Function to simulate the circuit
def logic_circuit(A, B, C):
    # First AND gate: A AND B
    and1 = AND_gate(A, B)
    
    # Second AND gate: B AND C
    and2 = AND_gate(B, C)
    
    # OR gate: (A AND B) OR (B AND C)
    or1 = OR_gate(and1, and2)
    
    # NOT gate: NOT C
    not1 = NOT_gate(C)
    
    # Third AND gate: A AND (NOT C)
    and3 = AND_gate(A, int(not1))  # Convert boolean to int for consistency
    
    # Final OR gate: ((A AND B) OR (B AND C)) OR (A AND (NOT C))
    Q = OR_gate(or1, and3)
    
    return Q

# Example test case:
# Inputs A, B, C
A = 1
B = 0
C = 1

# Call the circuit function with the inputs
output = logic_circuit(A, B, C)

print(f"Output Q for A={A}, B={B}, C={C} is: {output}")
