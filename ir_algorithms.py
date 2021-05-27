import openpyxl # for reading excel files
import sys

class Document:
    def __init__(self, doc_id, content, url) -> None:
        self.doc_id = doc_id
        self.content = content
        self.url = url


class Posting:
    def __init__(self, doc_id, freq) -> None:
        self.doc_id = doc_id
        self.freq = freq

    def __str__(self) -> str:
        return 'doc_id: ' + self.doc_id + '\tfreq: ' + self.freq

    def __repr__(self) -> str:
        return str(self)


class PostingsList:
    def __init__(self) -> None:
        self.plist = []
        self.term_freq = 0

    def __str__(self) -> str:
        return 'term_freq: ' + self.term_freq + '\t' + str(self.plist)

    def __repr__(self) -> str:
        return str(self)


class IR:
    def __init__(self) -> None:
        self.dictionary = dict()
        self.documents = None

    
    # building the inverted index
    def build_inverted_index(self, file_name):
        self.init_file(file_name)
        for doc in self.documents:
            self.process_document(doc)
        print('Inverted Index Matrix construction completed')


    # initializing documents list by reading the excel dataset
    def init_file(self, file_name):
        wb_obj = openpyxl.load_workbook(file_name)
        sheet = wb_obj.active
        headers = []
        dataset = []
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i == 0:
                for header in row:
                    headers.append(header)
            else:
                document = Document(row[0], row[1], row[2])
                dataset.append(document)
        self.documents = dataset
        print('Initialized Excel file')


    # processing the documents one by one for building the index
    def process_document(self, doc):
        tokens = self.get_tokens(doc)

    
    # get tokens for each document
    def get_tokens(self, doc):
        text = doc.content
        tokens = text.split()
        counts = dict()
        for token in tokens:
            modified_token = self.modify_token(token)
            if modified_token not in counts:
                counts[modified_token] = 1
            else:
                counts[modified_token] += 1
        unique_tokens = counts.keys()
        for unique_token in unique_tokens:
            posting = Posting(doc.doc_id, counts[unique_token])
            self.add_posting(posting, unique_token)


    # add posting to the postings_list of the corresponding term in dictionary
    def add_posting(self, posting, term):
        postings_list = None
        if term not in self.dictionary:
            postings_list = PostingsList()
        else:
            postings_list = self.dictionary[term]
        postings_list.term_freq += 1
        postings_list.plist.append(posting)
        self.dictionary[term] = postings_list
        
            

    
    # modify token with stemming, tokenization, normalization, etc
    def modify_token(self, token):
        # to be implemented...
        #
        #
        #
        return token


        
        