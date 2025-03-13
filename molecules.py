def multiply_atoms(atoms, multiplier):
    """Multiply the count of each atom in a dictionary by a multiplier."""
    return {atom: count * multiplier for atom, count in atoms.items()}


def merge_atoms(atoms1, atoms2):
    """Merge two dictionaries containing atom counts."""
    for atom, count in atoms2.items():
        atoms1[atom] = atoms1.get(atom, 0) + count
    return atoms1


def process_atom(formula, i):
    """Process an atom and its count."""
    j = i + 1
    while j < len(formula) and formula[j].islower():
        j += 1
    atom = formula[i:j]
    i = j
    count = 0
    while i < len(formula) and formula[i].isdigit():
        count = count * 10 + int(formula[i])
        i += 1
    count = count if count > 0 else 1
    return atom, count, i


def process_opening_bracket(stack, atom_counts):
    """Handle an opening bracket."""
    stack.append((atom_counts.copy(), None))


def process_closing_bracket(stack, atom_counts, i, formula):
    """Handle a closing bracket and apply multipliers."""
    j = i + 1
    multiplier = 0
    while j < len(formula) and formula[j].isdigit():
        multiplier = multiplier * 10 + int(formula[j])
        j += 1
    multiplier = multiplier if multiplier > 0 else 1
    i = j
    atom_counts = multiply_atoms(atom_counts, multiplier)
    previous_atoms, _ = stack.pop()
    return merge_atoms(previous_atoms, atom_counts), i


def parse_formula(formula):
    stack = []
    atom_counts = {}
    i = 0

    while i < len(formula):
        char = formula[i]

        if char.isupper():  # Found an atom
            atom, count, i = process_atom(formula, i)
            atom_counts[atom] = atom_counts.get(atom, 0) + count

        elif char in "([{":  # Opening bracket
            process_opening_bracket(stack, atom_counts)
            atom_counts = {}
            i += 1

        elif char in ")]}":  # Closing bracket
            atom_counts, i = process_closing_bracket(stack, atom_counts, i, formula)

        else:
            i += 1  # Move to next character

    while stack:  # Handle any remaining open brackets
        previous_atoms, _ = stack.pop()
        atom_counts = merge_atoms(previous_atoms, atom_counts)

    return atom_counts
