from urllib.request import urlretrieve as ur
from bs4 import BeautifulSoup as BS4
import requests


class Scrape_OSDB:
    def __init__(self, mode='IR', file_type='jdx', directory='OSDB'):
        self.url = 'https://osdb.stuchalk.domains.unf.edu'
        self.full_url = self.url + self.mode_select(mode)
        self.file_suffix = self.file_type_select(file_type)

        self.compound_list = self.gen_compound_list()
        self.compound_names = self.gen_name_list()
        self.compounds = dict(zip(self.compound_names, self.compound_list))
        self.download_spectra(directory)

    def mode_select(self, mode):
        match mode:
            case 'IR':
                return '/techniques/view/04'
            case '13C NMR':
                return '/techniques/view/01'
            case '1H NMR':
                return '/techniques/view/02'
            case 'MS':
                return '/techniques/view/03'
            case 'UVVis':
                return '/techniques/view/05'
            case _:
                return '/techniques/view/04'

    def file_type_select(self, file_type):
        match file_type:
            case 'jdx':
                return 'JCAMP'
            case 'xml':
                return 'XML'
            case 'json':
                return 'JSONLD'
            case _:
                return 'JCAMP'

    def gen_compound_list(self):
        return [link.get('href') for link in BS4(requests.get(self.full_url).content, 'html.parser').find_all('a', class_='btn btn-default')]

    def gen_name_list(self):
        return [BS4(requests.get(self.url + element).content, 'html.parser').find('small').getText() for element in self.compound_list]

    def download_spectra(self, directory):
        for element in self.compounds:
            ur(self.url + self.compounds[element] + self.file_suffix, '{}/{}.jdx'.format(directory, element))
            
            
if __name__ == "__main__":
  Scrape_OSDB('IR', 'JCAMP', 'OSDB')
