'''
배열이 주어졌을 때, 왼쪽으로 k만큼 Shift하는 연산을 만들어보자.

가장 쉬운 방법은 1칸 이동하는 알고리즘을 k번 반복하는 것인데, 1칸 이동하는 시간 복잡도를 고려하면 O(n)이므로
시간 복잡도가 O(nk)가 돼버린다.

그럼 이제 보다 효율적인 알고리즘들을 생각해보자.

두 번째로 떠오르는 방법은 대부분 비슷하지 않을까 싶다.

"k 만큼 한 번에 이동할 순 없을까 ?"

당연히 가능하다. 하지만 그에 따른 테크닉도 물론 필요하다.

[1 2 3 4 5 6 7 8 9 10 11 12 13] k=3 이라고 해보면, 다음과 같은 모습이 눈에 띄게 된다.

1 <- 4 <- 7 <- 10 <- 13 <- 3 <- 6 <- 9 <- 12 <- 2   (a<-b : a값이 존재하는 위치에 b를 삽입한다는 의미.)
2 <- 5 <- 8 <- 11

여기서는 1부터 시작해서 3씩 값을 증가시키다보면 1~13이라는 모든 숫자를 거쳐가는 것을 알 수 있다.

그 이유는 Z_13이 + 연산에서 group을 이루고 '3' 이라는 숫자가 generator이기 때문이다.

'대수학'을 참고하면  도움이 되겠지만, 결론부터 얘기하자면, 데이터개수와 shift를 의미하는 k의 최대공약수가 1인 경우에는 위와 같은 상황이 가능하다.

이번에는 데이터의 개수는 12개, k=2라고 생각해보자.
gcd(12,2) = 2 이므로 2개의 그룹이 생성될 것이다.

[0,1,2,3,4,5,6,7,8,9,10,11]

0<-2<-4<-6<-8<-10
1<-3<-5<-7<-9<-11

이제 이를 코드로 구현하기만 하면 된다. 시간복잡도는 O(n)이 된다.


이외에도 다양한 방법이 있으나, 한 가지 정도는 기억해두는 것이 프로그래밍 면접을 대비할 때 좋지 않을까 싶다.

'''
import math


def shift_k(arr, k):
    n = len(arr)
    gcd = math.gcd(n, k)
    visited = [0]*n

    for i in range(gcd):
        j = i
        temp = arr[j]
        while not visited[(j+k) % n]:
            visited[j] = 1
            arr[j] = arr[(j+k) % n]
            j = (j+k) % n

        arr[j] = temp


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
shift_k(arr, 2)

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
shift_k(arr2, 3)
print(arr)
print(arr2)