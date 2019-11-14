# require scipy
# pip install scipy
from scipy.spatial import distance 
from scipy.spatial.distance import squareform



def get_distance_matrix(x,mode="euclidean",p=2.):
    """
    ベクトルデータの距離行列を得る
    return：距離行列
    
    Example
    input:[[1,2,2],[1,2,3]]
    return:[[ 0.  1.]
            [ 1.  0.]]   
    """

    return squareform(distance.pdist(x, metric=mode, p=p)) 
print(get_distance_matrix([[1,2,2],[1,2,3]]))