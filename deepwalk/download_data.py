from data_utils.utils import download
import pathlib

pathlib.Path("./data").mkdir(parents=True, exist_ok=True)
for i in range(1, 14):
    dsn = download(scenario=i)
    dsn.to_csv(f'./data/scenario_{i}.csv', index=False)

