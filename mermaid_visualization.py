import streamlit_mermaid as stmd
import streamlit as st

code = """
graph TD
  subgraph GCS
    A[GCS Bucket] -->|Input Data| B(Processing Job)
  end

  subgraph Dataflow
    B -->|Process Data| C(Intermediate Data)
    C -->|Transform Data| D(Processed Data)
  end

  subgraph BigQuery
    D -->|Load Data| E(BigQuery Table)
  end

"""

stmd.st_mermaid(code)