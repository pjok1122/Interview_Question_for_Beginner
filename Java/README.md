# Part 2-1 Java

- [Part 2-1 Java](#part-2-1-java)
  - [JVM](#jvm)
    - [자바 프로그램 수행 과정](#%ec%9e%90%eb%b0%94-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%a8-%ec%88%98%ed%96%89-%ea%b3%bc%ec%a0%95)
    - [JVM의 구성](#jvm%ec%9d%98-%ea%b5%ac%ec%84%b1)
      - [Class Loader](#class-loader)
      - [Execution engine](#execution-engine)
      - [Interpreter](#interpreter)
      - [JIT(Just In Time)](#jitjust-in-time)
      - [GC(Garbage Collector)](#gcgarbage-collector)
      - [PC Register](#pc-register)
      - [JVM 스택 영역](#jvm-%ec%8a%a4%ed%83%9d-%ec%98%81%ec%97%ad)
      - [Native Method stack](#native-method-stack)
      - [Method Area (= class area = static area)](#method-area--class-area--static-area)
      - [Heap Area](#heap-area)
        - [New/Young 영역](#newyoung-%ec%98%81%ec%97%ad)
        - [Old 영역](#old-%ec%98%81%ec%97%ad)
        - [Reference](#reference)
  - [객체지향 프로그래밍](#%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d)
    - [특징](#%ed%8a%b9%ec%a7%95)
  - [Collection](#collection)
    - [List](#list)
      - [ArrayList](#arraylist)
      - [LinkedList](#linkedlist)
      - [Vector](#vector)
    - [Map](#map)
      - [HashMap](#hashmap)
      - [LinkedHashMap](#linkedhashmap)
      - [TreeMap](#treemap)
      - [HashTable](#hashtable)
    - [Set](#set)
      - [HashSet](#hashset)
      - [LinkedHashSet](#linkedhashset)
      - [TreeSet](#treeset)
    - [Queue](#queue)
      - [Deque](#deque)
      - [PriorityQueue](#priorityqueue)
  - [Annotation](#annotation)
      - [Reference](#reference-1)
  - [Generic](#generic)
  - [final keyword](#final-keyword)
  - [Overriding vs Overloading](#overriding-vs-overloading)
  - [Access Modifier](#access-modifier)
  - [Wrapper class](#wrapper-class)
    - [AutoBoxing](#autoboxing)
  - [static](#static)
  - [String](#string)
  - [String - equals](#string---equals)
  - [Multi-Thread 환경에서의 개발](#multi-thread-%ed%99%98%ea%b2%bd%ec%97%90%ec%84%9c%ec%9d%98-%ea%b0%9c%eb%b0%9c)
    - [Field member](#field-member)
    - [동기화(Synchronized)](#%eb%8f%99%ea%b8%b0%ed%99%94synchronized)
    - [ThreadLocal](#threadlocal)
    - [String, StringBuilder, StringBuffer](#string-stringbuilder-stringbuffer)
    - [abstract vs interface](#abstract-vs-interface)
      - [Personal Recommendation](#personal-recommendation)

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)

</br>

## JVM

> JVM은 자바 가상 머신의 약자로, 자바 어플리케이션을 실행하는 것을 도와주고 메모리 관리 또한 도와준다. JVM은 JAVA와 OS 사이에서 중개자 역할을 하기 때문에 JAVA가 OS에 구애받지 않고 동작할 수 있도록 한다.

### 자바 프로그램 수행 과정

![JVM](./images/JVM.png)

1. 프로그램이 실행되면 JVM은 OS로부터 프로그램이 필요로 하는 메모리를 할당받는다.
2. 자바 컴파일러(javac)가 자바 소스코드(.java)를 읽어들여 바이트 코드(.class)로 변환시킨다.
3. Class Loader를 통해 class 파일을 JVM으로 로딩한다.
4. Loading 된 파일들은 Excution engine을 통해 해석된다.
5. 해석된 바이트 코드는 Runtime Data Area로 배치되어 실질적인 수행이 이루어진다.  
   이러한 과정 속에서 JVM은 필요에 따라 Thread Synchronization과 GC와 같은 작업을 수행한다.

### JVM의 구성

#### Class Loader

JVM 내로 class 파일을 로드하고, 링크를 통해 배치하는 작업을 수행한다.

#### Execution engine

클래스를 실행하는 역할을 한다. 클래스 로더가 JVM 내의 런타임 데이터 영역에 바이트 코드를 배치시키고, 이것은 실행 엔진에 의해 실행된다. 바이트 코드는 완전한 기계어가 아니므로, 기계어로 번역하는 과정이 필요하다. 이 때 Interpreter와 JIT 두 가지 방식을 사용할 수 있다.

#### Interpreter

실행 엔진은 자바 바이트 코드를 명령어 단위로 읽어서 실행한다. 하지만 이 방식은 인터프리터의 단점을 그대로 가지고 있다. 즉, 한 줄씩 수행하기 때문에 수행 속도가 느리다.

#### JIT(Just In Time)

인터프리터 방식을 보완하기 위해 도입된 JIT 컴파일러이다. 인터프리터 방식으로 실행하다가 적절한 시점에 바이트코드 전체를 컴파일하여 Native Code로 변경하고, 이후에는 더 이상 인터프리팅 하지 않고 네이티브 코드로 직접 실행하는 방식이다. 네이티브 코드는 캐시에 보관하기 때문에 한 번 컴파일된 코드는 빠르게 수행한다.

#### GC(Garbage Collector)

사용되지 않는 자원을 메모리에서 내쫓는 역할을 하는 쓰레드가 존재한다.

#### PC Register

쓰레드가 수행할 다음 명령어의 주소를 가리킨다.

#### JVM 스택 영역

프로그램 수행 과정에서 임시로 할당되었다가 메소드를 빠져나가면 바로 소멸되는 특성의 데이터를 저장하는 영역이다.  
_ex) 매개변수, 지역변수, 리턴 값 등.._

#### Native Method stack

실제 수행할 수 있는 기계어로 작성된 프로그램을 실행시키는 영역이다.

#### Method Area (= class area = static area)

클래스 정보를 처음 메모리 공간에 올릴 때 초기화되는 대상을 저장하기 위한 메모리 공간.

_ref) Method Area는 클래스를 위한 공간이지만, Heap은 객체를 위한 공간이다. 두 영역 모두 GC의 관리 영역이다._

#### Heap Area

![java_heap](./images/java_heap.png)

객체를 저장하는 가상 메모리 공간이다. new 연산자로 생성된 객체와 배열을 저장한다. class Area에 올라온 클래스들만 객체로 생성이 가능하다. 힙은 세 부분으로 나뉜다.

##### New/Young 영역

- Eden : 객체들이 최초로 생성되는 공간
- Survivor 0 / 1 : Eden에서 참조되는 객체들이 저장되는 공간

##### Old 영역

Eden 영역이 가득찼을 때, GC(minor GC)가 발생한다. 이 때, Eden 영역에 있는 값들을 Survivor 영역으로 이동시킨다. 이 과정을 반복하다가 계속해서 살아남은 객체는 Old 영역으로 이동시킨다.

##### Reference

- [Java Virtual Machine 에 대해서](http://asfirstalways.tistory.com/158)
- [Garbage Collection 에 대해서](http://asfirstalways.tistory.com/159)

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## 객체지향 프로그래밍

변수와 메서드를 유기적으로 결합하여 하나의 객체로 만들고, 각 객체 간의 통신을 통해 프로그래밍을 수행하도록 로직을 구성하는 프로그래밍 기법이다.

**장점**

- 코드의 재사용성이 높다. (상속)
- 유지보수가 쉽다. (클래스 단위의 유지보수)
- 대형 프로젝트에 적합하다. (분업에 용이)

**단점**

- 처리 속도가 오래걸린다.
- 객체가 많으면 용량이 커질 수 있다.
- 설계 시 많은 노력이 필요하다.

### 특징

- 캡슐화 : 속성(field)과 행위(method)를 하나로 묶고, 불필요한 내용은 숨기는 것(private)을 말한다.
- 상속 : 부모 클래스의 특성을 자식에서 이어받는 것을 말한다. 코드의 재사용성이 높아진다.
- 다형성 : 객체가 하나의 타입으로 고정되는 것이 아니라, 상황에 따라서 여러 타입을 가질 수도 있다는 뜻이다.

</br>

## Collection

Java Collection 에는 `List`, `Map`, `Set` 인터페이스를 기준으로 여러 구현체가 존재한다. 이에 더해 `Stack`과 `Queue` 인터페이스도 존재한다. 왜 이러한 Collection 을 사용하는 것일까? 그 이유는 다수의 Data 를 다루는데 표준화된 클래스들을 제공해주기 때문에 DataStructure 를 직접 구현하지 않고 편하게 사용할 수 있기 때문이다. 또한 배열과 다르게 객체를 보관하기 위한 공간을 미리 정하지 않아도 되므로, 상황에 따라 객체의 수를 동적으로 정할 수 있다. 이는 프로그램의 공간적인 효율성 또한 높여준다.

### List

- `순서`가 있는 데이터를 저장한다.
- `중복`을 허용한다.

#### ArrayList

- 첫 크기를 10으로 할당하고, 공간이 가득차면 사이즈가 2배인 공간에 복사한다.
- 기존의 `Vector`를 개선한 클래스이다.
- 데이터 중간 삽입 시 시간복잡도가 O(n)이다.
- 검색에 대한 시간복잡도가 O(1)이다.
- `Thread-safe` 하지 않다. `synchronizedList(List list)`로 동기화처리가 가능하다.

#### LinkedList

- 크기가 정해져있지 않고, 왼쪽과 오른쪽을 참조할 수 있는 `Node`들의 연결로 이루어져있다.
- `Stack`과 `Queue`의 구현체로 `LinkedList`를 사용할 수 있다.
- 데이터 앞 뒤 삽입에 대한 시간복잡도는 O(1)이다.
- 데이터 검색에 대한 시간복잡도는 O(n)이다.
- `Thread-safe` 하지 않다. `synchronizedList(List list)`로 동기화처리가 가능하다.

#### Vector

- 첫 크기를 10으로 할당하고, 공간이 가득차면 사이즈가 2배인 공간에 복사한다.
- `ArrayList`의 구버전으로 현재는 사용되지 않는다.
- `Thread-safe` 하다.
- `Vector`를 상속한 `Stack`도 존재하는데, 가급적 `LinkedList`를 사용하자.

### Map

- `(key,value) 형식`의 데이터이다.
- key에 대해 중복을 허용하지 않는다. 이미 존재하는 key일 경우 데이터를 덮어쓴다.

#### HashMap

- `HashMap`에 들어오는 key는 `equals()`와 `hashCode()`를 기준으로 구분한다.
- `hashCode()`의 값을 Array의 index로 활용하여 배열처럼 사용이 가능하다.
- `hashCode()`의 값은 int 범위이므로 그냥 사용하게 되면 너무 많은 메모리를 사용해야 한다. 따라서 `int index = X.hashCode() % M`와 같은 방법으로 해시 버킷의 크기를 정할 수 있다.
- 충돌이 발생했을 때는 `Seperate Chaining` 기법을 사용한다. `get()`에 대한 평균 시간복잡도 : `O(N/M)` (N : 데이터 개수, M : 버킷의 크기)
- Java8에서는 `Seperate Chaining`을 버킷에 있는 데이터의 개수가 8개 이상이면 `Red-black Tree`로 구현하고 6개 이하면 `LinkedList`로 구현한다. 개수가 증가하고 줄어듦에 따라서 버킷의 구현체도 변경된다.
- 해시함수의 충돌가능성을 줄이기 위해 `보조 해시 함수`를 사용한다. `int index = X.hashCode() % M` 대신 `int index = X.hashCode() ^ (X.hashCode >> 16)`과 같은 방법을 사용한다. `>>`를 쓰는 이유는 속도가 빠르기 때문.

- `key`로 null을 사용할 수 있다.
- `get()`에 대한 최적의 시간복잡도 : `O(1)`
- `get()`에 대한 평균 시간복잡도 : `O(log(N/M))`
- `put()`에 대한 최적의 시간복잡도 : `O(1)`
- `put()`에 대한 평균 시간복잡도 : `O(log(N/M))`
- `Thread-safe` 하지 않다. `Collections.synchronizedMap(Map map)`을 이용해서 동기화 처리가 가능하다.

#### LinkedHashMap

- 입력 순서가 보장되는 HashMap이다.
- 버킷에 사용되는 LinkedList의 각 Node에는 `before`, `after`, `next`라는 포인터를 둬서 이전에 삽입된 데이터, 이후에 삽입된 데이터, 같은 버킷에 연결된 데이터를 구분할 수 있게 만들었다.
- 많은 상태정보를 저장해야 하므로 메모리 사용량이 HashMap에 비해 크다.

- `get()`에 대한 최적의 시간복잡도 : `O(1)`
- `put()`에 대한 최적의 시간복잡도 : `O(1)`
- `Thread-safe`하지 않다. `Collections.synchronizedMap(Map map)`을 이용해서 동기화 처리가 가능하다.

#### TreeMap

- `Red-Black-tree`의 형태로 `Node`를 저장한다.
- 각 `Node`는 `left`, `right`, `Entry<Key,Value>`로 이루어져있다.
- `Red-Black-tree`는 Balanced Binary Search Tree이므로 key의 hash 값이 오름차순으로 정렬되어있다.

- `get()`에 대한 평균 시간복잡도 : `O(logn)`
- `put()`에 대한 평균 시간복잡도 : `O(logn)`
- `Thread-safe`하지 않다. `Collections.synchronizedMap(Map map)`을 이용해서 동기화 처리가 가능하다.

#### HashTable

- 구버전의 HashMap이라고 볼 수 있다.
- 보조 해시 함수를 사용하지 않기 때문에 `HashMap`에 비해 충돌이 많이 발생한다.
- `Thread safe`하다.
- 사용하지 말자.

### Set

- 순서가 없는 데이터 컬렉션이다.
- 데이터 중복을 허용하지 않는다.
- 내부적으로 `Map<E, Object>`을 사용해 key의 중복을 제거한다.

#### HashSet

- 내부적으로 `HashMap`을 사용한다.
- null 삽입을 허용하지 않는다.

- `add()`에 대한 평균 시간복잡도 : `O(1)`
- `contains()`에 대한 평균 시간복잡도 : `O(1)`
- `Thread-safe`하지 않다. `Collections.synchronizedSet(Set set)`을 이용해서 동기화 처리가 가능하다.

#### LinkedHashSet

- 내부적으로 `LinkedHashMap`을 사용한다.
- 삽입 순서를 기억하고 있다.
- `add()`에 대한 평균 시간복잡도 : `O(1)`
- `contains()`에 대한 평균 시간복잡도 : `O(1)`
- `Thread-safe`하지 않다. `Collections.synchronizedSet(Set set)`을 이용해서 동기화 처리가 가능하다.

#### TreeSet

- `Red-black-tree`의 형태로 이루어진 자료구조이다.
- `Balanced Binary Search Tree`이므로 트리의 높이가 항상 `logN`을 유지한다.
- 데이터가 정렬되어있으므로 범위 검색에 용이하다.

- `add()`에 대한 평균 시간복잡도 : `O(logn)`
- `contains()`에 대한 평균 시간복잡도 : `O(logn)`

### Queue

- 선입선출 구조의 컬렉션
- `Queue`는 인터페이스이므로 `LinkedList`를 구현체로 사용한다.

- `add()`에 대한 평균 시간복잡도 : `O(1)`
- `poll()`에 대한 평균 시간복잡도 : `O(1)`

#### Deque

- 양방향 큐로 양쪽으로 데이터를 삽입,삭제 할수 있다.
- `Deque`는 인터페이스이므로 `LinkedList`를 구현체로 사용한다.

- `add()`에 대한 평균 시간복잡도 : `O(1)`
- `poll()`에 대한 평균 시간복잡도 : `O(1)`

#### PriorityQueue

- 우선순위 큐로 우선순위가 제일 높은 객체가 맨 앞에 위치한다.
- 우선순위 큐의 구현방식은 자유롭지만, 보통 `Heap` 자료구조의 구현방식을 따른다.
- 즉, 내부 구조는 배열의 형태로 이루어져있다.

- `add()`에 대한 평균 시간복잡도 : `O(logn)`
- `poll()`에 대한 평균 시간복잡도 : `O(logn)`
- `peek()`에 대한 평균 시간복잡도 : `O(1)`

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## Annotation

어노테이션이란 본래 주석이란 뜻으로, 인터페이스를 기반으로 한 문법이다. 주석과는 그 역할이 다르지만 주석처럼 코드에 달아 클래스에 특별한 의미를 부여하거나 기능을 주입할 수 있다. 또 해석되는 시점을 정할 수도 있다.(Retention Policy) 어노테이션에는 크게 세 가지 종류가 존재한다. JDK 에 내장되어 있는 `built-in annotation`과 어노테이션에 대한 정보를 나타내기 위한 어노테이션인 `Meta annotation` 그리고 개발자가 직접 만들어 내는 `Custom Annotation`이 있다. built-in annotation 은 상속받아서 메소드를 오버라이드 할 때 나타나는 @Override 어노테이션이 그 대표적인 예이다. 어노테이션의 동작 대상을 결정하는 Meta-Annotation 에도 여러 가지가 존재한다.

#### Reference

- http://asfirstalways.tistory.com/309

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## Generic

제네릭은 자바에서 안정성을 맡고 있다고 할 수 있다. 다양한 타입의 객체들을 다루는 메서드나 컬렉션 클래스에서 사용하는 것으로, **컴파일 과정에서 타입체크** 를 해주는 기능이다. 객체의 타입을 컴파일 시에 체크하기 때문에 객체의 타입 안전성을 높이고 형변환의 번거로움을 줄여준다. 자연스럽게 코드도 더 간결해진다. 예를 들면, Collection 에 특정 객체만 추가될 수 있도록, 또는 특정한 클래스의 특징을 갖고 있는 경우에만 추가될 수 있도록 하는 것이 제네릭이다. 이로 인한 장점은 **collection 내부에서 들어온 값이 내가 원하는 값인지 별도의 로직처리를 구현할 필요가 없어진다.** 또한 api 를 설계하는데 있어서 보다 명확한 의사전달이 가능해진다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## final keyword

- final class  
  다른 클래스에서 상속하지 못한다.

- final method  
  다른 메소드에서 오버라이딩하지 못한다.

- final variable  
  변하지 않는 상수값이 되어 새로 할당할 수 없는 변수가 된다.

추가적으로 혼동할 수 있는 두 가지를 추가해봤다.

- finally  
  `try-catch` or `try-catch-resource` 구문을 사용할 때, 정상적으로 작업을 한 경우와 에러가 발생했을 경우를 포함하여 마무리 해줘야하는 작업이 존재하는 경우에 해당하는 코드를 작성해주는 코드 블록이다.

- finalize()  
  keyword 도 아니고 code block 도 아닌 메소드이다. `GC`에 의해 호출되는 함수로 절대 호출해서는 안 되는 함수이다. `Object` 클래스에 정의되어 있으며 GC 가 발생하는 시점이 불분명하기 때문에 해당 메소드가 실행된다는 보장이 없다. 또한 `finalize()` 메소드가 오버라이딩 되어 있으면 GC 가 이루어질 때 바로 Garbage Collecting 되지 않는다. GC 가 지연되면서 OOME(Out of Memory Exception)이 발생할 수 있다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## Overriding vs Overloading

- 오버라이딩(Overriding)  
  상위 클래스에 존재하는 메소드를 하위 클래스에서 필요에 맞게 재정의하는 것을 의미한다.
- 오버로딩(Overloading)
  상위 클래스의 메소드와 이름은 동일하지만 매개변수 타입,개수,순서만 다른 메소드를 만드는 것을 의미한다. 다양한 상황에서 메소드가 호출될 수 있도록 한다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## Access Modifier

변수 또는 메소드의 접근 범위를 설정해주기 위해서 사용하는 Java 의 예약어를 의미하며 총 네 가지 종류가 존재한다.

- public  
  어떤 클래스에서라도 접근이 가능하다.

- protected  
  클래스가 정의되어 있는 해당 패키지 내 그리고 해당 클래스를 상속받은 외부 패키지의 클래스에서 접근이 가능하다.

- (default)  
  클래스가 정의되어 있는 해당 패키지 내에서만 접근이 가능하도록 접근 범위를 제한한다.

- private  
  정의된 해당 클래스에서만 접근이 가능하도록 접근 범위를 제한한다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## Wrapper class

기본 자료형(Primitive data type)에 대한 클래스 표현을 Wrapper class 라고 한다. `Integer`, `Float`, `Boolean` 등이 Wrapper class 의 예이다. int 를 Integer 라는 객체로 감싸서 저장해야 하는 이유가 있을까? 일단 컬렉션에서 제네릭을 사용하기 위해서는 Wrapper class 를 사용해줘야 한다. 또한 `null` 값을 반환해야만 하는 경우에는 return type 을 Wrapper class 로 지정하여 `null`을 반환하도록 할 수 있다. 하지만 이러한 상황을 제외하고 일반적인 상황에서 Wrapper class 를 사용해야 하는 이유는 객체지향적인 프로그래밍을 위한 프로그래밍이 아니고서야 없다. 일단 해당 값을 비교할 때, Primitive data type 인 경우에는 `==`로 바로 비교해줄 수 있다. 하지만 Wrapper class 인 경우에는 `.intValue()` 메소드를 통해 해당 Wrapper class 의 값을 가져와 비교해줘야 한다.

### AutoBoxing

JDK 1.5 부터는 `AutoBoxing`과 `AutoUnBoxing`을 제공한다. 이 기능은 각 Wrapper class 에 상응하는 Primitive data type 일 경우에만 가능하다.

```java
List<Integer> lists = new ArrayList<>();
lists.add(1);
```

우린 `Integer`라는 Wrapper class 로 설정한 collection 에 데이터를 add 할 때 Integer 객체로 감싸서 넣지 않는다. 자바 내부에서 `AutoBoxing`해주기 때문이다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

## static

static 변수는 static area(method area or class area)에 딱 하나만 생성되며, 클래스의 인스턴스들이 모두 공유하게 된다. 인스턴스가 생성되지 않아도 static 변수에 접근할 수 있다.

## String

`String`의 생성 방법은 2가지다. `literal`을 이용한 생성과 `new` 키워드를 이용한 객체 생성이다. `new` 키워드를 사용하면 매번 다른 객체를 생성하게 되고, `String a ="123"`과 같이 literal을 사용하면 `String constant pool`에 객체를 생성하고 그 객체를 가져온다. Java 7 이후에는 두 방식 모두 heap 영역을 사용한다는 공통점이 있지만, literal을 이용한 방식은 constant pool에 이미 해당하는 객체가 있을 경우, 그 객체를 반환한다. 이는 Java가 내부적으로 `object.intern("123")` 이라는 메서드를 사용하기 때문에 가능한 일이다. constant pool은 GC의 대상이며 `-xx:StringTableSize`로 크기를 지정할 수 있다.

## String - equals

String의 equals는 내부적으로 char를 하나씩 꺼내어 비교하는 방식으로 이루어져있다.

```java
public boolean equals(Object anObject) {
      if (this == anObject) {
          return true;
      }
      if (anObject instanceof String) {
          String anotherString = (String) anObject;
          int n = value.length;
          if (n == anotherString.value.length) {
              char v1[] = value;
              char v2[] = anotherString.value;
              int i = 0;
              while (n-- != 0) {
                  if (v1[i] != v2[i])
                          return false;
                  i++;
              }
              return true;
          }
      }
      return false;
  }
```

## Multi-Thread 환경에서의 개발

개발을 시작하는 입장에서 멀티 스레드를 고려한 프로그램을 작성할 일이 별로 없고 실제로 부딪히기 힘든 문제이기 때문에 많은 입문자들이 잘 모르고 있는 부분 중 하나라고 생각한다. 하지만 이 부분은 정말 중요하며 고려하지 않았을 경우 엄청난 버그를 양산할 수 있기 때문에 정말 중요하다.

### Field member

`필드(field)`란 클래스에 변수를 정의하는 공간을 의미한다. 이곳에 변수를 만들어두면 메소드 끼리 변수를 주고 받는 데 있어서 참조하기 쉬우므로 정말 편리한 공간 중 하나이다. 하지만 객체가 여러 스레드가 접근하는 싱글톤 객체라면 field 에서 상태값을 갖고 있으면 안된다. 모든 변수를 parameter 로 넘겨받고 return 하는 방식으로 코드를 구성해야 한다.

</br>

### 동기화(Synchronized)

필드에 Collection 이 불가피하게 필요할 때는 어떠한 방법을 사용할까? Java 에서는 `synchronized` 키워드를 사용하여 스레드 간 race condition 을 통제한다. 이 키워드를 기반으로 구현된 Collection 들도 많이 존재한다. `List`를 대신하여 `Vector`를 사용할 수 있고, `Map`을 대신하여 `HashTable`을 사용할 수 있다. 하지만 이 Collection 들은 제공하는 API 가 적고 성능도 좋지 않다.

기본적으로는 `Collections`라는 util 클래스에서 제공되는 static 메소드를 통해 이를 해결할 수 있다. `Collections.synchroziedList()`, `Collections.synchroziedSet()`, `Collections.synchroziedMap()` 등이 존재한다.
JDK 1.7 부터는 `concurrent package`를 통해 `ConcurrentHashMap`이라는 구현체를 제공한다. Collections util 을 사용하는 것보다 `synchronized` 키워드가 적용된 범위가 좁아서 보다 좋은 성능을 낼 수 있는 자료구조이다.

</br>

### ThreadLocal

스레드 사이에 간섭이 없어야 하는 데이터에 사용한다. 멀티스레드 환경에서는 클래스의 필드에 멤버를 추가할 수 없고 매개변수로 넘겨받아야 하기 때문이다. 즉, 스레드 내부의 싱글톤을 사용하기 위해 사용한다. 주로 사용자 인증, 세션 정보, 트랜잭션 컨텍스트에 사용한다.

스레드 풀 환경에서 ThreadLocal 을 사용하는 경우 ThreadLocal 변수에 보관된 데이터의 사용이 끝나면 반드시 해당 데이터를 삭제해 주어야 한다. 그렇지 않을 경우 재사용되는 쓰레드가 올바르지 않은 데이터를 참조할 수 있다.

_ThreadLocal 을 사용하는 방법은 간단하다._

1.  ThreadLocal 객체를 생성한다.
2.  ThreadLocal.set() 메서드를 이용해서 현재 스레드의 로컬 변수에 값을 저장한다.
3.  ThreadLocal.get() 메서드를 이용해서 현재 스레드의 로컬 변수 값을 읽어온다.
4.  ThreadLocal.remove() 메서드를 이용해서 현재 스레드의 로컬 변수 값을 삭제한다.

[뒤로](https://github.com/pjok1122/Interview_Question_for_Beginner)/[위로](#part-2-1-java)

</br>

### String, StringBuilder, StringBuffer

String은 `Immutatble` 하기 때문에 +연산 시 새로운 객체를 생성하기 때문에 메모리 공간의 낭비가 심하다. 하지만 Java 5 이후로는 String에 +연산이 있을 경우, 컴파일 타임에 `StringBuilder`로 변경해서 사용한다. 불변 객체이므로 `Thread-safe` 하다는 장점이 있다.

`StringBuilder`와 `StringBuffer`는 `Mutable` 객체이다. 따라서 문자열 연산이 많을 경우 String에 비해 장점이 많다. `StringBuilder`와 `StringBuffer`의 차이점은 `Thread-safe`이다. `StringBuilder`를 사용할 경우 `Thread-safe`하지 않고, `StringBuffer`를 사용할 경우 `Thread-safe`하다.

</br>

### abstract vs interface

추상클래스는 객체를 생성할 수 없는 클래스라고 볼 수 있다. 보통은 추상메서드가 1개 이상일 때 사용하는 것이 일반적이다. 추상클래스를 상속받은 클래스는 추상메서드를 구현하는 것이 강제된다.

인터페이스는 내부에 상수와 추상메서드로만 이루어져 있다. 접근제어자는 모두 public이며, 인터페이스의 구현체는 모든 추상메서드를 구현하는 것이 강제된다.

추상클래스와 인터페이스의 또다른 차이점은 상속이다. Java는 기본적으로 1개의 상속만 가능하지만, 인터페이스의 경우 다중상속(구현)이 가능하다는 장점이 있다.

#### Personal Recommendation

- (도서) [Effective Java 2nd Edition](http://www.yes24.com/24/goods/14283616?scode=032&OzSrank=9)
- (도서) [스프링 입문을 위한 자바 객체 지향의 원리와 이해](http://www.yes24.com/24/Goods/17350624?Acode=101)

[뒤로](https://github.com/JaeYeopHan/for_beginner)/[위로](#part-2-1-java)

</br>

</br>

_Java.end_
