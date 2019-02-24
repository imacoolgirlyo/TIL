## Object 만들긔

```js
var umbrella = {
	color : pink,
  	isOpen : false,
  	open : function(){
    	if(umbrella.isOpen === true){
        	return "already Open!"
        }else{
          umbrella.isOpen = true;
          return "A opens the umbrella"
        }
    }
}
```
- Object의 속성들은 {} 안에서 key : value 로 나타난다. 
- Object는 하나의 데이터 타입 중 하나이다. 
- 데이터 타입을 알고 싶을 때 typeof operator 사-용
 ```js
typeof "hello"
typeof true
typeof [1,2,3] // object
typeof function hello(){ }
````

#### JavaScript의 Primitive Data Types 
Strings, numbers , booleans , undefined , null 

### JavaScript Object
````js
typeof [1 ,2 ,3 ]; // "object" 
```
typeof [1,2,3] 은 array가 아니라 object 이다. (오..글쿤) 
- Object는 자바스크립트에서 특정 데이터를 저장할 때 사용하는 자료 구조이고 "key"를 통해 해당 데이터를 접근할 수 있도록 한다.

사람을 예로 들면 이름, 나이, 좋아하는 색 등등의 속성으로 나타낼 수 있다. 

### Object literal notation

````js 
var sister = {
	name : "Sarah",
    age : 23,
    favoriteColor : "purple",
    siblings : ["julia"],
    pets : true
};
```
- "key"는 property 나 method의 이름을 나타낸다. 

```js 
sister["siblings"]
sister.siblings

// returns ["julia"]
```
- branket notation, dot notation  두 방법으로 오브젝트의 속성값에 접근할 수 있다. 

주로 첫번쨰 branket의 경우 property 이름에 특정 문자열이나 공백문자열이 들어간 경우 사용된다. 

```
var propertyName = "center location";
circle[propertyName] = 
```