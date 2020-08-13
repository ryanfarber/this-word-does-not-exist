# run.py

from title_maker_pro.word_generator import WordGenerator

word_generator = WordGenerator(
	device="cpu",
	forward_model_path="./models/forward-dictionary-model-v1",
	inverse_model_path="./models/inverse-dictionary-model-v1",
	blacklist_path="./models/blacklist.pickle",
	quantize=False,
	)


# word from scratch
print(word_generator.generate_word())

# definition for a made up word
# print(word_generator.generate_definition("glooberyblipboop"))

# word made up from definition
# print(word_generator.generate_word_from_definition("a word that does not exist"))