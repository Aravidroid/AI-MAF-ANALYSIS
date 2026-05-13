import pandas as pd

def load_maf(filepath):

    df = pd.read_csv(
        filepath,
        sep="\t",
        comment="#",
        low_memory=False
    )

    return df

def analyze_mutations(df):

    total_mutations = len(df)

    top_genes = (
        df["Hugo_Symbol"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    variant_types = (
        df["Variant_Classification"]
        .value_counts()
        .to_dict()
    )

    return {
        "total_mutations": total_mutations,
        "top_genes": top_genes,
        "variant_types": variant_types
    }    