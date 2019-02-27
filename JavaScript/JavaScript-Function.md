## Function Expressions and Function Statements 
- 함수를 만드는 방법에는 두가지가 있다. 
### Function Statements , 함수 선언

```js
function sayHello(){
    console.log('hi');
}
```
함수 선언 후 메모리에 함수 객체가 저장된다. 

### Function Expressions , 함수 표현식 

```js
var a = function(){
    console.log('hi');
}

a();
```
표현식은 값을 반환한다. 자바스크립트에서는 함수도 객체이다. 객체(익명 함수) 자체를 변수 a가 가리키는 메모리의 주소에 넣는다. 