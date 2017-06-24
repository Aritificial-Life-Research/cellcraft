import os
from collections import defaultdict
import logging

############# TODO
### generate an algorithm that predicts color and texture of blocks taking into account a) biological features (GOterms) b) n_chains c) type of complex (prot complex, membrane, dna...)
### it should be a method in ProteinComplex(), Membrane() and Dna() instead of particular of each item (Protein(),Lipid()...)



# Setup for correct assignment of colors to example proteins

# colors EC id:color id
col = {'1': 6, '2': 1, '3': 9, '4': 2, '5': 5, '6': 4, '0': 7}

# testure path name:texture id
text = defaultdict(list)
names = ['Metabolism', 'Genetic Information Processing', 'Human Diseases', 'Drug Development',
         'Environmental Information Processing', 'Cellular Processes', 'Organismal Systems']

# texture 95 crystal, 159 full, 35 wool
textures = ['159', '35', '35', '35', '95', '95', '95']
for t, n in zip(textures, names):
    text[t].append(n)

current_env = os.environ.get('app_env')
root_logger = logging.getLogger()

if current_env == 'live':
    APP_HOST = '127.0.0.1'
    APP_PORT = 5000  # TODO
    root_logger.setLevel(logging.INFO)


elif current_env == 'dev':
    APP_HOST = '127.0.0.1'
    APP_PORT = 5000
    root_logger.setLevel(logging.DEBUG)

else:
    logging.warning('Please configure a environment using now default dev environment for config')
    root_logger.setLevel(logging.DEBUG)
