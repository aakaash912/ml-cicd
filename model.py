import spacy
import classy_classification
nlp=spacy.load("en_core_web_sm")
data = {
    "Positive": [
    "He is doing a great job.",
    "She is doing a great job.",
    "Today is a beautiful day.",
    "He makes a difference.",
    "She makes a difference.",
    "He is so kind.",
    "She is so kind.",
    "He should believe in himself.",
    "She should believe in herself.",
    "He is important.",
    "She is important.",
    "His smile is wonderful.",
    "Her smile is wonderful.",
    "He is loved.",
    "She is loved."],
  
    "Negative": [
    "He is not doing well.",
    "She is not doing well.",
    "Today is a bad day.",
    "He makes mistakes.",
    "She makes mistakes.",
    "He is unkind.",
    "She is unkind.",
    "He doubts himself.",
    "She doubts herself.",
    "He feels unimportant.",
    "She feels unimportant.",
    "His smile is missing.",
    "Her smile is missing.",
    "He feels unloved.",
    "She feels unloved.",
    "He struggles to achieve anything.",
    "She struggles to achieve anything."
]
}
sentence="This is an awfully good tasting Cherry Pie."
nlp.add_pipe("classy_classification",config={"data": data, "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"})
print(sentence)
classification=nlp(sentence)._.cats
print(classification)
with open('metrics.txt', 'w') as outfile:
    outfile.write(sentence,":")
    if classification["Positive"]>0.5:
        outfile.write('Positive')
    else:
        outfile.write('Negative')
