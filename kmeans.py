from scipy.cluster.vq import kmeans, vq


def calculate_kmeans(data):
    # computing K-Means with K = 2 (2 clusters)
    hashes = [item[1] for item in data]
    centroids, _ = kmeans(hashes, 970)
    # assign each sample to a cluster
    idx, _ = vq(hashes, centroids)
    result = []
    for index, group in enumerate(idx):
        result.append((data[index][0], group))
    return result
