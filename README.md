소속 : 국립안동대학교, 컴퓨터공학과
===========================

학적사항: 20181131, 최수환
----------------------------------------

2022_Summer_School
---------------------------

# Markdown문서 만들어보기

## BlockQuote실습

>This is a first blockqute
>	>This is a second blockqute
>	>	>This is a third blockqute

## List 실습

### 순서가 있는 목록(번호사용)
1. 첫번째 목록
2. 두번째 목록
3. 세번째 목록

### 순서가 없는 목록(글머리기호사용 : *,+,-사용)
* Color
  * Blue
  * Green
  * Red
  * Yellow

들여쓰기(code 를 작성할때 사용)
--------------------
* 문장간 띄우고 들여쓰기

동해물과 

	백두산이

마르고 닳도록
* 문장간 띄우지 않고 들여쓰기

동해물과
	백두산이
마르고 닳도록

## Code Block Method

1. pre,code태그 사용

<pre>
<code>
class Car{
	private String modelName;
}
</code>
</pre>

2. " ``` " 사용
```java
class Car{
	private String modelName;
}
```

* " ``` "뒤에 무슨언어인지 적어두면 그언어로 표현가능

## Draw Line

### 미리보기 출력시 페이지를 나누는 용도

```
* * *

***

*****

- - -

------------------------------------
//이렇게 5줄 입력시
```

* * *

***

*****

- - -

------------------------------------

## Link

* 참조링크

Link: [google][googlelink]

[googlelink]: https://www.google.co.kr "Let's Go Google"

* 외부링크

[Google](https://www.google.co.kr)

* 자동링크

## Emphasis

이텔릭체 *별표(asterisks)* 혹은 _언더바(underscore)_ 를 사용

두껍게는 **별표(asterisks)** 혹은 __언더바(underscore)__ 를 사용

**_이텔릭체_와 두껍게** 를 같이 사용할 수 있음

취소선은 ~~물결표시(tilde)~~ 를 사용

## Images

![son](son.jpg "son")

### 이미지 크기조절

<img src="son.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="son"></img><br/>
<img src="son.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="son"></img>


## Footnotes

다른사람것을쓰고는 참조를 꼭 달아주자

문장뒤에 부호표시후 부호에 참조표시

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2]. 

You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.

[^2]: Every new line should be prefixed with 2 spaces. 

This allows you to have a footnote with multiple lines.

[^note]: Named footnotes will still render with numbers instead of the text but allow easier identification and linking. 
This footnote also has been made with a different syntax using 4 spaces for new lines.

## Table

* <table> 태그로 변환됨
* 헤더 셀을 구분할 때 3개 이상의 -(hyphen/dash) 기호가 필요함
* 헤더 셀을 구분하면서 :(Colons) 기호로 셀(열/칸) 안에 내용을 정렬할 수 있음
* 가장 좌측과 가장 우측에 있는 ‘|(vertical bar)” 기호는 생략 가능

| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 | |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 | |
| `fixed` | 브라우저 창을 기준으로 배치 | |

- - -

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## 줄바꿈

* 일반 텍스트 문장: 문장 끝에 공백 2번(스페이스 2번)하면 줄 바꿈이 됨.
* 테이블 내에서나 일반적인 경우: <br> 사용

//example  
가나다라스페이스두번  
공백두번 넣은후<br>
br넣은후
