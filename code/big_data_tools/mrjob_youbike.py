import json

from mrjob.job import MRJob

class MRYouBikeETL(MRJob):
    def mapper(self, _, line):
        line = line.strip()
        data = json.loads(line)
