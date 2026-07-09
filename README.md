\# Git Bisect 과제 - 무료배송 버그 찾기



\## 과제 설명



이 저장소에는 `delivery.py`라는 무료배송 판별 프로그램이 있습니다.



무료배송 조건은 다음과 같습니다.



```text

주문 금액이 50,000원 이상이면 무료배송

```



따라서 `delivery.py`를 실행했을 때 정상 출력은 다음과 같아야 합니다.



```text

FREE\_SHIPPING

```



하지만 현재 최신 버전에서는 아래처럼 잘못된 결과가 출력됩니다.



```text

DELIVERY\_FEE\_REQUIRED

```



`git bisect`를 사용하여 \*\*어느 커밋부터 무료배송 조건이 잘못되었는지\*\* 찾으세요.



\---



\## 참고 사항



`git bisect`를 사용할 때는 반드시 다음 두 가지가 필요합니다.



```text

정상적으로 동작하는 good commit

잘못 동작하는 bad commit

```



현재 최신 버전은 실행 결과가 잘못되었으므로 bad commit으로 볼 수 있습니다.



하지만 good commit은 직접 확인해야 합니다.



과거 커밋 중 하나로 이동한 뒤 `delivery.py`를 실행해보고, 출력이 `FREE\_SHIPPING`으로 나오는 경우에만 그 커밋을 good commit으로 표시하세요.



즉, 단순히 오래된 커밋이라고 해서 바로 good으로 표시하지 말고, 반드시 실행 결과를 확인한 뒤 판단해야 합니다.



\---



\## 제출 내용



다음 내용을 캡처해서 제출하세요.



1\. `git log --oneline` 결과

2\. 최신 버전에서 `delivery.py`를 실행한 결과

3\. good commit을 직접 확인한 과정

4\. `git bisect`를 수행한 과정

5\. Git이 알려준 first bad commit 결과



\---



