자바스크립트의 객체는 어떻게 구성되어있고 그 중 프로토타입은 어떤 역할과 특징을 가지고 있을까 ? 

# Instantiation patterns

Instantiation patterns은 자바스크립트에서 뭘 만들 때 사용하는 방법들이다. 자바스크립트는 객체를 만드는 네가지 방법을 제공하고 무슨 방법을 쓰던 모든 메소드는 다음 기능을 한다.

- 객체를 만듬 
- 객체의 메소드와 속성을 만듬 

네가지 방법은 아래와 같다. 
1. Functional
2. Functional-shared
3. Prototypal
4. Pseudoclassical 


자바스크립트 객체는 key, value 로 만들어져있다. 객체를 만드는 제일 쉬운 방법은 {} 를 이용해서 만들고 . (dot notation)을 이용하여 객체 안의 속성을 추가한다. 

```sh
let animal = {}
animal.name = 'Leo'
animal.energe = '10'

animal.eat = function(amount){
    console.log(`${this.name} is eating`);
    this.energy += amount
}

animal.sleep = function(length){
    console.log(`${this.name}  is sleeping`)
    this.energy -= length
}

```
"
해당 속성들을 가지는 객체들을 만들기 위해서 앞의 로직들을 함수 형태로 만든다. 이를 Functional Instantation 패턴이라고 하며 이 함수는 실제로 새로운 객체를 만들기 때문에  Constructor function(생성자) 라고 부른다. 

## Functional Instantaion 

```sh
function Animal(name, energe) = {
    let animal = {}
    animal.name = name
    animal.energe = energe

    animal.eat = function(amount){
        console.log(`${this.name} is eating`)
        this.energy += amount
    }

    animal.sleep = function(length){
        console.log(`${this.name} is sleeping`)
        this.energy -= length
    }

    return animal

}

const leo = Animal('Leo', 7)
```

 모든 메소드 (eat, sleep)이 function 내에 있기 때문에 만약 해당 객체의 두번째 인스턴스를 만들면 메모리에 있는 모든 속성값들과 메소드들이 <mark>복사 </mark>된다. 이 방법으로 객체를 만든 다음 메서드를 변경하고 새 인스턴스를 만들면 서로 다른 메서드를 참조하게 된다. 
 또한 새로운 객체를 만들 때마다 메모리에 있는 메소드들을 그대~로 복사하게 되기 때문에 메모리 낭비가 이루어진다. 


 ## Functional Instantiation with Shared Methods

 Functional shard instantiation은 모든 객체들이 **메소드들 공유** 함으로써 앞에서 언급했던 Functial Instantiation의 단점을 보완한다. 

 먼저 빈 객체를 가지는 함수를 만들고, 함수안에 속성들을 정의한다. ** 메소드들은 다른 객체에 정의 하고 만든 객체와 메소드들을 연장시킨다. ** 마지막으로는 오브젝트를 리턴한다.  Functional shard instantiation로 만든 모든 객체는 복제 없이 모두 같은 메소드들을 가리키는 포인터를 갖게 된다. 


 ```sh
function Animal(name, energe){
    let animal = {};
    animal.name = name;
    anmimal.energy = energy;

    extend(animal, animalMethods);

    return animal;

}

function extend(animal , methods){
    for(var key in methods){
        animal[key] = methods[key]
    }
}

const animalMethods = {
    eat : function(){
        // code
    },

    sleep : function (){
        //
    }
}

const tiger = Aminal('Leo', 7);
tiger.eat();
tiger.sleep();

 ```

메소드를 일일이 복사하지 않기 때문에 메모리 낭비는 적어 졌다. 
하지만 객체가 인스턴스화 될때 공유 메소드들은 포인터를 갖게되는데 만약 메소드를 수정하고 새로운 객체를 만든다면 기존의 객체와 새로운 객체는 각각 다른 메소드를 참조하게 되는 문제가 생긴다. 

## Prototypal Instantiation

프로토 타입을 이용한 인스턴스화는 객체를 만들기 위해서 **프로토타입 체인** 을 이용한다. 메소드들은 Object.create 메소드를 이용해서 오브젝트의 프로토타입에 첨부(?), 붙게 된다. 

별도의 객체에서 모든 메소드를 만든다..? 그리고 function을 만든다. function 안에는 method 를 붙이기 위해서 Object.create 메소드를 이용하고 객체를 return 한다. 
```sh

function Animal(name,energy){
    // 메소드를 가지고 있는 별도의 객체를 생성
    const animal = Object.create(animalMethod); 

    animal.name = name;
    animal.energy = energy;

    return animal;

}

var animalMethods = {
    eat : function(){

    },
    sleep : function(){

    }
}

var leo = Aminal('Leo', 10);
leo.eat();
leo.sleep();

```
메소드들은 객체 내에서 리턴되는 것이 아니라 오브젝트의 prototype에 붙게된다. 모든 메소드들은 메모리 상에서 복사되지 않고 모든 객체마다 만들어지게 된다. 
하지만 이 방법을 이용하기 위해서는 객체를 하나 만든 다음 생성자 함수에서 객체를 반환해야 한다. 

- animal 은 Object.create(animalMethod)로 만들어졌기 때문에 animal에 찾는 property가 없다면 자바스크립트는 animalMethod에서 찾도록 시킨다. 

## Pseudoclassical Instantiation 

이 방법은 위의 수많은 코드들을 필요로 하는 prototylal instantiation의 단점을 개선하기 위해서 만들어졌다. 마찬가지로 prototype chain 을 이용한다. 
자바스크립트는 new 키워드를 사용하여 프로토 타입 인스턴스화로 만드는 기능 대부분을 제공한다.

새로운 변수를 만들고 해당 변수에 Objct.create()를 할당하는 대신에 **"this"** 에 할당하게 된다. 

새로운 함수를 만들고 this 키워드를 이용해서 속성들을 추가한다. 메소드들은 프로토타입에 할당된다. 새로운 객체를 만들기 위해서 new 키워드를 사용한다. 

```s
function Animal(name, energy){
    this.name = name;
    this.energy = energy;
}

Animal.prototype.sleep = function(){
    //
}

Animal.prototpye.eat = function(){
    //
}

var leo = new Animal('leo', 10);
leo.eat();
leo.sleep();

```
자바스크립트의 기본 기능들을 이용하기 때문에 객체 생성에 최적화된 방법이라고 할 수 있다. 

- **this** 는 해당 함수를 실행시키고 있는 객체를 가리키고 있음 
- this.property 를 함으로써 오브젝트에 속성 추가 

### new operator 의 역할 

```s
var leo = new Animal('leo', 10);s
```

- new operator는 먼저 {} 빈 객체를 생성한다. 
- this가 해당 빈 객체를 가리키게 한다. 
    > 디폴트로 `this` 는 글로벌 객체를 가리키고 있다. 브라우저에서의 this는 기본적으로 window 객체이다. 전역 객체 window를 만지는 일은 매우매우 안좋은 행동! 어플리케이션 어디에서든지 사용가능 하기 때문
-  그 다음 해당 객체를 Animal function 에서 리턴하게 한다. 



 
## Summary
자바스크립트 개발자들은 객체를 만드는 위의 다양한 방법들을 알고 있어야 한다. 각각의 방법들은 장단점이 있기 때문에 코드의 사이즈와 퍼포먼스에 맞는 방법을 찾아 쓸 수 있어야 한다. 

> 참고 
- [Instantiation Patterns in JavaScript](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)
- [A Beginner's Guide to JavaScript's Prototype](https://tylermcginnis.com/beginners-guide-to-javascript-prototype/)