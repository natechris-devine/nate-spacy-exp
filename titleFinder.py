import spacy
from spacy import displacy

text = "I have a Masters in User Experience Design from Stanford. I also got a BSc in Software Engineering"
text = "I went to Stanford and got a Masters Degree."
text = "I got my AWS Cert two years ago."
text = "I have my Bachelors in Economics and my Masters in Social Sciences."
text = "My masters degree was in Economics and I got it in two years"

"""
Task List:
1) 
"""

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

def noun_chunks(doc):
    chunks = []
    for chunk in doc.noun_chunks:
        chunks.append((chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text))
    return chunks

def titleFinder(doc):
    """Returns a list of tuples, in the form (title: spacy.doc.token, toQuery: Bool). - Idea, could also be a dict
    toQuery dictates if Resumate needs to confirm with the user 
    if the identified title is a title"""
    titles = []

    # KB - simulated
    possessVerbs = ["have", "obtain", "get"]

    # focus on using these hit words over the possessive verb. Hit a particular family of keywords/vocab/thesaurus
    # good heuristic would look for these strong trigger words
    # once we get a hit, do a tree search
    # Additionally, check relationships of links between tokens to ensure hit is relevant
    certs = ["masters", "bsc", "bachelors", "assosciate", "certificate", "degree", "diploma", "qualification"]

    # see if we can find a "thesaurus" tool to check if a word is similar to one of the hot words

    """When you hit a key word, navigate to the appropriate descendants to get the full title"""
    """Figuring out references to 'it'?"""

    for token in doc:
        if token.lemma_ in possessVerbs:
            for c in token.children:
                if c.dep_ not in ["nsubj", "punct", "advmod"]:
                    if c.lemma_.lower() in certs:
                        titles.append((c, False))
                    else:
                        titles.append((c, True))
    print(titles)
    return titles


def to_tree(token):
    """Returns a flat list of the children of a token"""
    children = list(token.children)
    if children == []:
        return token.text
    else:
        result = [token.text]
        result.append(list(map(to_tree, children)))
        return result

print(to_tree(doc[2]))


def dependencyDiagram(doc):
    """not working yet"""
    displacy.serve(doc, style='dep')

# print(noun_chunks(doc))
# titleFinder(doc)


"""Scrap Code"""
'''
print(token.text)
    print([t.text for t in token.subtree])
    # lst = []
'''