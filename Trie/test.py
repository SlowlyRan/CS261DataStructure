from trie import Trie
ins =  ['symmetrical', 'show', 'inhibition', 'electricity', 'magnet', 'immediate', 'solid', 'far', 'length', 'one', 'torque', 'loosely', 'examine', 'shock', 'piece', 'east', 'total', 'who', 'start', 'together', 'film', 'seal', 'tightness', 'related', 'leak', 'best', 'instruction', 'patch', 'track', 'weather', 'length', 'tertiary', 'electronic', 'spray', 'movement', 'across', 'satire', 'identification', 'structural', 'read', 'a', 'load', 'than', 'drink', 'fluid', 'the', 'curve', 'not', 'do', 'weigh']
uncompressed_trie = Trie(is_compressed=True)
uncompressed_trie.construct_trie_from_text(ins)
#uncompressed_trie.print_trie()
r = uncompressed_trie.search_and_get_depth("sho")
print(r)

#uncompressed_trie.print_trie()
"""
for i in keys:
    for j in range(len(i)):
        r = uncompressed_trie.search_and_get_depth(i[j:])
        print(r)



r = uncompressed_trie.search_and_get_depth("imm")
print(r)

for i in uncompressed_trie.root.children.keys():
    print(uncompressed_trie.root.children[i].val)
"""