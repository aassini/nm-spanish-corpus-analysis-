
import nltk
import os
import re
import string
import codecs



rootdir= "/Users/SanchoPanza/Desktop/NMCOSS/"

#function to preprocess line
def preprocess_line(transcription_line):
	unwanted = ["Mhm", "ah", "Oh", "oh", "Ah", "mhm", "Hm", "hm"]
	transcription_line = transcription_line.strip().split()
	processed_line = []
	for word in transcription_line:
		if word.strip(string.punctuation).isalpha() and word.strip(string.punctuation) != "X" and not word.strip(string.punctuation).startswith("XX") and word.strip(string.punctuation) not in unwanted and (len(word.strip(string.punctuation))>1 or word.strip(string.punctuation).lower() =="y" or word.strip(string.punctuation).lower() =="a") :
			processed_line.append(word.strip(string.punctuation))
			length_line = len(processed_line)
	return len(processed_line), processed_line




#function to count and then compare percent of each transcript is interviewer and consultant, write that to a file for each doc

#function to know which letter is the interviewer and consultant for this file

def people(data_lines):
	speaker = False	
	interviewer = ""
	consultant = ""
	for line in data_lines:
		if speaker == True and line.startswith("$ SPEAKER"):
			consultant = line[len("$ SPEAKER")+1]
			break
		if line.startswith("$ SPEAKER"): 
			interviewer = line[len("$ SPEAKER")+1]
			speaker = True
	return interviewer, consultant



#main function
def main(rootdir):
	num_words_consultant=0
	num_words_interviewer=0
	words_consultant =[]
	words_interviewer =[]
	bigrams_consultant = []

	utterance = []
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith(".doc") or filepath.endswith(".DOC") or filepath.endswith(".docx"):
				interview_metadata = file.rsplit(".", 1)[0]
				interview_metadata=interview_metadata.split("-")[0]
				transcription_raw= open(filepath, "r", encoding = "cp1254", errors = 'ignore')
				transcription_raw= transcription_raw.readlines()
				#to find the calls for the interviewer and consultant
				if not transcription_raw[0].startswith("$"):
					interviewer = "I"
					consultant = "C"
				else:
					interviewer, consultant = people(transcription_raw)
				speaker = True
				for line_t in transcription_raw:
					if line_t.startswith("$"):
						continue
					else:
						if line_t.startswith(interviewer + ":"):
							# if len(utterance)> 0:
								# bigrams = list(nltk.bigrams(utterance))
								# for bigram in bigrams:
									# bigrams_consultant.append([bigram, interview_metadata])
							speaker = False
							line_t.replace(interviewer + ":", "")
							num_wrds_intvr, wrds_intvr = preprocess_line(line_t)
							num_words_interviewer += num_wrds_intvr
							for word in wrds_intvr:
								words_interviewer.append((word.lower(), interview_metadata))
						if line_t.startswith(consultant + ":"):
							speaker = True
							line_t.replace(consultant + ":", "")
							num_wrds_conslt, wrds_conslt = preprocess_line(line_t)
							num_words_consultant += num_wrds_conslt
							for word in wrds_conslt:
								# utterance.append(word.lower())
								bigrams_consultant.append(word.lower())
								words_consultant.append((word.lower(), interview_metadata))
						else:
							if speaker == False:
								num_wrds_intvr, wrds_intvr = preprocess_line(line_t)
								num_words_interviewer += num_wrds_intvr
								for word in wrds_intvr:
									words_interviewer.append((word.lower(), interview_metadata))

							if speaker == True:
								
								num_wrds_conslt, wrds_conslt = preprocess_line(line_t)
								num_words_consultant += num_wrds_conslt
								for word in wrds_conslt:
									# utterance.append(word.lower())
									bigrams_consultant.append(word.lower())
									words_consultant.append((word.lower(), interview_metadata))
	own_bigrams=[]
	for i in range(len(words_consultant)-1):
		if words_consultant[i][1] == words_consultant[i+1][1]:
			bigram_ind = [words_consultant[i][0], words_consultant[i+1][0]]
			own_bigrams.append([bigram_ind, words_consultant[i][1]])

	own_trigrams=[]
	for i in range(len(words_consultant)-2):
		if words_consultant[i][1] == words_consultant[i+1][1] == words_consultant[i+2][1]:
			trigram_ind = [words_consultant[i][0], words_consultant[i+1][0], words_consultant[i+2][0]]
			own_trigrams.append([trigram_ind, words_consultant[i][1]])	

	# bigrams_con_test = list(nltk.bigrams(bigrams_consultant))
	return num_words_consultant, num_words_interviewer, words_consultant, words_interviewer, own_bigrams, own_trigrams	


num_w_consultant, num_w_interviewer, w_consultant, w_interviewer, create_bigrams, create_trigrams = main(rootdir)							


set_interviewer = set(w_interviewer)
set_consultant = set(w_consultant)


print("set of words consultant : ", len(set_consultant))
print("set of words interviewer : ", len(set_interviewer))
print ("total word count of consultant : ", len(w_consultant))

# from langdetect import detect_langs

# def englishOrSpanish(strings):
	# res = detect_langs(strings)
	# if res == "es" or res == "en":
		# print(res)
	# return None

def find_word(word, data_set):
	results ={}
	for item, doc_ID in data_set:
		if item.lower() == word and word not in results:
			results[item]=[doc_ID]
		if item.lower() == word and word in results:
			results[item].append(doc_ID)
	return results

school = find_word("school", w_consultant)
escuela = find_word("escuela", w_consultant)
job = find_word("job", w_consultant)
work = find_word("work", w_consultant)
trabajo = find_word("trabajo", w_consultant)
career = find_word("career", w_consultant)
carrera = find_word("carrera", w_consultant)
mom = find_word("mom", w_consultant)
mama=find_word("mamá", w_consultant)
madre = find_word("madre", w_consultant)
grandfather = find_word("grandfather", w_consultant)
grandpa= find_word("grandpa", w_consultant)
abuelo = find_word("abuelo", w_consultant)
abuelito = find_word("abuelito", w_consultant)
grandmother = find_word("grandmother", w_consultant)
grandma= find_word("grandma", w_consultant)
abuela = find_word("abuela", w_consultant)
abuelita= find_word("abuelita", w_consultant)
tia= find_word("tía", w_consultant)
aunt = find_word("aunt", w_consultant)
tio = find_word("tío", w_consultant)
uncle= find_word("uncle", w_consultant)
cousin = find_word("cousin", w_consultant)
primo = find_word("primo", w_consultant)
prima = find_word("prima", w_consultant)
hermana = find_word("hermana", w_consultant)
sister = find_word("sister", w_consultant)
hermano = find_word("hermano", w_consultant)
brother= find_word("brother", w_consultant)
father = find_word("father", w_consultant)
dad = find_word("dad", w_consultant)
padre = find_word("padre", w_consultant)
papa= find_word("papá", w_consultant)






print("number of times 'school' is used in English: " + str(len(school['school'])))

print("number of times 'escuela' is used in English: " + str(len(escuela['escuela'])))

print("number of times 'job' is used in English: " + str(len(job['job'])))

print("number of times 'work' is used in English: " + str(len(work['work'])))

print("number of times 'trabajo' is used in English: " + str(len(trabajo['trabajo'])))

print("number of times 'career' is used in English: " + str(len(career['career'])))

# print("number of times 'carrera' is used in English: " + str(len(carrera['carrera'])))


# def find_tuple(word1, word2, dataset_bigrams):
	# results={}
	# for item in dataset_bigrams:
	# 	word_first = item[0][0]
	# 	word_second = item[0][1]
	# 	dict_key =" ".join([word1, word2])
	# 	if item[0][0] == word1 and item[0][1] == word2 and dict_key not in results:
	# 		results[dict_key] = [dict_key]
	# 	elif item[0][0] == word1 and item[0][1] == word2 and dict_key in results:
	# 		results[dict_key].append(dict_key)
	# return results

def unigrams(dataset):
	words={}
	for word, docID in dataset:
		if word.lower() not in words:
			words[word.lower()]=[docID]
		else:
			words[word.lower()].append(docID)
	return words


def find_bigram(word1, word2, dataset_bigrams):
	results = {}
	for item in dataset_bigrams:
		dict_key = " ".join([word1, word2])
		if item[0][0] == word1 and item[0][1] == word2 and dict_key not in results:
			results[dict_key]= 1
		elif item[0][0] == word1 and item[0][1] == word2 and dict_key in results:
			results[dict_key] +=1
	return results

def find_bigram_speaker(word1, word2, dataset_bigrams):
	results = {}
	for item in dataset_bigrams:
		dict_key = " ".join([word1, word2])
		if item[0][0] == word1 and item[0][1] == word2 and dict_key not in results:
			results[dict_key] ={}
			results[dict_key][item[1]]= 1
		elif item[0][0] == word1 and item[0][1] == word2 and dict_key in results:
			if item[1] in results[dict_key]:
				results[dict_key][item[1]] +=1
			else:
				results[dict_key][item[1]]={}
				results[dict_key][item[1]] =1
	return results


def find_word_in_bigram(word, dataset_bigrams):
	for item in dataset_bigrams:
		if item[0][1]== word:
			print(item)


def find_word_in_trigram(word, dataset_trigrams):
	for item in dataset_trigrams:
		if item[0][1]== word:
			print(item)		

