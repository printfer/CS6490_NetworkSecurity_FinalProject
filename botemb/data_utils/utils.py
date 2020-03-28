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
        '1': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-42/detailed-bidirectional-flow-labels/capture20110810.binetflow',
        '2': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-43/detailed-bidirectional-flow-labels/capture20110811.binetflow',
        '3': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-44/detailed-bidirectional-flow-labels/capture20110812.binetflow',
        '4': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-45/detailed-bidirectional-flow-labels/capture20110815.binetflow',
        '5': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-46/detailed-bidirectional-flow-labels/capture20110815-2.binetflow',
        '6': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-47/detailed-bidirectional-flow-labels/capture20110816.binetflow',
        '7': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-48/detailed-bidirectional-flow-labels/capture20110816-2.binetflow',
        '8': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-49/detailed-bidirectional-flow-labels/capture20110816-3.binetflow',
        '9': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-50/detailed-bidirectional-flow-labels/capture20110817.binetflow',
        '10': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/detailed-bidirectional-flow-labels/capture20110818.binetflow',
        '11': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-52/detailed-bidirectional-flow-labels/capture20110818-2.binetflow',
        '12': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-53/detailed-bidirectional-flow-labels/capture20110819.binetflow',
        '13': r'https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-54/detailed-bidirectional-flow-labels/capture20110815-3.binetflow'
    }

    url = scenario_map[str(scenario)]
    print(f'Downloading scenario={scenario} from: {url}')
    return pd.read_csv(url)

        
if __name__ == '__main__':
    dsn = download(scenario=1)
    #print(dsn.head())