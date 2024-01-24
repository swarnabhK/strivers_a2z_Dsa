#approach1, using a temp array

#[1,2,3,4,5], if k==2, our temp array will start at k
def rotate_kplaces(arr,k):
    n = len(arr)
    res = [0]*n
    k = k%n #k can be > length of array, in that case we will normalize k.
    #copy the elements from the original array to the temp array.
    #temp = [5,6,7,1,2,3,4] , [1,2,3,4,5,6,7]. arr[0] is res[3],arr[1] is res[4],arr[2] is res[5],arr[3] is res[6],arr[4] is res[0] the relation between i and k is (i+k)%length of array, it goes from 4,5,6,0,1,2,3-> (i+k)%length of array
    for i in range(0,n):
        res[(i+k)%n] = arr[i]
    
    #copy over the elements from the temp array to the original array
    for i in range(n):
        arr[i] = res[i]


l = [1,2,3,4,5,6,7]
rotate_kplaces(l,3)
print(l)