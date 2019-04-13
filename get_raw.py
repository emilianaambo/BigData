# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import requests
import shutil

@click.command()
@click.argument('onput_filepath', type=click.Path(exists=True))
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Get the raw data from web)

# getting measures.tgz, cryptocurrencypricehistory.tgz and iris.data
baseurl = 'http://codeandbeer.org/virtual/BigData/Datasets/'
files = ['measures.tgz, cryptocurrencypricehistory.tgz, iris.data']
for filename in files
    r = requests.get(baseurl+"/"+filename, stream=True)
    if r.status_code==200:
        with open(output_filepath+"/"+filename, "wb") as f:
            r.raw.decode_content=True
                shutil.copyfileobj(r.raw, f)
                
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
