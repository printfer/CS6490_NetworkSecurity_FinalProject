import pandas as pd
import io
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download(scenario=None):

    """
    Downloads the bidirectional flow dataset corresponding to the provided scenario. 
    These datasets are labeled and can be used to create a graph.

    Arguments
    ---------
    scenario : int
        Specifies the scenario to download. Must be a value between 1 and 13 inclusive.

    Returns
    -------
    dataset : pd.DataFrame
        A DataFrame object containing the bidirectional flow data.
    """

    if scenario is None:
        raise ValueError('Must specify scenario')

    if not isinstance(scenario, int):
        raise TypeError('Scenario must be an integer')

    if scenario not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        raise ValueError('Invalid value passed to scenario')

    scenario_map = {
        '1': '42',
        '2': '43',
        '3': '44',
        '4': '45',
        '5': '46',
        '6': '47',
        '7': '48',
        '8': '49',
        '9': '50',
        '10': '51',
        '11': '52',
        '12': '53',
        '13': '54'
    }

    url = f'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-{scenario_map[str(scenario)]}/detailed-bidirectional-flow-labels/capture20110810.binetflow'
    print(f'Downloading scenario={scenario} from: {url}')
    return pd.read_csv(url)

        
if __name__ == '__main__':
    dsn = download(scenario=1)
    #print(dsn.head())