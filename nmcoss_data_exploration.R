#some weird formatting issues with this...need to figure out what it is and what this data was used for

nmcoss_lexicon.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/LEXICON.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)

head(nmcoss_lexicon.df)

#this file, potentially helpful....
nmcoss_master.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/MASTER.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_master.df)
dim(nmcoss_master.df)

new.df <-cbind(nmcoss_master.df$INT_NO, nmcoss_master.df$RES_YOUTH, nmcoss_master.df$COUNTY)
new.df
San_Miguel.df <- subset(nmcoss_master.df, COUNTY == "SM")
dim(San_Miguel.df)
San_Miguel.df

#County information, just codes and sectors, but not data specific to interviews collection
nmcoss_county.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/COUNTY.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_county.df)
dim(nmcoss_county.df)
nmcoss_county.df

#Grammar
nmcoss_grammar.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/GRAMMAR.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_grammar.df)
dim(nmcoss_grammar.df)

#Response
nmcoss_response.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/RESPONSE.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_response.df)
dim(nmcoss_response.df)
response_153 <- subset(nmcoss_response.df, INT_NO == "31")
dim(response_153)

nmcoss_response.df[nmcoss_response.df$INT_NO == "193"]
subset(nmcoss_response.df, INT_NO == 193)

#RANGE3
nmcoss_range3.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/RANGE3.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_range3.df)
dim(nmcoss_range3.df)


#RANGE5
nmcoss_range5.df <- read.csv("/Users/SanchoPanza/Desktop/nmcoss_public/new_mexico_colorado_spanish_survey/data/alternative_data_formats/csv/RANGE5.csv", header = TRUE, sep = ",", stringsAsFactors=FALSE)
head(nmcoss_range5.df)
dim(nmcoss_range5.df)

#NM demo info for transcripts
nm_transcripts.df <- read.csv("/Users/SanchoPanza/Desktop/NMCOSS/NM_demo_info.csv", header = TRUE, sep = ";", stringsAsFactors=FALSE)
nm_transcripts.df
