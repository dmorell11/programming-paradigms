
from pyke import knowledge_engine

# Create a knowledge base
engine = knowledge_engine.engine(__file__)

# Define facts in the knowledge base
engine.assert_('family', 'parent(juan, maria)')
engine.assert_('family', 'parent(juan, carlos)')
engine.assert_('family', 'parent(ana, maria)')

# Define logical rule for grandparent
@engine.prove
def grandparent(X, Y):
    return (
        engine.assert_('family', f'parent({X}, {Z})'),
        engine.assert_('family', f'parent({Z}, {Y})')
    )

# Queries
print(grandparent('juan', 'maria'))
print(grandparent('juan', 'carlos'))
print(grandparent('ana', 'maria'))
