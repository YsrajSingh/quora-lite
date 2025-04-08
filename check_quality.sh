#!/bin/bash

# echo "Running pylint..."
# pylint app/

echo "Running bandit..."
bandit -r app/

# echo "Running djLint on templates..."
# djlint templates/ --check

echo "All checks complete!"
