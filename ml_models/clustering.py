import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


DATA_INPUT_PATH = "data/processed/students_scored.csv"
DATA_OUTPUT_PATH = "data/processed/students_clustered.csv"


def load_data():
    """
    Load scored student data.
    """
    df = pd.read_csv(DATA_INPUT_PATH)
    features = df[["APS", "WWS", "PTMS", "CRS"]]
    return df, features


def scale_features(features):
    """
    Standardize features for clustering.
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features


def apply_kmeans(scaled_features, k=4):
    """
    Apply K-Means clustering.
    """
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    labels = kmeans.fit_predict(scaled_features)
    return labels


def attach_clusters(df, labels):
    """
    Attach cluster labels to dataframe.
    """
    df["cluster_id"] = labels
    return df


def save_clustered_data(df):
    """
    Save clustered dataset.
    """
    df.to_csv(DATA_OUTPUT_PATH, index=False)
    print(f"✅ Clustered data saved to {DATA_OUTPUT_PATH}")


def print_cluster_summary(df):
    """
    Print cluster-wise mean scores for interpretation.
    """
    summary = df.groupby("cluster_id")[["APS", "WWS", "PTMS", "CRS", "SRI"]].mean()
    print("\n📊 Cluster Summary (Mean Scores):")
    print(summary)


def run_clustering():
    """
    Full clustering pipeline.
    """
    df, features = load_data()
    scaled_features = scale_features(features)
    labels = apply_kmeans(scaled_features, k=4)

    df = attach_clusters(df, labels)
    save_clustered_data(df)
    print_cluster_summary(df)


if __name__ == "__main__":
    run_clustering()

