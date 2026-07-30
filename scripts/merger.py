import pandas as pd
from conf import FLOW_METRICS,SNAPSHOT_METRICS

def merge():
    """
       Merge multiple cleaned financial metric CSVs into one DataFrame.

       Returns
       -------
       pandas.DataFrame
           Master dataframe containing all metrics.
       """

    master= None

# flow metrics
    for tag in FLOW_METRICS.keys():
        df = pd.read_csv(f"data/processed/{tag}.csv")

        df["end"] = pd.to_datetime(df["end"])

        if tag == "Revenues":
            master = df[["start", "end", tag]]

        else:
            master = pd.merge(
                master,
                df[["end", tag]],
                on="end",
                how="outer"
            )

        # ---------- Snapshot Metrics ----------
    for tag in SNAPSHOT_METRICS.keys():
        df = pd.read_csv(f"data/processed/{tag}.csv")

        df["end"] = pd.to_datetime(df["end"])

        master = pd.merge(
            master,
            df[["end", tag]],
            on="end",
            how="outer"
        )

    master = master.sort_values("end")

    return master
