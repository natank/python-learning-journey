# Python Exercises

A collection of practice exercises for learning Python concepts.

## Setup

```bash
nx install python-exercises
```

## Running Exercises

### Calculator Functions
```bash
nx run-calculator python-exercises
```

### String Utilities
```bash
nx run-strings python-exercises
```

### Data Structures
```bash
nx run-data-structures python-exercises
```

## Testing

```bash
nx test python-exercises
```

## Exercises Included

- **Calculator**: Basic arithmetic operations (add, subtract, multiply, divide)
- **String Utils**: String manipulation utilities (reverse, palindrome check, vowel count)
- **Data Structures**: Stack and Queue implementations

## Adding New Exercises

1. Create new Python files in `src/`
2. Add corresponding Nx targets in `project.json`
3. Update `__init__.py` to export new functions/classes
