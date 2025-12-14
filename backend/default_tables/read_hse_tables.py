"""Get HSE accident injury types"""

import re
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests

RIDKIND_SRC = "https://www.hse.gov.uk/statistics/assets/docs/ridkind.xlsx"

RIDNAT_SRC = "https://www.hse.gov.uk/statistics/assets/docs/ridnat.xlsx"


def df_from_excel_download(url: str, table_name: str):
    parsed_url = urlparse(url).path
    fname = Path(parsed_url).name

    with (
        tempfile.TemporaryDirectory() as tmpdir,
        open(Path(tmpdir) / Path(fname), "wb") as infile,
        requests.get(url, stream=True, timeout=20) as response,
    ):
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=8192):
            infile.write(chunk)

        df = pd.read_excel(
            Path(tmpdir) / Path(fname),
            sheet_name=table_name,
            header=None,
        )
        header_row = df.index[df.iloc[:, 0].str.contains("Year")].to_list()[0]
        headers = (
            df.iloc[header_row : header_row + 1,]
            .squeeze()
            .apply(lambda x: re.sub(r"[\s]?\n.*$", "", x))
        )
        df = df.iloc[header_row + 1 :,]
        df.columns = headers.to_list()

    return df


def get_types(type: str):
    if type not in ["accident", "injury"]:
        raise ValueError("`type` must be one of 'accident' or 'injury'.")

    if type == "accident":
        source = RIDKIND_SRC
        types_col = "Accident Kind"
    elif type == "injury":
        source = RIDNAT_SRC
        types_col = "Nature of injury"

    fatal = df_from_excel_download(source, table_name="Table 1")
    nonfatal = df_from_excel_download(source, table_name="Table 2")

    types = pd.concat([fatal[types_col], nonfatal[types_col]]).unique()

    df = pd.DataFrame(types, columns=["name"])
    df = df.drop(df.index[df["name"].str.contains("All")]).reset_index(
        drop=True
    )

    df["name"] = df["name"].apply(lambda x: re.sub(r"[\s]?(\[Note).*$", "", x))

    df = df.reset_index().rename({"index": "id"}, axis=1)

    df.to_csv(Path(f"./default_tables/{type}.csv"), index=False)


if __name__ == "__main__":
    get_types("accident")
    get_types("injury")
