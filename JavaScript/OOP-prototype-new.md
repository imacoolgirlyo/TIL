# Prototype in JavaScript

자바스크립트 객체는 key, value 로 만들어져있다. 객체를 만드는 제일 쉬운 방법은 {} 를 이용해서 만들고 . (dot notation)을 이용하여 객체 안의 속성을 추가한다. 

```
let animal = {}
animal.name = 'Leo'
animal.energe = '10'

animal.eat = function(amount){
    console.log(`${this.name} is eating`);
    this.energy += amount
}

```
해당 속성들을 가지는 객체들을 만들기 위해서 앞의 로직들을 함수 형태로 만든다. 이를 Functional Instantation 패턴이라고 하며 이 함수는 실제로 새로운 객체를 만들기 때문에  Constructor function(생성자) 라고 부른다. 

## Functional Instantaion 

```
function Animal(name, energe) = {
    let animal = {}
    animal.name = 'Leo'
    animal.energe = '10'

    animal.eat = function(amount){
        console.log(`${this.name} is eating`)
        this.energy += amount
    }

}
```